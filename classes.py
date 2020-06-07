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

    def product_to_substitute(self, table):

        database = Database("aliment")
        database.cursor.execute(
            """select id, name, brand, store, country, quantity, nutriscore, url, 
            category from """+table+""" WHERE name = '"""+self.name+"""' 
            and brand = '"""+self.brand+"""' """
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

        return print("\nVoici le produit que tu cherches à substituer !\n\n{}\n".format(values))

    def substitute_it(self, table):

        print("\nEt Voici ceux qui peuvent le substituer.\n")
        nutriscore_level = ['a', 'b', 'c', 'd']
        for el in nutriscore_level:
            if el == self.nutriscore:
                break
            else:
                database = Database("aliment")
                database.cursor.execute(
                    """select * from """+table+""" WHERE nutriscore = '"""+el+"""' 
                    and category = '"""+self.category+"""' """
                    )
                result = (database.cursor.fetchmany())
                for value in result:

                    print("({0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8})\n".format
                    (value[0], value[1], value[2], value[3], value[4] ,value[5] ,
                    value[6] ,value[7] ,value[8]))

        the_one_user_pick = input("""\nSi tu désire en choisir un pour substituer """
        """ton produit tape son numéro (le premier dans les caractèristiques) et """
        """appuie sur 'Entrer'.\n""")
        database = Database("aliment")
        database.cursor.execute(
            """select id, name, brand, store, country, quantity, nutriscore, url, 
            category from """+table+""" WHERE id = '"""+the_one_user_pick+"""' """
            )
        values = (database.cursor.fetchall()[0])
        self.id = values[0]
        self.name = values[1]
        self.brand = values[2]
        self.store = values[3]
        self.country = values[4]
        self.quantity = values[5]
        self.nutriscore = values[6]
        self.url = values[7]
        self.category = values[8]

        print("\nVoici le produit de substitution.\n\n{}\n".format(values))

        return 


    def save_it(self):

        database = Database("aliment")
        database.cursor.execute(
            """INSERT INTO save_food VALUES("""+self.id+""", """+self.name+"""
            """+self.brand+""", """+self.store+""", """+self.country+""", 
            """+self.quantity+""", """+self.nutriscore+""", """+self.url+""", 
            """+self.category+""",)"""
            )


################################################################################
    #     brand = input("\nQuelle est la marque du produit à substituer ?\n")
    #     brand = brand.replace("'", "\\'", 10)
    #     name = input("\nQuel est son nom ?\n")
    #     name = name.replace("'", "\\'", 10)