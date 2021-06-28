from django.shortcuts import render, redirect
from django.contrib import messages
from dashboard.models import Additem
from reg.models import type_of_customer
from .models import Add_to_cart,Total_for_user,Total,checkout_details,User_participation
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
# Create your views here.


def add_to_cart(request,pk):
    h = User.objects.filter(username=request.user).exists()
    if h:
        t = type_of_customer.objects.filter(username=request.user).values_list('type', flat=True).get(
            username=request.user)

        if t == 'Buyer':
            #get user logged in
            flag=0
            total=0
            user_name = request.user.username
            #user_added = add to cart.objects.filter(username=user_name)

            # add items to add to cart
            items_ordered = Additem.objects.filter(id=pk).values_list('pk',flat=True)
            image = Additem.objects.filter(id=pk).values_list('image',flat=True).get(id=pk)
            description = Additem.objects.filter(id=pk).values_list('description', flat=True).get(id=pk)
            price = Additem.objects.filter(id=pk).values_list('price', flat=True).get(id=pk)
            amount = Additem.objects.filter(id=pk).values_list('amount', flat=True).get(id=pk)



            x=str(items_ordered[0])
            ids=Add_to_cart.objects.filter(product_id=x,user=request.user).values_list('product_id',flat=True)
            if x in ids:
                flag=1
            if flag==1:
                print('is included')
            else:
                user = Add_to_cart(username=user_name, user=request.user, product_id=items_ordered, image=image,
                                   description=description, price=price, product_quantity=amount)
                user.save()


            category = Additem.objects.filter(id=pk).values_list('category',flat=True).get(id=pk)
            print(category)
            if category == 'chairs':
                return redirect('/chairs')

            elif category == 'armchairs':
                return redirect('/armchairs')

            elif category == 'chaiselongues':
                return redirect('/chaiselongues')

            elif category == 'sofas':
                return redirect('/sofas')

            elif category == 'wardrobes':
                return redirect('/wardrobes')

            elif category == 'beds':
                return redirect('/beds')

            elif category == 'shelving units':
                return redirect('/shelving_units')

            elif category == 'tables':
                return redirect('/tables')
        else:
            return redirect('/log')

    else:
        return redirect('/log')


def show_items(request):
    product = Add_to_cart.objects.filter(user=request.user)

    return render(request,'cart.html',{'products':product})


def add_quantity(request,pk):
    total=0
    product = Add_to_cart.objects.filter(user=request.user)
    Total_for_user.objects.filter(product_id=pk,user=request.user).delete()

    try:
        quantity = float(request.POST['quantity'])
    except MultiValueDictKeyError:
        quantity = float(1)

    print(quantity)
    print(pk)

    amount = float(Additem.objects.filter(id=pk).values_list('amount', flat=True).get(id=pk))
    a = amount-quantity
    if a <0:
        a=0
    Additem.objects.filter(id=pk).update(amount=a)

    #amount = Additem.objects.filter(id=pk).values_list('amount', flat=True).get(id=pk)
    if quantity > amount:
        quantity=float(amount)

    price = Additem.objects.filter(id=pk).values_list('price',flat=True).get(id=pk)
    print(price)
    paid_cal = price * quantity

    Total_for_user(product_id=pk, user=request.user,quantity_ordered=quantity,amount_paid=paid_cal).save()

    #calculate total
    paid = Total_for_user.objects.filter(user=request.user).values_list('amount_paid', flat=True)
    print(paid_cal)
    for item in paid:
        total = total + item
    print(total)
    ids = Total.objects.filter(user=request.user).values_list('user',flat=True)
    if ids:
        Total.objects.filter(user=request.user).update(total=total)
    else:
        Total(user=request.user,total=total).save()
    Add_to_cart.objects.filter(user=request.user,product_id=pk).update(total=paid_cal,quantity=quantity)
    final = total + 150 + 100

    return render(request,'cart.html',{'products':product,'total':total,'final':final})

