use academix1;

select * from tema;
select * from subtema;
select * from beneficio;
select * from recurso;
select * from examen;
select * from pregunta;
select * from opcion;
SELECT * FROM tipo;

SELECT p.id_pregunta, p.contenido, COUNT(o.id_opcion) as num_opciones
FROM pregunta p
LEFT JOIN opcion o ON p.id_pregunta = o.id_pregunta
GROUP BY p.id_pregunta;

SELECT id_pregunta, contenido FROM pregunta ORDER BY id_pregunta;
SELECT contenido, COUNT(*) 
FROM pregunta 
WHERE id_examen = 26 
GROUP BY contenido 
HAVING COUNT(*) > 1;



INSERT INTO estado (id_estado, nombre) VALUES (1,'activo');
INSERT INTO estado (id_estado, nombre) VALUES (2,'inactivo');
INSERT INTO estado (id_estado, nombre) VALUES (3,'publicado');
INSERT INTO estado (id_estado, nombre) VALUES (4,'espera');
INSERT INTO estado (id_estado, nombre) VALUES (5,'rechazado');

INSERT INTO rol (id_rol, nombre) VALUES (1,'admin');
INSERT INTO rol (id_rol, nombre) VALUES (2,'normal');
INSERT INTO rol (id_rol, nombre) VALUES (3,'premium');

INSERT INTO tipo (id_tipo, nombre) VALUES (1,'pdf');
INSERT INTO tipo (id_tipo, nombre) VALUES (2,'videos');
INSERT INTO tipo (id_tipo, nombre) VALUES (3,'audiolibros');

insert into etiqueta (nombre) values ('álgebra');
insert into etiqueta (nombre) values ('biología celular');
insert into etiqueta (nombre) values ('cinemática');
insert into etiqueta (nombre) values ('derivadas');
insert into etiqueta (nombre) values ('estequiometría');
insert into etiqueta (nombre) values ('genética');
insert into etiqueta (nombre) values ('integrales');
insert into etiqueta (nombre) values ('leyes de newton');
insert into etiqueta (nombre) values ('reacciones químicas');

INSERT INTO recurso (titulo, contenido, descripcion, url_archivo, fecha_publicacion, id_tipo, id_estado, id_subtema, external_i)
VALUES ('Dracula','contenido 9','Dracula" by Bram Stoker is a Gothic horror novel published in 1897','https://www.gutenberg.org/cache/epub/345/pg345-images.html',NOW(), 1,1,1,'OL85892W');

Insert INTO recurso(contenido, titulo, descripcion, url_archivo, external_id, fecha_publicacion, id_tipo, id_estado, id_subtema)
VALUES('Musica Alemana', 'Marcha militar alemana Erika','Musica Alemana de la marcha militar llamada Erika ', 'https://youtu.be/AjPHXhDocWQ?si=H4iPLlXbhDJ-SQyt', '', NOW(), 2, 1, 6);

Insert INTO recurso(contenido, titulo, descripcion, url_archivo, external_id, fecha_publicacion, id_tipo, id_estado, id_subtema)
VALUES('Musica Extranjera', 'Noche Oscura"(Dark is the Night-Тёмная ночь)','Musica extranjera que es de amor pero suena triste y melancolica por el idioma', 'https://youtu.be/Pb9cOAnw6Y4?si=amUglfP6Q92ML8gp', '', NOW(), 2, 1, 7 );

insert into tema (nombre, descripcion, nivel_dificultad) values ('Fundamentos de Álgebra','Conceptos básicos de álgebra y operaciones fundamentales','intermedio');
insert into tema (nombre, descripcion, nivel_dificultad) values ('Introducción a la Biología','Principios esenciales de la biología general','intermedio');
insert into tema (nombre, descripcion, nivel_dificultad) values ('Cálculo Diferencial','Estudio de límites y derivadas','intermedio');
insert into tema (nombre, descripcion, nivel_dificultad) values ('Física Mecánica','Análisis del movimiento y fuerzas','avanzado');
insert into tema (nombre, descripcion, nivel_dificultad) values ('Química General','Estructura de la materia y reacciones químicas','avanzado');
insert into tema (nombre, descripcion, nivel_dificultad) values ('Ética Profesional','Principios éticos en el ejercicio profesional','básico');
insert into tema (nombre, descripcion, nivel_dificultad) values ('Ciencias Políticas','Conceptos fundamentales del sistema político','intermedio');
INSERT INTO tema (nombre, descripcion, nivel_dificultad) VALUES ('Goticas','es sobre como son las goticas','intermedio');

INSERT INTO subtema (id_subtema, nombre, descripcion, nivel_dificultad) VALUES (1,'subtema perron','perronsissimo','alto');
INSERT INTO subtema (id_subtema, nombre, descripcion, nivel_dificultad) VALUES (2,'subtema perron 2','perronsisssimo','alto');
INSERT INTO subtema (id_subtema, nombre, descripcion, nivel_dificultad) VALUES (3,'Biologia','subtema de biologia','alta');
INSERT INTO subtema (id_subtema, nombre, descripcion, nivel_dificultad) VALUES (4,'Ciencias','subtema de ciencia','alta');
INSERT INTO subtema (id_subtema, nombre, descripcion, nivel_dificultad) VALUES (5,'Matematicas','subtema de Matematicas','alta');
INSERT INTO subtema (id_subtema, nombre, descripcion, nivel_dificultad) VALUES (6,'Politica','subtema de Politica','alta');
INSERT INTO subtema (id_subtema, nombre, descripcion, nivel_dificultad) VALUES (7,'Etica','subtema de Etica','alta');

