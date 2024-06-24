from myapp.models import Speciality

specialities = [
    ('Школа Менеджмента', 'Менеджмент'),
    ('Школа Менеджмента', 'Логистика'),
    ('Школа Менеджмента', 'Маркетинг'),
    ('Школа Менеджмента', 'Digital marketing'),
    ('Школа Менеджмента', 'Digital Logistics'),
    ('Школа Менеджмента', 'Content, Marketing and Data analysis'),
    ('Школа Экономики и Финансов', 'Учет и аудит'),
    ('Школа Экономики и Финансов', 'Бизнес аналитика и Экономика'),
    ('Школа Экономики и Финансов', 'Финансы'),
    ('Школа Экономики и Финансов', 'FinTech and AI'),
    ('Школа Политики и Права', 'Бизнес право (Юриспруденция)'),
    ('Школа Политики и Права', 'Международные отношения и экономика'),
    ('Центр Урбанистики', 'Урбанистика и сити-менеджмент'),
    ('Центр Урбанистики', 'City Management and Data analysis'),
    ('Школа Гостеприимства и Туризма', 'Ресторанное дело и гостиничный бизнес'),
    ('Школа Гостеприимства и Туризма', 'Tourism and Event Management'),
    ('Школа Гостеприимства и Туризма', 'Travel Management and Data analysis'),
    ('Школа Цифровых Технологий', 'Информационные системы'),
    ('Школа Цифровых Технологий', 'Software engineering'),
    ('Школа Цифровых Технологий', 'Product management'),
    ('Школа Цифровых Технологий', 'Data science'),
    ('Школа Цифровых Технологий', 'FinTech and AI'),
    ('Школа Цифровых Технологий', 'Content, Marketing and Data analysis'),
    ('Школа Цифровых Технологий', 'City Management and Data analysis'),
    ('Школа Цифровых Технологий', 'Travel Management and Data analysis'),
    ('Школа Предпринимательства и Инноваций', 'Бизнес-администрирование в области предпринимательства'),
    ('Школа Медиа и Кино', 'Digital filmmaking'),
    ('Школа Медиа и Кино', 'Acting for film'),
    ('Школа Медиа и Кино', 'New Media'),
    ('Школа Медиа и Кино', 'Связь с общественностью (PR)'),
    ('Школа Медиа и Кино', 'Content, Marketing and Data analysis'),
    ('Sharmanov School of Health Sciences', 'Психология'),
    ('Sharmanov School of Health Sciences', 'Психология и Кинезиология'),
    ('Центр Спортивного Менеджмента', 'Спортивный менеджмент')
]

for school, speciality in specialities:
    Speciality.objects.create(school=school, name=speciality)
