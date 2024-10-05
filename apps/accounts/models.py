from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError


from apps.accounts.utils.address_utils import get_address, extract_coordinates
from apps.accounts.utils.phone_utils import ValidPhone


class CustomUser(AbstractUser):
    image = models.ImageField(upload_to='users_images/', null=True, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class Address(models.Model):
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
        help_text='Пользователь, которому принадлежит этот адрес'
    )

    geo_url = models.URLField(
        verbose_name='URL геолокации',
        help_text='Скопируйте URL из приложения 2GIS, Google Maps или Яндекс.Карты'
    )

    country = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name='Страна',
        help_text='Название страны'
    )
    city = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name='Город',
        help_text='Название города'
    )
    city_district = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name='Район',
        help_text='Название района (если применимо)'
    )
    street = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name='Улица',
        help_text='Название улицы'
    )

    postcode = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        verbose_name='Почтовый индекс',
        help_text='Почтовый индекс'
    )

    latitude = models.FloatField(
        default=0.0,
        blank=True,
        null=True,
        verbose_name='Широта',
        help_text='Координаты широты для местоположения'
    )
    longitude = models.FloatField(
        default=0.0,
        blank=True,
        null=True,
        verbose_name='Долгота',
        help_text='Координаты долготы для местоположения'
    )

    address = models.TextField(
        blank=True,
        null=True,
        verbose_name='Адрес',
        help_text='Полный адрес в текстовом виде'
    )

    def __str__(self):
        return f"{self.user.username}'s address"

    def clean(self):

        if '2gis' in self.geo_url or 'google' in self.geo_url or 'yandex' in self.geo_url:
            pass
        else:
            raise ValidationError(
                'Скопируйте URL из приложения 2GIS, Google Maps или Яндекс.Карты')

        super().clean()

    def save(self, *args, **kwargs) -> None:

        if self.geo_url:
            coordinates = extract_coordinates(self.geo_url)

            if coordinates:
                self.latitude, self.longitude = coordinates

            address_info = get_address(self.latitude, self.longitude)
            self.country = address_info[1].get(
                'country', '') if address_info else None
            self.city = address_info[1].get(
                'city', '') if address_info else None
            self.city_district = address_info[1].get(
                'city_district', '') if address_info else None
            self.street = address_info[1].get(
                'road', '') if address_info else None
            self.postcode = address_info[1].get(
                'postcode', '') if address_info else None
            self.address = address_info[0] if address_info else None

        else:
            raise ValidationError(
                'Скопируйте URL из приложения 2GIS, Google Maps или Яндекс.Карты')

        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'


class Phone(models.Model):
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
        help_text='Пользователь, которому принадлежит этот телефонный номер'
    )
    phone = models.CharField(
        max_length=20,
        verbose_name='Номер телефона',
        help_text='Основной номер телефона, включая код страны, если применимо'
    )
    phone_country = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name='Страна',
        help_text='Страна, где зарегистрирован телефонный номер'
    )
    phone_type = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        verbose_name='Тип телефона',
        help_text='Тип телефона (например, мобильный, домашний, рабочий)'
    )
    phone_local = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        verbose_name='Локальный номер',
        help_text='Локальный номер без международного кода'
    )
    phone_international = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        verbose_name='Международный номер',
        help_text='Полный международный номер телефона'
    )
    phone_carrier = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name='Оператор связи',
        help_text='Оператор связи или провайдер телефонных услуг'
    )
    phone_prefix = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        verbose_name='Префикс',
        help_text='Префикс телефонного номера, например, код города'
    )
    phone_code = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        verbose_name='Код',
        help_text='Код телефонного номера (например, код страны или области)'
    )

    def __str__(self):
        return f"{self.user.username}'s phone number"

    def clean(self) -> None:
        phone_number = ValidPhone(self.phone)
        data = phone_number.information_about_the_phone_number()

        if data.get('valid'):
            self.phone_country = data.get('location', '')
            self.phone_type = data.get('type', '')
            self.phone_local = data.get('format').get(
                'local', '') if data.get('format', False) else ''
            self.phone_international = data.get('format').get(
                'international', '') if data.get('format', False) else ''
            self.phone_carrier = data.get('carrier', '')
            self.phone_prefix = data.get('country').get(
                'prefix', '') if data.get('country', False) else ''
            self.phone_code = data.get('country').get(
                'code', '') if data.get('country', False) else ''
            self.save()
        else:
            raise ValidationError('Номер телефона не валиден')

        return super().clean()

    class Meta:
        verbose_name = 'Телефонный номер'
        verbose_name_plural = 'Телефонные номера'
