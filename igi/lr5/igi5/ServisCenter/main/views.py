from django.shortcuts import render, redirect
from .models import FAQ, Contacts, News, Vacancion, Discount, User, Job, Request, RequestId, Comment, Time, Report
from django.contrib import messages
from django.db.models import Sum
import requests
import pytz
from datetime import datetime
import calendar
import re
from loguru import logger
from django.db.models import Count
from django.utils.dateparse import parse_date

def index(request):
    order = request.GET.get('order', 'asc')  # Получение параметра сортировки из запроса
    elements = Job.objects.all()
    if order == 'desc':
        elements = Job.objects.all().order_by('-cost')
    else:
        elements = Job.objects.all().order_by('cost')

    context = {
        'elements': elements,
        'order': order,
    }
    logger.debug("Rendering index page")
    return render(request, 'main/main.html', context)
def aboba(request):
    logger.debug("Rendering index page")
    return render(request, 'main/aboba.html')

def get_weather_data(lat, lon, api_key):
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}'

    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        return None


def get_random_dog_image():
    url = 'https://dog.ceo/api/breeds/image/random'

    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        return None
def index2(request):
    order = request.GET.get('order', 'asc')  # Получение параметра сортировки из запроса
    elements = Job.objects.all()
    if order == 'desc':
        elements = Job.objects.all().order_by('-cost')
    else:
        elements = Job.objects.all().order_by('cost')
    logger.debug("Rendering index page")
    let = 53.893009
    lon = 27.567444
    api_key = '866a6fbfa627aefa1cdbbcbfcb2e3e90'
    data = get_weather_data(let, lon, api_key)
    data1 = get_random_dog_image()
    context = {
        'data': data,
        'data1': data1,
        'elements': elements,
        'order': order,
    }

    return render(request, 'main/usermain.html', context)

def about(request):
    return render(request, 'main/about.html')

def about2(request):
    return render(request, 'main/userabout.html')

def login(request):
    if request.method == 'POST':
        login = request.POST.get('login')
        password = request.POST.get('password')

        try:
            user = User.objects.get(login=login, password=password)
            request.session['user_id'] = user.id
            if user.administrator:
                return redirect('employee')
            else:
                return redirect('usermain')
        except User.DoesNotExist:
            messages.error(request, 'Неправильный логин или пароль')
    return render(request, 'main/login.html')

def registration(request):
    return render(request, 'main/registration.html')



def news(request):
    new = News.objects.all()
    return render(request, 'main/news.html', {'new': new})

def news2(request):
    new = News.objects.all()
    return render(request, 'main/usernews.html', {'new': new})
def faq(request):
    Qanswer = FAQ.objects.all()
    return render(request, 'main/faq.html', {'Qanswer': Qanswer})
def faq2(request):
    Qanswer = FAQ.objects.all()
    return render(request, 'main/userfaq.html', {'Qanswer': Qanswer})
def contacts(request):
    Contact = Contacts.objects.all()
    return render(request, 'main/contacts.html', {'Contact': Contact})
def contacts2(request):
    Contact = Contacts.objects.all()
    return render(request, 'main/usercontacts.html', {'Contact': Contact})
def policy(request):
    return render(request, 'main/policy.html')
def policy2(request):
    return render(request, 'main/userpolicy.html')
def vacancies(request):
    vacancion = Vacancion.objects.all()
    return render(request, 'main/vacancies.html',{'vacancion': vacancion})
def vacancies2(request):
    vacancion = Vacancion.objects.all()
    return render(request, 'main/uservacancies.html',{'vacancion': vacancion})
def feedback(request):
    comments = reversed(Comment.objects.all())
    return render(request, 'main/feedback.html',{'comments': comments})
def feedback2(request):
    if request.method == 'POST':
        obj = User.objects.get(id=int(request.session.get('user_id')))
        name = obj.fullName
        comment = request.POST.get('comment')
        mark = request.POST.get('mark')

        if comment != '':
            Comment.objects.create(UserName=name, text=request.POST.get('comment'), data=datetime.now(), mark=request.POST.get('mark'))
    comments = reversed(Comment.objects.all())
    return render(request, 'main/userfeedback.html',{'comments': comments})

def discount(request):
    discounts = Discount.objects.all()
    return render(request, 'main/discounts.html',{'discounts': discounts})
def discount2(request):
    discounts = Discount.objects.all()
    return render(request, 'main/userdiscounts.html',{'discounts': discounts})
