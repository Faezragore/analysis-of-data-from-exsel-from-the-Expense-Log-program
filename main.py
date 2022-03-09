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


list_of_product_categories = ['Еда', 'Хлеб (батон)', 'Фрукты', 'Овощи', 'Крупы,макароны', 'Печенье(конфеты и другое сладкое)', 'Молочка(молоко,кефир,творог)', 'Мясо(кура,гов,свинина,индейка)', 'Пюре,йогурт детям.', 'Ветчина(колбаса,сосиски)', 'Вкусности детям', 'Работа_еда']
product_categories_in_the_exel_file = pandas.read_excel('Report.xls', sheet_name='Report', keep_default_na=False)
all_product_position = product_categories_in_the_exel_file.to_dict(orient='record')
group_of_products = collections.defaultdict(list)
first_column_in_the_file_exel = product_categories_in_the_exel_file.columns.ravel()[0]
second_column_in_the_file_exel = product_categories_in_the_exel_file.columns.ravel()[1]
third_column_in_the_file_exel = product_categories_in_the_exel_file.columns.ravel()[2]
total_amount_for_product_category_year = collections.defaultdict(list)

def choose_a_month_or_a_year (): # Создаем экземпляр класса ArgumentParser
    month_or_year = argparse.ArgumentParser()
    month_or_year.add_argument ('--choosing_month', default=['year'], help='your choice')

    return month_or_year

def get_all_product_positions(position, selected_date):  # получить все позиции продукта
    total_amount = 0
    for one_product_position in all_product_position:
        one_product_position[first_column_in_the_file_exel] = str(one_product_position.get(first_column_in_the_file_exel)).split()[0]
        if position in one_product_position[second_column_in_the_file_exel]:
            if selected_date in one_product_position[first_column_in_the_file_exel][5:7]:
                total_amount += one_product_position[third_column_in_the_file_exel]


    group_of_products[position].append(total_amount)


def get_a_position_from_a_list_of_products(list_of_product_categories, selected_date): # получить_позицию из_списка_ категорий продуктов
    group_of_products.clear()
    for position in list_of_product_categories:
        get_all_product_positions(position, selected_date)


def show_expenses_for_year(group_of_products): # показать расходы за год
    list_of_months_in_a_year = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
    total_amount_for_year = 0
    for one_month_out_of_a_year in list_of_months_in_a_year:
        selected_date = one_month_out_of_a_year

        get_a_position_from_a_list_of_products(list_of_product_categories, selected_date)
        total_amount = 0    #итоговая сумма
        sorted_product_group_dictionary = sorted(group_of_products.items(), key=lambda x: x[1])  # отсортированный словарь группы продуктов
        for product_category, amount in dict(sorted_product_group_dictionary).items():
            total_amount += amount[0]
            total_amount_for_product_category_year[product_category].append(amount[0])
        total_amount_for_year += total_amount

    sorted_dictionary_of_product_categories_with_total_for_year = sorted(total_amount_for_product_category_year.items(), key=lambda x: x[1])  # отсортированный словарь группы продуктов
    for product_category, amount in dict(sorted_dictionary_of_product_categories_with_total_for_year).items():
        print("За год на", product_category, "потрачено", sum(amount), "рублей!")

    print("Итого за год на питание потрачено:", total_amount_for_year)


def show_monthly_expense(group_of_products): # показать месячные расходы
    selected_date = resulting_selection
    get_a_position_from_a_list_of_products(list_of_product_categories, selected_date)
    total_amount = 0    #итоговая сумма
    sorted_product_group_dictionary = sorted(group_of_products.items(), key=lambda x: x[1])  # отсортированный словарь группы продуктов
    for product_category, amount in dict(sorted_product_group_dictionary).items():
        total_amount += amount[0]
        print("За месяц на", product_category, "потрачено", amount[0], "рублей!")
    print("Итого за месяц на питание потрачено:", total_amount, "рублей!")


if __name__ == "__main__":
    list_of_months_in_a_year = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
    month_or_year = choose_a_month_or_a_year()
    namespase = month_or_year.parse_args(sys.argv[1:])
    resulting_selection = namespase.choosing_month # Записываем в переменную выбор месяца или за весь год
    if resulting_selection == "year":
        show_expenses_for_year(group_of_products)
    else:
        show_monthly_expense(group_of_products)