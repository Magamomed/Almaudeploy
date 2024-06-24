# myapp/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .forms import ApplicationForm
from django.http import HttpResponse
from .forms import InterviewScheduleForm
from .models import InterviewSchedule, Application
from .forms import EventForm
from .models import Event, Application, EventRegistration
from django.contrib import messages




def home(request):
    return render(request, 'home.html')


def application_form(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            print("Form is valid")
            form.save()
            return redirect('success')
        else:
            print("Form is not valid")
            print(form.errors)
    else:
        form = ApplicationForm()
    return render(request, 'application_form.html', {'form': form})




def schedule_interview(request):
    if request.method == 'POST':
        form = InterviewScheduleForm(request.POST)
        if form.is_valid():
            schedule = form.save(commit=False)
            try:
                application = Application.objects.get(email=request.POST.get('email'))
                schedule.application = application
                schedule.save()
                messages.success(request, 'Вы успешно записались на собеседование!')
                return redirect('success')
            except Application.DoesNotExist:
                messages.error(request, 'Анкета с таким email не найдена.')
        else:
            messages.error(request, 'Пожалуйста, исправьте ошибки в форме.')
    else:
        form = InterviewScheduleForm()
    return render(request, 'schedule_interview.html', {'form': form})





def schedule_event(request):
    events = Event.objects.all()
    return render(request, 'schedule_event.html', {'events': events})

def event_detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    if request.method == 'POST':
        # Логика записи на мероприятие
        application = Application.objects.latest('id')  # Это нужно адаптировать под вашу логику
        EventRegistration.objects.create(event=event, application=application)
        return redirect('success')
    return render(request, 'event_detail.html', {'event': event})

def success(request):
    return render(request, 'success.html')