-- MySQL dump 10.13  Distrib 8.0.45, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: academix
-- ------------------------------------------------------
-- Server version	9.6.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
SET @MYSQLDUMP_TEMP_LOG_BIN = @@SESSION.SQL_LOG_BIN;
SET @@SESSION.SQL_LOG_BIN= 0;

--
-- GTID state at the beginning of the backup 
--

SET @@GLOBAL.GTID_PURGED=/*!80000 '+'*/ '5df07814-1425-11f1-9545-005056c00001:1-109';

--
-- Dumping data for table `beneficio`
--

INSERT INTO beneficio (id_beneficio, nombre, descripcion) VALUES (1,'beneficio gotico','te dan una gotica musculosa');
INSERT INTO beneficio (id_beneficio, nombre, descripcion) VALUES (2,'beneficio gotico 2','te dan una gotica con grandes senos');
INSERT INTO beneficio (id_beneficio, nombre, descripcion) VALUES (3,'beneficio gotico 3','Una Nalgotica');
INSERT INTO beneficio (id_beneficio, nombre, descripcion) VALUES (5,'beneficio para testear','saber si sigue la secuencia o si queda el faltante 5');
INSERT INTO beneficio (id_beneficio, nombre, descripcion) VALUES (6,'beneficio gotica 6','te dan una gotica muslona');
INSERT INTO beneficio (id_beneficio, nombre, descripcion) VALUES (7,'beneficio gotica 7','te dan una gotica que tiene el paquete completo senos, gluteos y muslos');
INSERT INTO beneficio (id_beneficio, nombre, descripcion) VALUES (8,'Acceso Total Premium','Acceso ilimitado a todas las salas de estudio y tutorías personalizadas los fines de semana.');
INSERT INTO beneficio (id_beneficio, nombre, descripcion) VALUES (9,'Descargas Ilimitadas','Permite descargar todos los recursos en PDF y videos de alta definición sin restricciones mensuales.');
INSERT INTO beneficio (id_beneficio, nombre, descripcion) VALUES (10,'Soporte 24/7','Asistencia técnica y académica prioritaria en menos de 15 minutos a través de chat en vivo.');
INSERT INTO beneficio (id_beneficio, nombre, descripcion) VALUES (11,'Certificaciones Gratis','Derecho a obtener tres certificados de finalización de curso con validez curricular al mes.');
INSERT INTO beneficio (id_beneficio, nombre, descripcion) VALUES (12,'Acceso Total Premium','Acceso ilimitado a todas las salas de estudio y tutorías personalizadas los fines de semana.');
INSERT INTO beneficio (id_beneficio, nombre, descripcion) VALUES (13,'Descargas Ilimitadas','Permite descargar todos los recursos en PDF y videos de alta definición sin restricciones mensuales.');
INSERT INTO beneficio (id_beneficio, nombre, descripcion) VALUES (14,'Soporte 24/7','Asistencia técnica y académica prioritaria en menos de 15 minutos a través de chat en vivo.');
INSERT INTO beneficio (id_beneficio, nombre, descripcion) VALUES (15,'Certificaciones Gratis','Derecho a obtener tres certificados de finalización de curso con validez curricular al mes.');

--
-- Dumping data for table `estado`
--

INSERT INTO estado (id_estado, nombre) VALUES (1,'activo');
INSERT INTO estado (id_estado, nombre) VALUES (2,'inactivo');
INSERT INTO estado (id_estado, nombre) VALUES (3,'publicado');
INSERT INTO estado (id_estado, nombre) VALUES (4,'espera');
INSERT INTO estado (id_estado, nombre) VALUES (5,'rechazado');

--
-- Dumping data for table `etiqueta`
--

