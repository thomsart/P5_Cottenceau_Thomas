#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys

import mysql.connector as mc


################################################################################

class Database():

    def __init__(self, name):
        self.host = "localhost"
        self.user = "root"
        self.pwd = "Metalspirit77+"
        self.database = name
        self.connect = mc.connect(
        host=self.host,user=self.user, password=self.pwd, database=self.database
        )
        self.cursor = self.connect.cursor()

    def disconnect(self):
        self.connect.commit()
        self.connect.close()

################################################################################

class Product(Database):

    def __init__(self, nom, marque):
        Database.__init__(self, "aliment")

        self.id = ""
        self.name = nom
        self.brand = marque
        self.store = ""
        self.country = ""
        self.quantity = ""
        self.nutriscore = ""
        self.url = ""
        self.category = ""

    def select_product(self, table):
        database = Database("aliment")
        database.cursor.execute(
        """SELECT id FROM """+table+""" WHERE name = '"""+self.name+"""' 
        and brand = '"""+self.brand+"""' """
        )
        return database.cursor.fetchone()[0]

    def show_product(self, id_product, table):
        
        id_product = str(id_product)
        database = Database("aliment")
        list_attribut = database.cursor.execute(
                """select id, name, brand, store, country, quantity, nutriscore, url, 
                category from """+table+""" where id = '"""+id_product+"""' """
            )
        values = (database.cursor.fetchall())[0]
        self.id = values[0]
        self.name = values[1]
        self.brand = values[2]
        self.store = values[3]
        self.country = values[4]
        self.quantity = values[5]
        self.nutriscore = values[6]
        self.url = values[7]
        self.category = values[8]

        return print("\nVoici le produit que tu cherches à substituer !\n{}\n".format(values))



    # def product_to_substitute(self):

    #     # In this fonction we ask the user to tell the program which food he wants to 
    #     # substitute. Once the product is found in the self.on shot to
    #     # the user to be shure that it's the one the user is talking about. We return
    #     # the nutriscore in 'nut' to use it after in the next operation.

    #     brand = input("\nQuelle est la marque du produit à substituer ?\n")
    #     brand = brand.replace("'", "\\'", 10)
    #     name = input("\nQuel est son nom ?\n")
    #     name = name.replace("'", "\\'", 10)

    #     database = classes.Database("aliment")
    #     database.cursor.execute(
    #         """SELECT brand, name, nutriscore, store, country, url, category FROM 
    #     product WHERE brand = '"""+brand+"""' AND name = '"""+name+"""' """
    #     )
    #     test = cursor.fetchmany()

    #     if not test:
    #         print("\nCe produit n'existe pas !\n")
    #         nut = ""

    #     else:    
    #         print("\nVoici le produit que tu veux substituer !\n")
    #         article = cursor.fetchmany()
    #         for value in article:
    #             print("[{0}, {1}, {2}, {3}, {4}, {5}]\n".format(value[0], 
    #             value[1], value[2], value[3], value[4] ,value[5]))
    #             nut = "'"+value[2]+"'"

    #     database.disconnect()

    #     return nut


    # def healthier_one(nut_score, cat):

    #     """
    #     This fonction pick in the table 'product' the food the user choose to substitute 
    #     and shows some other food with better nutriscore than 'nut_score'.

    #     """

    #     database = classes.Database("aliment")
    #     print("Nous te proposons une liste de produits plus sains qui peuvent "
    #             "éventuellements substituer ton produit.\n")
    #     nutriscore_level = ['a', 'b', 'c', 'd']

    #     for el in nutriscore_level:

    #         if el == nut_score[1]:
    #             break

    #         else:
    #             database.cursor.execute(
    #                 """SELECT id, brand, name, nutriscore, store, url FROM product 
    #                 WHERE nutriscore = '"""+el+"""' and category = '"""+cat+"""' """
    #             )
    #             test = database.cursor.fetchmany()
                
    #             for value in test:
    #                 print("[{0}, {1}, {2}, {3}, {4}, {5}]\n".format(value[0], 
    #                 value[1], value[2], value[3], value[4] ,value[5]))

    #     num = input("Si tu désire le remplacer par l'un des ces produit il te suffit" 
    #     " de rentrer son numéro sinon tape sur 'Entrer'.\n")
    #     database.disconnect()

    #     return num


    def save_food(product_num):

        database = classes.Database("aliment")
        database.cursor.execute(
            """SELECT * FROM product WHERE id = """+str(product_num)+""" """
            )
        result = cursor.fetchone()
        print(result)
        database.cursor.execute(
            """INSERT INTO Save_food(name, brand, store, country, quantity,
            nutriscore, url, category) Values"""+str(result)+""" """
            )
        database.disconnect()

        return

################################################################################