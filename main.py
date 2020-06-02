#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys

import fonctions
import classes


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
            fonctions.show_categorys()
            choice2 = input("\n")

            try:
                    choice2 = int(choice2)
            except:
                print("\nCe choix n'est pas au menu !")
                continue

            if choice2 == 1:
                
                nut_score = classes.Product.product_to_substitute("corn_flakes")

                for letter in nut_score:

                    if letter in "abcd":
                        product_num = fonctions.healthier_one(nut_score, "corn_flakes")

                        try:
                            product_num = int(product_num)
                        except:
                            continue

                        fonctions.save_food(product_num, "corn_flakes")

                    else :
                        continue

            elif choice2 == 2:

                nut_score = classes.Product.product_to_substitute("pizza")
                
                for letter in nut_score:

                    if letter in "abcd":
                        product_num = fonctions.healthier_one(nut_score, "pizza")

                        try:
                            product_num = int(product_num)
                        except:
                            continue

                        fonctions.save_food(product_num, "pizza")

                    else :
                        continue

            elif choice2 == 3:

                nut_score = classes.Product.product_to_substitute("camenbert")
                
                for letter in nut_score:

                    if letter in "abcd":
                        product_num = fonctions.healthier_one(nut_score, "camenbert")

                        try:
                            product_num = int(product_num)
                        except:
                            continue

                        fonctions.save_food(product_num, "camenbert")

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