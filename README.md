# entryTestHM
Entry test that uses data from NASA api

# Task description
Задача:

Достать из api NASA объекты, близкие к земной орбите за заданный интервал дат
Вывести результат по заданному количеству строк на каждую дату (топ-5, топ-3 и т.д.) в виде:

дата
neo_reference_id: словарь со значениями по заданным ключам

Пример вывода: 

2022-02-23
3768654: {'name': '(2017 CX1)', 'absolute_magnitude_h': 28.2, 'is_potentially_hazardous_asteroid': False}

вывод отсортировать в рамках каждой даты по ключу absolute_magnitude_h по убыванию от большего

ключи: ['name', 'absolute_magnitude_h', 'is_potentially_hazardous_asteroid']

Пример GET запроса:
https://api.nasa.gov/neo/rest/v1/feed?start_date=2015-09-07&end_date=2015-09-08&api_key=DEMO_KEY

Допускается использовать только импорт модулей requests и datetime

На вход функция вывода должна уметь принимать дату начала поиска, дату окончания поиска, лимит вывода записей на каждую дату

# Info about project
Current version has commented inputs from terminal and uses hardcoded variables. Also, due to specification using of os package is prohibited therefore there is no key for NASA api.