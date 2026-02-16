-- Para ejecutar los inserts primero debe de crear la base de datos (se esta utilizando Xampp)
-- Luego ejecutar el backend para hacer las tablas de la base de datos
-- Luego se pueden realizar los inserts

insert into estado (nombre) values
('activo'),
('desactivado'),
('publicado'),
('espera'),
('rechazado');

insert into rol (nombre) values
('administrador'),
('usuario normal'),
('usuario premium');

insert into tipo (nombre) values
('PDF'),
('texto');

insert into tema (nombre, descripcion, nivel_dificultad) values
('Matemáticas', 'Desarrolla pensamiento abstracto y resolución de problemas matemáticos complejos.', 'avanzado'),
('Fisica', 'Explica fenómenos naturales mediante modelos matemáticos.', 'avanzado'),
('Quimica', 'Estudia la composición, estructura y transformación de la materia.', 'avanzado'),
('Biologia', 'Analiza procesos vitales a nivel celular y molecular.', 'avanzado');

insert into subtema (nombre, descripcion, nivel_dificultad) values
('Álgebra Lineal', 'Vectores y matrices', 'avanzado'),
('Cálculo Diferencial', 'Derivadas y aplicaciones', 'avanzado'),
('Cálculo Integral', 'Integrales definidas e indefinidas', 'avanzado'),
('Cinemática', 'Movimiento rectilíneo', 'avanzado'),
('Leyes de Newton', 'Dinámica clásica', 'avanzado'),
('Estequiometría', 'Relaciones cuantitativas', 'avanzado'),
('Biología Celular', 'Estructura y función celular', 'avanzado'),
('Genética', 'Herencia y ADN', 'avanzado');

insert into tema_subtema (id_tema, id_subtema) values
(1, 1),
(1, 2),
(1, 3),
(2, 4),
(2, 5),
(3, 6),
(4, 7),
(4, 8);

insert into etiqueta (nombre) values
('álgebra'),
('biología celular'),
('cinemática'),
('derivadas'),
('estequiometría'),
('genética'),
('integrales'),
('leyes de newton'),
('reacciones químicas');

insert into usuario (nombre, apellido_paterno, apellido_materno, correo, contrasena_hash, fecha_registro, id_rol, id_estado) values
('Jafet Jeshua', 'Gamboa', 'Lopez', 'jafetgamboa6@gmail.com', '$argon2id$v=19$m=65536,t=3,p=4$JcTYO0cIwXjvvXdOCWFsDQ$mbWDvrb9lfpEcdvmuxvq7t7uaJapT7FG+lUoLt5/bbw', '2026-02-10 03:15:31', 1, 1),
('Carlos', 'Hernandez', 'Lopez', 'carlos.hernandez@gmail.com', '$argon2id$v=19$m=65536,t=3,p=4$OwcgRMhZS2nNmXMOodT6vw$4vMC7XRxu9vaKz8LJkpTHF8JDFlh3pU+Ry54xxVWMlU', '2026-02-10 20:49:14', 1, 1),
('Maria', 'De La Concepcion', 'Gonzalez', 'maria.gonzalez@gmail.com', '$argon2id$v=19$m=65536,t=3,p=4$XkvJWUupdc5ZK4UQYiwF4A$Sgchaco20PQSTt2Y91udW9VyQyv4WOGu88xaQ2YKKbU', '2026-02-11 01:59:14', 1, 1),
('Luis', 'Ramirez', 'Torres', 'luis.ramirez@gmail.com', '$argon2id$v=19$m=65536,t=3,p=4$NUYoRQghxDjHuNea0/p/Lw$S6xe40JQu/ocQQYjXez7tgEPqUjvJow2LoLg0WCbYPo', '2026-02-11 01:59:54', 1, 1),
('Jose', 'Perez', 'Castillo', 'jose.perez@gmail.com', '$argon2id$v=19$m=65536,t=3,p=4$uTfGmLO29h7DuJcyJgSgdA$ZBBGwkkkOxi1T1ZsvMmOYJuEZB6uXBheGhFJx5aPsuU', '2026-02-11 02:00:40', 1, 1),
('Fernanda', 'Sanchez', 'Morales', 'fernanda.sanchez@gmail.com', '$argon2id$v=19$m=65536,t=3,p=4$G2MMIWSMEULIWYsxBmAMoQ$n8sEu97wxckt3+P95Ffh3FIkoQ5FzlIYCYPjno7HCZw', '2026-02-11 02:01:44', 1, 1),
('Diego', 'Navarro', 'Ortiz', 'diego.navarro@gmail.com', '$argon2id$v=19$m=65536,t=3,p=4$Ruh9z7n3HqP0HgMgROhdyw$nmrd3X5nlieJEbJS4Rj2QuZgoONHfAD8LOX4Gx42b3k', '2026-02-11 02:03:52', 1, 1),
('Laura', 'Cruz', 'Mendoza', 'laura.cruz@gmail.com', '$argon2id$v=19$m=65536,t=3,p=4$VEopJURIac25l1JKiZHSeg$e2uzMjEcE5RffJH8CUCsB6fyHvu4+Vu9mU3e3RMiYp8', '2026-02-11 02:04:45', 1, 1),
('Miguel', 'Rojas', 'Vazquez', 'miguel.rojas@gmail.com', '$argon2id$v=19$m=65536,t=3,p=4$hJASAkBIyXmPsTaG8L73vg$snfehwurCenc+DiOiKEcaamI0Rxppfj+hmS5VbesYBs', '2026-02-11 02:05:20', 1, 1),
('Daniela', 'Jimenez', 'Herrera', 'daniela.jimenez@gmail.com', '$argon2id$v=19$m=65536,t=3,p=4$FKI0JmRMybl3zjkHgBAihA$CbkbJ2ZI++rvPLSR7XEonun+cAmxNNOrDwNp5NRTmTk', '2026-02-11 02:05:56', 1, 1);