INSERT INTO examen (titulo, cantidad_preguntas, descripcion, id_subtema) VALUES ('examen de Goticas',12,'es sobre las goticas',1);
INSERT INTO examen (titulo, cantidad_preguntas, descripcion, id_subtema) VALUES ('examen de Dracula',12,'es sobre el libro de Dracula por Bram stoker',1);
INSERT INTO examen (id_examen, titulo, cantidad_preguntas, descripcion, id_subtema) VALUES (1,'examen perron',30,'es sobre las goticas',2);
INSERT INTO examen (id_examen, titulo, cantidad_preguntas, descripcion, id_subtema) VALUES (2,'examen de certificacion',30,'es el examen de certificacion en biologia',4);
INSERT INTO examen (id_examen, titulo, cantidad_preguntas, descripcion, id_subtema) VALUES (3,'examen de certificacion de ciencia',30,'es el examen de certificacion en ciencia',4);
INSERT INTO examen (id_examen, titulo, cantidad_preguntas, descripcion, id_subtema) VALUES (4,'examen de certificacion de matematicas',30,'es el examen de certificacion en matematicas',5);
INSERT INTO examen (id_examen, titulo, cantidad_preguntas, descripcion, id_subtema) VALUES (5,'examen de certificacion de politica',30,'es el examen de certificacion en politica',6);
INSERT INTO examen (id_examen, titulo, cantidad_preguntas, descripcion, id_subtema) VALUES (6,'examen de certificacion de etica',30,'es el examen de certificacion en Etica',7);
INSERT INTO examen (id_examen, titulo, cantidad_preguntas, descripcion, id_subtema) VALUES (7,'Examen Álgebra Lineal',3,'Evaluación básica',5);
INSERT INTO examen (id_examen, titulo, cantidad_preguntas, descripcion, id_subtema) VALUES (8,'Examen Derivadas',3,'Derivadas fundamentales',5);
INSERT INTO examen (id_examen, titulo, cantidad_preguntas, descripcion, id_subtema) VALUES (9,'Examen Cinemática',3,'Movimiento rectilíneo',4);
INSERT INTO examen (id_examen, titulo, cantidad_preguntas, descripcion, id_subtema) VALUES (10,'Examen Álgebra Lineal',3,'Evaluación básica',5);
INSERT INTO examen (id_examen, titulo, cantidad_preguntas, descripcion, id_subtema) VALUES (11,'Examen Derivadas',3,'Derivadas fundamentales',5);
INSERT INTO examen (id_examen, titulo, cantidad_preguntas, descripcion, id_subtema) VALUES (12,'Examen Cinemática',3,'Movimiento rectilíneo',4);
insert into examen (titulo, cantidad_preguntas, descripcion, id_subtema) values 
('Evaluación de Fundamentos de Álgebra Lineal',30,'Examen orientado a evaluar conocimientos sobre vectores, matrices y determinantes.',2);

insert into examen (titulo, cantidad_preguntas, descripcion, id_subtema) values 
('Examen de Certificación en Biología Celular',30,'Evaluación integral sobre estructura y función celular.',4);

insert into examen (titulo, cantidad_preguntas, descripcion, id_subtema) values 
('Evaluación en Fundamentos de Física',30,'Examen sobre conceptos básicos de cinemática y dinámica.',4);

insert into examen (titulo, cantidad_preguntas, descripcion, id_subtema) values 
('Examen de Certificación en Matemáticas',30,'Evaluación formal sobre cálculo diferencial y álgebra avanzada.',5);

insert into examen (titulo, cantidad_preguntas, descripcion, id_subtema) values 
('Examen de Certificación en Ciencias Políticas',30,'Evaluación sobre sistemas políticos y teoría del Estado.',6);

insert into examen (titulo, cantidad_preguntas, descripcion, id_subtema) values 
('Examen de Certificación en Ética Profesional',30,'Evaluación de principios éticos aplicados al entorno profesional.',7);

insert into examen (titulo, cantidad_preguntas, descripcion, id_subtema) values 
('Examen Diagnóstico de Álgebra Lineal',3,'Evaluación corta para identificar conocimientos previos.',5);

insert into examen (titulo, cantidad_preguntas, descripcion, id_subtema) values 
('Examen Diagnóstico de Derivadas',3,'Prueba breve sobre conceptos fundamentales de derivación.',5);

insert into examen (titulo, cantidad_preguntas, descripcion, id_subtema) values 
('Examen Diagnóstico de Cinemática',3,'Evaluación básica sobre movimiento rectilíneo.',4);

insert into examen (titulo, cantidad_preguntas, descripcion, id_subtema) values 
('Evaluación Complementaria de Álgebra Lineal',3,'Prueba adicional de refuerzo académico.',5);

insert into examen (titulo, cantidad_preguntas, descripcion, id_subtema) values 
('Evaluación Complementaria de Derivadas',3,'Refuerzo práctico en cálculo diferencial.',5);

insert into examen (titulo, cantidad_preguntas, descripcion, id_subtema) values 
('Evaluación Complementaria de Cinemática',3,'Ejercicios prácticos de aplicación en física básica.',4);

