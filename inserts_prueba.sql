-- 1. Tablas independientes (Sin llaves foráneas)
insert into estado (nombre) values ('activo');
insert into estado (nombre) values ('inactivo');
insert into estado (nombre) values ('publicado');
insert into estado (nombre) values ('espera');
insert into estado (nombre) values ('rechazado');

insert into rol (nombre) values ('admin');
insert into rol (nombre) values ('normal');
insert into rol (nombre) values ('premium');

insert into tipo (nombre) values ('pdf');
insert into tipo (nombre) values ('texto');

insert into etiqueta (nombre) values ('álgebra');
insert into etiqueta (nombre) values ('biología celular');
insert into etiqueta (nombre) values ('cinemática');
insert into etiqueta (nombre) values ('derivadas');
insert into etiqueta (nombre) values ('estequiometría');
insert into etiqueta (nombre) values ('genética');
insert into etiqueta (nombre) values ('integrales');
insert into etiqueta (nombre) values ('leyes de newton');
insert into etiqueta (nombre) values ('reacciones químicas');

insert into tema (nombre, descripcion, nivel_dificultad) values ('Fundamentos de Álgebra','Conceptos básicos de álgebra y operaciones fundamentales','intermedio');
insert into tema (nombre, descripcion, nivel_dificultad) values ('Introducción a la Biología','Principios esenciales de la biología general','intermedio');
insert into tema (nombre, descripcion, nivel_dificultad) values ('Cálculo Diferencial','Estudio de límites y derivadas','intermedio');
insert into tema (nombre, descripcion, nivel_dificultad) values ('Física Mecánica','Análisis del movimiento y fuerzas','avanzado');
insert into tema (nombre, descripcion, nivel_dificultad) values ('Química General','Estructura de la materia y reacciones químicas','avanzado');
insert into tema (nombre, descripcion, nivel_dificultad) values ('Ética Profesional','Principios éticos en el ejercicio profesional','básico');
insert into tema (nombre, descripcion, nivel_dificultad) values ('Ciencias Políticas','Conceptos fundamentales del sistema político','intermedio');

insert into subtema (nombre, descripcion, nivel_dificultad) values ('Vectores y Matrices','Operaciones con vectores y matrices','intermedio');
insert into subtema (nombre, descripcion, nivel_dificultad) values ('Derivadas Básicas','Conceptos fundamentales de derivación','intermedio');
insert into subtema (nombre, descripcion, nivel_dificultad) values ('Biología Celular','Estructura y función celular','intermedio');
insert into subtema (nombre, descripcion, nivel_dificultad) values ('Cinemática','Estudio del movimiento rectilíneo','avanzado');
insert into subtema (nombre, descripcion, nivel_dificultad) values ('Álgebra Lineal','Sistemas de ecuaciones y espacios vectoriales','avanzado');
insert into subtema (nombre, descripcion, nivel_dificultad) values ('Política Contemporánea','Análisis de sistemas políticos actuales','basico');
insert into subtema (nombre, descripcion, nivel_dificultad) values ('Ética y Sociedad','Relación entre ética y entorno social','intermedio');

-- 2. Membresías y beneficios
insert into beneficio (nombre, descripcion) values
('Acceso a Biblioteca','Permite acceder a los recursos educativos disponibles.'),
('Busqueda de Recursos','Permite buscar y filtrar recursos por diferentes criterios.'),
('Gestion de Notas','Permite crear, editar y eliminar notas personales.'),
('Notas Compartidas','Permite publicar notas visibles para otros usuarios.');

-- acceso
insert into beneficio (nombre, descripcion) values
('Acceso a Examenes Basicos','Permite realizar examenes de nivel basico.');

insert into beneficio (nombre, descripcion) values
('Acceso a Examenes Avanzados','Permite realizar examenes de nivel avanzado.');

-- intentos
insert into beneficio (nombre, descripcion) values
('Intentos Limitados (2 por examen)','Limita a solo dos intentos por examen.');

insert into beneficio (nombre, descripcion) values
('Intentos Ilimitados','Permite repetir examenes sin limite.');

-- resultados
insert into beneficio (nombre, descripcion) values
('Ver Solo Calificacion','Muestra solo la calificacion final.');

