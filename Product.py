#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import Database as D

###############################################################################

""" We create the class Product because it's more practic for the entire code.
The idea is to create an object with all the attributs of a product. """

###############################################################################


class Product(D.Database):

    def __init__(self):
        D.Database.__init__(self, "aliment", "client", "thecode")

        self.id = 0
        self.name = ""
        self.brand = ""
        self.store = ""
        self.country = ""
        self.quantity = ""
        self.nutriscore = ""
        self.url = ""
        self.category = ""
        self.sub = []

    def select_brand(self):

        """ This methode show all the differents brands of products we
        have in the databases. """

        print("Voici les marques de produits présents dans la base."
              "\nSelectionne celle dont tu recherche le produit en"
              " tapant son numéro.")
        list_brands = []
        self.cursor.execute("""SELECT brand FROM product""")
        result = self.cursor.fetchall()
        for elements in result:
            for brand in elements:
                if brand in list_brands:
                    continue
                else:
                    list_brands.append(brand)
        list_brand_sorted = []
        list_brand_sorted = sorted(list_brands)
        for number, brand in enumerate(list_brand_sorted):
            print("n°"+str(number)+": "+brand)
        self.brand = list_brand_sorted[int(input())]
        print(self.brand)

        return

    def select_name(self):

        """ This methode show all the differents names of products we
        have in the databases. """

        print("Voici les noms de produits référents à cette marque.")
        list_names = []
        self.cursor.execute("""SELECT name FROM product
                            WHERE brand = '"""+self.brand+"""' """)
        result = self.cursor.fetchall()
        for elements in result:
            for name in elements:
                if name in list_names:
                    continue
                else:
                    list_names.append(name)
        list_names_sorted = []
        list_names_sorted = sorted(list_names)
        for number, name in enumerate(list_names_sorted):
            print("n°" + str(number) + ": " + name)
        self.name = list_names_sorted[int(input())]
        print(self.name)

        return

    def product_to_substitute(self, table):

        """ This methode allow to find the product the user want to
        substitute."""

        self.cursor.execute("""select id, name, brand, store, country, quantity,
                            nutriscore, url, category from """+table+""" WHERE
                            name ='"""+self.name+"""' and brand = '"""
                            + self.brand + """' """)

        row = self.cursor.fetchall()
        try:
            values = row[0]
            self.id = values[0]
            self.name = values[1]
            self.brand = values[2]
            self.store = values[3]
            self.country = values[4]
            self.quantity = values[5]
            self.nutriscore = values[6]
            self.url = values[7]
            self.category = values[8]
            print("\nVoici le produit que tu cherches à substituer.\n{}\n"
                  .format(values))

        except IndexError:
            print("\nVisiblement ce produit n'existe pas, ou est mal"
                  "orthographié.")

        return

    def substitute_it(self, table):

        """ Now that we know wich one the user want to substitute we compare it
        to others products with better nutriscore. actually the idea was to
        turn the product to substitute into the one the user will choose as
        substitute. """

        print("\nCes produits peuvent le substituer.\n")
        nutriscore_level = ['a', 'b', 'c', 'd']
        list_product = []
        for el in nutriscore_level:
            if el == self.nutriscore:
                if self.nutriscore == 'a':
                    print("\nCe produit a un nutriscore 'A', ce n'est pas "
                          "néccessaire de le substituer.\n")
                    break
                else:
                    break
            else:
                self.cursor.execute("""select * from """+table+""" WHERE
                                    nutriscore = '"""+el+"""' and
                                    category = '"""+self.category+"""' """)

                row = (self.cursor.fetchall())

                for product in row:
                    if product[7] not in list_product:
                        list_product.append(product[7])
                        self.sub.append(str(product[0]))
                        print("Numero: "+str(product[0])+" de nutriscore: "
                              + str(product[6])+"\n", product[1], product[2],
                              product[3], product[4], product[7])
                    else:
                        continue

        the_one_user_pick = input("""\nSi tu désire en choisir un pour"""
                                  """ substituer ton produit tape son"""
                                  """ numéro et appuie sur 'Entrer'.\n""")

        if the_one_user_pick not in self.sub:
            print("Ce numero ne réfère pas à un produit proposé !")
            self.sub = []
            pass

        else:
            self.cursor.execute("""select id, name, brand, store, country,
                                quantity, nutriscore, url, category from
                                """+table+""" WHERE id = '"""
                                + the_one_user_pick + """' """)

            values = (self.cursor.fetchall()[0])
            self.id = values[0]
            self.name = values[1]
            self.brand = values[2]
            self.store = values[3]
            self.country = values[4]
            self.quantity = values[5]
            self.nutriscore = values[6]
            self.url = values[7]
            self.category = values[8]

            print("\nTu as choisis ce produit.\n\n{}\n"
                  .format(values))

        return

    def save_it(self):

        """ thanks to this methode the user can save it to keep it in
        memory. """

        self.cursor.execute("""INSERT INTO save_food (name, brand, store,
                            country, quantity, nutriscore, url, category)
                            VALUES('"""+self.name+"""', '"""+self.brand+"""',
                            '"""+self.store+"""', '"""+self.country+"""',
                            '"""+self.quantity+"""', '"""+self.nutriscore+"""',
                            '"""+self.url+"""', '"""+self.category+"""') """)

        return print("\nLe produit vient d'être ajouté à tes sauvegardes.\n")

###############################################################################
