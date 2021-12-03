from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.messages import success, error
from .models import SldModel
from .forms import SldForm


def isEmri_goruntule(request, id):
    is_emri = get_object_or_404(SldModel, id=id)

    return render(request, 'sld/isEmri_goruntule.html', context={'is_emri': is_emri})


def isEmri_olustur(request):
    if request.method == 'POST':
        form = SldForm(request.POST)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            success(request, f'{instance.crm} başarıyla oluşturuldu.')
            return redirect('sld:isEmri_listele')
        else:
            error(request, 'Lütfen formu eksiksiz doldurduğunuza emin olun!')
    elif request.method == 'GET':
        form = SldForm()
    context = {'form': form}
    return render(request, 'sld/isEmri_olustur.html', context)


def isEmri_listele(request):
    return render(request, 'sld/isEmri_listele.html', {'list': SldModel.objects.all()})


def pdf_olustur(request):
    return render(request, 'sld/pdf_olustur.html')


def mail_gonder(request):
    return render(request, 'sld/mail_gonder.html')


def sld_home(request):
    return render(request, 'sld/sld_home.html')


def giris_sayfasi(request):
    return render(request, 'sld/giris_sayfasi.html')