insert into beneficio (nombre, descripcion) values
('Ver Desglose Completo','Muestra respuestas correctas e incorrectas');

-- historial
insert into beneficio (nombre, descripcion) values
('Historial de Intentos','Permite ver intentos anteriores de examenes.');

insert into beneficio (nombre, descripcion) values
('Descarga Offline','Permite descargar recursos para uso sin internet.'),
('Modo Offline','Permite acceder a contenido sin conexion.'),
('Asistente IA','Permite obtener explicaciones con inteligencia artificial.'),
('Historial IA','Permite ver consultas anteriores con IA.');

insert into membresia (nombre, descripcion, costo, tipo, duracion_dias) values
('Plan Gratuito',
'Acceso basico a recursos, notas y examenes con limitaciones.',
0,
'Freemium',
36500); -- 100 años prácticamente ilimitado

insert into membresia (nombre, descripcion, costo, tipo, duracion_dias) values
('Plan Premium Mensual',
'Acceso completo sin restricciones incluyendo examenes avanzados, IA y contenido offline.',
99,
'Mensual',
30);

insert into membresia (nombre, descripcion, costo, tipo, duracion_dias) values
('Plan Premium Semestral',
'Acceso completo sin restricciones incluyendo examenes avanzados, IA y contenido offline.',
499,
'Semestral',
180);

insert into membresia (nombre, descripcion, costo, tipo, duracion_dias) values
('Plan Premium Anual',
'Acceso completo sin restricciones incluyendo examenes avanzados, IA y contenido offline.',
899,
'Anual',
365);

insert into membresias_beneficios values (1,1); -- biblioteca
insert into membresias_beneficios values (1,2); -- busqueda
insert into membresias_beneficios values (1,3); -- notas
insert into membresias_beneficios values (1,4); -- notas compartidas

-- examenes
insert into membresias_beneficios values (1,5); -- basicos
insert into membresias_beneficios values (1,7); -- 1 intento
insert into membresias_beneficios values (1,9); -- solo calificacion
insert into membresias_beneficios values (1,11);

-- base
insert into membresias_beneficios values (2,1);
insert into membresias_beneficios values (2,2);
insert into membresias_beneficios values (2,3);
insert into membresias_beneficios values (2,4);

-- examenes completos
insert into membresias_beneficios values (2,5); -- basicos
insert into membresias_beneficios values (2,6); -- avanzados
insert into membresias_beneficios values (2,8); -- ilimitados
insert into membresias_beneficios values (2,10); -- desglose
insert into membresias_beneficios values (2,11); -- historial

-- extras
insert into membresias_beneficios values (2,12); -- descarga
insert into membresias_beneficios values (2,13); -- offline
insert into membresias_beneficios values (2,14); -- IA
insert into membresias_beneficios values (2,15); -- historial IA

-- base
insert into membresias_beneficios values (3,1);
insert into membresias_beneficios values (3,2);
insert into membresias_beneficios values (3,3);
insert into membresias_beneficios values (3,4);

-- examenes completos
insert into membresias_beneficios values (3,5); -- basicos
insert into membresias_beneficios values (3,6); -- avanzados
insert into membresias_beneficios values (3,8); -- ilimitados
insert into membresias_beneficios values (3,10); -- desglose
insert into membresias_beneficios values (3,11); -- historial

-- extras
insert into membresias_beneficios values (3,12); -- descarga
insert into membresias_beneficios values (3,13); -- offline
insert into membresias_beneficios values (3,14); -- IA
insert into membresias_beneficios values (3,15); -- historial IA

-- base
insert into membresias_beneficios values (4,1);
insert into membresias_beneficios values (4,2);
insert into membresias_beneficios values (4,3);
insert into membresias_beneficios values (4,4);

-- examenes completos
insert into membresias_beneficios values (4,5); -- basicos
insert into membresias_beneficios values (4,6); -- avanzados
insert into membresias_beneficios values (4,8); -- ilimitados
insert into membresias_beneficios values (4,10); -- desglose
insert into membresias_beneficios values (4,11); -- historial