def remove_cart(request,pk):
    #one_item_total = float(Add_to_cart.objects.filter(product_id=pk, user=request.user).values_list('total',flat=True).get(product_id=pk, user=request.user))
    q = float(Add_to_cart.objects.filter(user=request.user, product_id=pk).values_list('quantity', flat=True).get(
        user=request.user, product_id=pk))
    Add_to_cart.objects.filter(product_id=pk, user=request.user).delete()
    Total_for_user.objects.filter(product_id=pk, user=request.user).delete()

    product = Add_to_cart.objects.filter(user=request.user)


    amount = Additem.objects.filter(id=pk).values_list('amount', flat=True).get(id=pk)
    a = amount + q
    if a <0:
        a=0
    Additem.objects.filter(id=pk).update(amount=a)

    f = Add_to_cart.objects.filter(user=request.user).exists()
    if f:
        # calculate total
        paid = Total_for_user.objects.filter(user=request.user).values_list('amount_paid', flat=True)
        total=0
        for item in paid:
            total = total + item
        print(total)
        ids = Total.objects.filter(user=request.user).values_list('user', flat=True)
        if ids:
            Total.objects.filter(user=request.user).update(total=total)
        else:
            Total(user=request.user, total=total).save()
        if total==0:
            final=0
        else:
            final = total + 150 + 100
    else:
        total = 0
        Total.objects.filter(user=request.user).update(total=total)
        final = 0

    #total1 = float(Total.objects.filter(user=request.user).values_list('total',flat=True).get(user=request.user))
    #total = total1 - one_item_total
    #Total.objects.filter(user=request.user).update(total=total)
    #final = total + 150 + 100

    return render(request, 'cart.html',{'products':product,'total':total,'final':final})

def checkout(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        city = request.POST['city']
        paymentMethod = request.POST['paymentMethod']



        try:
            country = request.POST['country']
        except MultiValueDictKeyError:
            country = 'Egypt'
        try:
            currency = request.POST['currency']
        except MultiValueDictKeyError:
            currency = 'EGP'

        #h = Add_to_cart.objects.filter(user=request.user).values_list('product_id').get(user=request.user)
        h = Add_to_cart.objects.filter(user=request.user).exists()
        if not h:
            messages.info(request, "!! empty cart")
            return redirect('/cart_items')


        else:
            checkout_details(username=username,email=email, phone=phone,address=address,city=city,country=country,
                             currency=currency,paymentMethod=paymentMethod).save()

            #particpation
            h = User_participation.objects.filter(user=request.user).exists()
            if h:
                get_count = User_participation.objects.filter(user=request.user).values_list('count',flat=True).get(user=request.user)
                print(get_count)

                inc_count = int(get_count) +1
                User_participation.objects.filter(user=request.user).update(count=inc_count)
            else:
                User_participation(user=request.user,count=1).save()

            Add_to_cart.objects.filter(user=request.user).delete()
            Total_for_user.objects.filter(user=request.user).delete()
            print('order completed')
            return redirect('/confirm')
    else:
        return render(request, 'checkout.html')


def offers(request):
    if User_participation.objects.filter(user=request.user).exists():
        count = int(User_participation.objects.filter(user=request.user).values_list('count',flat=True).get(user=request.user))
        print(count)
        #c=int(count)
        msg = ""
        if count ==1:
            msg = "ohh!! it's ur first time to order from our website. Wait for a special gift from our store on ship."
        elif count == 5:
            msg = "Thanks for shopping here. You made a record in ordering items. Wait for ur gift on ship. Please contact us to choose item up to 2000L.E. Enjooy ^--^"
        elif count == 20:
            msg = "Thanks for your trust in our items. A surprise on ship. Please contact us to choose item up to 60000L.E. Enjooy ^--^"
        elif count > 20:
            msg = "you aren't just a customer. we want to thank you from all our hearts for trusting our website. As Usual wait for ur Gift on ship. Enjooy ^--^"
        else:
            msg = 'Be active for more surprises. May be the next Purchase you are lucky and receive an offer.'
        return render(request,'offers.html',{'msg':msg})
    else:
        msg = 'Be active for more surprises. May be the next Purchase you are lucky and receive an offer.'
        return render(request,'offers.html',{'msg':msg})

def confirm(request):
    return render(request,'confirm.html')