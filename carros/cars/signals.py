from django.db.models.signals import post_save,  post_delete, pre_save
from django.dispatch import receiver
from django.db.models import Sum

from .models import Car, CarInventory

def update_inventory():
    cars_count = Car.objects.all().count()
    cars_value = Car.objects.aggregate(
        total_value=Sum('value')
    )['total_value']

    CarInventory.objects.create(cars_count=cars_count, cars_value=cars_value)

@receiver(post_save, sender=Car)
def update_inventory_save(sender, instance, **kwargs):
    update_inventory()


@receiver(post_delete, sender=Car)
def update_inventory_delete(sender, instance, **kwargs):
    update_inventory()


@receiver(pre_save, sender=Car)
def car_pre_save(sender, instance: Car, **kwargs):
    if not instance.description:
        instance.description = 'Descrição não informada'