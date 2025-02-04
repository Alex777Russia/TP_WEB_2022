# Домашнее задание 6

## Настройка веб-серверов
Цель домашнего задания подготовить инфраструктуру для будущего проекта и научиться настраивать веб-серверы. ***Внимание! Вместо pupkin используйте свою фамилию.***

### 1. Настройка gunicorn для запуска WSGI скриптов
Установите gunicorn
```Bash
$ pip install gunicorn
```
Затем, пользуясь [документацией Gunicorn](http://docs.gunicorn.org/en/latest/configure.html), напишите конфигурационный файл который запустит ваше приложение **askme_pupkin.wsgi** с двумя процессам-воркерами.

### 2. Создание простого WSGI-скрипта
Отдельно от вашего приложение создать простой WSGI-скрипт (функция или класс). Этот скрипт должен:
- зупускаться с помощью gunicorn;
- выводить список переданных **GET** и **POST** параметров;
- выполняеться при запросе **localhost:8081**;
- работать без использования Django.

### 3. Настройка nginx для отдачи статического контента
Необходимо настроить nginx следующим образом. Все файлы с URL начинающимся с **/uploads/** отдаются из **ask_pupkin/uploads**. Все файлы с расширением (**.js .css .jpeg** и т.д) — из директории **ask_pupkin/static**. Файлы должны отдаваться c заголовками, кэширующими файлы на стороне браузера. Файлы должны сжиматься на сервере для уменьшения размера передаваемых файлов. Размер конфига nginx не должен превышать 50 строк. Полученную конфигурацию необходимо запустить и проверить, для этого нужно разместить какой-либо файл (например **sample.html**) в директории **static** и загрузить его с помощью браузера **localhost/sample.html**.

### 4. Настройка проксирования в nginx
- Настроить nginx для проксирования всех нестатических запросов (URL без расширения, например **/** или **/login/**) на gunicorn;
- Настроить **upstream**;
- Настроить **proxy_cache** и проверить его работу.

### 5. Сравнение производительности
С помощью утилиты Apache Benchmark (ab, идет в комплекте с Apache, для Ubuntu пакет apache2-utils) или wrk сравните производительность nginx (отдача статики) и gunicorn (запуск wsgi скриптов). 

Необходимо провести пять измерений:

- Отдача статического документа напрямую через nginx;
- Отдача статического документа напрямую через gunicorn
- Отдача динамического документа напрямую через gunicorn;
- Отдача динамического документа через проксирование запроса с nginx на gunicorn;
- Отдача динамического документа через проксирование запроса с nginx на gunicorn, при кэшировние ответа на nginx (proxy cache).

**Размеры всех документов должны быть примерно одинаковыми**. По результатам измерений необходимо ответить на вопросы:

- Насколько быстрее отдается статика по сравнению с WSGI?
- Во сколько раз ускоряет работу proxy_cache?

### 6. Результат выполнения домашнего задания
Результат выполнения домашнего задания является:

- директория с созданным проектом;
- конфиг nginx;
- конфиг gunicorn;
- результаты нагрузочного тестирования (вывод утилиты ab/wrk).

### 7. Баллы

#### Максимальные баллы за ДЗ - 14 баллов

Настройка nginx для отдачи статического контента - 5:

- общее - 3;
- локейшен /uploads/ приоритетнее статики - 1;
- проксирование - 1.

Настройка gunicorn для запуска wsgi приложений - 2:

- общее - 2.

Создание WSGI-приложения - 2:

- наличие запускаемого скрипта - 1
- правильное отображение списка GET и POST параметров - 1.

Оценка производительности nginx и gunicorn - 5:

- статический документ напрямую через nginx и напрямую через gunicorn - 2;
- динамический документ напрямую через gunicorn - 1;
- динамический документ через nginx с проксирование на gunicorn, с кэшом и без кэша (proxy_cache) - 2;

### 8. Полезные ссылки
- [Nginx](http://nginx.org/ru/docs/).
- [О проксирования в nginx](http://nginx.org/ru/docs/http/ngx_http_proxy_module.html#example);
- [Gunicorn](http://docs.gunicorn.org/en/latest/configure.html);
- [ab](http://httpd.apache.org/docs/2.2/programs/ab.html).