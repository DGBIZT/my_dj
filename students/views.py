from django.contrib.messages.api import success
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import ListView, DeleteView, UpdateView, DetailView
from students.models import Student, MyModel
# Create your views here.

class MyModelCreteView(CreateView):
    model = MyModel
    fields = ['name', 'description']
    template_name = 'students/mymodel_form.html'
    success_url = reverse_lazy('students:mymodel_list')


class MyModelListView(ListView):
    model = MyModel
    template_name = 'students/mymodel_list.html'
    context_object_name = 'mymodels'

class MyModelDetailView(DetailView):
    model = MyModel
    TemplateName = 'students/mymodel_detail.html'
    context_object_name = 'mymodel'

class MyModelUpdateView(UpdateView):
    model = MyModel
    fields = ['name', 'description']
    template_name = 'students/mymodel_form.html'
    success_url = reverse_lazy('students:mymodel_list')

class MyModelDeleteView(DeleteView):
    model = MyModel
    template_name = 'students/mymodel_confirm_delete.html'
    success_url = reverse_lazy('students:mymodel_list')



def about(request):
    return render(request, 'students/about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        message = request.POST.get('message')

        return HttpResponse(f'Спасибо, {name}! Сообщение получено.')

    return render(request, 'students/contact.html')

def example_view(request):
    return render(request, 'students/example.html')

def index(request):
    student = Student.objects.get(id=1)
    context = {
        'student_name': f'{student.first_name} {student.last_name}',
        'student_year': student.get_year_display(),
    }
    return render(request, 'students/index.html', context=context)

def student_detail(request, student_id):
    student = Student.objects.get(id=student_id)
    context = {
        'student': student,
    }
    return render(request, 'students/student_detail.html', context=context)

def student_list(request):
    students = Student.objects.all()
    context = {
        'students': students,
    }
    return render(request, 'students/student_list.html', context=context)
def home(request):
    student = Student.objects.all()
    context = {
        'student': student,
    }
    return render(request, 'students/home.html', context=context)

def base(request):
    student = Student.objects.all()
    context = {
        'student': student,
    }
    return render(request, 'students/base.html', context=context)

def header(request):
    student = Student.objects.all()
    context = {
        'student': student,
    }
    return render(request, 'students/header.html', context=context)