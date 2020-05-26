#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys

import mysql.connector
import requests
import json

import classes


################################################################################

def create_the_database():

    """
    We create the database thanks to the file 'creation_of_the_database.sql'

    """



    return
     
################################################################################

def fill_the_database(food, nb_pages, table):

    """
    We take from Openfoodfact Api the 'food' we want and put it in a list of- 
    values. For that we create a for loop in fonction of the number of pages
    'nb_page'. And we put all datas in the table we want 'table'. 
    It's allows us to not repet for exemple 20 times the same request.

    """

    # First we connect to the database 'aliments'.

    
    # Now we choose to take here for exemple 20 pages of 'cornflakes' from the Api.
    nb_pages = 20
    for i in range(nb_pages):

        food = 'cornflakes'
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
                nom = product['product_name']
                marque = product['brands']
                magasin = product['stores']
                pays = product['countries']
                quantite = product['quantity']
                nutriscore = product['nutriscore_grade']
                url = product['url']
                product_list = [
                    nom, marque, magasin, pays, quantite, nutriscore, url
                    ]
                print(product_list)

            # We decide to not takes product which don't have the header- 
            # we need.
            except KeyError:
                count += 1
                continue

            count += 1

            # Now the idea is to put the product_list into the table we choose
            cursor.execute(
                """INSERT INTO """+table+""" (nom, marque, magasin, pays, 
            quantite, nutriscore, url) VALUE(%s, %s, %s, %s, %s, %s, %s)""", 
            product_list
            )

    return

################################################################################

def show_tables():

    """
    This fonction is quite simple, it's allow us to show all the tables we got for 
    exemple here we just have two tables 'Corn_flakes' and 'Pizza'.

    """

    cursor.execute("""SHOW TABLES""")
    result = cursor.fetchall()
    choice1 = str(result[0]).strip("()',")
    choice2 = str(result[1]).strip("()',")
    print("1  "+choice1+"\n2  "+choice2)

    return

################################################################################

def healthier_one(nut_score, table):

    """
    This fonction pick in a table the foood the user choose to substitute

    """

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

    return num

################################################################################

def save_food(product_num, table):

    product_num = str(product_num)
    
    cursor.execute("""SELECT * FROM """+table+""" WHERE id = """+product_num+""" """)
    result = cursor.fetchone()
    result = str(result)
    cursor.execute("""INSERT INTO Save_food(foreign_key, nom, marque, magasin, 
    pays, quantite, nutriscore, url, categorie) Values"""+result+""" """)

    return

################################################################################

def show_saved_food():

    cursor.execute("""SELECT categorie, nutriscore, marque, nom, magasin, url, 
    foreign_key FROM Save_food ORDER BY categorie""")
    rows = cursor.fetchall()
    for value in rows:
        print("\n[{0}, {1}, {2}, {3}, {4}, {5}, {6}]".format(value[0], value[1], 
        value[2], value[3], value[4], value[5], value[6]))

    return
