#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys

import classe_Database as cd
import classe_Product as cp

################################################################################

"""
This script create the database if it's not exist and fill all the tables 
by the same time.

"""
################################################################################

def main():
    
    # Firt we create the database 'aliment' composed by the table 'product',
    # the table 'category', the table 'product_category' and finally the table-
    # 'save_food'. we commit and the disconnect. Obviously you put in the fird-
    # argument your code in your database when you connect as Administrator(root).

    database = cd.Database('', 'root', 'Metalspirit77+')
    database.create_the_database()
    database.disconnect()

    # Once created we fill 'product' table wich contains all products from the API-
    # With the methode 'fill_table' of the object 'database'.
    # Here for exempe we pick all cornflakes, pizza, camembert and conichon.
    # now you have to connect to the database as 'client' with the code 'thecode'.
    # Here we just took four differents foods for the exemple but you can take what-
    # you want. You put in first argument the food you selected and in the second,
    # the quantity of pages for this food on the API.

    database = cd.Database('aliment', 'client', 'thecode')
    database.fill_tables('cornflakes', 20)
    database.fill_tables('pizza', 20)
    database.fill_tables('camembert', 20)
    database.fill_tables('cornichon', 20)
    database.disconnect()

    return 

################################################################################

if __name__ == "__main__":

    main()