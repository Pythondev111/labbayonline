from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from Myfiles.models import *
from .forms import RegisterUser
from django.contrib.auth import  login,authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


# Create your views here.
def index(request):
    uzunlik = Product.objects.all()
    if len(uzunlik)<4:
        yangi_maxsulotlar = Product.objects.all()
    else:
        u = len(uzunlik)-4
        yangi_maxsulotlar = Product.objects.all()[u:]
    telefonlar = Product.objects.filter(tur__nomi='Telefon va aksessuarlar')[0:6]
    akses = Product.objects.filter(tur__nomi='Uy rozgor buyumlar')[0:6]
    oshxona = Product.objects.filter(tur__nomi='Kitoblar')[0:6]
    kitob = Product.objects.filter(tur__nomi='Sovgalar suvinerlar')[0:6]
    toy = Product.objects.filter(tur__nomi='Parfumeriya')[0:6]
    kons = Product.objects.filter(tur__nomi='Bolajonlar')[0:6]
    rozgor = Product.objects.filter(tur__nomi='Tabiiy dori vositalar')[0:6]
    komp = Product.objects.filter(tur__nomi='Maishiy texnika')[0:6]
    kiyimlar = Product.objects.filter(tur__nomi='Sport tovarlar')[0:6]
    suviner = Product.objects.filter(tur__nomi='Qol soatlar')[0:6]

    contents={'phones':telefonlar,'akses':akses,'oshxona':oshxona,'kitob':kitob,
              'toy':toy,'kons':kons,'rozgor':rozgor,'komp':komp,'kiyimlar':kiyimlar,
              'suviner':suviner,'newww':yangi_maxsulotlar}
    if 'ddd' in request.POST or 'cmd' in request.POST:

        if request.user.is_authenticated:
            nomi = request.POST.get('w3ls_item')
            narxi = request.POST.get('amount')
            miqdor = request.POST.get('add')
            miqdor = int(miqdor)
            narxi = int(narxi)
            max_id = request.POST.get('idd')
            user_id = request.user.id
            username = User.objects.get(id=user_id)
            username = str(username)
            nomlar = []
            nom = Sotib_olingan_maxsulotlar.objects.filter(mijoz_id = user_id)

            for i in nom:
                nomlar.append(i.nomi)
             
            if nomi in nomlar:
                
                max_nomi = Sotib_olingan_maxsulotlar.objects.get(nomi = nomi)
                max_miqdori = max_nomi.miqdori
                max_idd = max_nomi.id
                max_miqdori += 1

                narxi = narxi*max_miqdori
                Sotib_olingan_maxsulotlar(max_idd, nomi, narxi, max_miqdori, username, user_id).save()
            else:
                ids = [0]
                mobiles = Sotib_olingan_maxsulotlar.objects.all()
                for mobile in mobiles:
                    ids.append(mobile.id)

                Sotib_olingan_maxsulotlar(max(ids)+1,nomi,narxi,miqdor,username,user_id).save()
        else:
            return render(request,'sign in.html')



    contents['new_products'] = yangi_maxsulotlar
    if 'Search' in request.POST:
        soz = request.POST.get('Search')
        soz = soz.strip()
        qidirish = Q(nomi__startswith=soz)|Q(narxi__startswith=soz)|Q(tur__nomi__startswith=soz)
        telefonlar = Product.objects.filter(qidirish)

        return render(request, 'index.html', {'phones':telefonlar,'search':2})
        
    user_id = request.user.id    
    raqamlar = Sotib_olingan_maxsulotlar.objects.filter(mijoz_id=user_id)
    soni = 0
    for i in raqamlar:
        soni += int(i.miqdori)
    contents = {'phones': telefonlar, 'akses': akses, 'oshxona': oshxona, 'kitob': kitob,
                'toy': toy, 'kons': kons, 'rozgor': rozgor, 'komp': komp, 'kiyimlar': kiyimlar,
                'suviner': suviner, 'newww': yangi_maxsulotlar,'soni':soni}
    return render(request,'index.html',contents)
