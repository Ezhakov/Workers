from django.http import HttpResponse
from django.shortcuts import render, redirect

from project.slaves.models import Resume
from project.slaves.forms import ResumeForms


def index_view(request):
    """Вьюха отображает главную страницу приложения"""
    qs = Resume.objects.all()
    context = {
        'title': 'Твой путь к успеху',
        'queryset': qs,
        }
    return render(request, 'slaves/index.html', context)


def creates_view(request):
    """ Показывает или обрабатывает форму """
    form = ResumeForms(request.POST or None)
    context = {
        'title': 'Новое резюме',
        'form': form,
        }
    if request.method == 'POST' and form.is_valid():
        form.save(request.user)
        return redirect('slaves:index')
    return render(request, 'slaves/create.html', context)
