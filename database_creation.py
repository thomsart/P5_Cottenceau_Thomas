#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys

import classe_Database as cd
import classe_Product as cp

"""
This script create the database if it's not exist and fill all the tables 
by the same time.

"""
################################################################################

def main():
    
    database = cd.Database('', 'root', 'Metalspirit77+')

    database.create_the_database()

    database.disconnect()

    database = cd.Database('aliment', 'client', 'thecode')

    database.fill_tables('cornflakes', 20)

    database.fill_tables('pizza', 20)

    database.fill_tables('camembert', 20)

    database.fill_tables('cornichon', 20)

    database.disconnect()

    return 

################################################################################

if __name__ == "__main__":

    main()