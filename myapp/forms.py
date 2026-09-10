from django import forms


class ItemForm(forms.Form):
    name = forms.CharField(max_length=100, label="Название")
    price = forms.IntegerField(label="Цена")
    description = forms.CharField(widget=forms.Textarea, label="Описание")