INSERT INTO etiqueta (id_etiqueta, nombre) VALUES (1,'álgebra');
INSERT INTO etiqueta (id_etiqueta, nombre) VALUES (2,'biología celular');
INSERT INTO etiqueta (id_etiqueta, nombre) VALUES (3,'cinemática');
INSERT INTO etiqueta (id_etiqueta, nombre) VALUES (4,'derivadas');
INSERT INTO etiqueta (id_etiqueta, nombre) VALUES (5,'estequiometría');
INSERT INTO etiqueta (id_etiqueta, nombre) VALUES (6,'genética');
INSERT INTO etiqueta (id_etiqueta, nombre) VALUES (7,'integrales');
INSERT INTO etiqueta (id_etiqueta, nombre) VALUES (8,'leyes de newton');
INSERT INTO etiqueta (id_etiqueta, nombre) VALUES (9,'reacciones químicas');

--
-- Dumping data for table `examen`
--

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

--
-- Dumping data for table `intento`
--

INSERT INTO intento (id_intento, calificacion, fecha, id_usuario, id_examen) VALUES (1,85,'2026-02-12 00:02:25',1,1);
INSERT INTO intento (id_intento, calificacion, fecha, id_usuario, id_examen) VALUES (2,90,'2026-02-12 00:02:25',2,2);
INSERT INTO intento (id_intento, calificacion, fecha, id_usuario, id_examen) VALUES (3,78,'2026-02-12 00:02:25',3,3);

--
-- Dumping data for table `membresia`
--

INSERT INTO membresia (id_membresia, nombre, costo, tipo, fecha_inicio, fecha_fin, id_estado, id_rol, descripcion) VALUES (1,'membresia perrona',200,'gotico version premium','2026-02-27 23:14:35','2026-08-27 23:14:35',1,1,'es la membresia perrona te trae diferentes tipos de goticas');
INSERT INTO membresia (id_membresia, nombre, costo, tipo, fecha_inicio, fecha_fin, id_estado, id_rol, descripcion) VALUES (4,'Memebresia ultra premium',400,'extras gotico','2026-02-28 00:37:14','2026-07-28 00:37:14',1,1,'Te trae todo lo anterior mas dos tipos mas de goticas y la gotica completa');
INSERT INTO membresia (id_membresia, nombre, costo, tipo, fecha_inicio, fecha_fin, id_estado, id_rol, descripcion) VALUES (5,'Membresía Estudiante Oro',49,'Mensual','2026-03-02 12:00:00','2026-04-02 12:00:00',1,2,'Plan diseñado para estudiantes de ingeniería que buscan material avanzado y soporte técnico 24/7.');
INSERT INTO membresia (id_membresia, nombre, costo, tipo, fecha_inicio, fecha_fin, id_estado, id_rol, descripcion) VALUES (6,'Membresía Profesional Anual',299,'Anual','2026-03-02 12:00:00','2027-03-02 12:00:00',1,3,'Acceso corporativo completo con certificaciones incluidas y red de contactos profesionales activa.');

--
-- Dumping data for table `membresias_beneficios`
--

INSERT INTO membresias_beneficios (id_membresia, id_beneficio) VALUES (5,1);
INSERT INTO membresias_beneficios (id_membresia, id_beneficio) VALUES (5,2);
INSERT INTO membresias_beneficios (id_membresia, id_beneficio) VALUES (6,8);
INSERT INTO membresias_beneficios (id_membresia, id_beneficio) VALUES (6,9);
INSERT INTO membresias_beneficios (id_membresia, id_beneficio) VALUES (6,10);
INSERT INTO membresias_beneficios (id_membresia, id_beneficio) VALUES (6,11);

--
-- Dumping data for table `nota`
--

