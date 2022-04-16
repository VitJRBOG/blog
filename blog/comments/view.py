from tkinter.messagebox import NO
from django.http import HttpRequest, JsonResponse
from .models import Comment


def add(request: HttpRequest):
    try:
        comment = Comment()
        comment.text = request.POST.get('text')
        comment.article_id = request.POST.get('article_id')
        comment.parent_id = request.POST.get('parent_id')
        comment.date = request.POST.get('date')

        comment.save()

        return JsonResponse({'status': 200})

    except Exception as e:
        # TODO: описать обработку разных типов ошибок и вывод кода статуса
        return JsonResponse({'error': str(e)})


def get(request: HttpRequest):
    id_ = request.GET.get('id')
    parent_id = request.GET.get('parent_id')
    article_id = request.GET.get('article_id')

    try:
        if id_ is not None:
            comments = Comment.objects.filter(
                id=id_).values()
        elif parent_id is not None and article_id is not None:
            comments = Comment.objects.filter(
                parent_id=parent_id).filter(article_id=article_id)
        elif parent_id is not None and article_id is None:
            comments = Comment.objects.filter(parent_id=parent_id)
        elif parent_id is None and article_id is not None:
            comments = Comment.objects.filter(article_id=article_id)
        else:
            comments = []

        return JsonResponse({'status': 200,
                             'list': list(comments),
                             'count': len(list(comments))})

    except Exception as e:
        # TODO: описать обработку разных типов ошибок и вывод кода статуса
        return JsonResponse({'error': str(e)})


def delete(request: HttpRequest):
    try:
        id_ = request.POST.get('id')

        Comment.objects.filter(id=id_).delete()

        return JsonResponse({'status': 200})

    except Exception as e:
        # TODO: описать обработку разных типов ошибок и вывод кода статуса
        return JsonResponse({'error': str(e)})
