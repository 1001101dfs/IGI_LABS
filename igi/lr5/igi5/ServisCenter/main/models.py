from django.db import models

class Contacts(models.Model):
    full_name = models.TextField('ФИО')
    phone = models.TextField('Номер телефона')
    description = models.TextField('Описание выполняемыхх работ')
    img = models.ImageField(upload_to='article', null=True)

    class Meta:
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'

class FAQ(models.Model):
    question = models.TextField('Вопрос')
    answer = models.TextField('Ответ')
    date = models.DateField('Дата добавления')

    class Meta:
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQ'

class News(models.Model):
    title = models.TextField('Заголовок')
    text = models.TextField('Текст')

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

class Vacancion(models.Model):
    title = models.TextField('Заголовок')
    text = models.TextField('Текст')

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'

class Discount(models.Model):
    title = models.TextField('Заголовок')
    text = models.TextField('Текст')

    class Meta:
        verbose_name = 'Скидка'
        verbose_name_plural = 'Скидки'

class User(models.Model):
    login = models.TextField('Логин')
    password = models.TextField('Пароль')
    fullName = models.TextField('ФИО')
    phone = models.TextField('ФИО')
    pasport = models.TextField('Паспорт')
    administrator = models.BooleanField('Работник', default=False)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

class RequestId(models.Model):
    idReq = models.IntegerField('Id заказа', null=True)
    UserId = models.IntegerField('Id пользователя')
    cost = models.IntegerField('Стоимость')
    ready = models.BooleanField("Заказ выполнен", default=False)

    class Meta:
        verbose_name = 'RequestId'
        verbose_name_plural = 'RequestId'

class Request(models.Model):
    requestId = models.IntegerField('Id заказа')
    JobId = models.IntegerField("Id услуги")

    class Meta:
        verbose_name = 'Request'
        verbose_name_plural = 'Request'
class Job(models.Model):
    idJob = models.IntegerField('id улсги', null=True)
    text = models.TextField('Услуга')
    cost = models.IntegerField('Цена')

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

class Comment(models.Model):
    UserName = models.TextField('ФИО пользователя')
    text = models.TextField('Текст комментария')
    data = models.DateTimeField('Время комментария')
    mark = models.IntegerField('Оценка')

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'



class Time(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Report(models.Model):
    text = models.TextField('Отчёт')
    userId = models.IntegerField('Id работника')

    class Meta:
        verbose_name = 'Отчёт'
        verbose_name_plural = 'Отчёты'
