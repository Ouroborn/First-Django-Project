from django.shortcuts import render
from django.http import HttpResponse
import datetime
import random
import string

# Create your views here.

def aboutme(request):
    context = {
        'name': 'Эльдар Термечиков',
        'age': '16 лет',
        'hobbies': ['Гейминг', 'Рисование (графика)', 'Программирование', 'Музыка (раньше написание в DAW)'],
        'fav_quote': "I'm not here, this isn't happening (Radiohead - How to Disappear Completely)",
        'hometown': 'Братск'
    }

    return render(request, 'myapp/aboutme.html', context)



def about(request):
    return HttpResponse("Меня зовут Айгуль. Я люблю рисовать и программировать!")

def now(request):
    return HttpResponse(f"Сейчас {datetime.datetime.now().strftime('%H:%M:%S')}")

def hello(request):
    name = request.GET.get('name', 'Гость')
    return HttpResponse(f"Привет, {name}!")

def add(request):
    a = int(request.GET.get('a', 0))
    b = int(request.GET.get('b', 0))
    return HttpResponse(f"Сумма: {a + b}")

def joke(request):
    jokes = ["Байт - это укус программиста.", "Python - не только змея!", "Тостер - хлебный сервер."]
    return HttpResponse(random.choice(jokes))

def password(request):
    pwd = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    return HttpResponse(f"Твой новый пароль: {pwd}")


def count(request):
    word = request.GET.get('word', '')
    return HttpResponse(f"В слове '{word}' - {len(word)} букв.")

def hello_time(request):
    hour = datetime.datetime.now().hour
    if hour < 12:
        msg = "Доброе утро!"
    elif hour < 18:
        msg = "Добрый день!"
    else:
        msg = "Добрый вечер!"
    return HttpResponse(msg)

def codecoin(request):
    coins = random.randint(1, 100)
    return HttpResponse(f"Ты заработал {coins} CodeCoin!")

def languages(request):
    langs = ["Python", "JavaScript", "C++", "Dart", "Kotlin"]
    return HttpResponse('<br>'.join(langs))

def next_lesson(request):
    today = datetime.date.today()
    next_day = today + datetime.timedelta(days=7)
    return HttpResponse(f"Следующее занятие: {next_day.strftime('%d.%m.%Y')}")