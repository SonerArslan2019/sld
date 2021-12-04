from django.shortcuts import render, redirect


def giris_sayfasi(request):
    if request.user.is_authenticated:
        return redirect('home:genel_kapilar')
    return render(request, 'giris_sayfasi.html')


def genel_kapilar(request):
    return render(request, 'genel_kapilar.html')


def sld_kapilar(request):
    return render(request, "kapilar/sld_kapilar.html")


def hata_401(request):
    return render(request, 'hata_401.html', {})
