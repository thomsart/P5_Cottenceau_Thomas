#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys

import mysql.connector


################################################################################

class Connection(mysql.connector):

    # We create the class Connection to connect and disconnect to the data base
    # 
    def __init__(self):
        self.host = "localhost"
        self.user = "student"
        self.pw = "Metalspirit77+"
        self.name = "aliments"

    def connect():
        # This fonction allows us to connect to the database
        connect = mysql.connector.connect(
            host=host,user=user, password=pw, 
            database=name
            )
        cur = connect.cursor()

        return cur

    def disconnect():
        # This fonction allows us to disconnect to the database and save before.
        connect.commit()
        connect.close()
    
        return print("Au revoir !")


################################################################################

class Product:

    def __init__(self, table):
        self.id = 0
        self.name = ""
        self.brand = ""
        self.shop = ""
        self.countrie = ""
        self.quantity = ""
        self.nutriscore = ""
        self.url = ""
        self.category = ""
        self.foreign_key = 0


    def product_to_substitute(table):

        # In this fonction we ask the user to tell the program which food he wants to 
        # substitute. Once the product is found in the database the fonction show it to
        # the user to be shure that it's the one the user is talking about. We return
        # the nutriscore in 'nut' to use it after in the next operation.

        table = str(table)
        brand = input("\nQuelle est la marque du produit à substituer ?\n")
        brand = brand.replace("'", "\\'", 10)
        name = input("\nQuel est son nom ?\n")
        name = name.replace("'", "\\'", 10)

        cursor = connect()
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