-- extras
insert into membresias_beneficios values (4,12); -- descarga
insert into membresias_beneficios values (4,13); -- offline
insert into membresias_beneficios values (4,14); -- IA
insert into membresias_beneficios values (4,15); -- historial IA

-- 3. Usuarios (Actualizados con tu nuevo listado, dependen de Rol y Estado)
insert into usuario (nombre, apellido_paterno, apellido_materno, correo, contrasena_hash, fecha_registro, id_rol, id_estado) values
('Jafet Jeshua', 'Gamboa', 'Lopez', 'jafetgamboa6@gmail.com', '$argon2id$v=19$m=65536,t=3,p=4$JcTYO0cIwXjvvXdOCWFsDQ$mbWDvrb9lfpEcdvmuxvq7t7uaJapT7FG+lUoLt5/bbw', '2026-02-10 03:15:31', 1, 1),
('Carlos', 'Hernandez', 'Lopez', 'carlos.hernandez@gmail.com', '$argon2id$v=19$m=65536,t=3,p=4$GUMoJQSgVAqhlBJi7L333g$aqxnkzUaQx9CxPpgWnz5mw4ijaQUBbb8H+s7YUKBKX4', '2026-02-10 20:49:14', 2, 1),
('Maria', 'De La Concepcion', 'Gonzalez', 'maria.gonzalez@gmail.com', '$argon2id$v=19$m=65536,t=3,p=4$GUMoJQSgVAqhlBJi7L333g$aqxnkzUaQx9CxPpgWnz5mw4ijaQUBbb8H+s7YUKBKX4', '2026-02-11 01:59:14', 2, 1),
('Luis', 'Ramirez', 'Torres', 'luis.ramirez@gmail.com', '$argon2id$v=19$m=65536,t=3,p=4$GUMoJQSgVAqhlBJi7L333g$aqxnkzUaQx9CxPpgWnz5mw4ijaQUBbb8H+s7YUKBKX4', '2026-02-11 01:59:54', 2, 1),
('Jose', 'Perez', 'Castillo', 'jose.perez@gmail.com', '$argon2id$v=19$m=65536,t=3,p=4$GUMoJQSgVAqhlBJi7L333g$aqxnkzUaQx9CxPpgWnz5mw4ijaQUBbb8H+s7YUKBKX4', '2026-02-11 02:00:40', 2, 1),
('Fernanda', 'Sanchez', 'Morales', 'fernanda.sanchez@gmail.com', '$argon2id$v=19$m=65536,t=3,p=4$GUMoJQSgVAqhlBJi7L333g$aqxnkzUaQx9CxPpgWnz5mw4ijaQUBbb8H+s7YUKBKX4', '2026-02-11 02:01:44', 2, 1),
('Diego', 'Navarro', 'Ortiz', 'diego.navarro@gmail.com', '$argon2id$v=19$m=65536,t=3,p=4$GUMoJQSgVAqhlBJi7L333g$aqxnkzUaQx9CxPpgWnz5mw4ijaQUBbb8H+s7YUKBKX4', '2026-02-11 02:03:52', 2, 1),
('Laura', 'Cruz', 'Mendoza', 'laura.cruz@gmail.com', '$argon2id$v=19$m=65536,t=3,p=4$GUMoJQSgVAqhlBJi7L333g$aqxnkzUaQx9CxPpgWnz5mw4ijaQUBbb8H+s7YUKBKX4', '2026-02-11 02:04:45', 3, 1),
('Miguel', 'Rojas', 'Vazquez', 'miguel.rojas@gmail.com', '$argon2id$v=19$m=65536,t=3,p=4$GUMoJQSgVAqhlBJi7L333g$aqxnkzUaQx9CxPpgWnz5mw4ijaQUBbb8H+s7YUKBKX4', '2026-02-11 02:05:20', 3, 1),
('Daniela', 'Jimenez', 'Herrera', 'daniela.jimenez@gmail.com', '$argon2id$v=19$m=65536,t=3,p=4$GUMoJQSgVAqhlBJi7L333g$aqxnkzUaQx9CxPpgWnz5mw4ijaQUBbb8H+s7YUKBKX4', '2026-02-11 02:05:56', 3, 1);

