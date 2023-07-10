from django.shortcuts import render

from sayt.models import Contact


# Create your views here.


def index(requests):
    ctx = {}
    if requests.POST:
        email = requests.POST.get('email')
        message = requests.POST.get('message')
        password = requests.POST.get('password')
        Contact.objects.create(
            email=email, message=message, password=password
        )

        ctx = {
            "contact": index,

        }
    return render(requests, "index.html", ctx)