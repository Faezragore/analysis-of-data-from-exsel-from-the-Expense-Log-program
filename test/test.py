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

def get_all_product_positions(position, selected_year):  # получить все позиции продукта
    #print(type(selected_year))
    total_amount = 0
    for one_product_position in all_product_position:
        one_product_position[first_column_in_the_file_exel] = str(one_product_position.get(first_column_in_the_file_exel)).split()[0]
        #print(one_product_position[first_column_in_the_file_exel])
        if selected_year == one_product_position[first_column_in_the_file_exel][0:4]:
            #print(one_product_position[first_column_in_the_file_exel])
            if position in one_product_position[second_column_in_the_file_exel]:
                #if selected_month in one_product_position[first_column_in_the_file_exel][5:7]:
                    #print(one_product_position[first_column_in_the_file_exel][5:7])
                #print(one_product_position[third_column_in_the_file_exel])
                total_amount += one_product_position[third_column_in_the_file_exel]


    group_of_products[position].append(total_amount)


def get_a_position_from_a_list_of_products(list_of_product_categories, selected_year): # получить_позицию из_списка_ категорий продуктов
    group_of_products.clear()
    for position in list_of_product_categories:
        #print(position)
        get_all_product_positions(position, selected_year)


def show_expenses_for_year(group_of_products, selected_year): # показать расходы за год
    #print(selected_year)
    #list_of_months_in_a_year = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
    total_amount_for_year = 0
    #for one_month_out_of_a_year in list_of_months_in_a_year:
        #selected_month = one_month_out_of_a_year

    get_a_position_from_a_list_of_products(list_of_product_categories, selected_year)
    total_amount = 0    #итоговая сумма
    sorted_product_group_dictionary = sorted(group_of_products.items(), key=lambda x: x[1])  # отсортированный словарь группы продуктов
    #print(sorted_product_group_dictionary)
    for product_category, amount in dict(sorted_product_group_dictionary).items():
        total_amount += amount[0]
        total_amount_for_product_category_year[product_category].append(amount[0])
    total_amount_for_year += total_amount

    sorted_dictionary_of_product_categories_with_total_for_year = sorted(total_amount_for_product_category_year.items(), key=lambda x: x[1])  # отсортированный словарь группы продуктов
    #print(sorted_dictionary_of_product_categories_with_total_for_year)
    for product_category, amount in dict(sorted_dictionary_of_product_categories_with_total_for_year).items():
        print("За год на", product_category, "потрачено", sum(amount), "рублей!")

    print("Итого за год на питание потрачено:", total_amount_for_year)




if __name__ == "__main__":
    list_of_months_in_a_year = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
    month_or_year = choose_a_month_or_a_year()
    namespase = month_or_year.parse_args(sys.argv[1:])
    resulting_selection = namespase.choosing_month # Записываем в переменную выбор месяца или за весь год
    #show_expenses_for_year(group_of_products)
    selected_year = resulting_selection
    print("Здравствуйте!")
    print("Вы находитесь  в скрипте: Анализ данных из exsel_файла из программы 'Журнала расходов'")
    print("Подсчет может вестись помесячно и за указанный год!")
    selected_year = str(input("Укажите пожалуйста год!: "))
    counting_for_year = str(input("Вам подсчитать за целый год? да или нет: "))
    if "да" in counting_for_year:
        show_expenses_for_year(group_of_products, str(selected_year))
    else:
        choosing_month = str("Укажите месяц! : ")
        show_monthly_expense(group_of_products, selected_year, choosing_month)


# год 
#show_expenses_for_year(group_of_products)
# get_a_position_from_a_list_of_products
#   get_all_product_positions(position, selected_date)
# месяц
#show_monthly_expense(group_of_products)
#  get_a_position_from_a_list_of_products(list_of_product_categories, selected_date)
#     et_all_product_positions(position, selected_date)
