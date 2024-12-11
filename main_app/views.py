from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Reflection

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def reflections_index(request):
    reflections = Reflection.objects.all()
    return render(request, 'reflections/index.html', {'reflections': reflections})

def reflection_detail(request, reflection_id):
    reflection = Reflection.objects.get(id=reflection_id)
    return render(request, 'reflections/detail.html', {'reflection': reflection})

class ReflectionCreate(CreateView):
    model = Reflection
    fields = '__all__'

class ReflectionUpdate(UpdateView):
    model=Reflection
    fields='__all__'

class ReflectionDelete(DeleteView):
    model=Reflection
    success_url='/reflections/'