INSERT INTO nota (id_nota, contenido, fecha_creacion, fecha_actualizacion, es_compartida, id_usuario, id_recurso) VALUES (1,'Repasar matrices y determinantes para el examen final de álgebra',NULL,NULL,1,1,12);
INSERT INTO nota (id_nota, contenido, fecha_creacion, fecha_actualizacion, es_compartida, id_usuario, id_recurso) VALUES (2,'Fórmulas importantes de cálculo integral y derivadas parciales',NULL,NULL,0,2,12);
INSERT INTO nota (id_nota, contenido, fecha_creacion, fecha_actualizacion, es_compartida, id_usuario, id_recurso) VALUES (3,'Ejercicios clave sobre leyes de Newton y dinámica de fluidos',NULL,NULL,1,3,12);

--
-- Dumping data for table `opcion`
--

INSERT INTO opcion (id_opcion, respuesta, es_correcta, id_pregunta) VALUES (1,'Magnitud con dirección',1,1);
INSERT INTO opcion (id_opcion, respuesta, es_correcta, id_pregunta) VALUES (2,'Solo número',0,1);
INSERT INTO opcion (id_opcion, respuesta, es_correcta, id_pregunta) VALUES (3,'Arreglo de números',1,2);
INSERT INTO opcion (id_opcion, respuesta, es_correcta, id_pregunta) VALUES (4,'Ecuación diferencial',0,2);
INSERT INTO opcion (id_opcion, respuesta, es_correcta, id_pregunta) VALUES (5,'Valor escalar',1,3);
INSERT INTO opcion (id_opcion, respuesta, es_correcta, id_pregunta) VALUES (6,'Vector unitario',0,3);
INSERT INTO opcion (id_opcion, respuesta, es_correcta, id_pregunta) VALUES (7,'Razón de cambio',1,4);
INSERT INTO opcion (id_opcion, respuesta, es_correcta, id_pregunta) VALUES (8,'Área bajo la curva',0,4);
INSERT INTO opcion (id_opcion, respuesta, es_correcta, id_pregunta) VALUES (9,'2x',1,5);
INSERT INTO opcion (id_opcion, respuesta, es_correcta, id_pregunta) VALUES (10,'x',0,5);
INSERT INTO opcion (id_opcion, respuesta, es_correcta, id_pregunta) VALUES (11,'0',1,6);
INSERT INTO opcion (id_opcion, respuesta, es_correcta, id_pregunta) VALUES (12,'1',0,6);
INSERT INTO opcion (id_opcion, respuesta, es_correcta, id_pregunta) VALUES (13,'Cambio de posición',1,7);
INSERT INTO opcion (id_opcion, respuesta, es_correcta, id_pregunta) VALUES (14,'Fuerza aplicada',0,7);
INSERT INTO opcion (id_opcion, respuesta, es_correcta, id_pregunta) VALUES (15,'Cambio de velocidad',1,8);
INSERT INTO opcion (id_opcion, respuesta, es_correcta, id_pregunta) VALUES (16,'Distancia recorrida',0,8);
INSERT INTO opcion (id_opcion, respuesta, es_correcta, id_pregunta) VALUES (17,'m/s²',1,9);
INSERT INTO opcion (id_opcion, respuesta, es_correcta, id_pregunta) VALUES (18,'m/s',0,9);
INSERT INTO opcion (id_opcion, respuesta, es_correcta, id_pregunta) VALUES (19,'Magnitud con dirección',1,1);
INSERT INTO opcion (id_opcion, respuesta, es_correcta, id_pregunta) VALUES (20,'Solo número',0,1);
INSERT INTO opcion (id_opcion, respuesta, es_correcta, id_pregunta) VALUES (21,'Arreglo de números',1,2);
INSERT INTO opcion (id_opcion, respuesta, es_correcta, id_pregunta) VALUES (22,'Ecuación diferencial',0,2);
INSERT INTO opcion (id_opcion, respuesta, es_correcta, id_pregunta) VALUES (23,'Valor escalar',1,3);
INSERT INTO opcion (id_opcion, respuesta, es_correcta, id_pregunta) VALUES (24,'Vector unitario',0,3);
INSERT INTO opcion (id_opcion, respuesta, es_correcta, id_pregunta) VALUES (25,'Razón de cambio',1,4);
INSERT INTO opcion (id_opcion, respuesta, es_correcta, id_pregunta) VALUES (26,'Área bajo la curva',0,4);
INSERT INTO opcion (id_opcion, respuesta, es_correcta, id_pregunta) VALUES (27,'2x',1,5);
INSERT INTO opcion (id_opcion, respuesta, es_correcta, id_pregunta) VALUES (28,'x',0,5);
INSERT INTO opcion (id_opcion, respuesta, es_correcta, id_pregunta) VALUES (29,'0',1,6);
INSERT INTO opcion (id_opcion, respuesta, es_correcta, id_pregunta) VALUES (30,'1',0,6);
INSERT INTO opcion (id_opcion, respuesta, es_correcta, id_pregunta) VALUES (31,'Cambio de posición',1,7);
INSERT INTO opcion (id_opcion, respuesta, es_correcta, id_pregunta) VALUES (32,'Fuerza aplicada',0,7);
INSERT INTO opcion (id_opcion, respuesta, es_correcta, id_pregunta) VALUES (33,'Cambio de velocidad',1,8);
INSERT INTO opcion (id_opcion, respuesta, es_correcta, id_pregunta) VALUES (34,'Distancia recorrida',0,8);
INSERT INTO opcion (id_opcion, respuesta, es_correcta, id_pregunta) VALUES (35,'m/s²',1,9);
INSERT INTO opcion (id_opcion, respuesta, es_correcta, id_pregunta) VALUES (36,'m/s',0,9);