def maxsulotlar(request):
    telefonlar = Product.objects.filter(tur__nomi='Telefon va aksessuarlar')
    akses = Product.objects.filter(tur__nomi='Uy rozgor buyumlar')
    oshxona = Product.objects.filter(tur__nomi='Kitoblar')
    kitob = Product.objects.filter(tur__nomi='Sovgalar suvinerlar')
    toy = Product.objects.filter(tur__nomi='Parfumeriya')
    kons = Product.objects.filter(tur__nomi='Bolajonlar')
    rozgor = Product.objects.filter(tur__nomi='Tabiiy dori vositalar')
    komp = Product.objects.filter(tur__nomi='Maishiy texnika')
    kiyimlar = Product.objects.filter(tur__nomi='Sport tovarlar')
    suviner = Product.objects.filter(tur__nomi='Qol soatlar')
    form = AuthenticationForm()

    if 'ddd' in request.POST or 'cmd' in request.POST :

        if request.user.is_authenticated :
            nomi = request.POST.get('w3ls_item')
            narxi = request.POST.get('amount')
            miqdor = request.POST.get('add')
            miqdor = int(miqdor)
            narxi = int(narxi)
            max_id = request.POST.get('idd')
            user_id = request.user.id
            username = User.objects.get(id=user_id)
            username = str(username)
            nomlar = []
            nom = Sotib_olingan_maxsulotlar.objects.filter(mijoz_id = user_id)

            for i in nom:
                nomlar.append(i.nomi)
             
            if nomi in nomlar:
                
                max_nomi = Sotib_olingan_maxsulotlar.objects.get(nomi = nomi)
                max_miqdori = max_nomi.miqdori
                max_idd = max_nomi.id
                max_miqdori += 1

                narxi = narxi*max_miqdori
                Sotib_olingan_maxsulotlar(max_idd, nomi, narxi, max_miqdori, username, user_id).save()
            else:
                ids = [0]
                mobiles = Sotib_olingan_maxsulotlar.objects.all()
                for mobile in mobiles:
                    ids.append(mobile.id)

                Sotib_olingan_maxsulotlar(max(ids)+1,nomi,narxi,miqdor,username,user_id).save()
        else:
            return render(request,'sign in.html')

    elif 'Search' in request.POST:
        soz = request.POST.get('Search')
        soz = soz.strip()
        qidirish = Q(nomi__startswith=soz) | Q(narxi__startswith=soz) | Q(tur__nomi__startswith=soz)
        telefonlar = Product.objects.filter(qidirish)

        return render(request, 'products.html', {'phones': telefonlar, 'search': 2,})
    user_id = request.user.id    
    raqamlar = Sotib_olingan_maxsulotlar.objects.filter(mijoz_id=user_id)
    soni = 0
    for i in raqamlar:
        soni += int(i.miqdori)

    contents = {'phones': telefonlar, 'akses': akses, 'oshxona': oshxona, 'kitob': kitob,
                'toy': toy, 'kons': kons, 'rozgor': rozgor, 'komp': komp, 'kiyimlar': kiyimlar,
                'suviner': suviner, 'forms': form, 'soni': soni}



    return render(request,'products.html',contents)
def boglanish(request):
    if 'Name' in request.POST:
        ism = request.POST.get('Name')
        mail = request.POST.get('Email')
        tel = request.POST.get('Telephone')
        matn = request.POST.get('message')
        idlar = [0]
        textt = Murojatlar.objects.all()

        for i in textt:
            idlar.append(i.id)

        Murojatlar(max(idlar)+1,ism,mail,tel,matn).save()
    raqamlar = Sotib_olingan_maxsulotlar.objects.all()
    soni = 0
    for i in raqamlar:
        soni += int(i.miqdori)
    return render(request,'mail.html',{'soni':soni})
def about(request):
    raqamlar = Sotib_olingan_maxsulotlar.objects.all()
    soni = 0
    for i in raqamlar:
        soni += int(i.miqdori)
    return render(request,'about.html',{'soni':soni})
