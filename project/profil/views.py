from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from product.models import UserCar

# Create your views here.
@login_required
def profile(request):
    car = UserCar.objects.filter(user = request.user)
    return render(request, 'profile.html', {'car': car})