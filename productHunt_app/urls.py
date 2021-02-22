from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_product, name='create'),
    # path('create',views.create_product),

]
