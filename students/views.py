from django.shortcuts import render
from django.http import HttpResponse
from students.models import Student
# Create your views here.

# def example_view(request):
#     return render(request, 'app/example.html')
#
# def show_data(request):
#     if request.method == 'GET':
#         return render(request, 'app/show_data.html')
#
# def submit_data(request):
#     # request.GET
#     # request.POST
#     if request.method == 'POST':
#         return  HttpResponse("Данные отправлены")
#
#
# def show_item(request, item_id):
#     return render(request, 'app/item.html', {'item_id': item_id})
#


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

def student_detail(request):
    student = Student.objects.get(id=2)
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