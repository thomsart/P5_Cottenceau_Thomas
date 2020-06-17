# P5_Cottenceau_Thomas

    1 que fait ce programme ?
    
  Ce programme est une application qui intéragit avec les données de l'API 'Open Food Facts'
hébergée sur internet (https://fr.openfoodfacts.org) par l'intermédiaire de requettes codées 
en Python à l'aide de la librairie 'mysql.connector'. Le fonctionnement est simple, l'utilisateur 
rentre dans le programme un produit alimentaire et ce dernier lui propose un produit alternatif 
plus sain : dont le nutri-score est plus haut.

    2 Création de la base de donnée avec Mysql :

  Tout dabord il faut télécharger Mysql en fonction de l'Os que vous possédez et créer une base
de données que nous appelerons 'aliments' pour laquelle on définit un utilisateur que l'on appelera
'student' par exemple et qui possède tout les droits sur cette base. Dans cette base nous créerons
par exemple une table 'Corn_flakes' dans laquelle nous y mettrons tout les corn-flakes de l'api
deux autres tables de même facture que l'on nommera 'Pizza' et 'camenbert' et pour finir nous ferons 
une table dans laquelle nous sauvegarderons les aliments de substitutions choisis par l'utilisateur 
qui pourra ainsi les consulter, quand il le désire, que l'on nommera 'Save_food. La création complête 
de la base se fait par la commande 'python database_creation.py'.

    3 Importer le programme à partir de github :

  Pour importer le programme ouvrez votre éditeur de texte habituel et cloner le programme 
à l'aide de la commande 'git clone https://github.com/thomsart/P5_Cottenceau_Thomas.git'.
Pensez à bien créer au préalable un dossier vide dans lequel vous vous trouvez au moment
d'exécuter la procédure. Créez votre environnement virtuel et activez le à l'aide de la commande
'.\venv\Scripts\activate' puis faite un import de toutes les librairies nécéssaires à l'aide de 
la commande 'pip install -r requirements.txt'.