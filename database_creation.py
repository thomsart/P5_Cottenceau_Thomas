#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys

import fonctions


"""
This script create the database if it not exist and fill the tables by the same time.

"""
################################################################################

def main():

    fonctions.create_the_database()

    # fonctions.fill_tables('cornflakes', 20, 'corn_flakes')

    # fonctions.fill_tables('pizza', 20, 'pizza')

    # fonctions.fill_tables('camenbert', 20, 'camenbert')

    return 

################################################################################

if __name__ == "__main__":

    main()