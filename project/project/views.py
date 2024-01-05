from django.shortcuts import redirect , render
from product.models import brandModel, productModel
def home(request , carname = None):
    car = productModel.objects.all()
    model = brandModel.objects.all()
    if carname is not None:
        brand = brandModel.objects.get(name = carname)
        car = productModel.objects.filter(brand = brand)
        print(car)
        return render(request, 'index.html', {'car': car, 'model': model})
    return render(request, 'index.html', {'car':car , 'model':model})


