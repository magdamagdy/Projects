from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Additem
from .forms import AdditemForm
from home.models import Seller_rating, Rating, Reviews, Whishlist, Product_rating
from home.views import seller_rating
from cart.models import Add_to_cart, Total_for_user


# Create your views here.

def dashboard(request):

    if request.method == 'POST':
        form = AdditemForm(request.POST, request.FILES)
        if form.is_valid():
            additem=form.save(commit=False)
            additem.user=request.user
            additem.save()
            items = Additem.objects.filter(user=request.user)
            ID = User.objects.values_list('id', flat=True).get(username=request.user)
            seller_rating()
            if (Seller_rating.objects.filter(user_id=ID).exists()) == False:
                rating=0
            else:
                rating = Seller_rating.objects.values_list('rating', flat=True).get(user_id=ID)
            return render(request, 'dashboard.html', {'form': form, 'items': items, 'rating': rating})

    else:
        form = AdditemForm()
        items = Additem.objects.filter(user=request.user)
        ID = User.objects.values_list('id', flat=True).get(username=request.user)
        seller_rating()
        if (Seller_rating.objects.filter(user_id=ID).exists()) == False:
            rating = 0
        else:
            rating = Seller_rating.objects.values_list('rating', flat=True).get(user_id=ID)
        return render(request, 'dashboard.html', {'form': form, 'items': items, 'rating': rating})


def remove_item(request, pk):
    if request.method == 'POST':
        form = AdditemForm(request.POST, request.FILES)
        if form.is_valid():
            additem = form.save(commit=False)
            additem.user = request.user
            additem.save()
            items = Additem.objects.filter(user=request.user)
            ID = User.objects.values_list('id', flat=True).get(username=request.user)
            seller_rating()
            if (Seller_rating.objects.filter(user_id=ID).exists()) == False:
                rating = 0
            else:
                rating = Seller_rating.objects.values_list('rating', flat=True).get(user_id=ID)
            return render(request, 'dashboard.html', {'form': form, 'items': items, 'rating': rating})

    else:
        #delete item from dashboard
        Additem.objects.filter(id=pk).delete()
        Rating.objects.filter(item_id=pk).delete()
        Reviews.objects.filter(item_id=pk).delete()
        Whishlist.objects.filter(old_id=pk).delete()
        Product_rating.objects.filter(item_id=pk).delete()
        form = AdditemForm()
        items = Additem.objects.filter(user=request.user)

        #delete same item from cart
        Add_to_cart.objects.filter(product_id=pk).delete()
        Total_for_user.objects.filter(product_id=pk, user=request.user).delete()
        ID = User.objects.values_list('id', flat=True).get(username=request.user)
        seller_rating()
        if (Seller_rating.objects.filter(user_id=ID).exists()) == False:
            rating = 0
        else:
            rating = Seller_rating.objects.values_list('rating', flat=True).get(user_id=ID)
        return render(request, 'dashboard.html', {'form': form, 'items': items, 'rating': rating})