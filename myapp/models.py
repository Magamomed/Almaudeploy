# myapp/models.py

from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File
import random
import string
from django.contrib.auth.models import User


    
SCHOOL_CHOICES = [
    ('School of Management', 'Школа Менеджмента'),
    ('School of Economics and Finance', 'Школа Экономики и Финансов'),
    ('School of Politics and Law', 'Школа Политики и Права'),
    ('Urbanism Center', 'Центр Урбанистики'),
    ('School of Hospitality and Tourism', 'Школа Гостеприимства и Туризма'),
    ('School of Digital Technologies', 'Школа Цифровых Технологий'),
    ('School of Entrepreneurship and Innovation', 'Школа Предпринимательства и Инноваций'),
    ('School of Media and Cinema', 'Школа Медиа и Кино'),
    ('Sharmanov School of Health Sciences', 'Sharmanov School of Health Sciences'),
    ('Sports Management Center', 'Центр Спортивного Менеджмента'),
]

class Speciality(models.Model):
    school = models.CharField(max_length=100)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.school}: {self.name}"

class Application(models.Model):
    fio = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    school = models.CharField(max_length=100)
    student_class = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    telegram = models.CharField(max_length=255, blank=True, null=True)
    instagram = models.CharField(max_length=255, blank=True, null=True)
    parent_contacts = models.CharField(max_length=255)
    parent_fio = models.CharField(max_length=255)
    university = models.TextField()
    specialties = models.ManyToManyField(Speciality, blank=True)
    language_kaz = models.BooleanField(default=False)
    language_rus = models.BooleanField(default=False)
    language_eng = models.BooleanField(default=False)

    def __str__(self):
        return self.fio

class InterviewSchedule(models.Model):
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return f"{self.application.fio} - {self.date}"
    



class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    banner_image = models.ImageField(upload_to='event_banners/', blank=True, null=True)

    def __str__(self):
        return self.title
    




class EventRegistration(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.application.fio} - {self.event.title}"
    

class ApplicationSpeciality(models.Model):
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    speciality = models.ForeignKey(Speciality, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('application', 'speciality')



