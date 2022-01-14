from django.template import loader
from django.urls import reverse
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from wikipedia_converter.models import User


def get_create_user(request):
    template = loader.get_template('registration/create_user.html')

    context = {}

    return HttpResponse(template.render(context, request))


def create_user(request):
    user = User.objects.create_user(username=request.POST["username"], password=request.POST["password"])
    user.save()

    return HttpResponseRedirect("login")
