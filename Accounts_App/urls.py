from django.urls import path
from .views import Record, Login, Logout, Product

urlpatterns = [
    path('register/', Record.as_view(), name="register"),
    path('login/', Login.as_view(), name="login"),
    path('logout/', Logout.as_view(), name="logout"),
    path('product/', Product.as_view(), name="product"),

]