--
-- Dumping data for table `pregunta`
--

INSERT INTO pregunta (id_pregunta, contenido, id_examen) VALUES (1,'¿Qué es un vector?',1);
INSERT INTO pregunta (id_pregunta, contenido, id_examen) VALUES (2,'¿Qué es una matriz?',1);
INSERT INTO pregunta (id_pregunta, contenido, id_examen) VALUES (3,'¿Qué es el determinante?',1);
INSERT INTO pregunta (id_pregunta, contenido, id_examen) VALUES (4,'¿Qué es una derivada?',2);
INSERT INTO pregunta (id_pregunta, contenido, id_examen) VALUES (5,'Derivada de x^2',4);
INSERT INTO pregunta (id_pregunta, contenido, id_examen) VALUES (6,'Derivada de una constante',2);
INSERT INTO pregunta (id_pregunta, contenido, id_examen) VALUES (7,'¿Qué es velocidad?',3);
INSERT INTO pregunta (id_pregunta, contenido, id_examen) VALUES (8,'¿Qué es aceleración?',3);
INSERT INTO pregunta (id_pregunta, contenido, id_examen) VALUES (9,'Unidad de aceleración',3);
INSERT INTO pregunta (id_pregunta, contenido, id_examen) VALUES (10,'¿Qué es un vector?',1);
INSERT INTO pregunta (id_pregunta, contenido, id_examen) VALUES (11,'¿Qué es una matriz?',1);
INSERT INTO pregunta (id_pregunta, contenido, id_examen) VALUES (12,'¿Qué es el determinante?',1);
INSERT INTO pregunta (id_pregunta, contenido, id_examen) VALUES (13,'¿Qué es una derivada?',2);
INSERT INTO pregunta (id_pregunta, contenido, id_examen) VALUES (14,'Derivada de x^2',4);
INSERT INTO pregunta (id_pregunta, contenido, id_examen) VALUES (15,'Derivada de una constante',2);
INSERT INTO pregunta (id_pregunta, contenido, id_examen) VALUES (16,'¿Qué es velocidad?',3);
INSERT INTO pregunta (id_pregunta, contenido, id_examen) VALUES (17,'¿Qué es aceleración?',3);
INSERT INTO pregunta (id_pregunta, contenido, id_examen) VALUES (18,'Unidad de aceleración',3);

--
-- Dumping data for table `publicacion`
--

