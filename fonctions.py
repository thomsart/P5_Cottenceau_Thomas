#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys

import mysql.connector as mc
import requests
import json

import classes

################################################################################ 

################################################################################

def create_the_database():

    """
    We create the database in this fonction thanks to the file 'database_creation.py'

    """
    # We connecte to our database
    database = classes.Database("")
    
    with open('script_database_aliment.sql', 'r') as sql :
        block = ""
        for line in sql:
            if line[0] == "\n":
                continue
            elif line[0] == "-":
                continue
            else:
                if ";" in line:
                    block = block+line
                    database.cursor.execute(block)
                    block = ""
                
                else:
                    block = block+line

    # We disconnect to the database
    database.disconnect()

    return
     
################################################################################

def fill_tables(food, nb_pages):

    """
    We take from Openfoodfact Api the 'food' we want and put it in a list of- 
    values in order to fill the table made for it in our database. 
    For that we create a for loop in fonction of the number of pages 'nb_page' 
    of the product on the Api, and we put all datas in the table we want with 
    the argument 'table'.It's allows us to not repet for exemple 20 times the 
    same request.

    """
    database = classes.Database("aliment")
    # Now we choose to take here for exemple 20 pages of 'cornflakes' from the Api.
    for i in range(nb_pages):

        # We decide to pick only the pizza and cornflakes for this exemple but-
        # we can choose any other food actually before checking in the Api-
        # 'Openfoodfact' of course. 
        url = 'https://fr-en.openfoodfacts.org/category/'+str(food)+'/'+str(i)+'.json'
        response = requests.get(url) # we do the request we need.
        data = response.json() # we convert the type of the document in Json.
        key = data.get("products")  # we catch all the number of differents- 
                                    # products which are actually Keys of a dict.
        number_of_product = len(key) # now we count them in a int/type 
        
        count = 0

        # Now we do a while loop to browse and catch all the vallues which we-
        # need for our table.

        while count < number_of_product:

            try:
                product = key[count]
                name = product['product_name']
                brand = product['brands']
                store = product['stores']
                country = product['countries']
                quantity = product['quantity']
                nutriscore = product['nutriscore_grade']
                url = product['url']
                category = str(food)
                product_list = [
                    name, brand, store, country, quantity, nutriscore, url, category
                    ]
                print(product_list)

            # We decide to not takes product which don't have the header- 
            # we need.
            except KeyError:
                count += 1
                continue

            count += 1

            # Now the idea is to put the product_list into the table we choose
            database.cursor.execute(
                """INSERT INTO product (name, brand, store, country, quantity, 
                nutriscore, url, category) VALUE(%s, %s, %s, %s, %s, %s, %s, %s)
                """, product_list
            )
            
            # mettre les produits dans les tables product_category et category    

    database.disconnect()

    return

################################################################################

def show_categorys():



    return

################################################################################

def product_to_substitute():









    return

################################################################################

def healthier_one(nut_score, table):

    """
    This fonction pick in the 'table' the food the user choose to substitute and
    shows some other food with better nutriscore than 'nut_score'.

    """

    cursor = connect()
    print("Nous te proposons une liste de produits plus sains qui peuvent "
            "éventuellements substituer ton produit.\n")
    nutriscore_level = ['a', 'b', 'c', 'd']

    for el in nutriscore_level:

        if el == nut_score[1]:
            break

        else:
            cursor.execute("""SELECT id, marque, nom, nutriscore, magasin, url 
            FROM """+table+""" WHERE nutriscore = '"""+el+"""' """)
            test = cursor.fetchmany()
            
            for value in test:
                print("[{0}, {1}, {2}, {3}, {4}, {5}]\n".format(value[0], 
                value[1], value[2], value[3], value[4] ,value[5]))

    num = input("Si tu désire le remplacer par l'un des ces produit il te suffit" 
    " de rentrer son numéro sinon tape sur Entrer.\n")
    disconnect()

    return num

################################################################################

def save_food(product_num):

    cursor = connect()
    cursor.execute("""SELECT * FROM product WHERE id = """+str(product_num)+""" """)
    result = cursor.fetchone()
    cursor.execute("""INSERT INTO Save_food(foreign_key, nom, marque, magasin, 
    pays, quantite, nutriscore, url, categorie) Values"""+str(result)+""" """)
    disconnect()

    return

################################################################################

def show_saved_food():

    cursor = connect()
    cursor.execute("""SELECT categorie, nutriscore, marque, nom, magasin, url, 
    foreign_key FROM Save_food ORDER BY categorie""")
    rows = cursor.fetchall()
    for value in rows:
        print("\n[{0}, {1}, {2}, {3}, {4}, {5}, {6}]".format(value[0], value[1], 
        value[2], value[3], value[4], value[5], value[6]))
    disconnect()

    return
