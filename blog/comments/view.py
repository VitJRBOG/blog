from django.http import HttpRequest, JsonResponse
from .models import Comment


def add(request: HttpRequest):

    if request.method == 'POST':
        text = request.POST.get('text')
        article_id = request.POST.get('article_id')
        parent_id = request.POST.get('parent_id')
        date = request.POST.get('date')
    else:
        return JsonResponse({'status_code': 400,
                             'error': f'{request.method} method is not allowed'})

    params = []
    if text is None:
        params.append('text')
    if article_id is None:
        params.append('article_id')
    if parent_id is None:
        params.append('parent_id')
    if date is None or type(date):
        params.append('date')
    if len(params) > 0:
        return JsonResponse({'status_code': 400,
                            'error': f'the following parameters are not valid: {params}'})

    comment = Comment()
    comment.text = text
    comment.article_id = article_id
    comment.parent_id = parent_id
    comment.date = date

    try:
        comment.save()

        return JsonResponse({'status_code': 200})

    except Exception as e:
        return JsonResponse({'status_code': 500, 'error': str(e)})


def get(request: HttpRequest):

    if request.method == 'GET':
        id_ = request.GET.get('id')
        parent_id = request.GET.get('parent_id')
        article_id = request.GET.get('article_id')
    else:
        return JsonResponse({'status_code': 400,
                             'error': f'{request.method} method is not allowed'})

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
            return JsonResponse({'status_code': 400,
                                'error': 'some parameters are not valid'})

        return JsonResponse({'status_code': 200,
                             'list': list(comments),
                             'count': len(list(comments))})

    except Exception as e:
        return JsonResponse({'status_code': 500, 'error': str(e)})


def delete(request: HttpRequest):

    if request.method == 'POST':
        id_ = request.POST.get('id')
    else:
        return JsonResponse({'status_code': 400,
                             'error': f'{request.method} method is not allowed'})

    if request.POST.get('id') is None:
        return JsonResponse({'status_code': 400,
                             'error': 'the following parameters are not valid: \'id\''})

    try:

        Comment.objects.filter(id=id_).delete()

        return JsonResponse({'status_code': 200})

    except Exception as e:
        return JsonResponse({'status_code': 500, 'error': str(e)})
