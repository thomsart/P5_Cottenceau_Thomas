#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys

import Database as D
import Product as P


################################################################################

""" This script is the executable of the proramme once you create the database 
with the 'database_creation.py'. """

################################################################################

def main():

    print("\nBonjour, que souhaites tu faire ?")

    on = True

    while on:
        
        """ We ask the user to do something by pressing the number of the action 
        he wants to do. """

        choice = input("\n1 Remplacer un aliment\n2 Retrouver " 
        "tes aliments sauvegardés\n3 Quitter\n\n")

        try:
            choice = int(choice)
        except Exception:
            print("\nCe n'est pas un chiffre que tu rentres.")


        if choice == 1:
            
            """ The programme show him all the differents foods that composed the 
            database. """

            print("\nVoici les catégories de produits présents dans le programme"
            " pour le moment.\n")

            database = D.Database("aliment", "client", "thecode")
            database.show_category()
            database.disconnect()

            """ We Ask the user to enter the Brand and the name of the product he 
            want to substitute. And then when the program found it, it propose a 
            safer one and allow the user to save it if he wants. """

            brand = input("\nQuelle est la marque du produit à substituer ?\n")
            brand = brand.replace("'", "\\'", 10)
            name = input("\nQuel est son nom ?\n")
            name = name.replace("'", "\\'", 10)

            product = P.Product(name, brand)
            product.product_to_substitute("product")

            if product.id == 0:
                continue
               
            else:
                product.substitute_it("product")
                product.save_it()
                product.disconnect()

        elif choice == 2:

            """ Here the program shows to the user the food he saved in the 
            database. """
            
            print("\nVoici tes aliments de substitution rangés par catégorie.")
            database = D.Database("aliment", "client", "thecode")
            database.show_saved_food()
            database.disconnect()

        elif choice == 3:

            """ The user can close the program at any time if he wants by pressing 
            3 in the menu. """ 

            on = False
            print("\nAu revoir !\n")
        
        else:
            print("Ce choix n'est pas au menu.")


    return

################################################################################

if __name__ == "__main__":

    main()