insert into usuario_membresia(id_usuario, id_membresia, fecha_inicio, fecha_fin, activa)
values
(1, 1, '2026-02-10 03:15:31', '2126-02-10 03:15:31', true),
(2, 1, '2026-02-10 20:49:14', '2126-02-10 20:49:14', true),
(3, 1, '2026-02-11 01:59:14', '2126-02-11 01:59:14', true),
(4, 1, '2026-02-11 01:59:54', '2126-02-11 01:59:54', true),
(5, 1, '2026-02-11 02:00:40', '2126-02-11 02:00:40', true),
(6, 1, '2026-02-11 02:01:44', '2126-02-11 02:01:44', true),
(7, 1, '2026-02-11 02:03:52', '2126-02-11 02:03:52', true),
(8, 2, '2026-02-11 02:04:45', '2126-02-11 02:04:45', true),
(9, 3, '2026-02-11 02:05:20', '2126-02-11 02:05:20', true),
(10,4, '2026-02-11 02:05:56', '2126-02-11 02:05:56', true);

-- 4. Recursos y Exámenes (Dependen de Subtema, Tipo y Estado)

insert into recurso (contenido, titulo, descripcion, url_archivo, fecha_publicacion, id_tipo, id_estado, id_subtema) values 
('En esta guía encontrarás una explicación paso a paso sobre el concepto de derivada, su interpretación geométrica y su aplicación en problemas reales. Incluye ejemplos resueltos y ejercicios propuestos para reforzar el aprendizaje.',
'Guía de Derivadas PDF',
'Documento con teoría y ejercicios resueltos de cálculo diferencial.',
'https://academix/documentos/derivadas.pdf',
'2026-03-02 02:54:20',
2,3,2);

insert into recurso (contenido, titulo, descripcion, url_archivo, fecha_publicacion, id_tipo, id_estado, id_subtema) values 
('Material introductorio sobre cinemática que explica los conceptos de desplazamiento, velocidad y aceleración. Se presentan fórmulas fundamentales y problemas prácticos aplicados a situaciones reales.',
'Cinemática en PDF',
'Fundamentos del movimiento rectilíneo uniformemente acelerado.',
'https://academix/documentos/cinematica.pdf',
'2026-03-02 02:54:44',
2,3,4);

insert into recurso (contenido, titulo, descripcion, url_archivo, fecha_publicacion, id_tipo, id_estado, id_subtema) values 
('Documento académico que desarrolla el tema de estequiometría, incluyendo balanceo de ecuaciones químicas y cálculos de reactivos y productos. Contiene ejercicios de práctica con soluciones detalladas.',
'Estequiometría PDF',
'Guía práctica para resolución de problemas químicos.',
'https://academix/documentos/estequiometria.pdf',
'2026-03-02 02:54:55',
2,3,6);

insert into recurso (contenido, titulo, descripcion, url_archivo, fecha_publicacion, id_tipo, id_estado, id_subtema) values 
('Recurso enfocado en genética básica, donde se explican las leyes de Mendel, los cuadros de Punnett y la herencia dominante y recesiva. Incluye ejemplos ilustrativos y ejercicios de aplicación.',
'Genética Básica PDF',
'Introducción a los principios fundamentales de la genética.',
'https://academix/documentos/genetica.pdf',
'2026-03-02 02:56:56',
2,3,7);

INSERT INTO recurso (titulo, contenido, descripcion, url_archivo, fecha_publicacion, id_tipo, id_estado, id_subtema, external_id)
VALUES ('Dracula','contenido 9','Dracula" by Bram Stoker is a Gothic horror novel published in 1897','https://www.gutenberg.org/cache/epub/345/pg345-images.html',NOW(), 1,1,1,'OL85892W');

Insert INTO recurso(contenido, titulo, descripcion, url_archivo, external_id, fecha_publicacion, id_tipo, id_estado, id_subtema)
VALUES('Musica Alemana', 'Marcha militar alemana Erika','Musica Alemana de la marcha militar llamada Erika ', 'https://youtu.be/AjPHXhDocWQ?si=H4iPLlXbhDJ-SQyt', '', NOW(), 2, 1, 6);

