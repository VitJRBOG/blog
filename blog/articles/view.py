from django.http import HttpRequest, JsonResponse
from .models import Article


def add(request: HttpRequest):
    try:
        article = Article()
        article.title = request.POST.get('title')
        article.definition = request.POST.get('definition')
        article.text = request.POST.get('text')
        article.date = request.POST.get('date')
        article.save()

        return JsonResponse({'status': 200})

    except Exception as e:
        # TODO: описать обработку разных типов ошибок и вывод кода статуса
        return JsonResponse({'error': str(e)})


def get(request: HttpRequest):
    try:
        id_ = request.GET.get('id')

        articles = Article.objects.filter(id=id_).values()

        return JsonResponse({'status': 200,
                             'items': list(articles),
                             'count': len(list(articles))})

    except Exception as e:
        # TODO: описать обработку разных типов ошибок и вывод кода статуса
        return JsonResponse({'error': str(e)})


def delete(request: HttpRequest):
    try:
        id_ = request.POST.get('id')

        Article.objects.filter(id=id_).delete()

        return JsonResponse({'status': 200})

    except Exception as e:
        # TODO: описать обработку разных типов ошибок и вывод кода статуса
        return JsonResponse({'error': str(e)})