INSERT INTO publicacion (id_publicacion, titulo, descripcion, texto, fecha_creacion, id_usuario, id_estado) VALUES (1,'Consejos para cálculo','Tips útiles','Practica diario','2026-02-12 00:02:25',1,3);
INSERT INTO publicacion (id_publicacion, titulo, descripcion, texto, fecha_creacion, id_usuario, id_estado) VALUES (2,'Física sin miedo','Motivación','Entiende conceptos','2026-02-12 00:02:25',2,3);
INSERT INTO publicacion (id_publicacion, titulo, descripcion, texto, fecha_creacion, id_usuario, id_estado) VALUES (3,'Química fácil','Guía rápida','Balancea ecuaciones','2026-02-12 00:02:25',3,3);

--
-- Dumping data for table `recurso`
--

INSERT INTO recurso (id_recurso, contenido, titulo, descripcion, url_archivo, fecha_publicacion, id_tipo, id_estado, id_subtema) VALUES (9,'contenido 2','Guía de Derivadas PDF','Ejercicios resueltos','https://academix/documentos/derivadas.pdf','2026-03-02 02:54:20',2,3,2);
INSERT INTO recurso (id_recurso, contenido, titulo, descripcion, url_archivo, fecha_publicacion, id_tipo, id_estado, id_subtema) VALUES (10,'contenido 4','Cinemática en PDF','Movimiento rectilíneo','https://academix/documentos/cinematica.pdf','2026-03-02 02:54:44',2,3,4);
INSERT INTO recurso (id_recurso, contenido, titulo, descripcion, url_archivo, fecha_publicacion, id_tipo, id_estado, id_subtema) VALUES (11,'contenido 6','Estequiometría PDF','Ejercicios químicos','https://academix/documentos/estequiometria.pdf','2026-03-02 02:54:55',2,3,6);
INSERT INTO recurso (id_recurso, contenido, titulo, descripcion, url_archivo, fecha_publicacion, id_tipo, id_estado, id_subtema) VALUES (12,'contenido 6','E PDF','Ejercicios','https://academix/documentos/genetica.pdf','2026-03-02 02:56:56',2,3,7);

--
-- Dumping data for table `recurso_etiqueta`
--

INSERT INTO recurso_etiqueta (id_recurso, id_etiqueta) VALUES (9,1);
INSERT INTO recurso_etiqueta (id_recurso, id_etiqueta) VALUES (10,1);
INSERT INTO recurso_etiqueta (id_recurso, id_etiqueta) VALUES (11,1);
INSERT INTO recurso_etiqueta (id_recurso, id_etiqueta) VALUES (12,1);

--
-- Dumping data for table `rol`
--

INSERT INTO rol (id_rol, nombre) VALUES (1,'admin');
INSERT INTO rol (id_rol, nombre) VALUES (2,'normal');
INSERT INTO rol (id_rol, nombre) VALUES (3,'premium');

--
-- Dumping data for table `subtema`
--

INSERT INTO subtema (id_subtema, nombre, descripcion, nivel_dificultad) VALUES (1,'subtema perron','perronsissimo','alto');
INSERT INTO subtema (id_subtema, nombre, descripcion, nivel_dificultad) VALUES (2,'subtema perron 2','perronsisssimo','alto');
INSERT INTO subtema (id_subtema, nombre, descripcion, nivel_dificultad) VALUES (3,'Biologia','subtema de biologia','alta');
INSERT INTO subtema (id_subtema, nombre, descripcion, nivel_dificultad) VALUES (4,'Ciencias','subtema de ciencia','alta');
INSERT INTO subtema (id_subtema, nombre, descripcion, nivel_dificultad) VALUES (5,'Matematicas','subtema de Matematicas','alta');
INSERT INTO subtema (id_subtema, nombre, descripcion, nivel_dificultad) VALUES (6,'Politica','subtema de Politica','alta');
INSERT INTO subtema (id_subtema, nombre, descripcion, nivel_dificultad) VALUES (7,'Etica','subtema de Etica','alta');

