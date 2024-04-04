from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import Car, Brand
from .forms import CarForm

class CarsView(ListView):
    model = Car
    template_name = 'cars.html'
    context_object_name = 'cars'
    
    def get_queryset(self):
        cars = super().get_queryset().order_by('-value')
        search = self.request.GET.get('search')
        if search:
            cars = cars.filter(model__icontains=search)
        return cars


@method_decorator(login_required(login_url='login'), name='dispatch')
class NewCarView(CreateView):
    model = Car
    form_class = CarForm
    template_name = 'new_car.html'
    context_object_name = 'car'
    success_url = '/cars/'
    

class CarDetail(DetailView):
    model = Car
    template_name = 'car_detail.html'


@method_decorator(login_required(login_url='login'), name='dispatch')
class CarUpdate(UpdateView):
    model = Car
    form_class = CarForm
    context_object_name = 'car'
    template_name = 'car_update.html'

    def get_success_url(self) -> str:
        return reverse_lazy('car_detail', kwargs={'pk': self.object.pk})


@method_decorator(login_required(login_url='login'), name='dispatch')
class CarDelete(DeleteView):
    model = Car
    template_name = 'car_delete.html'
    context_object_name = 'car'
    success_url = '/cars/'