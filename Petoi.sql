# Creamos la base de datos para el uso del petoi
create database if not exists base_petoi;

# Seleccion de la base de datos
use base_petoi;

#Creamos las tablas a usar sin relaciones todavia

CREATE TABLE IF NOT EXISTS registro(
	id_video INT NOT NULL,
    lat FLOAT(10) NOT NULL,
    lon FLOAT(10) NOT NULL,
    fecha DATE NOT NULL,
    PRIMARY KEY(id_video)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;


CREATE TABLE IF NOT EXISTS videos(
	id_vi INT NOT NULL,
    referencia CHAR(45) NOT NULL,
    PRIMARY KEY(id_vi),
    id_ref_reg INT NOT NULL,
    CONSTRAINT relacion
    FOREIGN KEY (id_ref_reg)
    REFERENCES registro(id_video)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

