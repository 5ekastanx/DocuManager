# Generated by Django 5.1.1 on 2024-10-03 10:05

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('image', models.ImageField(blank=True, null=True, upload_to='users_images/')),
                ('age', models.PositiveIntegerField(blank=True, null=True)),
                ('is_verified', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geo_url', models.URLField(help_text='Скопируйте URL из приложения 2GIS, Google Maps или Яндекс.Карты', verbose_name='URL геолокации')),
                ('country', models.CharField(blank=True, help_text='Название страны', max_length=100, null=True, verbose_name='Страна')),
                ('city', models.CharField(blank=True, help_text='Название города', max_length=100, null=True, verbose_name='Город')),
                ('city_district', models.CharField(blank=True, help_text='Название района (если применимо)', max_length=100, null=True, verbose_name='Район')),
                ('street', models.CharField(blank=True, help_text='Название улицы', max_length=100, null=True, verbose_name='Улица')),
                ('postcode', models.CharField(blank=True, help_text='Почтовый индекс', max_length=20, null=True, verbose_name='Почтовый индекс')),
                ('latitude', models.FloatField(blank=True, default=0.0, help_text='Координаты широты для местоположения', null=True, verbose_name='Широта')),
                ('longitude', models.FloatField(blank=True, default=0.0, help_text='Координаты долготы для местоположения', null=True, verbose_name='Долгота')),
                ('address', models.TextField(blank=True, help_text='Полный адрес в текстовом виде', null=True, verbose_name='Адрес')),
                ('user', models.ForeignKey(help_text='Пользователь, которому принадлежит этот адрес', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Адрес',
                'verbose_name_plural': 'Адреса',
            },
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(help_text='Основной номер телефона, включая код страны, если применимо', max_length=20, verbose_name='Номер телефона')),
                ('phone_country', models.CharField(blank=True, help_text='Страна, где зарегистрирован телефонный номер', max_length=100, null=True, verbose_name='Страна')),
                ('phone_type', models.CharField(blank=True, help_text='Тип телефона (например, мобильный, домашний, рабочий)', max_length=20, null=True, verbose_name='Тип телефона')),
                ('phone_local', models.CharField(blank=True, help_text='Локальный номер без международного кода', max_length=20, null=True, verbose_name='Локальный номер')),
                ('phone_international', models.CharField(blank=True, help_text='Полный международный номер телефона', max_length=20, null=True, verbose_name='Международный номер')),
                ('phone_carrier', models.CharField(blank=True, help_text='Оператор связи или провайдер телефонных услуг', max_length=100, null=True, verbose_name='Оператор связи')),
                ('phone_prefix', models.CharField(blank=True, help_text='Префикс телефонного номера, например, код города', max_length=20, null=True, verbose_name='Префикс')),
                ('phone_code', models.CharField(blank=True, help_text='Код телефонного номера (например, код страны или области)', max_length=20, null=True, verbose_name='Код')),
                ('user', models.ForeignKey(help_text='Пользователь, которому принадлежит этот телефонный номер', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Телефонный номер',
                'verbose_name_plural': 'Телефонные номера',
            },
        ),
    ]
