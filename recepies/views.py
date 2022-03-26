from django.shortcuts import render
from recepies.models import Receipe
# Create your views here.
from rest_framework import viewsets
from rest_framework.response import Response
from recepies.serializers import ReceipeSerializer
from rest_framework import mixins
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie, vary_on_headers
from django.core.cache import cache

class ReceipeViewSet(viewsets.ModelViewSet):

    queryset = Receipe.objects.all()
    serializer_class = ReceipeSerializer

    # @method_decorator(cache_page(60*60*2))
    def retrieve(self, request, *args, **kwargs):
        print(cache.keys('*'))
        # for k,v in cache.items():
            # prisssnt(k)
        if cache.get('cache_data'):
            print("From Cache -----------")
            instance = cache.get('cache_data')
        else:
            instance = self.get_object()
            print("From Db -----------")
            cache.set('cache_data',instance)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)