Insert INTO recurso(contenido, titulo, descripcion, url_archivo, external_id, fecha_publicacion, id_tipo, id_estado, id_subtema)
VALUES('Musica Extranjera', 'Noche Oscura"(Dark is the Night-Тёмная ночь)','Musica extranjera que es de amor pero suena triste y melancolica por el idioma', 'https://youtu.be/Pb9cOAnw6Y4?si=amUglfP6Q92ML8gp', '', NOW(), 2, 1, 7 );

insert into recurso_etiqueta (id_recurso, id_etiqueta) values (1,1);
insert into recurso_etiqueta (id_recurso, id_etiqueta) values (2,1);
insert into recurso_etiqueta (id_recurso, id_etiqueta) values (3,1);
insert into recurso_etiqueta (id_recurso, id_etiqueta) values (4,1);

insert into recurso_etiqueta (id_recurso, id_etiqueta) values (5,1);
insert into recurso_etiqueta (id_recurso, id_etiqueta) values (6,1);
insert into recurso_etiqueta (id_recurso, id_etiqueta) values (7,1);

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

INSERT INTO examen (titulo, cantidad_preguntas, descripcion, id_subtema) VALUES ('examen de Dracula',12,'es sobre el libro de Dracula por Bram stoker',1);

-- 5. Preguntas y Opciones (Dependen de Examen)
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

-- 6. Interacciones de Usuario (Dependen de Usuario, Recurso, Examen)
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
2,3);

insert into publicacion (titulo, descripcion, texto, fecha_creacion, id_usuario, id_estado) values 
('Recomendaciones para química general',
'Experiencia de estudio',
'Al estudiar estequiometría es fundamental practicar el balanceo de ecuaciones antes de realizar cálculos. Dominar ese paso simplifica todos los ejercicios posteriores.',
'2026-02-12 00:02:25',
3,3);

insert into intento (calificacion, fecha, id_usuario, id_examen) values (85,'2026-02-12 00:02:25',1,1);
insert into intento (calificacion, fecha, id_usuario, id_examen) values (90,'2026-02-12 00:02:25',2,2);
insert into intento (calificacion, fecha, id_usuario, id_examen) values (78,'2026-02-12 00:02:25',3,3);

insert into nota (titulo, contenido, fecha_creacion, fecha_actualizacion, es_compartida, id_usuario, id_recurso) 
values ('Nota 1', 'Repasar matrices y determinantes para el examen final de algebra','2026-03-01 22:00:00','2026-03-01 22:00:00',1,1,4);
insert into nota (titulo, contenido, fecha_creacion, fecha_actualizacion, es_compartida, id_usuario, id_recurso) 
values ('Formulas de calculo', 'Formulas importantes de calculo integral y derivadas parciales','2026-03-01 22:05:00','2026-03-01 22:05:00',0,2,4);
insert into nota (titulo, contenido, fecha_creacion, fecha_actualizacion, es_compartida, id_usuario, id_recurso) 
values ('Mis notas', 'Ejercicios clave sobre leyes de Newton y dinamica de fluidos','2026-03-01 22:10:00','2026-03-01 22:10:00',1,3,4);

-- 7. Para conectar los Temas con los Subtemas
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
insert into usuario_recurso (id_usuario, id_recurso) values (2, 3);
insert into usuario_recurso (id_usuario, id_recurso) values (3, 4);

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

-- Examen dracula
-- preguntas de examen de dracula 
INSERT INTO pregunta (contenido, id_examen) VALUES
('¿En qué año fue publicada la novela Drácula?', 13),
('¿Cómo se llama el abogado que visita el castillo de Drácula al inicio?', 13),
('¿En qué país está ubicado el castillo del Conde Drácula?', 13),
('¿Cómo se llama la prometida de Jonathan Harker?', 13),
('¿Quién es el cazador de vampiros que lidera al grupo?', 13),
('¿Cómo se llama el barco en que viaja Drácula a Inglaterra?', 13),
('¿Quién es Lucy Westenra en la historia?', 13),
('¿Qué formato narrativo usa principalmente la novela?', 13),
('¿Qué le sucede a Renfield en el manicomio?', 13),
('¿Cómo destruyen finalmente al Conde Drácula?', 13),
('¿Qué debilita al Conde Drácula según la novela?', 13),
('¿Qué transformaciones puede hacer el Conde Drácula?', 13);

