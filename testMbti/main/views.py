from django.shortcuts import render
from .models import Foreword
from .models import Strings
from django.http import HttpResponse
# Create your views here.


def index(request):
    forewords = Foreword.objects.all()
    return render(request, 'main/index.html', {'year': Strings.year, 'forewords':forewords, 'header':Strings.header, 'buttonStart':Strings.start })