def contact_view(request):
    if request.method == 'POST':
        age_check = request.POST.get('ageCheck')
        selected_date_str = request.POST.get('date')
        if selected_date_str:
            selected_date = parse_date(selected_date_str)
            if selected_date:
                today = datetime.today().date()
                age = today.year - selected_date.year - (
                            (today.month, today.day) < (selected_date.month, selected_date.day))
                if age >= 18:
                    login = request.POST.get('login')
                    password = request.POST.get('password')
                    fullName = request.POST.get('secondName') + ' ' + request.POST.get('frstName') + ' ' + request.POST.get('lastName')
                    phone = request.POST.get('phone')
                    pasport = request.POST.get('pasport')

                    phone_pattern = re.compile(r'^\+375 \(29\) \d{3}-\d{2}-\d{2}$')

                    if not phone_pattern.match(phone):
                        error_message = "Введите телефон в формате +375 (29) XXX-XX-XX"
                        return render(request, 'main/registration.html', {'error_message': error_message})

                    # Создаем запись в базе данных
                    User.objects.create(login=login, password=password, fullName=fullName, phone=phone, pasport=pasport)

                    last_obj = User.objects.order_by('-id').first()
                    last_id = last_obj.id if last_obj else 0
                    request.session['user_id'] = last_id

                    return redirect('usermain')  # Перенаправление на страницу успеха после сохранения
    return render(request, 'main/registration.html')

def MyReques(request):
    if request.method == 'POST':

        selected_ids = request.POST.getlist('records')
        selected_records = Job.objects.filter(id__in=selected_ids)

        cost = selected_records.aggregate(total_cost=Sum('cost'))['total_cost']


        selected_ids_list = selected_records.values_list('id', flat=True)


        last_obj = RequestId.objects.order_by('-id').first()
        last_id = last_obj.id if last_obj else 0
        last_id += 1

        for job_id in selected_ids_list:
            Request.objects.create(requestId=RequestId.objects.count() + 1, JobId=job_id)

        RequestId.objects.create(idReq=RequestId.objects.count() + 1, UserId=int(request.session.get('user_id')), cost=cost)

    job = Job.objects.all()
    return render(request, 'main/request.html',{'job': job})

def userTime(request):
    # Получаем текущую дату и время в UTC
    utc_now = datetime.utcnow().replace(tzinfo=pytz.utc)

    # Предположим, что тайм зона пользователя хранится в настройках пользователя
    # Здесь для примера используем тайм зону 'Europe/Moscow'
    user_timezone = pytz.timezone('Europe/Moscow')
    user_time = utc_now.astimezone(user_timezone)

    # Получаем данные из базы данных
    data = Time.objects.all().values('name', 'created_at', 'updated_at')

    # Преобразуем даты для тайм зоны пользователя и для UTC
    data_list = []
    for item in data:
        created_at_utc = item['created_at']
        updated_at_utc = item['updated_at']
        item['created_at_user'] = created_at_utc.astimezone(user_timezone).strftime('%d/%m/%Y')
        item['created_at_utc'] = created_at_utc.strftime('%d/%m/%Y')
        item['updated_at_user'] = updated_at_utc.astimezone(user_timezone).strftime('%d/%m/%Y')
        item['updated_at_utc'] = updated_at_utc.strftime('%d/%m/%Y')
        data_list.append(item)

    # Генерация календаря на текущий месяц для тайм зоны пользователя
    cal = calendar.HTMLCalendar(calendar.SUNDAY)
    calendar_html = cal.formatmonth(user_time.year, user_time.month)

    # Формируем контекст для передачи в шаблон
    context = {
        'user_timezone': user_timezone,
        'user_time': user_time.strftime('%d/%m/%Y %H:%M:%S'),
        'utc_time': utc_now.strftime('%d/%m/%Y %H:%M:%S'),
        'data_list': data_list,
        'calendar_html': calendar_html,
    }

    return render(request, 'main/time.html', context)
def employee(request):
    if request.method == 'POST':
        text = request.POST.get('comment')
        if text != '':
            Report.objects.create(text=text, userId=int(request.session.get('user_id')))
    jobs = Job.objects.all()
    requests = Request.objects.all()

    most_frequent = Request.objects.values('JobId').annotate(count=Count('JobId')).order_by('-count').first()
    # Получаем самый частый requestId и количество его вхождений
    most_frequent_id = most_frequent['JobId'] if most_frequent else None
    most_frequent_count = most_frequent['count'] if most_frequent else 0

    context = {
        'jobs': jobs,
        'requests': requests,
        'most_frequent_id': most_frequent_id,
        'most_frequent_count': most_frequent_count,
    }
    return render(request, 'main/employee.html', context)

def order(request):
    requestIds = RequestId.objects.all()
    requests = Request.objects.all()
    jobs = Job.objects.all()
    context = {
        'jobs': jobs,
        'requests': requests,
        'requestIds': requestIds,
        'userId': int(request.session.get('user_id')),
    }
    print(int(request.session.get('user_id')))
    return render(request, 'main/order.html', context)