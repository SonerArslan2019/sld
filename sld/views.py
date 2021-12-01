from django.shortcuts import render


def detail_view(request, id):
    return render(request, 'sld/detail.html')


def create_view(request):
    return render(request, 'sld/create.html')


def list_view(request):
    return render(request, 'sld/list.html')


def make_pdf(request, id):
    return render(request, 'sld/pdf.html')


def send_mail(request, id):
    return render(request, 'sld/mail.html')
