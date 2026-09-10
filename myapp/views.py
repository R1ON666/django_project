from django.shortcuts import render, redirect
from .forms import ItemForm

ITEMS = [
    {"id": 1, "name": "Ноутбук", "price": 75000, "description": "Мощный и лёгкий"},
    {"id": 2, "name": "Смартфон", "price": 45000, "description": "Флагман 2025"},
    {"id": 3, "name": "Наушники", "price": 12000, "description": "Беспроводные"},
]


def index(request):
    return render(request, "myapp/index.html", {"items": ITEMS})


def item_detail(request, item_id):
    item = next((i for i in ITEMS if i["id"] == item_id), None)
    return render(request, "myapp/detail.html", {"item": item})


def add_item(request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            new_item = {
                "id": len(ITEMS) + 1,
                "name": form.cleaned_data["name"],
                "price": form.cleaned_data["price"],
                "description": form.cleaned_data["description"],
            }
            ITEMS.append(new_item)
            return redirect("index")
    else:
        form = ItemForm()
    return render(request, "myapp/add.html", {"form": form})