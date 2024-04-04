from django.urls import path

from .views import CarsView, NewCarView, CarDetail, CarUpdate, CarDelete

urlpatterns = [
    path('', CarsView.as_view(), name='cars_list'),
    path('new_car/', NewCarView.as_view(), name='new_car'),
    path('<int:pk>/', CarDetail.as_view(), name='car_detail'),
    path('<int:pk>/update/', CarUpdate.as_view(), name='car_update'),
    path('<int:pk>/delete/', CarDelete.as_view(), name='car_delete'),
]