insert into recurso (contenido, titulo, descripcion, url_archivo, fecha_publicacion, id_tipo, id_estado, id_subtema) values
('Introducción al álgebra lineal', 'Álgebra Lineal Básica', 'Apuntes introductorios', NULL, '2026-02-12 00:02:25', 1, 3, 1),
(NULL, 'Guía de Derivadas PDF', 'Ejercicios resueltos', 'https://academix/documentos/derivadas.pdf', '2026-02-12 00:02:25', 2, 3, 2),
('Teoría de integrales', 'Integrales', 'Resumen teórico', NULL, '2026-02-12 00:02:25', 1, 3, 3),
(NULL, 'Cinemática en PDF', 'Movimiento rectilíneo', 'https://academix/documentos/cinematica.pdf', '2026-02-12 00:02:25', 2, 3, 4),
('Explicación de leyes de Newton', 'Leyes de Newton', 'Contenido teórico', NULL, '2026-02-12 00:02:25', 1, 3, 5),
(NULL, 'Estequiometría PDF', 'Ejercicios químicos', 'https://academix/documentos/estequiometria.pdf', '2026-02-12 00:02:25', 2, 3, 6),
('Estructura celular', 'Biología Celular', 'Resumen completo', NULL, '2026-02-12 00:02:25', 1, 3, 7),
(NULL, 'Genética Básica', 'Introducción a genética', 'https://academix/documentos/genetica.pdf', '2026-02-12 00:02:25', 2, 3, 8);

insert into recurso_etiqueta (id_recurso, id_etiqueta) values
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5),
(6, 6),
(7, 8),
(8, 9);

insert into examen (titulo, cantidad_preguntas, descripcion, id_subtema) values
('Examen Álgebra Lineal', 3, 'Evaluación básica', 1),
('Examen Derivadas', 3, 'Derivadas fundamentales', 2),
('Examen Cinemática', 3, 'Movimiento rectilíneo', 4);

insert into pregunta (contenido, id_examen) values
('¿Qué es un vector?', 1),
('¿Qué es una matriz?', 1),
('¿Qué es el determinante?', 1),
('¿Qué es una derivada?', 2),
('Derivada de x^2', 2),
('Derivada de una constante', 2),
('¿Qué es velocidad?', 3),
('¿Qué es aceleración?', 3),
('Unidad de aceleración', 3);

insert into opcion (respuesta, es_correcta, id_pregunta) values
('Magnitud con dirección', 1, 1),
('Solo número', 0, 1),
('Arreglo de números', 1, 2),
('Ecuación diferencial', 0, 2),
('Valor escalar', 1, 3),
('Vector unitario', 0, 3),
('Razón de cambio', 1, 4),
('Área bajo la curva', 0, 4),
('2x', 1, 5),
('x', 0, 5),
('0', 1, 6),
('1', 0, 6),
('Cambio de posición', 1, 7),
('Fuerza aplicada', 0, 7),
('Cambio de velocidad', 1, 8),
('Distancia recorrida', 0, 8),
('m/s²', 1, 9),
('m/s', 0, 9);

insert into publicacion (titulo, descripcion, texto, fecha_creacion, id_usuario, id_estado) values
('Consejos para cálculo', 'Tips útiles', 'Practica diario', '2026-02-12 00:02:25', 1, 3),
('Física sin miedo', 'Motivación', 'Entiende conceptos', '2026-02-12 00:02:25', 2, 3),
('Química fácil', 'Guía rápida', 'Balancea ecuaciones', '2026-02-12 00:02:25', 3, 3);

insert into intento (calificacion, fecha, id_usuario, id_examen) values
(85, '2026-02-12 00:02:25', 1, 1),
(90, '2026-02-12 00:02:25', 2, 2),
(78, '2026-02-12 00:02:25', 3, 3);

insert into nota (contenido, fecha_creacion, fecha_actualizacion, es_compartida, id_usuario, id_recurso) values
('Repasar matrices', '2026-02-12 00:02:25', '2026-02-12 00:02:25', 1, 1, 1),
('Fórmulas importantes', '2026-02-12 00:02:25', '2026-02-12 00:02:25', 0, 2, 2),
('Ejercicios clave', '2026-02-12 00:02:25', '2026-02-12 00:02:25', 1, 3, 3);

insert into usuario_recurso (id_usuario, id_recurso) values
(1, 1),
(1, 2),
(2, 3),
(3, 4),
(4, 5),
(5, 6);
