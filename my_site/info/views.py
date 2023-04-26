from django.shortcuts import render,  redirect
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth import  logout
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Task
from .forms import  RegistrationForm , LoginForm
from django.contrib.auth.views import LoginView
from django.views.generic import ListView, CreateView,UpdateView, View, DetailView, DeleteView

# Create your views here.

class IndexView(ListView):
    model = Task
    template_name = 'base.html'
    context_object_name = 'tasks'
    
    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user.id)


class TaskView(ListView):
    model = Task
    template_name = 'task.html'
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = Task.objects.all()
        return context  


class TaskDetailView(DetailView):
    model = Task
    template_name  = 'info/view.html'
    context_object_name  = 'task' 
    pk_url_kwarg = 'task_id'   


class TaskCreateView(LoginRequiredMixin,CreateView):
    model = Task
    template_name = 'info/create.html'
    fields =  ['title', 'description']
    success_url = reverse_lazy('index')
    login_url =  reverse_lazy('login')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class TaskUpdateView(LoginRequiredMixin,UpdateView):
    model = Task
    template_name = 'info/update.html'
    fields = ['title', 'description', 'completed']
    success_url = reverse_lazy('index')
    login_url = reverse_lazy('login')


   


class DeleteTaskView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'info/delete.html'
    success_url = reverse_lazy('index')
    pk_url_kwarg = 'task_pk'
    login_url = reverse_lazy('login')



class RegistrationView(View):
    form_class = RegistrationForm
    template_name = 'info/register.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        return render(request, self.template_name, {'form': form})
    
# Этот код определяет класс RegistrationView, который наследуется от View, в Django. 
# Он использует UserCreationForm из django.contrib.auth.forms для создания формы регистрации пользователя.
# form_class определяет класс формы, который используется в представлении.
# template_name определяет имя шаблона, которое будет использоваться для отображения страницы регистрации.
# get метод создает объект UserCreationForm и передает его в шаблон registration.html, который будет использоваться для отображения страницы регистрации.
# post метод проверяет, была ли отправлена форма, и если да, то создает объект UserCreationForm на основе данных, отправленных пользователем. 
# Если форма прошла проверку на валидность, то создается новый пользователь на основе данных, введенных в форму.
# После этого происходит перенаправление пользователя на страницу входа (login).
# Если форма не прошла проверку на валидность, то она возвращается обратно в шаблон registration.html для отображения ошибок.

class AuthLoginView(LoginView):
    authentication_form = LoginForm
    template_name = 'info/login.html'


    def get_success_url(self):
        return reverse_lazy('index')


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')