-- preguntas de examen de dracula 
INSERT INTO pregunta (contenido, id_examen) VALUES
('¿En qué año fue publicada la novela Drácula?', 26),
('¿Cómo se llama el abogado que visita el castillo de Drácula al inicio?', 26),
('¿En qué país está ubicado el castillo del Conde Drácula?', 26),
('¿Cómo se llama la prometida de Jonathan Harker?', 26),
('¿Quién es el cazador de vampiros que lidera al grupo?', 26),
('¿Cómo se llama el barco en que viaja Drácula a Inglaterra?', 26),
('¿Quién es Lucy Westenra en la historia?', 26),
('¿Qué formato narrativo usa principalmente la novela?', 26),
('¿Qué le sucede a Renfield en el manicomio?', 26),
('¿Cómo destruyen finalmente al Conde Drácula?', 26),
('¿Qué debilita al Conde Drácula según la novela?', 26),
('¿Qué transformaciones puede hacer el Conde Drácula?', 26);

-- Opciones examen 26
-- 1. Año de publicación
INSERT INTO opcion (respuesta, es_correcta, id_pregunta) VALUES
('1897', 1, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿En qué año fue publicada la novela Drácula?' AND id_examen = 26)),
('1883', 0, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿En qué año fue publicada la novela Drácula?' AND id_examen = 26)),
('1905', 0, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿En qué año fue publicada la novela Drácula?' AND id_examen = 26)),
('1850', 0, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿En qué año fue publicada la novela Drácula?' AND id_examen = 26));

-- 2. El abogado
INSERT INTO opcion (respuesta, es_correcta, id_pregunta) VALUES
('Jonathan Harker', 1, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿Cómo se llama el abogado que visita el castillo de Drácula al inicio?' AND id_examen = 26)),
('Van Helsing', 0, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿Cómo se llama el abogado que visita el castillo de Drácula al inicio?' AND id_examen = 26)),
('Renfield', 0, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿Cómo se llama el abogado que visita el castillo de Drácula al inicio?' AND id_examen = 26)),
('Arthur Holmwood', 0, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿Cómo se llama el abogado que visita el castillo de Drácula al inicio?' AND id_examen = 26));

-- 3. Ubicación del castillo
INSERT INTO opcion (respuesta, es_correcta, id_pregunta) VALUES
('Transilvania, Rumanía', 1, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿En qué país está ubicado el castillo del Conde Drácula?' AND id_examen = 26)),
('Baviera, Alemania', 0, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿En qué país está ubicado el castillo del Conde Drácula?' AND id_examen = 26)),
('Londres, Inglaterra', 0, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿En qué país está ubicado el castillo del Conde Drácula?' AND id_examen = 26)),
('Viena, Austria', 0, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿En qué país está ubicado el castillo del Conde Drácula?' AND id_examen = 26));

-- 4. La prometida
INSERT INTO opcion (respuesta, es_correcta, id_pregunta) VALUES
('Mina Murray', 1, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿Cómo se llama la prometida de Jonathan Harker?' AND id_examen = 26)),
('Lucy Westenra', 0, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿Cómo se llama la prometida de Jonathan Harker?' AND id_examen = 26)),
('Elizabeth Báthory', 0, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿Cómo se llama la prometida de Jonathan Harker?' AND id_examen = 26)),
('Mary Shelley', 0, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿Cómo se llama la prometida de Jonathan Harker?' AND id_examen = 26));

-- 5. El cazador
INSERT INTO opcion (respuesta, es_correcta, id_pregunta) VALUES
('Abraham Van Helsing', 1, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿Quién es el cazador de vampiros que lidera al grupo?' AND id_examen = 26)),
('Arthur Holmwood', 0, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿Quién es el cazador de vampiros que lidera al grupo?' AND id_examen = 26)),
('Dr. John Seward', 0, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿Quién es el cazador de vampiros que lidera al grupo?' AND id_examen = 26)),
('Quincey Morris', 0, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿Quién es el cazador de vampiros que lidera al grupo?' AND id_examen = 26));

-- 6. El barco
INSERT INTO opcion (respuesta, es_correcta, id_pregunta) VALUES
('El Demeter', 1, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿Cómo se llama el barco en que viaja Drácula a Inglaterra?' AND id_examen = 26)),
('El Nautilus', 0, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿Cómo se llama el barco en que viaja Drácula a Inglaterra?' AND id_examen = 26)),
('El Titanic', 0, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿Cómo se llama el barco en que viaja Drácula a Inglaterra?' AND id_examen = 26)),
('La Perla Negra', 0, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿Cómo se llama el barco en que viaja Drácula a Inglaterra?' AND id_examen = 26));

-- 7. Lucy Westenra
INSERT INTO opcion (respuesta, es_correcta, id_pregunta) VALUES
('La mejor amiga de Mina', 1, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿Quién es Lucy Westenra en la historia?' AND id_examen = 26)),
('La esposa de Van Helsing', 0, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿Quién es Lucy Westenra en la historia?' AND id_examen = 26)),
('La hermana de Drácula', 0, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿Quién es Lucy Westenra en la historia?' AND id_examen = 26)),
('Una sirvienta del castillo', 0, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿Quién es Lucy Westenra en la historia?' AND id_examen = 26));

-- 8. Formato narrativo
INSERT INTO opcion (respuesta, es_correcta, id_pregunta) VALUES
('Cartas y diarios', 1, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿Qué formato narrativo usa principalmente la novela?' AND id_examen = 26)),
('Narrador omnisciente', 0, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿Qué formato narrativo usa principalmente la novela?' AND id_examen = 26)),
('Poema épico', 0, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿Qué formato narrativo usa principalmente la novela?' AND id_examen = 26)),
('Guion cinematográfico', 0, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿Qué formato narrativo usa principalmente la novela?' AND id_examen = 26));

-- 9. Renfield
INSERT INTO opcion (respuesta, es_correcta, id_pregunta) VALUES
('Come insectos y obedece a Drácula', 1, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿Qué le sucede a Renfield en el manicomio?' AND id_examen = 26)),
('Se convierte en vampiro', 0, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿Qué le sucede a Renfield en el manicomio?' AND id_examen = 26)),
('Escapa y huye a Francia', 0, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿Qué le sucede a Renfield en el manicomio?' AND id_examen = 26)),
('Mata a Van Helsing', 0, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿Qué le sucede a Renfield en el manicomio?' AND id_examen = 26));

-- 10. Destrucción de Drácula
INSERT INTO opcion (respuesta, es_correcta, id_pregunta) VALUES
('Con una estaca en el corazón y cortándole la cabeza', 1, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿Cómo destruyen finalmente al Conde Drácula?' AND id_examen = 26)),
('Exponiéndolo a la luz del sol', 0, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿Cómo destruyen finalmente al Conde Drácula?' AND id_examen = 26)),
('Con agua bendita y rezos', 0, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿Cómo destruyen finalmente al Conde Drácula?' AND id_examen = 26)),
('Quemándolo vivo en su ataúd', 0, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿Cómo destruyen finalmente al Conde Drácula?' AND id_examen = 26));

-- 11. Debilidades
INSERT INTO opcion (respuesta, es_correcta, id_pregunta) VALUES
('La luz del sol y el ajo', 1, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿Qué debilita al Conde Drácula según la novela?' AND id_examen = 26)),
('La plata y el fuego', 0, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿Qué debilita al Conde Drácula según la novela?' AND id_examen = 26)),
('El oro y las esmeraldas', 0, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿Qué debilita al Conde Drácula según la novela?' AND id_examen = 26)),
('El hierro frío y la sal', 0, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿Qué debilita al Conde Drácula según la novela?' AND id_examen = 26));

-- 12. Transformaciones
INSERT INTO opcion (respuesta, es_correcta, id_pregunta) VALUES
('En murciélago, lobo y niebla', 1, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿Qué transformaciones puede hacer el Conde Drácula?' AND id_examen = 26)),
('Solo en murciélago', 0, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿Qué transformaciones puede hacer el Conde Drácula?' AND id_examen = 26)),
('En rata, gato y cuervo', 0, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿Qué transformaciones puede hacer el Conde Drácula?' AND id_examen = 26)),
('En pantera y serpiente', 0, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿Qué transformaciones puede hacer el Conde Drácula?' AND id_examen = 26));



--  preguntas de examen de goticas
INSERT INTO pregunta (contenido, id_examen) VALUES
('¿Qué caracteriza a una mujer gótica en la literatura del siglo XIX?', 25),
('¿En qué novela aparece el personaje femenino gótico más famoso, Milady de Winter?', 25),
('¿Cómo se llama la protagonista femenina de "Rebeca" de Daphne du Maurier?', 25),
('¿Qué representa la mujer fatal en la literatura gótica?', 25),
('¿Quién escribió "La dama de blanco", considerada novela gótica clásica?', 25),
('¿Qué elemento es símbolo recurrente de la feminidad gótica?', 25),
('¿Cómo se llama la esposa loca encerrada en el ático en "Jane Eyre"?', 25),
('¿Qué autora escribió "Frankenstein", obra cumbre del gótico romántico?', 25),
('¿Cuál es el rasgo físico más común de la mujer vampiro en la literatura gótica?', 25),
('¿En qué obra aparece Carmilla, uno de los primeros vampiros femeninos?', 25),
('¿Qué sentimiento predomina en los personajes femeninos góticos?', 25),
('¿Que tipos de goticas existen?', 25);

-- Opciones examen 25
-- 1. ¿Qué caracteriza a una mujer gótica en la literatura del siglo XIX?
INSERT INTO opcion (respuesta, es_correcta, id_pregunta) VALUES
('Misterio, palidez y melancolía', 1, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿Qué caracteriza a una mujer gótica en la literatura del siglo XIX?' AND id_examen = 25)),
('Alegría y vida en sociedad', 0, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿Qué caracteriza a una mujer gótica en la literatura del siglo XIX?' AND id_examen = 25)),
('Optimismo y amor por la naturaleza brillante', 0, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿Qué caracteriza a una mujer gótica en la literatura del siglo XIX?' AND id_examen = 25)),
('Racionalismo y pragmatismo absoluto', 0, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿Qué caracteriza a una mujer gótica en la literatura del siglo XIX?' AND id_examen = 25));

-- 2. ¿En qué novela aparece el personaje femenino gótico más famoso, Milady de Winter?
INSERT INTO opcion (respuesta, es_correcta, id_pregunta) VALUES
('Los tres mosqueteros', 1, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿En qué novela aparece el personaje femenino gótico más famoso, Milady de Winter?' AND id_examen = 25)),
('El conde de Montecristo', 0, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿En qué novela aparece el personaje femenino gótico más famoso, Milady de Winter?' AND id_examen = 25)),
('Los miserables', 0, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿En qué novela aparece el personaje femenino gótico más famoso, Milady de Winter?' AND id_examen = 25)),
('Orgullo y prejuicio', 0, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿En qué novela aparece el personaje femenino gótico más famoso, Milady de Winter?' AND id_examen = 25));

-- 3. ¿Cómo se llama la protagonista femenina de "Rebeca" de Daphne du Maurier?
INSERT INTO opcion (respuesta, es_correcta, id_pregunta) VALUES
('No tiene nombre, se llama "yo"', 1, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿Cómo se llama la protagonista femenina de "Rebeca" de Daphne du Maurier?' AND id_examen = 25)),
('Rebeca', 0, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿Cómo se llama la protagonista femenina de "Rebeca" de Daphne du Maurier?' AND id_examen = 25)),
('Mrs. Danvers', 0, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿Cómo se llama la protagonista femenina de "Rebeca" de Daphne du Maurier?' AND id_examen = 25)),
('Beatrice Lacy', 0, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿Cómo se llama la protagonista femenina de "Rebeca" de Daphne du Maurier?' AND id_examen = 25));

-- 4. ¿Qué representa la mujer fatal en la literatura gótica?
INSERT INTO opcion (respuesta, es_correcta, id_pregunta) VALUES
('Peligro, seducción y muerte', 1, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿Qué representa la mujer fatal en la literatura gótica?' AND id_examen = 25)),
('Inocencia y pureza', 0, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿Qué representa la mujer fatal en la literatura gótica?' AND id_examen = 25)),
('Sabiduría maternal y guía espiritual', 0, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿Qué representa la mujer fatal en la literatura gótica?' AND id_examen = 25)),
('La estabilidad del hogar tradicional', 0, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿Qué representa la mujer fatal en la literatura gótica?' AND id_examen = 25));

-- 5. ¿Quién escribió "La dama de blanco", considerada novela gótica clásica?
INSERT INTO opcion (respuesta, es_correcta, id_pregunta) VALUES
('Wilkie Collins', 1, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿Quién escribió "La dama de blanco", considerada novela gótica clásica?' AND id_examen = 25)),
('Edgar Allan Poe', 0, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿Quién escribió "La dama de blanco", considerada novela gótica clásica?' AND id_examen = 25)),
('Charles Dickens', 0, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿Quién escribió "La dama de blanco", considerada novela gótica clásica?' AND id_examen = 25)),
('Oscar Wilde', 0, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿Quién escribió "La dama de blanco", considerada novela gótica clásica?' AND id_examen = 25));

-- 6. ¿Qué elemento es símbolo recurrente de la feminidad gótica?
INSERT INTO opcion (respuesta, es_correcta, id_pregunta) VALUES
('La luna llena y las rosas negras', 1, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿Qué elemento es símbolo recurrente de la feminidad gótica?' AND id_examen = 25)),
('El sol y las flores amarillas', 0, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿Qué elemento es símbolo recurrente de la feminidad gótica?' AND id_examen = 25)),
('El arcoíris y las palomas blancas', 0, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿Qué elemento es símbolo recurrente de la feminidad gótica?' AND id_examen = 25)),
('El trigo y el cielo despejado', 0, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿Qué elemento es símbolo recurrente de la feminidad gótica?' AND id_examen = 25));

-- 7. ¿Cómo se llama la esposa loca encerrada en el ático en "Jane Eyre"?
INSERT INTO opcion (respuesta, es_correcta, id_pregunta) VALUES
('Bertha Mason', 1, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿Cómo se llama la esposa loca encerrada en el ático en "Jane Eyre"?' AND id_examen = 25)),
('Grace Poole', 0, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿Cómo se llama la esposa loca encerrada en el ático en "Jane Eyre"?' AND id_examen = 25)),
('Adele Varens', 0, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿Cómo se llama la esposa loca encerrada en el ático en "Jane Eyre"?' AND id_examen = 25)),
('Blanche Ingram', 0, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿Cómo se llama la esposa loca encerrada en el ático en "Jane Eyre"?' AND id_examen = 25));

-- 8. ¿Qué autora escribió "Frankenstein", obra cumbre del gótico romántico?
INSERT INTO opcion (respuesta, es_correcta, id_pregunta) VALUES
('Mary Shelley', 1, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿Qué autora escribió "Frankenstein", obra cumbre del gótico romántico?' AND id_examen = 25)),
('Ann Radcliffe', 0, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿Qué autora escribió "Frankenstein", obra cumbre del gótico romántico?' AND id_examen = 25)),
('Emily Brontë', 0, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿Qué autora escribió "Frankenstein", obra cumbre del gótico romántico?' AND id_examen = 25)),
('Charlotte Smith', 0, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿Qué autora escribió "Frankenstein", obra cumbre del gótico romántico?' AND id_examen = 25));

-- 9. ¿Cuál es el rasgo físico más común de la mujer vampiro en la literatura gótica?
INSERT INTO opcion (respuesta, es_correcta, id_pregunta) VALUES
('Piel pálida y ojos oscuros', 1, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿Cuál es el rasgo físico más común de la mujer vampiro en la literatura gótica?' AND id_examen = 25)),
('Cabello rubio y ojos azules', 0, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿Cuál es el rasgo físico más común de la mujer vampiro en la literatura gótica?' AND id_examen = 25)),
('Piel bronceada y complexión robusta', 0, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿Cuál es el rasgo físico más común de la mujer vampiro en la literatura gótica?' AND id_examen = 25)),
('Apariencia infantil y pecas', 0, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿Cuál es el rasgo físico más común de la mujer vampiro en la literatura gótica?' AND id_examen = 25));

-- 10. ¿En qué obra aparece Carmilla, uno de los primeros vampiros femeninos?
INSERT INTO opcion (respuesta, es_correcta, id_pregunta) VALUES
('Carmilla de Sheridan Le Fanu', 1, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿En qué obra aparece Carmilla, uno de los primeros vampiros femeninos?' AND id_examen = 25)),
('Drácula de Bram Stoker', 0, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿En qué obra aparece Carmilla, uno de los primeros vampiros femeninos?' AND id_examen = 25)),
('Entrevista con el vampiro', 0, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿En qué obra aparece Carmilla, uno de los primeros vampiros femeninos?' AND id_examen = 25)),
('El vampiro de John Polidori', 0, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿En qué obra aparece Carmilla, uno de los primeros vampiros femeninos?' AND id_examen = 25));

-- 11. ¿Qué sentimiento predomina en los personajes femeninos góticos?
INSERT INTO opcion (respuesta, es_correcta, id_pregunta) VALUES
('Angustia, represión y soledad', 1, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿Qué sentimiento predomina en los personajes femeninos góticos?' AND id_examen = 25)),
('Esperanza y alegría', 0, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿Qué sentimiento predomina en los personajes femeninos góticos?' AND id_examen = 25)),
('Satisfacción y plenitud social', 0, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿Qué sentimiento predomina en los personajes femeninos góticos?' AND id_examen = 25)),
('Indiferencia y apatía total', 0, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿Qué sentimiento predomina en los personajes femeninos góticos?' AND id_examen = 25));
 
INSERT INTO opcion (respuesta, es_correcta, id_pregunta) VALUES
('Goticas Orientales', 0, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿Que tipos de goticas existen?' AND id_examen = 25)),
('Nalgoticas', 0, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿Que tipos de goticas existen? AND id_examen' = 25)),
('Nu Goth', 1, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿Que tipos de goticas existen?' AND id_examen = 25)),
('Gotica europea', 0, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿Que tipos de goticas existen?' AND id_examen = 25));



insert into pregunta (contenido, id_examen) values ('¿Qué es un vector?',1);
insert into pregunta (contenido, id_examen) values ('¿Qué es una matriz?',1);
insert into pregunta (contenido, id_examen) values ('¿Qué es el determinante?',1);
insert into pregunta (contenido, id_examen) values ('¿Qué es una derivada?',2);
insert into pregunta (contenido, id_examen) values ('Derivada de x^2',4);
insert into pregunta (contenido, id_examen) values ('Derivada de una constante',2);
insert into pregunta (contenido, id_examen) values ('¿Qué es velocidad?',3);
insert into pregunta (contenido, id_examen) values ('¿Qué es aceleración?',3);
insert into pregunta (contenido, id_examen) values ('Unidad de aceleración',3);
insert into pregunta (contenido, id_examen) values ('¿Qué es un vector?',1);
insert into pregunta (contenido, id_examen) values ('¿Qué es una matriz?',1);
insert into pregunta (contenido, id_examen) values ('¿Qué es el determinante?',1);
insert into pregunta (contenido, id_examen) values ('¿Qué es una derivada?',2);
insert into pregunta (contenido, id_examen) values ('Derivada de x^2',4);
insert into pregunta (contenido, id_examen) values ('Derivada de una constante',2);
insert into pregunta (contenido, id_examen) values ('¿Qué es velocidad?',3);
insert into pregunta (contenido, id_examen) values ('¿Qué es aceleración?',3);
insert into pregunta (contenido, id_examen) values ('Unidad de aceleración',3);

insert into opcion (respuesta, es_correcta, id_pregunta) values ('Magnitud con dirección',1,1);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('Solo número',0,1);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('Arreglo de números',1,2);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('Ecuación diferencial',0,2);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('Valor escalar',1,3);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('Vector unitario',0,3);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('Razón de cambio',1,4);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('Área bajo la curva',0,4);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('2x',1,5);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('x',0,5);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('0',1,6);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('1',0,6);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('Cambio de posición',1,7);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('Fuerza aplicada',0,7);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('Cambio de velocidad',1,8);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('Distancia recorrida',0,8);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('m/s²',1,9);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('m/s',0,9);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('Magnitud con dirección',1,1);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('Solo número',0,1);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('Arreglo de números',1,2);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('Ecuación diferencial',0,2);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('Valor escalar',1,3);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('Vector unitario',0,3);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('Razón de cambio',1,4);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('Área bajo la curva',0,4);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('2x',1,5);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('x',0,5);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('0',1,6);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('1',0,6);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('Cambio de posición',1,7);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('Fuerza aplicada',0,7);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('Cambio de velocidad',1,8);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('Distancia recorrida',0,8);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('m/s²',1,9);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('m/s',0,9);

insert into intento (calificacion, fecha, id_usuario, id_examen) values (85,'2026-02-12 00:02:25',1,1);
insert into intento (calificacion, fecha, id_usuario, id_examen) values (90,'2026-02-12 00:02:25',1,2);
insert into intento (calificacion, fecha, id_usuario, id_examen) values (78,'2026-02-12 00:02:25',1,3);

insert into publicacion (titulo, descripcion, texto, fecha_creacion, id_usuario, id_estado) values 
('Consejos para mejorar en cálculo diferencial',
'Reflexión académica',
'Una estrategia que me ha funcionado es practicar derivadas todos los días y entender su interpretación gráfica. No solo memoricen fórmulas, intenten comprender qué representa la pendiente en cada punto.',
'2026-02-12 00:02:25',
1,3);

insert into publicacion (titulo, descripcion, texto, fecha_creacion, id_usuario, id_estado) values 
('Cómo entender mejor la física',
'Aporte educativo',
'Para comprender la cinemática recomiendo analizar primero el concepto de movimiento antes de aplicar fórmulas. Entender la relación entre desplazamiento, velocidad y aceleración facilita mucho la resolución de problemas.',
'2026-02-12 00:02:25',
1,3);

insert into publicacion (titulo, descripcion, texto, fecha_creacion, id_usuario, id_estado) values 
('Recomendaciones para química general',
'Experiencia de estudio',
'Al estudiar estequiometría es fundamental practicar el balanceo de ecuaciones antes de realizar cálculos. Dominar ese paso simplifica todos los ejercicios posteriores.',
'2026-02-12 00:02:25',
1,3);

insert into beneficio (nombre, descripcion) values ('Acceso a Biblioteca Virtual','Permite visualizar los recursos educativos organizados por temas y subtemas dentro de la plataforma.');
insert into beneficio (nombre, descripcion) values ('Busqueda y Filtros Avanzados','Permite buscar recursos por texto, etiquetas, dificultad y tema.');
insert into beneficio (nombre, descripcion) values ('Gestion de Notas Personales','Permite crear, editar y eliminar notas personales asociadas o no a recursos.');
insert into beneficio (nombre, descripcion) values ('Publicacion de Notas Compartidas','Permite publicar notas en formato textual para que otros usuarios las consulten.');
insert into beneficio (nombre, descripcion) values ('Examenes por Tema','Permite realizar examenes practicos asociados a temas especificos con calificacion automatica.');
insert into beneficio (nombre, descripcion) values ('Descarga para Uso Offline','Permite descargar recursos para acceso sin conexion segun el rol del usuario.');
insert into beneficio (nombre, descripcion) values ('Acceso a Funcionamiento Offline','Permite acceder a recursos y notas almacenadas localmente sin conexion a internet.');
insert into beneficio (nombre, descripcion) values ('Asistencia Inteligente Contextual','Permite enviar texto seleccionado para recibir explicaciones generadas por IA.');
insert into beneficio (nombre, descripcion) values ('Historial de Consultas IA','Permite visualizar el historial de preguntas realizadas mediante asistencia inteligente.');
insert into beneficio (nombre, descripcion) values ('Acceso Premium Completo','Habilita todas las funcionalidades avanzadas incluyendo asistencia inteligente y descargas extendidas.');
INSERT INTO beneficio (nombre, descripcion) VALUES ('beneficio gotico 2','te dan una gotica con grandes senos');
INSERT INTO beneficio (nombre, descripcion) VALUES ('beneficio gotica','te dan una gotica que tiene el paquete completo senos, gluteos y muslos');

insert into membresia (nombre, descripcion, costo, tipo, duracion_dias) values
('Plan Gratuito',
'Permite acceso basico a la biblioteca virtual, gestion de notas y examenes por tema.',
0,
'Freemium',
36500); -- 100 años prácticamente ilimitado

insert into membresia (nombre, descripcion, costo, tipo, duracion_dias) values
('Plan Premium Mensual',
'Incluye asistencia inteligente contextual, historial de consultas IA y descargas extendidas.',
99,
'Mensual',
30);

insert into membresia (nombre, descripcion, costo, tipo, duracion_dias) values
('membresia perrona',
'es la membresia perrona te trae diferentes tipos de goticas',
499,
'Semestral',
180);
insert into membresia (nombre, descripcion, costo, tipo, duracion_dias) values
('Plan Premium Semestral',
'Incluye todas las funcionalidades premium con acceso extendido por seis meses.',
499,
'Semestral',
180);

insert into membresias_beneficios (id_membresia, id_beneficio) values (1,1);
insert into membresias_beneficios (id_membresia, id_beneficio) values (1,2);
insert into membresias_beneficios (id_membresia, id_beneficio) values (1,3);
insert into membresias_beneficios (id_membresia, id_beneficio) values (1,4);
insert into membresias_beneficios (id_membresia, id_beneficio) values (1,5);
insert into membresias_beneficios (id_membresia, id_beneficio) values (1,7);

insert into membresias_beneficios (id_membresia, id_beneficio) values (2,1);
insert into membresias_beneficios (id_membresia, id_beneficio) values (2,2);
insert into membresias_beneficios (id_membresia, id_beneficio) values (2,3);
insert into membresias_beneficios (id_membresia, id_beneficio) values (2,4);
insert into membresias_beneficios (id_membresia, id_beneficio) values (2,5);
insert into membresias_beneficios (id_membresia, id_beneficio) values (2,6);
insert into membresias_beneficios (id_membresia, id_beneficio) values (2,7);
insert into membresias_beneficios (id_membresia, id_beneficio) values (2,11);
insert into membresias_beneficios (id_membresia, id_beneficio) values (2,12);
insert into membresias_beneficios (id_membresia, id_beneficio) values (2,10);

insert into membresias_beneficios (id_membresia, id_beneficio) values (3,1);
insert into membresias_beneficios (id_membresia, id_beneficio) values (3,12);
insert into membresias_beneficios (id_membresia, id_beneficio) values (3,3);
insert into membresias_beneficios (id_membresia, id_beneficio) values (3,4);
insert into membresias_beneficios (id_membresia, id_beneficio) values (3,11);
insert into membresias_beneficios (id_membresia, id_beneficio) values (3,6);
insert into membresias_beneficios (id_membresia, id_beneficio) values (3,7);
insert into membresias_beneficios (id_membresia, id_beneficio) values (3,11);
insert into membresias_beneficios (id_membresia, id_beneficio) values (3,9);
insert into membresias_beneficios (id_membresia, id_beneficio) values (3,10);

insert into membresias_beneficios (id_membresia, id_beneficio) values (4,12);
insert into membresias_beneficios (id_membresia, id_beneficio) values (4,2);
insert into membresias_beneficios (id_membresia, id_beneficio) values (4,12);
insert into membresias_beneficios (id_membresia, id_beneficio) values (4,4);
insert into membresias_beneficios (id_membresia, id_beneficio) values (4,5);
insert into membresias_beneficios (id_membresia, id_beneficio) values (4,11);
insert into membresias_beneficios (id_membresia, id_beneficio) values (4,7);
insert into membresias_beneficios (id_membresia, id_beneficio) values (4,11);
insert into membresias_beneficios (id_membresia, id_beneficio) values (4,9);
insert into membresias_beneficios (id_membresia, id_beneficio) values (4,12);

insert into usuario_membresia(id_usuario, id_membresia, fecha_inicio, fecha_fin, activa)
values
(1, 1, '2026-02-10 03:15:31', '2126-02-10 03:15:31', true),
(1, 1, '2026-02-10 20:49:14', '2126-02-10 20:49:14', true),
(1, 1, '2026-02-11 01:59:14', '2126-02-11 01:59:14', true),
(1, 1, '2026-02-11 01:59:54', '2126-02-11 01:59:54', true),
(5, 1, '2026-02-11 02:00:40', '2126-02-11 02:00:40', true),
(6, 1, '2026-02-11 02:01:44', '2126-02-11 02:01:44', true),
(7, 1, '2026-02-11 02:03:52', '2126-02-11 02:03:52', true),
(8, 1, '2026-02-11 02:04:45', '2126-02-11 02:04:45', true),
(9, 1, '2026-02-11 02:05:20', '2126-02-11 02:05:20', true),
(10,1, '2026-02-11 02:05:56', '2126-02-11 02:05:56', true);


insert into tema_subtema (id_tema, id_subtema) values (1, 1);
insert into tema_subtema (id_tema, id_subtema) values (1, 2);
insert into tema_subtema (id_tema, id_subtema) values (3, 3);
insert into tema_subtema (id_tema, id_subtema) values (4, 4);
insert into tema_subtema (id_tema, id_subtema) values (5, 5);
insert into tema_subtema (id_tema, id_subtema) values (6, 6);
insert into tema_subtema (id_tema, id_subtema) values (7, 7);

-- 8. Para asignarle recursos vistos/guardados a los usuarios
insert into usuario_recurso (id_usuario, id_recurso) values (1, 1);
insert into usuario_recurso (id_usuario, id_recurso) values (1, 2);
insert into usuario_recurso (id_usuario, id_recurso) values (1, 3);
insert into usuario_recurso (id_usuario, id_recurso) values (1, 4);

-- 9. Nuevas tablas vista de recursos y progreso de lectura.
insert into vista_contenido (id_usuario, id_recurso, fecha_vista) values (1,1,'2026-03-03 10:00:00');
insert into vista_contenido (id_usuario, id_recurso, fecha_vista) values (2,1,'2026-03-03 10:05:00');
insert into vista_contenido (id_usuario, id_recurso, fecha_vista) values (3,2,'2026-03-03 10:10:00');
insert into vista_contenido (id_usuario, id_recurso, fecha_vista) values (4,3,'2026-03-03 10:12:00');
insert into vista_contenido (id_usuario, id_recurso, fecha_vista) values (5,4,'2026-03-03 10:15:00');
insert into vista_contenido (id_usuario, id_recurso, fecha_vista) values (6,1,'2026-03-03 10:18:00');
insert into vista_contenido (id_usuario, id_recurso, fecha_vista) values (7,2,'2026-03-03 10:20:00');

insert into vista_contenido (id_usuario, id_publicacion, fecha_vista) values (1,1,'2026-03-03 11:00:00');
insert into vista_contenido (id_usuario, id_publicacion, fecha_vista) values (2,1,'2026-03-03 11:02:00');
insert into vista_contenido (id_usuario, id_publicacion, fecha_vista) values (3,2,'2026-03-03 11:05:00');
insert into vista_contenido (id_usuario, id_publicacion, fecha_vista) values (4,2,'2026-03-03 11:06:00');
insert into vista_contenido (id_usuario, id_publicacion, fecha_vista) values (5,3,'2026-03-03 11:10:00');
insert into vista_contenido (id_usuario, id_publicacion, fecha_vista) values (6,3,'2026-03-03 11:12:00');

insert into progreso_contenido (id_usuario, id_recurso, porcentaje_leido, ultima_posicion, completado) values (1,1,100,5200,true);
insert into progreso_contenido (id_usuario, id_recurso, porcentaje_leido, ultima_posicion, completado) values (2,1,65,3400,false);
insert into progreso_contenido (id_usuario, id_recurso, porcentaje_leido, ultima_posicion, completado) values (3,2,40,2100,false);
insert into progreso_contenido (id_usuario, id_recurso, porcentaje_leido, ultima_posicion, completado) values (4,3,90,4800,false);
insert into progreso_contenido (id_usuario, id_recurso, porcentaje_leido, ultima_posicion, completado) values (5,4,100,6000,true);

insert into progreso_contenido (id_usuario, id_publicacion, porcentaje_leido, ultima_posicion, completado) values (1,1,100,1800,true);
insert into progreso_contenido (id_usuario, id_publicacion, porcentaje_leido, ultima_posicion, completado) values (2,1,50,900,false);
insert into progreso_contenido (id_usuario, id_publicacion, porcentaje_leido, ultima_posicion, completado) values (3,2,75,1200,false);
insert into progreso_contenido (id_usuario, id_publicacion, porcentaje_leido, ultima_posicion, completado) values (4,3,30,500,false);
