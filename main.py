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


def get_all_product_positions_for_year(position, selected_year):  # получить все позиции продукта для года
    total_amount = 0
    for one_product_position in all_product_position:
        one_product_position[first_column_in_the_file_exel] = str(one_product_position.get(first_column_in_the_file_exel)).split()[0]
        if selected_year == one_product_position[first_column_in_the_file_exel][0:4]:
            if position in one_product_position[second_column_in_the_file_exel]:
                total_amount += -1 * (one_product_position[third_column_in_the_file_exel])

    group_of_products[position].append(total_amount)


def get_all_product_positions_for_month(position, selected_year, choosing_month):  # получить все позиции продукта для месяца
    total_amount = 0
    for one_product_position in all_product_position:
        one_product_position[first_column_in_the_file_exel] = str(one_product_position.get(first_column_in_the_file_exel)).split()[0]
        if selected_year == one_product_position[first_column_in_the_file_exel][0:4]:
            if choosing_month == one_product_position[first_column_in_the_file_exel][5:7]:
                if position in one_product_position[second_column_in_the_file_exel]:
                    total_amount += one_product_position[third_column_in_the_file_exel]


    group_of_products[position].append(total_amount)


def get_a_position_from_a_list_of_products(list_of_product_categories, selected_year, choosing_month): # получить_позицию из_списка_ категорий продуктов
    group_of_products.clear()
    for position in list_of_product_categories:
        if choosing_month:
            get_all_product_positions_for_month(position, selected_year, choosing_month)
        else:
            get_all_product_positions_for_year(position, selected_year)


def show_expenses_for_year(group_of_products, selected_year, choosing_month): # показать расходы за год
    total_amount_for_year = 0
    table = Table(title="потрачено на еду за год")
    table.add_column("Категория", justify="right", style="cyan")
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
        #print("За год на", product_category, "потрачено", sum(amount), "рублей!")
    console = Console()
    console.print(table)
    print("Итого за год на питание потрачено:", total_amount_for_year)

def show_monthly_expense(group_of_products, choosing_month, selected_year): # показать месячные расходы
    get_a_position_from_a_list_of_products(list_of_product_categories, choosing_month, selected_year)
    total_amount = 0    #итоговая сумма
    sorted_product_group_dictionary = sorted(group_of_products.items(), key=lambda x: x[1])  # отсортированный словарь группы продуктов
    for product_category, amount in dict(sorted_product_group_dictionary).items():
        total_amount += amount[0]
        print("За месяц на", product_category, "потрачено", amount[0], "рублей!")
    print("Итого за месяц на питание потрачено:", total_amount, "рублей!")


if __name__ == "__main__":
    print("Здравствуйте!")
    print("Вы находитесь  в скрипте: Анализ данных из exsel_файла из программы 'Журнала расходов'")
    print("Подсчет может вестись помесячно и за указанный год!")
    selected_year = str(input("Укажите пожалуйста год!: "))
    counting_for_year = str(input("Вам подсчитать за целый год? да или нет: "))
    if "да" in counting_for_year:
        choosing_month = False
        show_expenses_for_year(group_of_products, str(selected_year), choosing_month)
    else:
        choosing_month = str(input("Укажите месяц! : "))
        show_monthly_expense(group_of_products, selected_year, choosing_month)
