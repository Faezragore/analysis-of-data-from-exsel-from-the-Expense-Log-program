## Анализ данных из exsel_файла из программы "Журнала расходов".  

Подсчет расходов из exsel_файла.  
Расходы веду в программе "Журнал расходов".  
Там скачиваем exsel_файл.  
[Ссылка на программу](https://play.google.com/store/apps/details?id=com.vitvov.profit&hl=ru&gl=US)  


Используем язык программирования Python.
Используемая версия Python 3.9.5

## Используемые библиотеки.
Модуль pandas: библиотека для анализа данных.  
Библиотека xlrd – дает возможность читать файлы Excel.  
модуль collections: дополняет функциональность встроенных типов данных(входит в стандартный набор Python).  
Библиотеки используемые в проекте находятся в файле requirements.txt.  
Установить можно командой `pip3 install -r requirements.txt`

## Структура Exsel файла.
* Первая колонка "datetime" время записи в журнал.
* Вторая колонка "category" категория продукта или товара.
* Третья колонка "sum" сумма(в рублях).

Используемые переменные.
* `list_of_product_categories` категория продукта или товара записана в список.
* `product_categories_in_the_exel_file` = pandas.read_excel('Report.xls', sheet_name='Report', keep_default_na=False)
    Указываем название файла и название листа((искать в exsel_файле внизу).
* all_product_position = product_categories_in_the_exel_file.to_dict(orient='record')  
    Нужно заполнить только одним параметром:orient
    orient =‘dict’, Является ли функция по умолчанию преобразованной словарной формой: {столбец (имя столбца): {индекс (имя строки): значение (значение))}};  
* `group_of_products` = collections.defaultdict(list) 
    Мы используем метод  collections.defaultdict
    Соответствующему конструктору в качестве аргумента передается тип элемента по умолчанию(в нашем случае список)
* `first_column_in_the_file_exel` первая колонка в файле.
* `second_column_in_the_file_exel` = вторая колонка в файле.
* `third_column_in_the_file_exel` = третья колонка в файле.

## Что получаем в итоге.
* итоговую сумму по каждой категории указанных в переменной `list_of_product_categories`  
(Подсчет может вестись помесячно или сумма за год).
* Подсчет суммы всех категорий указанных в переменной `list_of_product_categories`  
(Подсчет может вестись помесячно или сумма за год).

## Запуск программы.
- Вести расходы в программе "Журнал расходов".
- Скачиваем exsel_файл.
- exsel_файл должен лежать в папке запуска программы.
 Прописываем значения в переменных.  
  - Прописываем требуемые категории в переменную `list_of_product_categories`  
  - Прописываем название файла и название листа в переменную `product_categories_in_the_exel_file`.
- Запускаем программу.  
  - В командной строке используем команду `main.py`  
  - Указываем нужное значение: месяц или год  
- Вывод будет на экране и сохраняется в txt_файл в папке запуска программы.

## Что сделано!
* итоговую сумму по каждой категории указанных в переменной `list_of_product_categories`  
(Подсчет может вестись помесячно).
* Подсчет суммы всех категорий указанных в переменной `list_of_product_categories`  
(Подсчет может вестись помесячно).

## Что надо доделать!
* Сейчас расчет идет только за один месяц.
* Сделать расчет за указанные месяцы и за год.
* после запуска программы указать в каком значении вести расчет - месяц или за год.
* Вывод суммы в файл.

Хотелки.
* Сделать телеграмм бота,чтобы указанные параметры указывать там и получать расчет суммы.