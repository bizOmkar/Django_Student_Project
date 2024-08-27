from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages 
from django.contrib.auth.mixins import LoginRequiredMixin



from .models import Student
from .models import Mark

# Create your views here.

class StudentsListView(ListView):
    model = Student
    context_object_name = 'all_students' #default 'sunlight_list' (modelname_list)
    ordering = ['id']
    template_name = 'index.html'
    
# def deatail_info(request, pk):
#     marks = Mark.objects.get(pk=pk)
#     return render(request, 'detail_info.html', {'marks':marks})

class StudentDetailView(DetailView):
    model = Mark
    context_object_name = 'marks'
    template_name = 'detail_info.html'
    
class StudentCreateView(LoginRequiredMixin, SuccessMessageMixin,CreateView):
    model = Student
    fields = '__all__'
    extra_context = {'extra_context':"this is a extra context"}
    template_name = 'new_student.html'
    success_message = "Student Enrolled successflly:"
    success_url = reverse_lazy('index')
    
class StudentUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Student 
    fields = '__all__'
    template_name = 'edit.html'
    success_message = "Student Detail Updated successflly"
    success_url = reverse_lazy('index')
    
class MarkUpdateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Mark 
    fields = '__all__'
    template_name = 'edit_marks.html'
    success_message = "Marks Updated successflly"
    success_url = reverse_lazy('index')


    
class StudentDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Student
    template_name = 'delete.html'
    success_message = "Student deleted successfully"
    success_url = reverse_lazy('index')




    

