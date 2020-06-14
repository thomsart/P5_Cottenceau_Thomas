#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys

import classe_Database as cd
import classe_Product as cp


################################################################################

def main():

    print(
        "\nBonjour, que souhaites tu faire ?"
    )

    on = True

    while on:
        
        print("\n1 Remplacer un aliment\n2 Retrouver " 
        "tes aliments sauvegardés\n3 Quitter\n")

        choice = input()

        try:
            choice = int(choice)
        except:
            print("\nCe choix n'est pas au menu !")


        if choice == 1:

            print("\nVoici les catégories de produits présents dans le programme"
            " pour le moment.\n")

            database = cd.Database("aliment", "client", "thecode")
            database.show_category()
            database.disconnect()

            brand = input("\nQuelle est la marque du produit à substituer ?\n")
            brand = brand.replace("'", "\\'", 10)
            name = input("\nQuel est son nom ?\n")
            name = name.replace("'", "\\'", 10)

            product = cp.Product(name, brand)
            product.product_to_substitute("product")
            product.substitute_it("product")
            product.save_it()
            product.disconnect()

        elif choice == 2:
            
            print("\nVoici tes aliments de substitution rangés par catégorie.")
            database = cd.Database("aliment", "client", "thecode")
            database.show_saved_food()
            database.disconnect()

        elif choice == 3:

            on = False
            print("\nAu revoir !\n")

    return

################################################################################

if __name__ == "__main__":

    main()