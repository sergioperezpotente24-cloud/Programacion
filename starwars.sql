DROP DATABASE IF EXISTS StarWars;
CREATE DATABASE StarWars;
USE StarWars;

CREATE TABLE Episodio (
    idEpisodio INT PRIMARY KEY,
    titulo VARCHAR(100) NOT NULL,
    anioEstreno INT NOT NULL,
    director VARCHAR(100) NOT NULL,
    duracionMinutos INT NOT NULL
);

CREATE TABLE Personaje (
    idPersonaje INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    especie VARCHAR(50) NOT NULL,
    planetaOrigen VARCHAR(100),
    afiliacion VARCHAR(100) NOT NULL,
    usaFuerza BOOLEAN NOT NULL DEFAULT FALSE,
    idEpisodio INT NOT NULL,
    FOREIGN KEY (idEpisodio) REFERENCES Episodio(idEpisodio)
);

BEGIN;

INSERT INTO Episodio (idEpisodio, titulo, anioEstreno, director, duracionMinutos) VALUES
(1, 'La amenaza fantasma', 1999, 'George Lucas', 136),
(2, 'El ataque de los clones', 2002, 'George Lucas', 142),
(3, 'La venganza de los Sith', 2005, 'George Lucas', 140),
(4, 'Una nueva esperanza', 1977, 'George Lucas', 121),
(5, 'El Imperio contraataca', 1980, 'Irvin Kershner', 124),
(6, 'El retorno del Jedi', 1983, 'Richard Marquand', 131),
(7, 'El despertar de la Fuerza', 2015, 'J. J. Abrams', 138),
(8, 'Los últimos Jedi', 2017, 'Rian Johnson', 152),
(9, 'El ascenso de Skywalker', 2019, 'J. J. Abrams', 142);

INSERT INTO Personaje (nombre, especie, planetaOrigen, afiliacion, usaFuerza, idEpisodio) VALUES
('Anakin Skywalker', 'Humano', 'Tatooine', 'Orden Jedi', TRUE, 1),
('Obi-Wan Kenobi', 'Humano', 'Stewjon', 'Orden Jedi', TRUE, 1),
('Qui-Gon Jinn', 'Humano', 'Coruscant', 'Orden Jedi', TRUE, 1),
('Padmé Amidala', 'Humano', 'Naboo', 'República Galáctica', FALSE, 1),
('Yoda', 'Desconocida', NULL, 'Orden Jedi', TRUE, 1),
('Darth Maul', 'Zabrak', 'Dathomir', 'Sith', TRUE, 1),
('Palpatine', 'Humano', 'Naboo', 'Sith', TRUE, 1),
('Jar Jar Binks', 'Gungan', 'Naboo', 'República Galáctica', FALSE, 1),
('R2-D2', 'Droide', 'Naboo', 'República Galáctica', FALSE, 1),
('C-3PO', 'Droide', 'Tatooine', 'República Galáctica', FALSE, 1),
('Conde Dooku', 'Humano', 'Serenno', 'Separatistas', TRUE, 2),
('Jango Fett', 'Humano', 'Concord Dawn', 'Cazarrecompensas', FALSE, 2),
('Boba Fett', 'Humano', 'Kamino', 'Cazarrecompensas', FALSE, 2),
('Lama Su', 'Kaminoano', 'Kamino', 'Gobierno de Kamino', FALSE, 2),
('General Grievous', 'Kaleesh', 'Kalee', 'Separatistas', FALSE, 3),
('Comandante Cody', 'Humano', 'Kamino', 'Gran Ejército de la República', FALSE, 3),
('Chewbacca', 'Wookiee', 'Kashyyyk', 'Alianza Rebelde', FALSE, 3),
('Luke Skywalker', 'Humano', 'Polis Massa', 'Alianza Rebelde', TRUE, 3),
('Leia Organa', 'Humano', 'Polis Massa', 'Alianza Rebelde', TRUE, 3),
('Han Solo', 'Humano', 'Corellia', 'Alianza Rebelde', FALSE, 4),
('Wilhuff Tarkin', 'Humano', 'Eriadu', 'Imperio Galáctico', FALSE, 4),
('Greedo', 'Rodiano', 'Rodia', 'Cazarrecompensas', FALSE, 4),
('Wedge Antilles', 'Humano', 'Corellia', 'Alianza Rebelde', FALSE, 4),
('Lando Calrissian', 'Humano', 'Socorro', 'Alianza Rebelde', FALSE, 5),
('Lobot', 'Humano', NULL, 'Ciudad Nube', FALSE, 5),
('Bossk', 'Trandoshano', 'Trandosha', 'Cazarrecompensas', FALSE, 5),
('Jabba el Hutt', 'Hutt', 'Nal Hutta', 'Cártel Hutt', FALSE, 6),
('Wicket', 'Ewok', 'Endor', 'Tribu ewok', FALSE, 6),
('Almirante Ackbar', 'Mon Calamari', 'Mon Cala', 'Alianza Rebelde', FALSE, 6),
('Mon Mothma', 'Humano', 'Chandrila', 'Alianza Rebelde', FALSE, 6),
('Rey', 'Humano', 'Hyperkarn', 'Resistencia', TRUE, 7),
('Finn', 'Humano', NULL, 'Resistencia', FALSE, 7),
('Poe Dameron', 'Humano', 'Yavin 4', 'Resistencia', FALSE, 7),
('Kylo Ren', 'Humano', 'Chandrila', 'Primera Orden', TRUE, 7),
('BB-8', 'Droide', NULL, 'Resistencia', FALSE, 7),
('Capitana Phasma', 'Humano', 'Parnassos', 'Primera Orden', FALSE, 7),
('Snoke', 'Humanoide artificial', 'Exegol', 'Primera Orden', TRUE, 7),
('Rose Tico', 'Humano', 'Hays Minor', 'Resistencia', FALSE, 8),
('Amilyn Holdo', 'Humano', 'Gatalenta', 'Resistencia', FALSE, 8),
('DJ', 'Humano', NULL, 'Independiente', FALSE, 8),
('Jannah', 'Humano', NULL, 'Resistencia', FALSE, 9),
('Zorii Bliss', 'Humano', 'Kijimi', 'Contrabandistas', FALSE, 9),
('Babu Frik', 'Anzellano', NULL, 'Contrabandistas', FALSE, 9);

COMMIT;
