
from rest_framework import routers
from recepies.views import ReceipeViewSet
router = routers.SimpleRouter()
router.register(r'receipe', ReceipeViewSet)
# router.register(r'accounts', AccountViewSet)

urlpatterns = [
    # path('forgot-password/', ForgotPasswordFormView.as_view()),
]

urlpatterns += router.urls