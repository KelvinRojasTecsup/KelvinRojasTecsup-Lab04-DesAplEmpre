from django.shortcuts import render
from .models import Receta

# Create your views here.
def index(request):
    latest_question_list = Receta.objects.all()
    context = {
        'latest_question_list':latest_question_list
    }
    return render(request,'recetas/index.html',context)

# Create your views here.
