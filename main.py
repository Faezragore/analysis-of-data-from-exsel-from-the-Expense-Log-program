#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pandas
import xlrd
import collections
import datetime
import sys
import os
import argparse
from pandas._libs.tslibs.timestamps import Timestamp
from rich.console import Console
from rich.table import Table


list_of_product_categories = ['Еда', 'Хлеб (батон)', 'Фрукты', 'Овощи', 'Крупы,макароны', 'Печенье(конфеты и другое сладкое)', 'Молочка(молоко,кефир,творог)', 'Мясо(кура,гов,свинина,индейка)', 'Пюре,йогурт детям.', 'Ветчина(колбаса,сосиски)', 'Вкусности детям', 'Работа_еда']
product_categories_in_the_exel_file = pandas.read_excel('Report.xls', sheet_name='Report', keep_default_na=False)
all_product_position = product_categories_in_the_exel_file.to_dict(orient='record')
group_of_products = collections.defaultdict(list)
first_column_in_the_file_exel = product_categories_in_the_exel_file.columns.ravel()[0]
second_column_in_the_file_exel = product_categories_in_the_exel_file.columns.ravel()[1]
third_column_in_the_file_exel = product_categories_in_the_exel_file.columns.ravel()[2]
total_amount_for_product_category_year = collections.defaultdict(list)


def get_all_product_positions(position, selected_year, choosing_month): # получить все позиции продукта
    total_amount = 0
    for one_product_position in all_product_position:
        date_comparison = str(one_product_position['DateTime'])
        if selected_year in date_comparison:
            if position in one_product_position[second_column_in_the_file_exel]:
                if choosing_month == "False":
                    total_amount += -1 * one_product_position[third_column_in_the_file_exel]
                else:
                    date_comparison = date_comparison[5:7]
                    if choosing_month == date_comparison:
                        total_amount += -1 * one_product_position[third_column_in_the_file_exel]

    group_of_products[position].append(total_amount)

def get_a_position_from_a_list_of_products(list_of_product_categories, selected_year, choosing_month): # получить_позицию из_списка_ категорий продуктов
    group_of_products.clear()
    for position in list_of_product_categories:
        get_all_product_positions(position, selected_year, choosing_month)


def show_expenses_for_year(group_of_products, selected_year, choosing_month): # показать расходы за год
    total_amount_for_year = 0
    table = Table(title="потрачено на еду за год")
    table.add_column("Категория", justify="left", style="cyan")
    table.add_column("Сумма", style="magenta")

    get_a_position_from_a_list_of_products(list_of_product_categories, selected_year, choosing_month)
    total_amount = 0    #итоговая сумма
    sorted_product_group_dictionary = sorted(group_of_products.items(), key=lambda x: x[1])  # отсортированный словарь группы продуктов
    for product_category, amount in dict(sorted_product_group_dictionary).items():
        total_amount += amount[0]
        total_amount_for_product_category_year[product_category].append(amount[0])
    total_amount_for_year += total_amount

    sorted_dictionary_of_product_categories_with_total_for_year = sorted(total_amount_for_product_category_year.items(), key=lambda x: x[1])  # отсортированный словарь группы продуктов
    for product_category, amount in dict(sorted_dictionary_of_product_categories_with_total_for_year).items():
        table.add_row(product_category, str(round(sum(amount))))
    console = Console()
    console.print(table)
    print("Итого за", selected_year, "год на питание потрачено:", str(round(total_amount_for_year)))

def show_monthly_expense(group_of_products, choosing_month, selected_year): # показать месячные расходы
    table = Table(title="потрачено на еду за месяц")
    table.add_column("Категория", justify="left", style="cyan")
    table.add_column("Сумма", style="magenta")
    get_a_position_from_a_list_of_products(list_of_product_categories, choosing_month, selected_year)
    total_amount = 0    #итоговая сумма
    sorted_product_group_dictionary = sorted(group_of_products.items(), key=lambda x: x[1])  # отсортированный словарь группы продуктов
    for product_category, amount in dict(sorted_product_group_dictionary).items():
        total_amount += amount[0]
        #print(product_category , amount[0])
        #print(total_amount)
        table.add_row(product_category, str(round(amount[0])))
    console = Console()
    console.print(table)
    print("Итого за месяц на питание потрачено:", round(total_amount), "рублей!")


if __name__ == "__main__":
    print("Здравствуйте!")
    print("Вы находитесь  в скрипте: Анализ данных из exsel_файла из программы 'Журнала расходов'")
    print("Подсчет может вестись помесячно и за указанный год!")
    print("Выберите один из трех вариантов")
    print("вариант 1:За год!")
    print("вариант 2:За месяц!")
    print("вариант 3:Все время в файле!")
    choice = str(input("Введите вариант!: "))
    if choice == "1":
        selected_year = input("Введите год!: ")
        choosing_month = False
        show_expenses_for_year(group_of_products, str(selected_year), str(choosing_month))
    elif choice == "2":
        month_and_year = str(input("Введите год и месяц в формате- '2022_05': "))
        selected_year = month_and_year[0:4]
        choosing_month = month_and_year[5:]
        show_monthly_expense(group_of_products, str(selected_year), str(choosing_month))
    elif choice == "3":
        pass

    
   ***************************
