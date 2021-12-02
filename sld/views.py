from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.messages import success, error
from .models import SldModel
from .forms import SldForm


def detail_view(request, id):
    is_emri = get_object_or_404(SldModel, id=id)

    return render(request, 'sld/detail.html', context={'is_emri': is_emri})


def create_view(request):
    if request.method == 'POST':
        form = SldForm(request.POST)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            success(request, f'{instance.crm} başarıyla oluşturuldu.')
            return redirect('sld:list')
        else:
            error(request, 'Lütfen formu eksiksiz doldurduğunuza emin olun!')
    elif request.method == 'GET':
        form = SldForm()
    context = {'form': form}
    return render(request, 'sld/create.html', context)


def list_view(request):
    return render(request, 'sld/list.html', {'list': SldModel.objects.all()})


def make_pdf(request):
    return render(request, 'sld/pdf.html')


def send_mail(request):
    return render(request, 'sld/mail.html')


def home(request):
    return render(request, 'sld/home.html')


def ana_sayfa(request):
    return render(request, 'sld/ana_sayfa.html')
