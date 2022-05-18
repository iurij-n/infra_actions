from django.http import HttpResponse


def index(request):
    return HttpResponse('У меня получилось!!!!!!!!!\n\n\n\nДолжно быть сообщение в телеге.')


def second_page(request):
    return HttpResponse('А это вторая страница!')
