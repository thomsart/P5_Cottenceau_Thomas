#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys

import mysql.connector
import requests
import json

import main


################################################################################

# This fonction is quite simple, it's allow us to show all the tables we got for 
# exemple here we just have two tables 'Corn_flakes' and 'Pizza'.

def show_tables():

    connect = mysql.connector.connect(host="localhost",user="student",
            password="Metalspirit77+", database="aliments")
    cursor = connect.cursor()
    cursor.execute("""SHOW TABLES""")
    result = cursor.fetchall()
    choice1 = str(result[0]).strip("()',")
    choice2 = str(result[1]).strip("()',")
    print("1  "+choice1+"\n2  "+choice2)
    connect.close()

    return

################################################################################

# In this fonction we ask the user to tell the program which food he wants to 
# substitute. Once the product is found in the database the fonction show it to
# the user to be shure that it's the one the user is talking about. We return
# the nutriscore in 'nut' to use it after in the next operation.

def product_to_substitute(table):

    table = str(table)
    brand = input("\nQuelle est la marque du produit à substituer ?\n")
    brand = brand.replace("'", "\\'", 10)
    name = input("\nQuel est son nom ?\n")
    name = name.replace("'", "\\'", 10)
    connect = mysql.connector.connect(host="localhost",user="student",
        password="Metalspirit77+", database="aliments")
    cursor = connect.cursor()
    cursor.execute("""SELECT marque, nom, nutriscore, magasin, pays, url FROM 
    """+table+""" WHERE marque = '"""+brand+"""' AND nom = '"""+name+"""' """)
    test = cursor.fetchmany()

    if not test:
        print("\nCe produit n'existe pas !\n")
        nut = ""

    else:    
        print("\nVoici le produit que tu veux substituer !\n")
        article = cursor.fetchmany()
        for value in article:
            print("[{0}, {1}, {2}, {3}, {4}, {5}]\n".format(value[0], 
            value[1], value[2], value[3], value[4] ,value[5]))
            nut = "'"+value[2]+"'"

    connect.close()

    return nut

################################################################################

# Now that we have the nutriscore we use it in this fonction which will 

def healthier_one(nut_score, table):

    print("Nous te proposons une liste de produits plus sains qui peuvent "
            "éventuellements substituer ton produit.\n")
    nutriscore_level = ['a', 'b', 'c', 'd']

    for el in nutriscore_level:
        if el == nut_score[1]:
            break
        else:
            connect = mysql.connector.connect(host="localhost",user="student",
                password="Metalspirit77+", database="aliments")
            cursor = connect.cursor()
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
    connect = mysql.connector.connect(host="localhost",user="student",
        password="Metalspirit77+", database="aliments")
    cursor = connect.cursor()
    cursor.execute("""SELECT * FROM """+table+""" WHERE id = """+product_num+""" """)
    result = cursor.fetchone()
    result = str(result)
    cursor.execute("""INSERT INTO Save_food(foreign_key, nom, marque, magasin, 
    pays, quantite, nutriscore, url, categorie) Values"""+result+""" """)
    connect.commit()
    connect.close()

    return

################################################################################

def show_saved_food():

    connect = mysql.connector.connect(host="localhost",user="student",
            password="Metalspirit77+", database="aliments")
    cursor = connect.cursor()
    cursor.execute("""SELECT categorie, nutriscore, marque, nom, magasin, url, 
    foreign_key FROM Save_food ORDER BY categorie""")
    rows = cursor.fetchall()
    for value in rows:
        print("\n[{0}, {1}, {2}, {3}, {4}, {5}, {6}]".format(value[0], value[1], 
        value[2], value[3], value[4], value[5], value[6]))
    connect.close()

    return

################################################################################