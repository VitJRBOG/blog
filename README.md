# Blog

Прототип REST API системы комментирования блога.
___

## Documentation

### **Добавление новой статьи**

`/articles/add`

Выполняется POST-запросом с следующими параметрами:

`title` - заголовок статьи; **строка** длиной в 50 символов;

`definition` - краткое описание статьи; **строка** длиной в 140 символов;

`text` - основной текст статьи; **строка**;

`date` - дата публикации статьи (следует передавать в формате unixtimestamp); **целое число**.

Возвращает ответ JSON-формата. При успешном запросе вернет поле `status_code` с кодом `200`. При ошибке будут возвращены поля `status_code` с кодом ошибки и `error` с описанием ошибки.

### **Получение статьи из базы данных**

`/articles/get`

Выполняется GET-запросом со следующим параметром:

`id` - идентификатор статьи; целое число.

Возвращает ответ JSON-формата, где `status_code` равен `200`, `items` содержит выборку элементов из базы данных, а `count` равен количеству полученных элементов.
Пример ответа при успешном запросе:

```
> example.com/articles/get?id=1

{
    "status_code": 200,
    "items": [
        {
            "id"; 1,
            "title": "Example of title",
            "definition": "Example of definition.",
            "text": "Example of full text.",
            "date": 1650170114
        }
    ],
    "count": 1
}

```

При ошибке будут возвращены поля `status_code` с кодом ошибки и `error` с описанием ошибки.

### **Удаление статьи из базы данных**

`/articles/delete`

Выполняется POST-запросом со следующим параметром:

`id` - идентификатор статьи; **целое число**.

Возвращает ответ JSON-формата. При успешном запросе вернет поле `status_code` с кодом `200`. При ошибке будут возвращены поля `status_code` с кодом ошибки и `error` с описанием ошибки.

### **Добавление нового комментария**

`/comments/add`

Выполняется POST-запросом с следующими параметрами:

`text` - основной текст комментария; **строка**;

`article_id` - идентификатор статьи, к которой прикреплен комментарий; **целое число**;

`parent_id` - идентификатор комментария-родителя (при отсутствии адресата следует передавать `0`); **целое число**;

`date` - дата публикации статьи (следует передавать в формате unixtimestamp); **целое число**.

Возвращает ответ JSON-формата. При успешном запросе вернет поле `status_code` с кодом `200`. При ошибке будут возвращены поля `status_code` с кодом ошибки и `error` с описанием ошибки.

### **Получение комментариев из базы данных**

`/comments/get`

Выполняется GET-запросом со следующими параметрами (обязательным является наличие минимум одного параметра):

`id` - идентификатор комментария; **целое число**;

`article_id` - идентификатор статьи, к которой прикреплен комментарий; **целое число**;

`parent_id` - идентификатор комментария-родителя; **целое число**;

Возвращает ответ JSON-формата, где `status_code` равен `200`, `items` содержит выборку элементов из базы данных, а `count` равен количеству полученных элементов. Пример ответа при успешном запросе:

```
> example.com/comments/get?article_id=1

{
    "status_code": 200,
    "items": [
        {
            "id": 1,
            "text": "Example of text.",
            "article_id": 1,
            "parent_id": 0,
            "date": 1650170341
        },
        {
            "id": 2,
            "text": "Second example of text.",
            "article_id": 1,
            "parent_id": 1,
            "date": 1650171982
        },
        {
            "id": 3,
            "text": "Third example of text.",
            "article_id": 1,
            "parent_id": 2,
            "date": 1650172621
        },
        {
            "id": 4,
            "text": "Fourth example of text.",
            "article_id": 1,
            "parent_id": 3,
            "date": 1650173123
        },
        {
            "id": 5,
            "text": "Fifth example of text.",
            "article_id": 1,
            "parent_id": 0,
            "date": 1650173752
        }
    ],
    "count": 5
}

```

При ошибке будут возвращены поля `status_code` с кодом ошибки и `error` с описанием ошибки.

### **Удаление комментария из базы данных**

`/comments/delete`

Выполняется POST-запросом со следующим параметром:

`id` - идентификатор комментария; **целое число**.

Возвращает ответ JSON-формата. При успешном запросе вернет поле `status_code` с кодом `200`. При ошибке будут возвращены поля `status_code` с кодом ошибки и `error` с описанием ошибки.

### **Возвращаемые ошибки**

При попытке отправить *не* GET-запрос на методы `/articles/get` и `/comments/get` будет возвращена ошибка с текстом `%method_type% method is not allowed`.

При попытке отправить *не* POST-запрос на методы `/articles/add`, `/articles/delete`, `/comments/add` и `/comments/delete` будет возвращена ошибка с текстом `%method_type% method is not allowed`.

При попытке отправить не все необходимые параметры в POST-запросе на методы `/articles/add` и `/comments/add` будет возвращена ошибка с текстом `the following parameters are not valid: %params%`.

При попытке отправить GET-запрос на методы `/articles/get` и `/comments/get` *вообще* без передачи параметров будет возвращена ошибка `the following parameters are not valid: 'id'`.

При попытке отправить POST-запрос на методы `/articles/delete` и `/comments/delete` без передачи параметра `id` будет возвращена ошибка `the following parameters are not valid: 'id'`.