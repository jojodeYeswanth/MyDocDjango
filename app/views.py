from django.views.generic import TemplateView
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from app.forms import SignUpForm, AddDoctorForm, AppointmentForm
from django.views import generic
from app.models import AddDoctor, Appointment
from django.views.generic import DetailView
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView

class HomePageView(TemplateView) :
	template_name = 'index.html'
class PaymentPageView(TemplateView):
    template_name = 'payment.html'
class PaymentConfirmPageView(TemplateView):
    template_name = 'confirmation.html'
class BookPageView(TemplateView):
    template_name = 'app.html'

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            User = authenticate(username=username, password=raw_password)
            login(request, User)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


class DocListView(generic.ListView):
    model = AddDoctor
    context_object_name = 'doc_list'
    template_name = 'doctor.html'

    def get_queryset(self):
        return AddDoctor.objects.order_by('Doctor_Name')

class DocDetailView(DetailView):
    model = AddDoctor
    template_name = 'book.html'

def AddDoctorView(request):
    if request.method == 'POST':
        form = AddDoctorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddDoctorForm()
    return render(request, 'adddoctor.html', {'form': form})

def AddAppointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('payment')
    else:
        form = AppointmentForm()
    return render(request, 'app.html', {'form': form})

class AppointmentListView(generic.ListView):
    model = Appointment
    context_object_name = 'app_list'
    template_name = 'profile.html'

    def get_queryset(self):
        return Appointment.objects.filter(first_name=self.request.user)

class AppointmentDelete(DeleteView):
    model = Appointment
    template_name = 'delete_app.html'
    success_url = reverse_lazy('profile')