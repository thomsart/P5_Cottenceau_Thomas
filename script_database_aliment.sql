-- MySQL Script generated by MySQL Workbench
-- Wed May 27 23:37:05 2020
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema aliment
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema aliment
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `aliment` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `aliment` ;

-- -----------------------------------------------------
-- Table `aliment`.`save_food`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `aliment`.`save_food` (
  `id` SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
  `nom` TEXT NULL DEFAULT NULL,
  `marque` VARCHAR(50) NULL DEFAULT NULL,
  `magasin` VARCHAR(50) NULL DEFAULT NULL,
  `pays` TEXT NULL DEFAULT NULL,
  `quantite` VARCHAR(15) NULL DEFAULT NULL,
  `nutriscore` VARCHAR(1) NULL DEFAULT NULL,
  `url` TEXT NULL DEFAULT NULL,
  `categorie` VARCHAR(50) NULL DEFAULT NULL,
  `foreign_key` SMALLINT UNSIGNED NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 1
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `aliment`.`corn_flakes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `aliment`.`corn_flakes` (
  `id` SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
  `nom` TEXT NULL DEFAULT NULL,
  `marque` VARCHAR(50) NULL DEFAULT NULL,
  `magasin` VARCHAR(50) NULL DEFAULT NULL,
  `pays` TEXT NULL DEFAULT NULL,
  `quantite` TEXT NULL DEFAULT NULL,
  `nutriscore` VARCHAR(1) NULL DEFAULT NULL,
  `url` TEXT NULL DEFAULT NULL,
  `categorie` VARCHAR(12) NULL DEFAULT 'corn_flakes',
  `save_food_id` SMALLINT UNSIGNED NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_corn_flakes_save_food_idx` (`save_food_id` ASC) VISIBLE,
  CONSTRAINT `fk_corn_flakes_save_food`
    FOREIGN KEY (`save_food_id`)
    REFERENCES `aliment`.`save_food` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
AUTO_INCREMENT = 1
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `aliment`.`pizza`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `aliment`.`pizza` (
  `id` SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
  `nom` TEXT NULL DEFAULT NULL,
  `marque` VARCHAR(50) NULL DEFAULT NULL,
  `magasin` VARCHAR(50) NULL DEFAULT NULL,
  `pays` TEXT NULL DEFAULT NULL,
  `quantite` TEXT NULL DEFAULT NULL,
  `nutriscore` VARCHAR(1) NULL DEFAULT NULL,
  `url` TEXT NULL DEFAULT NULL,
  `categorie` VARCHAR(20) NOT NULL DEFAULT 'pizza',
  `save_food_id` SMALLINT UNSIGNED NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_pizza_save_food1_idx` (`save_food_id` ASC) VISIBLE,
  CONSTRAINT `fk_pizza_save_food1`
    FOREIGN KEY (`save_food_id`)
    REFERENCES `aliment`.`save_food` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
AUTO_INCREMENT = 1
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `aliment`.`camenbert`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `aliment`.`camembert` (
  `id` SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
  `nom` TEXT NULL DEFAULT NULL,
  `marque` VARCHAR(50) NULL DEFAULT NULL,
  `magasin` VARCHAR(50) NULL DEFAULT NULL,
  `pays` TEXT NULL DEFAULT NULL,
  `quantite` TEXT NULL DEFAULT NULL,
  `nutriscore` VARCHAR(1) NULL DEFAULT NULL,
  `url` TEXT NULL DEFAULT NULL,
  `categorie` VARCHAR(12) NULL DEFAULT 'camenbert',
  `save_food_id` SMALLINT UNSIGNED NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_camenbert_save_food1_idx` (`save_food_id` ASC) VISIBLE,
  CONSTRAINT `fk_camenbert_save_food1`
    FOREIGN KEY (`save_food_id`)
    REFERENCES `aliment`.`save_food` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
AUTO_INCREMENT = 1
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;