import phonenumbers

from django import forms

from store.models import *


class ClientForm(forms.ModelForm):
    def clean_phone(self):
        phone = self.cleaned_data["phone"]
        if not phone:
            raise forms.ValidationError("Input your phone number")
        try:
            parsed_phone = phonenumbers.parse(phone, None)
            if not phonenumbers.is_possible_number(parsed_phone):
                raise forms.ValidationError("Wrong number")
        except phonenumbers.NumberParseException as error:
            raise forms.ValidationError(error.args[0])
        return phonenumbers.format_number(
            parsed_phone, phonenumbers.PhoneNumberFormat.INTERNATIONAL
        )

    class Meta:
        model = Client
        fields = ["name", "email", "phone"]


# class DealershipForm(forms.Form):
#     name = forms.CharField(max_length=50)
#     available_car_types = forms.ModelMultipleChoiceField(
#         queryset=CarType.objects.all(), widget=forms.CheckboxSelectMultiple
#     )
#     clients = forms.ModelMultipleChoiceField(
#         queryset=Client.objects.all(), widget=forms.CheckboxSelectMultiple
#     )

class DealershipForm(forms.ModelForm):
    class Meta:
        model = Dealership
        fields = ["name", "clients", "available_car_types"]


class CarTypeForm(forms.ModelForm):
    class Meta:
        model = CarType
        fields = ["brand", "model_auto", "price"]


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ["car_type", "color", "year", "blocked_by_order", "owner"]


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["client", "dealership", "car"]


class QuantityForm(forms.ModelForm):
    class Meta:
        model = OrderQuantity
        fields = ["order", "quantity", "is_paid"]
