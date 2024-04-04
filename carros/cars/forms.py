from django import forms

from .models import Car, Brand

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'

    def clean_value(self):
        value = self.cleaned_data['value']
        if value < 20 * 1000:
            self.add_error('value', 'O valor do carro deve ser maior que R$ 20.000,00')
        return value
    
    def clean_factory_year(self):
        factory_year = self.cleaned_data['factory_year']
        if factory_year < 1975:
            self.add_error('factory_year',  'Somente carros fabricados após 1975 são aceitos')
        return factory_year