--
-- Dumping data for table `tema`
--

INSERT INTO tema (id_tema, nombre, descripcion, nivel_dificultad) VALUES (1,'Tema 1','temamaste','intermedio');
INSERT INTO tema (id_tema, nombre, descripcion, nivel_dificultad) VALUES (2,'Goticas','es sobre como son las goticas','intermedio');
INSERT INTO tema (id_tema, nombre, descripcion, nivel_dificultad) VALUES (3,'Tema 2','Temas numero 2','intermedio');
INSERT INTO tema (id_tema, nombre, descripcion, nivel_dificultad) VALUES (4,'Tema 3','Tema numero 3','avanzado');
INSERT INTO tema (id_tema, nombre, descripcion, nivel_dificultad) VALUES (5,'Tema 4','Tema numero 4','avanzado');
INSERT INTO tema (id_tema, nombre, descripcion, nivel_dificultad) VALUES (6,'Tema 5','Tema numero 5','básico');
INSERT INTO tema (id_tema, nombre, descripcion, nivel_dificultad) VALUES (7,'Tema 6','Tema numero 6','intermedio');

--
-- Dumping data for table `tema_subtema`
--


--
-- Dumping data for table `tipo`
--

INSERT INTO tipo (id_tipo, nombre) VALUES (1,'pdf');
INSERT INTO tipo (id_tipo, nombre) VALUES (2,'texto');

--
-- Dumping data for table `usuario`
--

INSERT INTO usuario (id_usuario, nombre, apellido_paterno, apellido_materno, correo, contrasena_hash, fecha_registro, id_rol, id_estado, id_membresia) VALUES (1,'Arath','Porcayo','Mercado','arath@gmail.com','$argon2id$v=19$m=65536,t=3,p=4$A0CotRZCCKH0ntNaS4kxJg$8iRnYmBJ94/6iXxQ/I62vG4VPSe/5Rgd/ZU6NKz1OR4','2026-02-27 23:24:37',1,1,1);
INSERT INTO usuario (id_usuario, nombre, apellido_paterno, apellido_materno, correo, contrasena_hash, fecha_registro, id_rol, id_estado, id_membresia) VALUES (2,'Ramses','Porcayo','Mercado','ramses@gmail.com','$argon2id$v=19$m=65536,t=3,p=4$6h0DAIAwBkCI0ZqTUupdCw$933XRJE8DSURZv8bTLU3Erbyu//J7whKrCn2358dt2E','2026-02-28 00:22:55',2,1,1);
INSERT INTO usuario (id_usuario, nombre, apellido_paterno, apellido_materno, correo, contrasena_hash, fecha_registro, id_rol, id_estado, id_membresia) VALUES (3,'Aratheo','Porcayo','Mercado','aratheo@gmail.com','$argon2id$v=19$m=65536,t=3,p=4$R2jtfS+F8H5vTem99/5/bw$g9FyzaAqd2QuJRKgEqr8DMv+XK3yOePhOpEefvSrhh0','2026-02-28 02:39:54',1,1,1);
INSERT INTO usuario (id_usuario, nombre, apellido_paterno, apellido_materno, correo, contrasena_hash, fecha_registro, id_rol, id_estado, id_membresia) VALUES (14,'Jafet Jeshua','Gamboa','Lopez','jafetgamboa6@gmail.com','$argon2id$v=19$m=65536,t=3,p=4$e8+5V0rJ+X+vFUII4RxjzA$KFc6foCOPs8D23iFAIesdlfpwYeeB07hOhLS2oK9LTc','2026-03-02 03:31:29',1,1,1);

--
-- Dumping data for table `usuario_recurso`
--

SET @@SESSION.SQL_LOG_BIN = @MYSQLDUMP_TEMP_LOG_BIN;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed
