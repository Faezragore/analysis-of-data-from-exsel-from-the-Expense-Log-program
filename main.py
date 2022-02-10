#!/usr/bin/python3
# -*- coding: utf-8 -*-


import pandas
import xlrd
import collections
import datetime
from pandas._libs.tslibs.timestamps import Timestamp


list_of_products = ['Еда', 'Хлеб (батон)', 'Фрукты', 'Овощи', 'Крупы,макароны', 'Печенье(конфеты и другое сладкое)', 'Молочка(молоко,кефир,творог)', 'Мясо(кура,гов,свинина,индейка)', 'Пюре,йогурт детям.', 'Ветчина(колбаса,сосиски)', 'Вкусности детям', 'Работа_еда']
excel_data_df = pandas.read_excel('Report.xls', sheet_name='Report', keep_default_na=False)
food_card = excel_data_df.to_dict(orient='record')
group_of_products = collections.defaultdict(list)


def get_a_product_group(position):
    qwe = 0
    for i in food_card:
         i["datetime"] = str(i.get("datetime")).split()[0]
         if position in i["category"]:
             if '01' in i['datetime'][5:7]:
                qwe += i['sum']
    group_of_products[position].append(qwe)


def get_a_position_from_list_of_products(list_of_products):
    for position in list_of_products:
        get_a_product_group(position)


def get_a_product_group1():
    wine_store_products = pandas.read_excel('wine3.xlsx', sheet_name='Лист1', keep_default_na=False)
    wine_cards = wine_store_products.to_dict(orient='record')
    group_of_products = collections.defaultdict(list)
    first_column = wine_store_products.columns.ravel()[0]
    for position in wine_cards:
        if position[first_column] in position[first_column]:
            group_of_products[position[first_column]].append(position)


def show_monthly_expense(group_of_products):
    get_a_position_from_list_of_products(list_of_products)
    qwe = 0
    sorted_tuple = sorted(group_of_products.items(), key=lambda x: x[1])
    for key, value in dict(sorted_tuple).items():
        qwe += value[0]
        print("За месяц на", key, "потрачено", value[0], "рублей!")
    print("Итого за месяц на питание потрачено:", qwe)


if __name__ == "__main__":
    show_monthly_expense(group_of_products)
