from django.shortcuts import render

from project.slaves.models import Resume


def index_view(request):
    """Вьюха отображает главную страницу приложения"""
    qs = Resume.objects.all()
    context = {
        'title': 'Твой путь к успеху',
        'queryset': qs,
    }
    return render(request, 'slaves/index.html', context)