#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pandas
import xlrd
import collections
import datetime
import sys
import os
import argparse
from pandas._libs.tslibs.timestamps import Timestamp
from rich.console import Console
from rich.table import Table


list_of_product_categories = ['Еда', 'Хлеб (батон)', 'Фрукты', 'Овощи', 'Крупы,макароны', 'Печенье(конфеты и другое сладкое)', 'Молочка(молоко,кефир,творог)', 'Мясо(кура,гов,свинина,индейка)', 'Пюре,йогурт детям.', 'Ветчина(колбаса,сосиски)', 'Вкусности детям', 'Работа_еда']
product_categories_in_the_exel_file = pandas.read_excel('Report.xls', sheet_name='Report', keep_default_na=False)
all_product_position = product_categories_in_the_exel_file.to_dict(orient='record')
group_of_products = collections.defaultdict(list)
first_column_in_the_file_exel = product_categories_in_the_exel_file.columns.ravel()[0]
second_column_in_the_file_exel = product_categories_in_the_exel_file.columns.ravel()[1]
third_column_in_the_file_exel = product_categories_in_the_exel_file.columns.ravel()[2]
total_amount_for_product_category_year = collections.defaultdict(list)


def get_all_product_positions(position, selected_year, choosing_month): # получить все позиции продукта
    #print(selected_year)
    total_amount = 0
    for one_product_position in all_product_position:
        #print(one_product_position)
        date_comparison = str(one_product_position['DateTime'])
        if position in one_product_position[second_column_in_the_file_exel]:
            if selected_year in date_comparison:
                #print(selected_year)
                if choosing_month == "False":
                    total_amount += -1 * one_product_position[third_column_in_the_file_exel]
                else:
                    date_comparison = date_comparison[5:7]
                    if choosing_month == date_comparison:
                        total_amount += -1 * one_product_position[third_column_in_the_file_exel]

    group_of_products[position].append(total_amount)


def get_a_position_from_a_list_of_products(list_of_product_categories, selected_year, choosing_month): # получить_позицию из_списка_ категорий продуктов
    #print(selected_year)
    group_of_products.clear()
    for position in list_of_product_categories:
        #print(selected_year)
        #print(type(choosing_month))
        get_all_product_positions(position, selected_year, choosing_month)


def count_monthly_expenses_for_a_year(group_of_products, selected_year): # считать месячные расходы для года
    list_of_months = ['01','02','03','04','05','06','07','08','09','10','11','12']
    #dictionary_of_annual_reports = {}
    test = []
    for choosing_month in list_of_months:
        selected_year = selected_year
        get_a_position_from_a_list_of_products(list_of_product_categories, selected_year, choosing_month)
        total_amount = 0    #итоговая сумма
        sorted_product_group_dictionary = sorted(group_of_products.items(), key=lambda x: x[1])  # отсортированный словарь группы продуктов
        #print(dict(sorted_product_group_dictionary).items())
        for product_category, amount in dict(sorted_product_group_dictionary).items():
            #print(product_category)
            #dictionary_of_annual_reports['year'] = selected_year
            #dictionary_of_annual_reports['month'] = choosing_month
            test.append(product_category)
            test.append(round(amount[0]))
        test.append(choosing_month)
        #dictionary_of_expenses_by_year['month'] = choosing_month
    dictionary_of_expenses_by_year[selected_year] = test

            #dictionary_of_annual_reports[product_category] = round(amount[0])
            #total_amount += amount[0]
            #print(dictionary_of_annual_reports.values())
            #print(product_category , round(amount[0]))
                #print(total_amount)
        #print("Итого за месяц ", choosing_month, "года ", selected_year,   "на питание потрачено:", round(total_amount), "рублей!")
    #dictionary_of_expenses_by_year[selected_year] = dictionary_of_annual_reports
    #print(dictionary_of_annual_reports.values())
    #print(dictionary_of_expenses_by_year.keys())
    #print(dictionary_of_expenses_by_year.values())

def count_for_all_time_in_file(selected_year):
    count_monthly_expenses_for_a_year(group_of_products, selected_year)

if __name__ == "__main__":
    dictionary_of_expenses_by_year = {}
    dictionary_of_annual_reports = {}
    list_of_years = ['2021']
    for selected_year in list_of_years:
        count_for_all_time_in_file(selected_year)
    #print(dictionary_of_annual_reports.values())
    for item in dictionary_of_expenses_by_year.items():
        print(item, end=' ')