def korzinka(request):
    user_id = request.user.id
    basket = Sotib_olingan_maxsulotlar.objects.filter(mijoz_id = user_id)
    if 'anketa' in request.POST:
        ism = request.POST.get('ism')
        fam= request.POST.get('fam')
        yosh= request.POST.get('yosh')
        jins= request.POST.get('jins')
        shaxar= request.POST.get('shaxar')
        username= request.POST.get('anketa')
        tel= request.POST.get('tel')
        anketalar = Anketa.objects.all()
        idlar = [0]
        for i in anketalar:
            idlar.append(i.id)
        maxx_id = max(idlar)
        Anketa(maxx_id+1,ism,fam,tel,jins,yosh,shaxar,username).save()
        return HttpResponseRedirect('/')

    summa = 0
    mobiles = Sotib_olingan_maxsulotlar.objects.filter(mijoz_id=user_id)
    for mobile in mobiles:
        summa += int(mobile.narxi)

    summa = format(summa,',')

    return render(request,'korzinka.html',{'basket':basket,'summa':summa})
def signin(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,message="Ro'yxatdan o'tdiz")
            return render(request,'anketa.html')
        else:
            messages.error(request, message='Username yoki parolda xatolik bor ...')


    else:
        form = UserCreationForm()



    return render(request, 'sign in.html',{'form':form})

def anketa(request):
    return render(request,'anketa.html')

def loginn(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            messages.warning(request, "Login Error !! Username or Password is incorrect")
            return HttpResponseRedirect('/login')
    else:
        form = AuthenticationForm()
    return render(request,'log in.html',{"form":form})
def logoutt(request):
    logout(request)
    return HttpResponseRedirect('/')
def single(request,id):

    if 'Name' in request.POST:
        ism = request.POST.get('Name')
        mail = request.POST.get('Email')
        tel = request.POST.get('Telephone')
        matn = request.POST.get('Review')
        tur = request.POST.get('tur')
        idlar = [0]
        textt = Comment.objects.all()

        for i in textt:
            idlar.append(i.id)

        Comment(max(idlar) + 1, ism, mail, tel, matn,tur).save()
    maxsulot = Product.objects.get(id=id)
    max_tur = maxsulot.tur
    commentlar = Comment.objects.filter(tur=max_tur)
    raqamlar = Sotib_olingan_maxsulotlar.objects.all()
    soni = 0
    for i in raqamlar:
        soni += int(i.miqdori)
    return render(request,'single.html',{"maxsulot":maxsulot,'comments':commentlar,'soni':soni})



def deletee(request,id):
    idlar = [0]
    user_id = request.user.id
    maxx = Sotib_olingan_maxsulotlar.objects.filter(mijoz_id=user_id)
    for i in maxx:
        idlar.append(i.id)
    
    if int(id) in idlar:
        maxsulot = Sotib_olingan_maxsulotlar.objects.get(id=id)
        if int(maxsulot.miqdori)>1:
            max_nomi = Sotib_olingan_maxsulotlar.objects.get(id=id)
            max_miqdori =int( max_nomi.miqdori)
            max_miqdori -= 1
            nomi = maxsulot.nomi
            user_id = request.user.id
            username = User.objects.get(id=user_id)
            username = str(username)
            narxi = maxsulot.narxi/maxsulot.miqdori * max_miqdori

            Sotib_olingan_maxsulotlar(id, nomi, narxi, max_miqdori, username, user_id).save()
        else:
            maxsulot = Sotib_olingan_maxsulotlar.objects.get(id=id).delete()

    user_id = request.user.id

    maxx = Sotib_olingan_maxsulotlar.objects.filter(mijoz_id = user_id)
    
       
   

    summa = 0
    mobiles =  Sotib_olingan_maxsulotlar.objects.filter(mijoz_id = user_id)
    for mobile in mobiles:
        summa += int(mobile.narxi)
    summa = format(summa, ',')
    basket = Sotib_olingan_maxsulotlar.objects.filter(mijoz_id=user_id)
    return render(request, 'korzinka.html', {'basket': basket,'summa':summa})
    