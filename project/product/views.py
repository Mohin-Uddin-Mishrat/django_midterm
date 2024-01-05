from django.shortcuts import render, redirect
from .models import brandModel, productModel ,UserCar,comments
from .forms import commentForm
# Create your views here.

def details(request, id ):
    car = productModel.objects.get(id = id)
    cmnt = comments.objects.filter(car = car)
    print(cmnt)
    if request.method == 'POST':
        form = commentForm(request.POST)
        if form.is_valid() :
            form.instance.user = request.user
            form.instance.car = car
            form.save()
    form = commentForm()
    return render(request, 'dtl.html', {'car': car, 'form':form , 'comments': cmnt})


def buy(request, id ):
    car = productModel.objects.get(id = id)
    product = productModel()
    qty = int(car.quantity)
    car.quantity = str(qty -1)
    car.save()
    print(car.quantity)
    form = UserCar()
    form.user = request.user
    form.car = car
    form.save()
    return redirect('profile')

