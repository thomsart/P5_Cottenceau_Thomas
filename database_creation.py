#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys

import fonctions
import classes

"""
This script create the database if it not exist and fill the tables by the same time.

"""
################################################################################

def main():

    produit = classes.Product("Camembert 22 %", "Campagnette")
    id_product = produit.select_product("product")
    produit.show_product(id_product, "product")

    print(produit.category)
    # fonctions.create_the_database()

    # fonctions.fill_tables('cornflakes', 3)

    # fonctions.fill_tables('pizza', 3)

    # fonctions.fill_tables('camembert', 3)

    return 

################################################################################

if __name__ == "__main__":

    main()