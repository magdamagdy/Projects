from django.shortcuts import render,redirect
import random
from dashboard.models import Additem
from .models import save_products
# Create your views here.


def recommendation(request):
    #count = random.randint(0,10)
    #if count == 5 or count == 10 or count == 7:
    save_products.objects.all().delete()
    random_id = random.sample(range(1,100),50)
    #count = 0
    #products_id = []
    for item in random_id:
        if Additem.objects.filter(id=item).exists():
            #products_id.append(item)
            d=Additem.objects.filter(id=item).values_list('description',flat=True).get(id=item)
            i = Additem.objects.filter(id=item).values_list('image', flat=True).get(id=item)
            p = Additem.objects.filter(id=item).values_list('price', flat=True).get(id=item)

            print(d)
            print(i)
            print(p)
            save_products(description=d,image=i,price=p).save()

            #print(count)
            #print(products_id)
            print(random_id)

    product = save_products.objects.all()
    return render(request, 'Recommendations.html', {'products': product})

