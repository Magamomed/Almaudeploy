from django.contrib import admin
from .models import Application, Speciality, InterviewSchedule, Event, EventRegistration, Schedule


@admin.register(Speciality)
class SpecialityAdmin(admin.ModelAdmin):
    list_display = ('name', 'school')
    search_fields = ('name', 'school')

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('fio', 'city', 'school', 'student_class', 'phone', 'email', 'parent_fio')
    search_fields = ('fio', 'city', 'school', 'phone', 'email', 'parent_fio')
    filter_horizontal = ('specialties',)
    


@admin.register(InterviewSchedule)
class InterviewScheduleAdmin(admin.ModelAdmin):
    list_display = ('get_application_fio', 'get_application_email', 'date')
    search_fields = ('application__fio', 'application__email', 'date')

    def get_application_fio(self, obj):
        return obj.application.fio if obj.application else 'No Application'
    get_application_fio.short_description = 'Applicant FIO'

    def get_application_email(self, obj):
        return obj.application.email if obj.application else 'No Email'
    get_application_email.short_description = 'Email'


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('school_name', 'date_time', 'format', 'location')
    list_filter = ('school_name', 'format')
    search_fields = ('school_name', 'location')


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    search_fields = ('title', 'date')

@admin.register(EventRegistration)
class EventRegistrationAdmin(admin.ModelAdmin):
    list_display = ('event', 'application', 'registration_date')
    search_fields = ('event__title', 'application__fio', 'registration_date')
