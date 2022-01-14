from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.views import login_required
from django.contrib.messages import success, error
from .models import SldModel
from .forms import SldForm


@login_required
def isEmri_goruntule(request, id):
    is_emri = get_object_or_404(SldModel, id=id)

    return render(request, 'sld/isEmri_goruntule.html', context={'is_emri': is_emri})


@login_required
def isEmri_olustur(request):
    if request.method == 'POST':
        form = SldForm(request.POST)

        if form.is_valid():
            form_ornek = form.save(commit=False)
            form_ornek.user = request.user
            form_ornek.save()
            success(request, f'{form_ornek.crm} başarıyla oluşturuldu.')
            return redirect('sld:isEmri_listele')
        else:
            error(request, 'Lütfen formu eksiksiz doldurduğunuza emin olun!')
    elif request.method == 'GET':
        form = SldForm()
    return render(request, 'sld/isEmri_olustur.html', {'form': form})


@login_required
def isEmri_listele(request):
    return render(request, 'sld/isEmri_listele.html', {'list': SldModel.objects.all()})


@login_required
def pdf_olustur(request):
    return render(request, 'sld/pdf_olustur.html')


@login_required
def mail_gonder(request):
    return render(request, 'sld/mail_gonder.html')