-- Opciones examen 13
-- 1. Año de publicación
INSERT INTO opcion (respuesta, es_correcta, id_pregunta) VALUES
('1897', 1, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿En qué año fue publicada la novela Drácula?' AND id_examen = 13)),
('1883', 0, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿En qué año fue publicada la novela Drácula?' AND id_examen = 13)),
('1905', 0, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿En qué año fue publicada la novela Drácula?' AND id_examen = 13)),
('1850', 0, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿En qué año fue publicada la novela Drácula?' AND id_examen = 13));

-- 2. El abogado
INSERT INTO opcion (respuesta, es_correcta, id_pregunta) VALUES
('Jonathan Harker', 1, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿Cómo se llama el abogado que visita el castillo de Drácula al inicio?' AND id_examen = 13)),
('Van Helsing', 0, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿Cómo se llama el abogado que visita el castillo de Drácula al inicio?' AND id_examen = 13)),
('Renfield', 0, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿Cómo se llama el abogado que visita el castillo de Drácula al inicio?' AND id_examen = 13)),
('Arthur Holmwood', 0, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿Cómo se llama el abogado que visita el castillo de Drácula al inicio?' AND id_examen = 13));

-- 3. Ubicación del castillo
INSERT INTO opcion (respuesta, es_correcta, id_pregunta) VALUES
('Transilvania, Rumanía', 1, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿En qué país está ubicado el castillo del Conde Drácula?' AND id_examen = 13)),
('Baviera, Alemania', 0, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿En qué país está ubicado el castillo del Conde Drácula?' AND id_examen = 13)),
('Londres, Inglaterra', 0, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿En qué país está ubicado el castillo del Conde Drácula?' AND id_examen = 13)),
('Viena, Austria', 0, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿En qué país está ubicado el castillo del Conde Drácula?' AND id_examen = 13));

-- 4. La prometida
INSERT INTO opcion (respuesta, es_correcta, id_pregunta) VALUES
('Mina Murray', 1, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿Cómo se llama la prometida de Jonathan Harker?' AND id_examen = 13)),
('Lucy Westenra', 0, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿Cómo se llama la prometida de Jonathan Harker?' AND id_examen = 13)),
('Elizabeth Báthory', 0, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿Cómo se llama la prometida de Jonathan Harker?' AND id_examen = 13)),
('Mary Shelley', 0, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿Cómo se llama la prometida de Jonathan Harker?' AND id_examen = 13));

-- 5. El cazador
INSERT INTO opcion (respuesta, es_correcta, id_pregunta) VALUES
('Abraham Van Helsing', 1, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿Quién es el cazador de vampiros que lidera al grupo?' AND id_examen = 13)),
('Arthur Holmwood', 0, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿Quién es el cazador de vampiros que lidera al grupo?' AND id_examen = 13)),
('Dr. John Seward', 0, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿Quién es el cazador de vampiros que lidera al grupo?' AND id_examen = 13)),
('Quincey Morris', 0, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿Quién es el cazador de vampiros que lidera al grupo?' AND id_examen = 13));

-- 6. El barco
INSERT INTO opcion (respuesta, es_correcta, id_pregunta) VALUES
('El Demeter', 1, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿Cómo se llama el barco en que viaja Drácula a Inglaterra?' AND id_examen = 13)),
('El Nautilus', 0, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿Cómo se llama el barco en que viaja Drácula a Inglaterra?' AND id_examen = 13)),
('El Titanic', 0, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿Cómo se llama el barco en que viaja Drácula a Inglaterra?' AND id_examen = 13)),
('La Perla Negra', 0, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿Cómo se llama el barco en que viaja Drácula a Inglaterra?' AND id_examen = 13));

-- 7. Lucy Westenra
INSERT INTO opcion (respuesta, es_correcta, id_pregunta) VALUES
('La mejor amiga de Mina', 1, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿Quién es Lucy Westenra en la historia?' AND id_examen = 13)),
('La esposa de Van Helsing', 0, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿Quién es Lucy Westenra en la historia?' AND id_examen = 13)),
('La hermana de Drácula', 0, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿Quién es Lucy Westenra en la historia?' AND id_examen = 13)),
('Una sirvienta del castillo', 0, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿Quién es Lucy Westenra en la historia?' AND id_examen = 13));

-- 8. Formato narrativo
INSERT INTO opcion (respuesta, es_correcta, id_pregunta) VALUES
('Cartas y diarios', 1, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿Qué formato narrativo usa principalmente la novela?' AND id_examen = 13)),
('Narrador omnisciente', 0, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿Qué formato narrativo usa principalmente la novela?' AND id_examen = 13)),
('Poema épico', 0, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿Qué formato narrativo usa principalmente la novela?' AND id_examen = 13)),
('Guion cinematográfico', 0, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿Qué formato narrativo usa principalmente la novela?' AND id_examen = 13));

-- 9. Renfield
INSERT INTO opcion (respuesta, es_correcta, id_pregunta) VALUES
('Come insectos y obedece a Drácula', 1, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿Qué le sucede a Renfield en el manicomio?' AND id_examen = 13)),
('Se convierte en vampiro', 0, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿Qué le sucede a Renfield en el manicomio?' AND id_examen = 13)),
('Escapa y huye a Francia', 0, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿Qué le sucede a Renfield en el manicomio?' AND id_examen = 13)),
('Mata a Van Helsing', 0, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿Qué le sucede a Renfield en el manicomio?' AND id_examen = 13));

-- 10. Destrucción de Drácula
INSERT INTO opcion (respuesta, es_correcta, id_pregunta) VALUES
('Con una estaca en el corazón y cortándole la cabeza', 1, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿Cómo destruyen finalmente al Conde Drácula?' AND id_examen = 13)),
('Exponiéndolo a la luz del sol', 0, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿Cómo destruyen finalmente al Conde Drácula?' AND id_examen = 13)),
('Con agua bendita y rezos', 0, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿Cómo destruyen finalmente al Conde Drácula?' AND id_examen = 13)),
('Quemándolo vivo en su ataúd', 0, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿Cómo destruyen finalmente al Conde Drácula?' AND id_examen = 13));

-- 11. Debilidades
INSERT INTO opcion (respuesta, es_correcta, id_pregunta) VALUES
('La luz del sol y el ajo', 1, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿Qué debilita al Conde Drácula según la novela?' AND id_examen = 13)),
('La plata y el fuego', 0, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿Qué debilita al Conde Drácula según la novela?' AND id_examen = 13)),
('El oro y las esmeraldas', 0, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿Qué debilita al Conde Drácula según la novela?' AND id_examen = 13)),
('El hierro frío y la sal', 0, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿Qué debilita al Conde Drácula según la novela?' AND id_examen = 13));

-- 12. Transformaciones
INSERT INTO opcion (respuesta, es_correcta, id_pregunta) VALUES
('En murciélago, lobo y niebla', 1, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿Qué transformaciones puede hacer el Conde Drácula?' AND id_examen = 13)),
('Solo en murciélago', 0, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿Qué transformaciones puede hacer el Conde Drácula?' AND id_examen = 13)),
('En rata, gato y cuervo', 0, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿Qué transformaciones puede hacer el Conde Drácula?' AND id_examen = 13)),
('En pantera y serpiente', 0, (SELECT id_pregunta FROM pregunta WHERE contenido = '¿Qué transformaciones puede hacer el Conde Drácula?' AND id_examen = 13));

-- ============================================================
-- RESPUESTAS PARA INTENTO 1 (usuario 1, examen 1, cal=85)
-- Preguntas 1,2,3 → 3 preguntas, para 85% necesitamos ~2-3 correctas
-- Con 3 preguntas: 3/3=100%, 2/3=66% → ponemos las 3 correctas
-- y ajustamos la calificacion al recalcular (los datos de seed son aproximados)
-- ============================================================

-- Pregunta 1: ¿Qué es un vector? → correcta: 'Magnitud con dirección' (opcion 1)
INSERT INTO respuesta_intento (id_intento, id_pregunta, id_opcion, es_correcta)
VALUES (1, 1, 1, true);

-- Pregunta 2: ¿Qué es una matriz? → correcta: 'Arreglo de números' (opcion 3)
INSERT INTO respuesta_intento (id_intento, id_pregunta, id_opcion, es_correcta)
VALUES (1, 2, 3, true);

-- Pregunta 3: ¿Qué es el determinante? → incorrecta: 'Vector unitario' (opcion 6)
INSERT INTO respuesta_intento (id_intento, id_pregunta, id_opcion, es_correcta)
VALUES (1, 3, 6, false);

-- ============================================================
-- RESPUESTAS PARA INTENTO 2 (usuario 2, examen 2, cal=90)
-- Examen 2 tiene preguntas 4, 6, 13
-- Pregunta 4: ¿Qué es una derivada?
-- Pregunta 6: Derivada de una constante
-- Pregunta 13: ¿Qué es una derivada? (repetida en examen 2)
-- ============================================================

-- Pregunta 4: ¿Qué es una derivada? → correcta: 'Razón de cambio' (opcion 7)
INSERT INTO respuesta_intento (id_intento, id_pregunta, id_opcion, es_correcta)
VALUES (2, 4, 7, true);

-- Pregunta 6: Derivada de una constante → correcta: '0' (opcion 11)
INSERT INTO respuesta_intento (id_intento, id_pregunta, id_opcion, es_correcta)
VALUES (2, 6, 11, true);

-- Pregunta 13: ¿Qué es una derivada? → incorrecta: 'Área bajo la curva' (opcion 8)
INSERT INTO respuesta_intento (id_intento, id_pregunta, id_opcion, es_correcta)
VALUES (2, 13, 8, false);

-- ============================================================
-- RESPUESTAS PARA INTENTO 3 (usuario 3, examen 3, cal=78)
-- Examen 3 tiene preguntas 7, 8, 9
-- Pregunta 7: ¿Qué es velocidad?
-- Pregunta 8: ¿Qué es aceleración?
-- Pregunta 9: Unidad de aceleración
-- ============================================================

-- Pregunta 7: ¿Qué es velocidad? → correcta: 'Cambio de posición' (opcion 13)
INSERT INTO respuesta_intento (id_intento, id_pregunta, id_opcion, es_correcta)
VALUES (3, 7, 13, true);

-- Pregunta 8: ¿Qué es aceleración? → incorrecta: 'Distancia recorrida' (opcion 16)
INSERT INTO respuesta_intento (id_intento, id_pregunta, id_opcion, es_correcta)
VALUES (3, 8, 16, false);

-- Pregunta 9: Unidad de aceleración → correcta: 'm/s²' (opcion 17)
INSERT INTO respuesta_intento (id_intento, id_pregunta, id_opcion, es_correcta)
VALUES (3, 9, 17, true);

-- OFFLINE
-- Usuario 1 descarga recurso 1 y 2
insert into offline (id_usuario, id_recurso, fecha_descarga, ultima_sincronizacion, activo)
values (1, 1, NOW(), NOW(), true);

insert into offline (id_usuario, id_recurso, fecha_descarga, ultima_sincronizacion, activo)
values (1, 2, NOW(), NOW(), true);

-- Usuario 2 descarga recurso 3
insert into offline (id_usuario, id_recurso, fecha_descarga, ultima_sincronizacion, activo)
values (2, 3, NOW(), NOW(), true);

-- Usuario 3 descarga recurso 4 pero lo eliminó (soft delete)
insert into offline (id_usuario, id_recurso, fecha_descarga, ultima_sincronizacion, activo)
values (3, 4, NOW(), NOW(), false);

-- Usuario premium descarga varios
insert into offline (id_usuario, id_recurso, fecha_descarga, ultima_sincronizacion, activo)
values (8, 1, NOW(), NOW(), true);

insert into offline (id_usuario, id_recurso, fecha_descarga, ultima_sincronizacion, activo)
values (8, 2, NOW(), NOW(), true);

insert into offline (id_usuario, id_recurso, fecha_descarga, ultima_sincronizacion, activo)
values (8, 3, NOW(), NOW(), true);
