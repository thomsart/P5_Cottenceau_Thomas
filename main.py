#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys

import mysql.connector
import requests
import json

import fonctions


################################################################################

def main():

    print("\nBonjour !")

    on = True

    while on:
        
        print('\n1 Remplacer un aliment\n2 Retrouver ' 
        'tes aliments sauvegardés\n3 Quitter\n')
        choice = input()

        try:
            choice = int(choice)
        except:
            print("\nCe choix n'est pas au menu !")


        if choice == 1:

            print("\nSelectionne la catégorie qui t'intérèsse ?\n")
            fonctions.show_tables()
            choice2 = input("\n")

            try:
                    choice2 = int(choice2)
            except:
                print("\nCe choix n'est pas au menu !")
                continue

            if choice2 == 1:
                
                table = "Corn_flakes"
                nut_score = fonctions.product_to_substitute(table)

                for letter in nut_score:

                    if letter in "abcd":
                        product_num = fonctions.healthier_one(nut_score, table)

                        try:
                            product_num = int(product_num)
                        except:
                            continue

                        fonctions.save_food(product_num, table)

                    else :
                        continue

            elif choice2 == 2:

                table = "Pizza"
                nut_score = fonctions.product_to_substitute(table)
                
                for letter in nut_score:

                    if letter in "abcd":
                        product_num = fonctions.healthier_one(nut_score, table)

                        try:
                            product_num = int(product_num)
                        except:
                            continue

                        fonctions.save_food(product_num, table)

                    else :
                        continue

        elif choice == 2:
            
            print("\nVoici tes aliments de substitution rangés par catégorie.")
            fonctions.show_saved_food()

        elif choice == 3:

            on = False
            print("\nAu revoir !\n")

    return

################################################################################

if __name__ == "__main__":

    main()