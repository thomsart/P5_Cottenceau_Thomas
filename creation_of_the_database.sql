



PS C:\Program Files\MySQL\MySQL Server 8.0\bin>
.\/mysql -h localhost -u root -p
**************
CREATE DATABASE aliments;
USE aliments;
SET NAMES 'utf8';
CREATE USER 'student'@'localhost' IDENTIFIED BY 'mot_de_passe';
GRANT ALL PRIVILEGES ON aliments.* TO 'student'@'localhost';

CREATE TABLE Corn_flakes(
id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
nom TEXT,
marque VARCHAR(50),
magasin VARCHAR(50),
pays TEXT,
quantite TEXT,
nutriscore char(1)
url TEXT,
categorie VARCHAR(20),
PRIMARY KEY (id))
ENGINE=INNODB;

CREATE TABLE Pizza(
id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
nom TEXT,
marque VARCHAR(50),
magasin VARCHAR(50),
pays TEXT,
quantite TEXT,
nutriscore char(1)
url TEXT,
categorie VARCHAR(20),
PRIMARY KEY (id))
ENGINE=INNODB;

CREATE TABLE Save_food(
id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
nom TEXT,
marque VARCHAR(50),
magasin VARCHAR(50),
pays TEXT,
quantite TEXT,
nutriscore char(1)
url TEXT,
categorie VARCHAR(20),
foreign_key SMALLINT UNSIGNED,
PRIMARY KEY (id))
ENGINE=INNODB;

