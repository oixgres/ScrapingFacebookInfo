-- MySQL Script generated by MySQL Workbench
-- Sun Apr 11 00:03:06 2021
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering
-- Scrapping Facebook Data Base
-- Guerra Cervantes Sergio Enrique
-- Feng Haosheng

SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;

-- -----------------------------------------------------
-- Table Post
-- -----------------------------------------------------
DROP TABLE IF EXISTS post ;

CREATE TABLE IF NOT EXISTS post (
  id_post VARCHAR(30) NOT NULL,
  url TEXT NOT NULL,
  persona VARCHAR(50) NOT NULL,
  texto TEXT NOT NULL,
  fecha DATE NULL,
  PRIMARY KEY (id_post))
ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;

-- -----------------------------------------------------
-- Table Comentarios
-- -----------------------------------------------------
DROP TABLE IF EXISTS comentario ;

CREATE TABLE IF NOT EXISTS comentario (
  id_comentario VARCHAR(30) NOT NULL,
  id_post  VARCHAR(30) NOT NULL,
  persona TEXT NOT NULL,
  texto TEXT NULL,
  PRIMARY KEY (id_comentario),
  FOREIGN KEY (id_post)
  REFERENCES post (id_post)
  ON DELETE CASCADE )
ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;

-- -----------------------------------------------------
-- Table Respuesta
-- -----------------------------------------------------
DROP TABLE IF EXISTS respuesta ;

CREATE TABLE IF NOT EXISTS respuesta (
  id_respuesta VARCHAR(30) NOT NULL,
  id_post VARCHAR(30) NOT NULL,
  id_comentario VARCHAR(30) NOT NULL,
  persona TEXT NOT NULL,
  texto TEXT NULL,
  persona_destinada varchar(30)
  PRIMARY KEY (id_respuesta),
  FOREIGN KEY (id_comentario)
  REFERENCES comentario (id_comentario)
  ON DELETE CASCADE)
ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;


-- -----------------------------------------------------
-- Table Compartir
-- -----------------------------------------------------
DROP TABLE IF EXISTS compartir ;

CREATE TABLE IF NOT EXISTS compartir (
  id_compartir INT NOT NULL AUTO_INCREMENT,
  id_post varchar(30) NOT NULL,
  persona VARCHAR(50) NULL,
  PRIMARY KEY (id_compartir),
  FOREIGN KEY (id_post)
  REFERENCES post (id_post)
  ON DELETE CASCADE)
ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;

ALTER TABLE compartir AUTO_INCREMENT=0;

-- -----------------------------------------------------
-- Table Reacciones
-- -----------------------------------------------------
DROP TABLE IF EXISTS Reacciones ;

CREATE TABLE IF NOT EXISTS reaccion (
  id_reaccion INT NOT NULL AUTO_INCREMENT,
  tipo VARCHAR(10) NOT NULL,
  persona VARCHAR(50) NOT NULL,
  id_post VARCHAR(50) NOT NULL,
  PRIMARY KEY (id_reaccion),
  FOREIGN KEY (id_post)
  REFERENCES post (id_post)
  ON DELETE CASCADE)
ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;

ALTER TABLE reaccion AUTO_INCREMENT=0;

SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
