# P5_Cottenceau_Thomas

    1 Que fait ce programme ?
    
  Ce programme est une application qui propose à un utilisateur un substitut alimentaire de 
meilleur nutriscore qu'il peut si il le souhaite sauvegarder afin de le consulter à volonté.
Le programme puise les données de l'API 'Open Food Facts' par des requêtes à l'aide de la 
librairie 'request' pour ensuite les insérer dans une base de données grâce à la librairie
'mysql.connector'.
Ce programme est codé en Python et éxécute la création de la base grâce à un script Sql.

    2 Outils utilisés.

  Tout dabord ce programme fonctionne avec la version de Python 3.7.4 32-bit.
Il faut télécharger ensuite le SGBDR 'MySQL 8.0' en fonction de l'Os que vous possédez et
y définir un compte en tant qu'administrateur 'root' et le mot de passe de votre choix,
tout ceci ce fait lors du téléchargement de 'MySQL'.

    3 Importer le programme à partir de github.

  Pour importer le programme ouvrez votre éditeur de texte habituel et cloner le programme 
à l'aide de la commande 'git clone https://github.com/thomsart/P5_Cottenceau_Thomas.git'.
Pensez à bien créer au préalable un dossier vide dans lequel vous vous trouvez au moment
d'exécuter la procédure. Créez votre environnement virtuel et activez le à l'aide de la commande
'.\venv\Scripts\activate' puis faite un import de toutes les librairies nécéssaires à l'aide de 
la commande 'pip install -r requirements.txt'.

    4 Créer la base et la remplir.

  La première fois que vous éxécuterez ce programme ouvrez le fichier 'database_creation.py' 
chargé de créer la base de donnée 'aliment'. A la ligne 27 lors de la création de l'objet 
'database' de la Classe 'Database' mettez en troisième paramêtre votre mot de passe pour votre
connexion à MySQl en tant qu'administrateur (à la place des '########'). La méthode 
'create_the_database' comme son nom l'indique va créer la base de données grâce au fichier
nommé 'script_database_aliment.sql'.
Plus bas vous verrez que je me reconnecte en tant que user de nom 'client' et de mot de passe
'thecode' pour plus de sécurité. Puis on instancie un objet 'database' en utilisant la méthode
'fill_tables' qui va tout simplement remplir les tables d'aliments que l'on souhaite, par exemple
ici nous avons des Corn-flakes des Pizzas des Camemberts et enfin des Cornichons. Libre à vous
de requêter autant de fois que vous le souhaitez d'autres aliments. Pensez juste à vérifier le 
nombre de page (le deuxième argument de la méthode) présent sur l'API pour l'aliment que vous 
souhaitez importer dans la base.
Une fois ces considérations prises en compte il ne vous reste plus qu'a éxécuter ce script
en tapant la commande 'python database_creation.py' qui vas donc créer la base et la remplir 
en même temps.

    5 Lancer le programme.

  Maintenant que la base de données est remplis, éxécutez le fichier 'main.py' avec la commande 
'python main.py'.
