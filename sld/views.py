from django.shortcuts import render


def detail_view(request):
    return render(request, 'sld/detail.html')


def create_view(request):
    return render(request, 'sld/create.html')


def list_view(request):
    return render(request, 'sld/list.html')


def make_pdf(request):
    return render(request, 'sld/pdf.html')


def send_mail(request):
    return render(request, 'sld/mail.html')


def home(request):
    return render(request, 'sld/home.html')


def ana_sayfa(request):
    return render(request, 'sld/ana_sayfa.html')
