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

    produit = classes.Product("frosties", "kellogg\\'s")
    produit.product_to_substitute("product")
    produit.substitute_it("product")
    
    

    
    # fonctions.create_the_database()

    # fonctions.fill_tables('cornflakes', 3)

    # fonctions.fill_tables('pizza', 3)

    # fonctions.fill_tables('camembert', 3)

    return 

################################################################################

if __name__ == "__main__":

    main()