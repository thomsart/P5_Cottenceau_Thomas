#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys

import mysql.connector
import requests
import json


################################################################################

# In our programme the action to catch and put in the database the datas we need-
# is doing manualy. Like that we have the controle for the moment on the datas-
# we chose and the numbers of page we want. Obviously we can, in the futur, make-
# it automaticly by the actions of the user.

################################################################################

def main():

    # We take from Openfoodfact Api the datas we need and put them in a list of- 
    # values. For that we create a for loop in fonction of the number of pages-
    # for an article we need like pizza and corn flakes and catch the number of-
    # pages in nb_page. It's allows us to not repet for exemple 20 times the-
    # same request.

    # First we connect to the database 'aliments'.
    connect = mysql.connector.connect(host="localhost",user="student",
        password="Metalspirit77+", database="aliments")
    cursor = connect.cursor()
    
    # Now we choose to take here for exemple 20 pages of 'cornflakes' from the Api.
    for i in range(20):

        nb_pages = i # here 20 pages
        food = 'cornflakes'
        # We decide to pick only the pizza and cornflakes for this exemple but-
        # we can choose any other food actually before checking in the Api-
        # 'Openfoodfact' of course. 
        url = 'https://fr-en.openfoodfacts.org/category/'+str(food)+'/'+str(nb_pages)+'.json'
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

            # Now the idea is to put the product_list into our table
            cursor.execute(
                """INSERT INTO Corn_flakes (nom, marque, magasin, pays, 
            quantite, nutriscore, url) VALUE(%s, %s, %s, %s, %s, %s, %s)""", 
            product_list
            )

    connect.commit() # We save everything.
    connect.close()  # And we close the database.

    return

################################################################################

if __name__ == "__main__":

    main()