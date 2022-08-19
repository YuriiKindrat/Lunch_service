from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from menu_choice_app.views import (
    RestaurantViewSet,
    MenuViewSet,
    VoteViewSet,
    CreateUserView,
    ManageUserView
)

router = routers.DefaultRouter()
router.register("restaurants", RestaurantViewSet)
router.register("menus", MenuViewSet)
router.register("votes", VoteViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("register/", CreateUserView.as_view(), name="create"),
    path("me/", ManageUserView.as_view(), name="manage"),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refres/', TokenRefreshView.as_view(), name='token_refresh'),
]

app_name = "menu_choice_app"
