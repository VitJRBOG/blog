from django.http import HttpRequest, JsonResponse
from .models import Article


def add(request: HttpRequest):

    if request.method == 'POST':
        title = request.POST.get('title')
        definition = request.POST.get('definition')
        text = request.POST.get('text')
        date = request.POST.get('date')
    else:
        return JsonResponse({'status_code': 400,
                             'error': f'{request.method} method is not allowed'})

    params = []
    if text is None:
        params.append('text')
    if definition is None:
        params.append('article_id')
    if text is None:
        params.append('parent_id')
    if date is None or type(date):
        params.append('date')
    if len(params) > 0:
        return JsonResponse({'status_code': 400,
                            'error': f'the following parameters are not valid: {params}'})

    article = Article()
    article.title = title
    article.definition = definition
    article.text = text
    article.date = date

    try:
        article.save()

        return JsonResponse({'status_code': 200})

    except Exception as e:
        return JsonResponse({'status_code': 500, 'error': str(e)})


def get(request: HttpRequest):

    if request.method == 'GET':
        id_ = request.GET.get('id')
    else:
        return JsonResponse({'status_code': 400,
                             'error': f'{request.method} method is not allowed'})

    if id_ is None:
        return JsonResponse({'status_code': 400,
                             'error': 'the following parameters are not valid: \'id\''})

    try:

        articles = Article.objects.filter(id=id_).values()

        return JsonResponse({'status_code': 200,
                             'items': list(articles),
                             'count': len(list(articles))})

    except Exception as e:
        return JsonResponse({'status_code': 500, 'error': str(e)})


def delete(request: HttpRequest):
    if request.method == 'POST':
        id_ = request.POST.get('id')
    else:
        return JsonResponse({'status_code': 400,
                             'error': f'{request.method} method is not allowed'})

    if id_ is None:
        return JsonResponse({'status_code': 400,
                             'error': 'the following parameters are not valid: \'id\''})

    try:

        Article.objects.filter(id=id_).delete()

        return JsonResponse({'status_code': 200})

    except Exception as e:
        return JsonResponse({'status_code': 500, 'error': str(e)})
