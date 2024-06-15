from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Smena(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False, verbose_name="Название смены")
    start_at = models.DateField(null=False, blank=False, verbose_name="Начало")
    end_at = models.DateField(null=False, blank=False, verbose_name="Конец")
    is_curent = models.BooleanField(verbose_name="Текущая смена")

    def __str__(self):
        return f"Смена '{self.title}' ({self.start_at})"

    class Meta:
        verbose_name="Смена"
        verbose_name_plural="Смены"


class Party(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False, verbose_name="Название отряда")
    smena = models.ForeignKey(Smena, models.CASCADE, related_name="partys", null=False, blank=False, verbose_name="Смена")
    
    def __str__(self):
        return f"{self.smena} {self.title}"

    class Meta:
        verbose_name="Отряд"
        verbose_name_plural="Отряды"
        ordering = ["smena__start_at"]


class SocialOption(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False, verbose_name="Название")
    
    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name="Социальный статус"
        verbose_name_plural="Социальные статусы"


class StudyPlaceOption(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False, verbose_name="Название")

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name="Тип учереждения образования"
        verbose_name_plural="Типы учереждений образования"


SEX_CHOISE = [
    ("M","Мужской"),
    ("F","Женский"),
]

REGION_CHOISE = [
    ("1","Брестская область"),
    ("2","Витебская область"),
    ("3","Гомельская область"),
    ("4","Гродненская область"),
    ("5","Минская область"),
    ("5","Могилевская область"),
    ("6","Город Минск"),
]

class Child(models.Model):
    first_name = models.CharField(max_length=255, null=False, blank=False, verbose_name="Имя")
    second_name = models.CharField(max_length=255, null=False, blank=False, verbose_name="Фамилия")
    third_name = models.CharField(max_length=255, null=True, blank=True, verbose_name="Отчество")
    
    party = models.ManyToManyField(Party, verbose_name="Отряд")

    sex = models.CharField(max_length=1, null=True, blank=True, choices=SEX_CHOISE, verbose_name="Пол")
    birth_date = models.DateField(null=True, blank=True, verbose_name="Дата рождения")
    phone_number = PhoneNumberField(null=True, blank=True, verbose_name="Номер телефона")

    live_place_full = models.CharField(max_length=255, null=True, blank=True, verbose_name="Место жительства (полностью)")
    region = models.CharField(max_length=1, null=True, blank=True, choices=REGION_CHOISE, verbose_name="Область")
    from_city = models.BooleanField(verbose_name="Из города")

    study_place_full = models.CharField(max_length=255, null=True, blank=True, verbose_name="Место обучение (полностью)")
    study_place_type = models.ForeignKey(StudyPlaceOption, models.CASCADE, related_name="childrens", null=True, blank=True, verbose_name="Тип учебного заведения" )

    order_number = models.CharField(max_length=255, null=True, blank=True, verbose_name="Номер путевки")
    order_state = models.CharField(max_length=255, null=True, blank=True, verbose_name="Кем выдана")

    social_type = models.ForeignKey(SocialOption, models.CASCADE, related_name="childrens", null=True, blank=True, verbose_name="Социальный статус" )
   
    mother_full_name = models.CharField(max_length=255, null=True, blank=True, verbose_name="Полное имя матери")
    mother_birth_date = models.DateField(null=True, blank=True, verbose_name="Дата рождения матери")
    mother_work = models.CharField(max_length=255, null=True, blank=True, verbose_name="Место работы матери")
    mother_post = models.CharField(max_length=255, null=True, blank=True, verbose_name="Должность матери")
    mother_phone = PhoneNumberField(null=True, blank=True, verbose_name="Номер телефона матери")
    
    father_full_name = models.CharField(max_length=255, null=True, blank=True, verbose_name="Полное имя отца")
    father_birth_date = models.DateField(null=True, blank=True, verbose_name="Дата рождения отца")
    father_work = models.CharField(max_length=255, null=True, blank=True, verbose_name="Место работы отца")
    father_post = models.CharField(max_length=255, null=True, blank=True, verbose_name="Должность отца")
    father_phone = PhoneNumberField(null=True, blank=True, verbose_name="Номер телефона отца")
    
    comment = models.TextField(null=True, blank=True, verbose_name="Комментарий")

    def __str__(self):
        return f"{self.second_name} {self.first_name} {self.third_name}"

    class Meta:
        verbose_name="Воспитаник"
        verbose_name_plural="Воспитаники"
        ordering = ["second_name","first_name","third_name"]