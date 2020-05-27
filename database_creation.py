#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys

import fonctions


"""
This script create the database if it not exist and fill it by the same time.

"""
################################################################################

def main():

    fonctions.create_the_database()

    fonctions.fill_the_database('cornflakes', 20, 'Corn_flakes')

    fonctions.fill_the_database('pizza', 20, 'Pizza')

    return 

################################################################################

if __name__ == "__main__":

    main()