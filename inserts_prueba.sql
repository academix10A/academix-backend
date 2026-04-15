-- ============================================================
-- inserts_prueba.sql
-- Tablas fijas: estado, rol, tipo, beneficio, membresia,
--   membresias_beneficios, usuario, usuario_membresia, recurso
-- Tablas regeneradas coherentemente con los 17 recursos reales
-- ============================================================

-- ============================================================
-- 1. TABLAS INDEPENDIENTES (sin llaves foráneas)
-- ============================================================

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

-- Etiquetas ajustadas a los temas reales de los 17 recursos
insert into etiqueta (nombre) values ('álgebra');           -- 1
insert into etiqueta (nombre) values ('biología celular');  -- 2
insert into etiqueta (nombre) values ('cinemática');        -- 3
insert into etiqueta (nombre) values ('derivadas');         -- 4
insert into etiqueta (nombre) values ('estequiometría');    -- 5
insert into etiqueta (nombre) values ('genética');          -- 6
insert into etiqueta (nombre) values ('integrales');        -- 7
insert into etiqueta (nombre) values ('leyes de newton');   -- 8
insert into etiqueta (nombre) values ('reacciones químicas'); -- 9
insert into etiqueta (nombre) values ('historia');          -- 10
insert into etiqueta (nombre) values ('literatura');        -- 11
insert into etiqueta (nombre) values ('matemáticas');       -- 12
insert into etiqueta (nombre) values ('política');          -- 13

-- Temas (7 temas que agrupan los subtemas)
insert into tema (nombre, descripcion, nivel_dificultad) values
  ('Fundamentos de Álgebra',   'Conceptos básicos de álgebra y operaciones fundamentales', 'intermedio'); -- 1
insert into tema (nombre, descripcion, nivel_dificultad) values
  ('Introducción a la Biología', 'Principios esenciales de la biología general', 'intermedio');           -- 2
insert into tema (nombre, descripcion, nivel_dificultad) values
  ('Cálculo Diferencial',       'Estudio de límites y derivadas', 'intermedio');                          -- 3
insert into tema (nombre, descripcion, nivel_dificultad) values
  ('Física Mecánica',           'Análisis del movimiento y fuerzas', 'avanzado');                         -- 4
insert into tema (nombre, descripcion, nivel_dificultad) values
  ('Química General',           'Estructura de la materia y reacciones químicas', 'avanzado');            -- 5
insert into tema (nombre, descripcion, nivel_dificultad) values
  ('Historia y Política',       'Historia nacional y sistemas políticos', 'intermedio');                  -- 6
insert into tema (nombre, descripcion, nivel_dificultad) values
  ('Humanidades',               'Literatura, ética y ciencias sociales', 'básico');                       -- 7

-- Subtemas mapeados exactamente a los recursos existentes
insert into subtema (nombre, descripcion, nivel_dificultad) values
  ('Álgebra Lineal',         'Sistemas de ecuaciones, vectores y matrices', 'avanzado');      -- 1
insert into subtema (nombre, descripcion, nivel_dificultad) values
  ('Derivadas Básicas',      'Conceptos fundamentales de derivación', 'intermedio');          -- 2
insert into subtema (nombre, descripcion, nivel_dificultad) values
  ('Biología Celular',       'Estructura y función celular', 'intermedio');                   -- 3
insert into subtema (nombre, descripcion, nivel_dificultad) values
  ('Cinemática',             'Estudio del movimiento rectilíneo', 'avanzado');                -- 4
insert into subtema (nombre, descripcion, nivel_dificultad) values
  ('Aritmética y Álgebra',   'Operaciones aritméticas y fundamentos algebraicos', 'básico'); -- 5
insert into subtema (nombre, descripcion, nivel_dificultad) values
  ('Política Contemporánea', 'Análisis de sistemas políticos e historia nacional', 'intermedio'); -- 6
insert into subtema (nombre, descripcion, nivel_dificultad) values
  ('Literatura y Ética',     'Literatura, humanidades y principios éticos', 'básico');        -- 7
insert into subtema (nombre, descripcion, nivel_dificultad) values
  ('Genética',               'Principios de genética y herencia biológica', 'avanzado');      -- 8
insert into subtema (nombre, descripcion, nivel_dificultad) values
  ('Química Analítica',      'Estequiometría y equilibrio químico', 'avanzado');              -- 9
insert into subtema (nombre, descripcion, nivel_dificultad) values
  ('Historia de las Matemáticas', 'Evolución histórica y filosófica de las matemáticas', 'básico'); -- 10

-- ============================================================
-- 2. MEMBRESÍAS Y BENEFICIOS (sin cambios)
-- ============================================================

insert into beneficio (nombre, descripcion) values
  ('Acceso a Biblioteca Virtual', 'Permite acceder a los recursos educativos disponibles.'),   -- 1
  ('Busqueda de Recursos',        'Permite buscar y filtrar recursos por diferentes criterios.'), -- 2
  ('Gestion de Notas',            'Permite crear, editar y eliminar notas personales.'),         -- 3
  ('Notas Compartidas',           'Permite publicar notas visibles para otros usuarios.');        -- 4

insert into beneficio (nombre, descripcion) values
  ('Acceso a Examenes Basicos',   'Permite realizar examenes de nivel basico.');                 -- 5

insert into beneficio (nombre, descripcion) values
  ('Acceso a Examenes Avanzados', 'Permite realizar examenes de nivel avanzado.');               -- 6

insert into beneficio (nombre, descripcion) values
  ('Intentos Limitados (2 por examen)', 'Limita a solo dos intentos por examen.');              -- 7

insert into beneficio (nombre, descripcion) values
  ('Intentos Ilimitados', 'Permite repetir examenes sin limite.');                               -- 8

insert into beneficio (nombre, descripcion) values
  ('Ver Solo Calificacion', 'Muestra solo la calificacion final.');                              -- 9

insert into beneficio (nombre, descripcion) values
  ('Ver Desglose Completo', 'Muestra respuestas correctas e incorrectas');                       -- 10

insert into beneficio (nombre, descripcion) values
  ('Historial de Intentos', 'Permite ver intentos anteriores de examenes.');                     -- 11

insert into beneficio (nombre, descripcion) values
  ('Descarga Offline',  'Permite descargar recursos para uso sin internet.'),                    -- 12
  ('Modo Offline',      'Permite acceder a contenido sin conexion.'),                            -- 13
  ('Asistente IA',      'Permite obtener explicaciones con inteligencia artificial.'),            -- 14
  ('Historial IA',      'Permite ver consultas anteriores con IA.');                             -- 15

insert into membresia (nombre, descripcion, costo, tipo, duracion_dias) values
  ('Plan Gratuito',
   'Acceso basico a recursos, notas y examenes con limitaciones.',
   0, 'Freemium', 36500);                                                                        -- 1

insert into membresia (nombre, descripcion, costo, tipo, duracion_dias) values
  ('Plan Premium Mensual',
   'Acceso completo sin restricciones incluyendo examenes avanzados, IA y contenido offline.',
   99, 'Mensual', 30);                                                                           -- 2

insert into membresia (nombre, descripcion, costo, tipo, duracion_dias) values
  ('Plan Premium Semestral',
   'Acceso completo sin restricciones incluyendo examenes avanzados, IA y contenido offline.',
   499, 'Semestral', 180);                                                                       -- 3

insert into membresia (nombre, descripcion, costo, tipo, duracion_dias) values
  ('Plan Premium Anual',
   'Acceso completo sin restricciones incluyendo examenes avanzados, IA y contenido offline.',
   899, 'Anual', 365);                                                                           -- 4

-- Plan Gratuito (id=1)
insert into membresias_beneficios values (1,1);   -- biblioteca
insert into membresias_beneficios values (1,2);   -- busqueda
insert into membresias_beneficios values (1,3);   -- notas
insert into membresias_beneficios values (1,4);   -- notas compartidas
insert into membresias_beneficios values (1,5);   -- examenes basicos
insert into membresias_beneficios values (1,7);   -- intentos limitados
insert into membresias_beneficios values (1,9);   -- solo calificacion
insert into membresias_beneficios values (1,11);  -- historial intentos

-- Plan Premium Mensual (id=2)
insert into membresias_beneficios values (2,1);
insert into membresias_beneficios values (2,2);
insert into membresias_beneficios values (2,3);
insert into membresias_beneficios values (2,4);
insert into membresias_beneficios values (2,5);   -- basicos
insert into membresias_beneficios values (2,6);   -- avanzados
insert into membresias_beneficios values (2,8);   -- ilimitados
insert into membresias_beneficios values (2,10);  -- desglose
insert into membresias_beneficios values (2,11);  -- historial
insert into membresias_beneficios values (2,12);  -- descarga
insert into membresias_beneficios values (2,13);  -- offline
insert into membresias_beneficios values (2,14);  -- IA
insert into membresias_beneficios values (2,15);  -- historial IA

-- Plan Premium Semestral (id=3)
insert into membresias_beneficios values (3,1);
insert into membresias_beneficios values (3,2);
insert into membresias_beneficios values (3,3);
insert into membresias_beneficios values (3,4);
insert into membresias_beneficios values (3,5);
insert into membresias_beneficios values (3,6);
insert into membresias_beneficios values (3,8);
insert into membresias_beneficios values (3,10);
insert into membresias_beneficios values (3,11);
insert into membresias_beneficios values (3,12);
insert into membresias_beneficios values (3,13);
insert into membresias_beneficios values (3,14);
insert into membresias_beneficios values (3,15);

-- Plan Premium Anual (id=4)
insert into membresias_beneficios values (4,1);
insert into membresias_beneficios values (4,2);
insert into membresias_beneficios values (4,3);
insert into membresias_beneficios values (4,4);
insert into membresias_beneficios values (4,5);
insert into membresias_beneficios values (4,6);
insert into membresias_beneficios values (4,8);
insert into membresias_beneficios values (4,10);
insert into membresias_beneficios values (4,11);
insert into membresias_beneficios values (4,12);
insert into membresias_beneficios values (4,13);
insert into membresias_beneficios values (4,14);
insert into membresias_beneficios values (4,15);

-- ============================================================
-- 3. USUARIOS (sin cambios)
-- ============================================================

insert into usuario (nombre, apellido_paterno, apellido_materno, correo, contrasena_hash, fecha_registro, id_rol, id_estado) values
  ('Jafet Jeshua', 'Gamboa',           'Lopez',    'jafetgamboa6@gmail.com',        '$argon2id$v=19$m=65536,t=3,p=4$JcTYO0cIwXjvvXdOCWFsDQ$mbWDvrb9lfpEcdvmuxvq7t7uaJapT7FG+lUoLt5/bbw', '2026-02-10 03:15:31', 1, 1),
  ('Carlos',        'Hernandez',        'Lopez',    'carlos.hernandez@gmail.com',    '$argon2id$v=19$m=65536,t=3,p=4$GUMoJQSgVAqhlBJi7L333g$aqxnkzUaQx9CxPpgWnz5mw4ijaQUBbb8H+s7YUKBKX4', '2026-02-10 20:49:14', 2, 1),
  ('Maria',         'De La Concepcion', 'Gonzalez', 'maria.gonzalez@gmail.com',      '$argon2id$v=19$m=65536,t=3,p=4$GUMoJQSgVAqhlBJi7L333g$aqxnkzUaQx9CxPpgWnz5mw4ijaQUBbb8H+s7YUKBKX4', '2026-02-11 01:59:14', 2, 1),
  ('Luis',          'Ramirez',          'Torres',   'luis.ramirez@gmail.com',        '$argon2id$v=19$m=65536,t=3,p=4$GUMoJQSgVAqhlBJi7L333g$aqxnkzUaQx9CxPpgWnz5mw4ijaQUBbb8H+s7YUKBKX4', '2026-02-11 01:59:54', 2, 1),
  ('Jose',          'Perez',            'Castillo', 'jose.perez@gmail.com',          '$argon2id$v=19$m=65536,t=3,p=4$GUMoJQSgVAqhlBJi7L333g$aqxnkzUaQx9CxPpgWnz5mw4ijaQUBbb8H+s7YUKBKX4', '2026-02-11 02:00:40', 2, 1),
  ('Fernanda',      'Sanchez',          'Morales',  'fernanda.sanchez@gmail.com',    '$argon2id$v=19$m=65536,t=3,p=4$GUMoJQSgVAqhlBJi7L333g$aqxnkzUaQx9CxPpgWnz5mw4ijaQUBbb8H+s7YUKBKX4', '2026-02-11 02:01:44', 2, 1),
  ('Diego',         'Navarro',          'Ortiz',    'diego.navarro@gmail.com',       '$argon2id$v=19$m=65536,t=3,p=4$GUMoJQSgVAqhlBJi7L333g$aqxnkzUaQx9CxPpgWnz5mw4ijaQUBbb8H+s7YUKBKX4', '2026-02-11 02:03:52', 2, 1),
  ('Laura',         'Cruz',             'Mendoza',  'laura.cruz@gmail.com',          '$argon2id$v=19$m=65536,t=3,p=4$GUMoJQSgVAqhlBJi7L333g$aqxnkzUaQx9CxPpgWnz5mw4ijaQUBbb8H+s7YUKBKX4', '2026-02-11 02:04:45', 3, 1),
  ('Miguel',        'Rojas',            'Vazquez',  'miguel.rojas@gmail.com',        '$argon2id$v=19$m=65536,t=3,p=4$GUMoJQSgVAqhlBJi7L333g$aqxnkzUaQx9CxPpgWnz5mw4ijaQUBbb8H+s7YUKBKX4', '2026-02-11 02:05:20', 3, 1),
  ('Daniela',       'Jimenez',          'Herrera',  'daniela.jimenez@gmail.com',     '$argon2id$v=19$m=65536,t=3,p=4$GUMoJQSgVAqhlBJi7L333g$aqxnkzUaQx9CxPpgWnz5mw4ijaQUBbb8H+s7YUKBKX4', '2026-02-11 02:05:56', 3, 1);

insert into usuario_membresia (id_usuario, id_membresia, fecha_inicio, fecha_fin, activa) values
  (1,  1, '2026-02-10 03:15:31', '2126-02-10 03:15:31', true),
  (2,  1, '2026-02-10 20:49:14', '2126-02-10 20:49:14', true),
  (3,  1, '2026-02-11 01:59:14', '2126-02-11 01:59:14', true),
  (4,  1, '2026-02-11 01:59:54', '2126-02-11 01:59:54', true),
  (5,  1, '2026-02-11 02:00:40', '2126-02-11 02:00:40', true),
  (6,  1, '2026-02-11 02:01:44', '2126-02-11 02:01:44', true),
  (7,  1, '2026-02-11 02:03:52', '2126-02-11 02:03:52', true),
  (8,  2, '2026-02-11 02:04:45', '2126-02-11 02:04:45', true),
  (9,  3, '2026-02-11 02:05:20', '2126-02-11 02:05:20', true),
  (10, 4, '2026-02-11 02:05:56', '2126-02-11 02:05:56', true);

-- ============================================================
-- 4. RECURSOS (sin cambios — 17 PDFs originales)
-- id_subtema corregido para coincidir con los nuevos subtemas:
--   5 = Aritmética y Álgebra  |  2 = Derivadas  |  6 = Política
--   3 = Biología Celular      |  1 = Álgebra Lineal
--   7 = Literatura y Ética    |  8 = Genética
--   9 = Química Analítica     | 10 = Historia de las Matemáticas
--   4 = Cinemática
-- ============================================================

-- Recurso 1: Aritmética → subtema 5 (Aritmética y Álgebra)
INSERT INTO recurso (contenido, titulo, descripcion, url_archivo, external_id, fecha_publicacion, id_tipo, id_estado, id_subtema)
VALUES ('Aritmética - Pamer',
        'Aritmética',
        'Aritmética',
        'https://drive.google.com/file/d/1X9CMcx7MgqUyBQWCgLxZfSru9k12aGQv/view?usp=drive_link',
        '1X9CMcx7MgqUyBQWCgLxZfSru9k12aGQv',
        NULL, 1, 1, 5);

-- Recurso 2: Cálculo Diferencial → subtema 2 (Derivadas Básicas)
INSERT INTO recurso (contenido, titulo, descripcion, url_archivo, external_id, fecha_publicacion, id_tipo, id_estado, id_subtema)
VALUES ('Libro de cálculo diferencial.',
        'Calculo Diferencial 1',
        'Material de cálculo diferencial.',
        'https://drive.google.com/file/d/1wiWD6PQMuNqta0Ss-FwVUeC_6u9H_Rc5/view?usp=drive_link',
        NULL, '2026-04-11 05:25:54', 1, 1, 2);

-- Recurso 3: Historia México → subtema 6 (Política Contemporánea)
INSERT INTO recurso (contenido, titulo, descripcion, url_archivo, external_id, fecha_publicacion, id_tipo, id_estado, id_subtema)
VALUES ('Antología de lecturas sobre historia nacional.',
        'Antologia de Lecturas Historia de mexico',
        'Material de apoyo de Historia de México.',
        'https://drive.google.com/file/d/1Bd-SHuEPD01PQJs-i0kWOmkJXykQNkwV/view?usp=sharing',
        NULL, '2026-04-11 05:25:54', 1, 1, 6);

-- Recurso 4: Biología Humana → subtema 3 (Biología Celular)
INSERT INTO recurso (contenido, titulo, descripcion, url_archivo, external_id, fecha_publicacion, id_tipo, id_estado, id_subtema)
VALUES ('Libro de biología humana.',
        'Biologia Humana',
        'Material general de biología humana.',
        'https://drive.google.com/file/d/1r7zibwQO3zwakgzEPQMtdJyxA93KUUdd/view?usp=sharing',
        NULL, '2026-04-11 05:25:54', 1, 1, 3);

-- Recurso 5: Álgebra Trilce → subtema 1 (Álgebra Lineal)
INSERT INTO recurso (contenido, titulo, descripcion, url_archivo, external_id, fecha_publicacion, id_tipo, id_estado, id_subtema)
VALUES ('Compendio de álgebra.',
        'Compe Algebra Trilce',
        'Material general de álgebra.',
        'https://drive.google.com/file/d/1j5_Dz8XDCUpjMYjywccoCdDdan9-noi3/view?usp=sharing',
        NULL, '2026-04-11 05:25:54', 1, 1, 1);

-- Recurso 6: Literatura Trilce → subtema 7 (Literatura y Ética)
INSERT INTO recurso (contenido, titulo, descripcion, url_archivo, external_id, fecha_publicacion, id_tipo, id_estado, id_subtema)
VALUES ('Compendio de literatura.',
        'Compe Literatura Trilce',
        'Material general de literatura.',
        'https://drive.google.com/file/d/1v2mEzAWAGUUlild5YHX_j1onSj30UVTi/view?usp=sharing',
        NULL, '2026-04-11 05:25:54', 1, 1, 7);

-- Recurso 7: Conceptos básicos de genética → subtema 8 (Genética)
INSERT INTO recurso (contenido, titulo, descripcion, url_archivo, external_id, fecha_publicacion, id_tipo, id_estado, id_subtema)
VALUES ('Libro introductorio de genética.',
        'Conceptos basicos de genetica',
        'Conceptos básicos de genética.',
        'https://drive.google.com/file/d/1iZV21wcJe-g4unoD69VLhCn7ibzuK54J/view?usp=sharing',
        NULL, '2026-04-11 05:25:54', 1, 1, 8);

-- Recurso 8: Revolución Mexicana → subtema 6 (Política Contemporánea)
INSERT INTO recurso (contenido, titulo, descripcion, url_archivo, external_id, fecha_publicacion, id_tipo, id_estado, id_subtema)
VALUES ('Material histórico de la Revolución Mexicana.',
        'Cuadernos De Historia La Revolucion Mexicana 1985',
        'Obra sobre el proceso revolucionario mexicano.',
        'https://drive.google.com/file/d/1gxcmorF1goExVSgh7_eU6pNOBhWW-zPu/view?usp=sharing',
        NULL, '2026-04-11 05:25:54', 1, 1, 6);

-- Recurso 9: Historia de México I → subtema 6 (Política Contemporánea)
INSERT INTO recurso (contenido, titulo, descripcion, url_archivo, external_id, fecha_publicacion, id_tipo, id_estado, id_subtema)
VALUES ('Libro de Historia de México.',
        'Historia de Mexico I',
        'Primer curso general de Historia de México.',
        'https://drive.google.com/file/d/1RaPKmmwQakkmKoyCzwvAVWGSXx3zx2c0/view?usp=sharing',
        NULL, '2026-04-11 05:25:54', 1, 1, 6);

-- Recurso 10: Estequiometría → subtema 9 (Química Analítica)
INSERT INTO recurso (contenido, titulo, descripcion, url_archivo, external_id, fecha_publicacion, id_tipo, id_estado, id_subtema)
VALUES ('Material de química.',
        'ESTEQUIOMETRIA Y EQUILIBRIO',
        'Material de estequiometría y equilibrio químico.',
        'https://drive.google.com/file/d/1YpvxSiWcI62bn4pl_53kjsbtc5wuzuev/view?usp=sharing',
        NULL, '2026-04-11 05:25:54', 1, 1, 9);

-- Recurso 11: Genética General → subtema 8 (Genética)
INSERT INTO recurso (contenido, titulo, descripcion, url_archivo, external_id, fecha_publicacion, id_tipo, id_estado, id_subtema)
VALUES ('Libro de genética general.',
        'Genetica General',
        'Material de genética general.',
        'https://drive.google.com/file/d/1wFrn1iHo44yVDOsp1mqRRUnQPmni7_hS/view?usp=sharing',
        NULL, '2026-04-11 05:25:54', 1, 1, 8);

-- Recurso 12: Razones y proporciones → subtema 5 (Aritmética y Álgebra)
INSERT INTO recurso (contenido, titulo, descripcion, url_archivo, external_id, fecha_publicacion, id_tipo, id_estado, id_subtema)
VALUES ('Guía de razones y proporciones.',
        'Guía-N°-2-Matemática-Razones-y-proporciones',
        'Material de matemáticas sobre razones y proporciones.',
        'https://drive.google.com/file/d/1UkAYeVsXAlbF411IsZXlf2boIkqX-55E/view?usp=sharing',
        NULL, '2026-04-11 05:25:54', 1, 1, 5);

-- Recurso 13: Historia y filosofía de las matemáticas → subtema 10
INSERT INTO recurso (contenido, titulo, descripcion, url_archivo, external_id, fecha_publicacion, id_tipo, id_estado, id_subtema)
VALUES ('Libro de historia y filosofía matemática.',
        'Historia-y-filosofia-de-las-matematicas',
        'Obra sobre la historia y la filosofía de las matemáticas.',
        'https://drive.google.com/file/d/1VmWd2dYXWFRhxZVhIIJ25-njbmw7kDFq/view?usp=sharing',
        NULL, '2026-04-11 05:25:54', 1, 1, 10);

-- Recurso 14: Literatura Pamer → subtema 7 (Literatura y Ética)
INSERT INTO recurso (contenido, titulo, descripcion, url_archivo, external_id, fecha_publicacion, id_tipo, id_estado, id_subtema)
VALUES ('Libro escolar de literatura.',
        'Literatura - Pamer',
        'Material general de literatura.',
        'https://drive.google.com/file/d/1yuKFGbhh6FCofNRK9oLe2VxQp3NN4JWQ/view?usp=sharing',
        NULL, '2026-04-11 05:25:54', 1, 1, 7);

-- Recurso 15: Matemática Básica para Educación Superior → subtema 5
INSERT INTO recurso (contenido, titulo, descripcion, url_archivo, external_id, fecha_publicacion, id_tipo, id_estado, id_subtema)
VALUES ('Libro de matemáticas básicas.',
        'MATEMÁTICA BÁSICA PARA LA EDUCACIÓN SUPERIOR',
        'Material general de matemáticas básicas.',
        'https://drive.google.com/file/d/1MqaVE6Lt2gkXRH59xh3d2KA7hE94OyQf/view?usp=sharing',
        NULL, '2026-04-11 05:25:54', 1, 1, 5);

-- Recurso 16: Historia de México II → subtema 6 (Política Contemporánea)
INSERT INTO recurso (contenido, titulo, descripcion, url_archivo, external_id, fecha_publicacion, id_tipo, id_estado, id_subtema)
VALUES ('Libro de Historia de México.',
        'Historia de Mexico II',
        'Segundo curso general de Historia de México.',
        'https://drive.google.com/file/d/1cFneEGa2aiJ0F7ZRkmPW-wvXWAw_4kh5/view?usp=sharing',
        NULL, '2026-04-11 05:25:54', 1, 1, 6);

-- Recurso 17: Historia de las matemáticas 10000 años → subtema 10
INSERT INTO recurso (contenido, titulo, descripcion, url_archivo, external_id, fecha_publicacion, id_tipo, id_estado, id_subtema)
VALUES ('Libro histórico sobre matemáticas.',
        'historia-de-las-matematicas en los ultimos 10000 años',
        'Obra sobre la evolución histórica de las matemáticas.',
        'https://drive.google.com/file/d/1b6kHolkRFKdUt9ir708SRZGR6-YxlNlB/view?usp=sharing',
        NULL, '2026-04-11 05:25:54', 1, 1, 10);

-- ============================================================
-- 5. RELACIÓN TEMA ↔ SUBTEMA
-- ============================================================
-- Tema 1 (Álgebra) → subtemas 1 (Álgebra Lineal) y 5 (Aritmética)
insert into tema_subtema (id_tema, id_subtema) values (1, 1);
insert into tema_subtema (id_tema, id_subtema) values (1, 5);

-- Tema 2 (Biología) → subtemas 3 (Biología Celular) y 8 (Genética)
insert into tema_subtema (id_tema, id_subtema) values (2, 3);
insert into tema_subtema (id_tema, id_subtema) values (2, 8);

-- Tema 3 (Cálculo) → subtema 2 (Derivadas)
insert into tema_subtema (id_tema, id_subtema) values (3, 2);

-- Tema 4 (Física) → subtema 4 (Cinemática)
insert into tema_subtema (id_tema, id_subtema) values (4, 4);

-- Tema 5 (Química) → subtema 9 (Química Analítica)
insert into tema_subtema (id_tema, id_subtema) values (5, 9);

-- Tema 6 (Historia y Política) → subtema 6 (Política Contemporánea)
insert into tema_subtema (id_tema, id_subtema) values (6, 6);

-- Tema 7 (Humanidades) → subtemas 7 (Literatura y Ética) y 10 (Historia Matemáticas)
insert into tema_subtema (id_tema, id_subtema) values (7, 7);
insert into tema_subtema (id_tema, id_subtema) values (7, 10);

-- ============================================================
-- 6. ETIQUETAS POR RECURSO (coherentes con el contenido real)
-- ============================================================

-- Recurso 1: Aritmética → álgebra, matemáticas
insert into recurso_etiqueta (id_recurso, id_etiqueta) values (1, 1);   -- álgebra
insert into recurso_etiqueta (id_recurso, id_etiqueta) values (1, 12);  -- matemáticas

-- Recurso 2: Cálculo Diferencial → derivadas, integrales
insert into recurso_etiqueta (id_recurso, id_etiqueta) values (2, 4);   -- derivadas
insert into recurso_etiqueta (id_recurso, id_etiqueta) values (2, 7);   -- integrales

-- Recurso 3: Antología Historia México → historia, política
insert into recurso_etiqueta (id_recurso, id_etiqueta) values (3, 10);  -- historia
insert into recurso_etiqueta (id_recurso, id_etiqueta) values (3, 13);  -- política

-- Recurso 4: Biología Humana → biología celular
insert into recurso_etiqueta (id_recurso, id_etiqueta) values (4, 2);   -- biología celular

-- Recurso 5: Compe Álgebra Trilce → álgebra, matemáticas
insert into recurso_etiqueta (id_recurso, id_etiqueta) values (5, 1);   -- álgebra
insert into recurso_etiqueta (id_recurso, id_etiqueta) values (5, 12);  -- matemáticas

-- Recurso 6: Compe Literatura Trilce → literatura
insert into recurso_etiqueta (id_recurso, id_etiqueta) values (6, 11);  -- literatura

-- Recurso 7: Conceptos básicos de genética → genética, biología celular
insert into recurso_etiqueta (id_recurso, id_etiqueta) values (7, 6);   -- genética
insert into recurso_etiqueta (id_recurso, id_etiqueta) values (7, 2);   -- biología celular

-- Recurso 8: Revolución Mexicana → historia, política
insert into recurso_etiqueta (id_recurso, id_etiqueta) values (8, 10);  -- historia
insert into recurso_etiqueta (id_recurso, id_etiqueta) values (8, 13);  -- política

-- Recurso 9: Historia de México I → historia, política
insert into recurso_etiqueta (id_recurso, id_etiqueta) values (9, 10);  -- historia
insert into recurso_etiqueta (id_recurso, id_etiqueta) values (9, 13);  -- política

-- Recurso 10: Estequiometría y Equilibrio → estequiometría, reacciones químicas
insert into recurso_etiqueta (id_recurso, id_etiqueta) values (10, 5);  -- estequiometría
insert into recurso_etiqueta (id_recurso, id_etiqueta) values (10, 9);  -- reacciones químicas

-- Recurso 11: Genética General → genética, biología celular
insert into recurso_etiqueta (id_recurso, id_etiqueta) values (11, 6);  -- genética
insert into recurso_etiqueta (id_recurso, id_etiqueta) values (11, 2);  -- biología celular

-- Recurso 12: Razones y Proporciones → álgebra, matemáticas
insert into recurso_etiqueta (id_recurso, id_etiqueta) values (12, 1);  -- álgebra
insert into recurso_etiqueta (id_recurso, id_etiqueta) values (12, 12); -- matemáticas

-- Recurso 13: Historia y Filosofía de las Matemáticas → matemáticas, historia
insert into recurso_etiqueta (id_recurso, id_etiqueta) values (13, 12); -- matemáticas
insert into recurso_etiqueta (id_recurso, id_etiqueta) values (13, 10); -- historia

-- Recurso 14: Literatura Pamer → literatura
insert into recurso_etiqueta (id_recurso, id_etiqueta) values (14, 11); -- literatura

-- Recurso 15: Matemática Básica para Educación Superior → matemáticas, álgebra
insert into recurso_etiqueta (id_recurso, id_etiqueta) values (15, 12); -- matemáticas
insert into recurso_etiqueta (id_recurso, id_etiqueta) values (15, 1);  -- álgebra

-- Recurso 16: Historia de México II → historia, política
insert into recurso_etiqueta (id_recurso, id_etiqueta) values (16, 10); -- historia
insert into recurso_etiqueta (id_recurso, id_etiqueta) values (16, 13); -- política

-- Recurso 17: Historia de las Matemáticas 10000 años → matemáticas, historia
insert into recurso_etiqueta (id_recurso, id_etiqueta) values (17, 12); -- matemáticas
insert into recurso_etiqueta (id_recurso, id_etiqueta) values (17, 10); -- historia

-- ============================================================
-- 7. EXÁMENES (uno por subtema relevante + examen Drácula)
-- ============================================================
-- Examen 1: Álgebra Lineal (subtema 1)
insert into examen (titulo, cantidad_preguntas, descripcion, id_subtema) values
  ('Evaluación de Álgebra Lineal', 5, 'Examen sobre vectores, matrices y sistemas de ecuaciones.', 1);

-- Examen 2: Derivadas Básicas (subtema 2)
insert into examen (titulo, cantidad_preguntas, descripcion, id_subtema) values
  ('Evaluación de Cálculo Diferencial', 5, 'Examen sobre límites, derivadas y reglas de derivación.', 2);

-- Examen 3: Biología Celular (subtema 3)
insert into examen (titulo, cantidad_preguntas, descripcion, id_subtema) values
  ('Evaluación de Biología Celular', 5, 'Examen sobre estructura y función de la célula.', 3);

-- Examen 4: Cinemática (subtema 4)
insert into examen (titulo, cantidad_preguntas, descripcion, id_subtema) values
  ('Evaluación de Cinemática', 5, 'Examen sobre movimiento rectilíneo, velocidad y aceleración.', 4);

-- Examen 5: Aritmética y Álgebra (subtema 5)
insert into examen (titulo, cantidad_preguntas, descripcion, id_subtema) values
  ('Evaluación de Aritmética', 5, 'Examen sobre operaciones aritméticas, razones y proporciones.', 5);

-- Examen 6: Política Contemporánea (subtema 6)
insert into examen (titulo, cantidad_preguntas, descripcion, id_subtema) values
  ('Evaluación de Historia de México', 5, 'Examen sobre historia nacional y política contemporánea.', 6);

-- Examen 7: Literatura y Ética (subtema 7)
insert into examen (titulo, cantidad_preguntas, descripcion, id_subtema) values
  ('Evaluación de Literatura', 5, 'Examen sobre géneros literarios, autores y obras representativas.', 7);

-- Examen 8: Genética (subtema 8)
insert into examen (titulo, cantidad_preguntas, descripcion, id_subtema) values
  ('Evaluación de Genética', 5, 'Examen sobre herencia, ADN y principios de genética.', 8);

-- Examen 9: Química Analítica (subtema 9)
insert into examen (titulo, cantidad_preguntas, descripcion, id_subtema) values
  ('Evaluación de Estequiometría', 5, 'Examen sobre balanceo de ecuaciones y cálculos estequiométricos.', 9);

-- Examen 10: Historia de las Matemáticas (subtema 10)
insert into examen (titulo, cantidad_preguntas, descripcion, id_subtema) values
  ('Evaluación de Historia de las Matemáticas', 5, 'Examen sobre la evolución histórica y filosófica de las matemáticas.', 10);

-- ============================================================
-- 8. PREGUNTAS Y OPCIONES
-- ============================================================

-- -----------------------------------------------------------
-- Examen 1: Álgebra Lineal (id_examen = 1)
-- -----------------------------------------------------------
insert into pregunta (contenido, id_examen) values ('¿Qué es un vector?', 1);                            -- p1
insert into pregunta (contenido, id_examen) values ('¿Qué es una matriz?', 1);                           -- p2
insert into pregunta (contenido, id_examen) values ('¿Qué es el determinante de una matriz?', 1);        -- p3
insert into pregunta (contenido, id_examen) values ('¿Qué es una matriz identidad?', 1);                 -- p4
insert into pregunta (contenido, id_examen) values ('¿Cuándo un sistema de ecuaciones tiene solución única?', 1); -- p5

insert into opcion (respuesta, es_correcta, id_pregunta) values ('Magnitud con dirección y sentido', 1, 1);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('Solo un número sin dirección', 0, 1);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('Un conjunto de ecuaciones', 0, 1);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('Una función matemática', 0, 1);

insert into opcion (respuesta, es_correcta, id_pregunta) values ('Arreglo rectangular de números organizado en filas y columnas', 1, 2);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('Una ecuación diferencial', 0, 2);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('Un vector de tres dimensiones', 0, 2);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('Un número complejo', 0, 2);

insert into opcion (respuesta, es_correcta, id_pregunta) values ('Valor escalar que indica si la matriz es invertible', 1, 3);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('La suma de todos los elementos de la matriz', 0, 3);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('El número de filas de la matriz', 0, 3);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('El vector unitario de la matriz', 0, 3);

insert into opcion (respuesta, es_correcta, id_pregunta) values ('Matriz cuadrada con unos en la diagonal y ceros fuera', 1, 4);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('Matriz con todos sus elementos iguales a cero', 0, 4);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('Matriz con filas y columnas invertidas', 0, 4);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('Matriz que no se puede multiplicar', 0, 4);

insert into opcion (respuesta, es_correcta, id_pregunta) values ('Cuando el determinante del sistema es distinto de cero', 1, 5);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('Cuando todas las ecuaciones son iguales', 0, 5);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('Cuando el sistema tiene más variables que ecuaciones', 0, 5);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('Cuando las variables son todas positivas', 0, 5);

-- -----------------------------------------------------------
-- Examen 2: Cálculo Diferencial (id_examen = 2)
-- -----------------------------------------------------------
insert into pregunta (contenido, id_examen) values ('¿Qué representa la derivada de una función?', 2);       -- p6
insert into pregunta (contenido, id_examen) values ('¿Cuál es la derivada de una constante?', 2);            -- p7
insert into pregunta (contenido, id_examen) values ('¿Cuál es la derivada de x²?', 2);                      -- p8
insert into pregunta (contenido, id_examen) values ('¿Qué es un límite en cálculo?', 2);                    -- p9
insert into pregunta (contenido, id_examen) values ('¿Cuál es la regla de la cadena?', 2);                  -- p10

insert into opcion (respuesta, es_correcta, id_pregunta) values ('La razón de cambio instantánea de la función', 1, 6);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('El área bajo la curva', 0, 6);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('El valor máximo de la función', 0, 6);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('La integral de la función', 0, 6);

insert into opcion (respuesta, es_correcta, id_pregunta) values ('Cero', 1, 7);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('Uno', 0, 7);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('La misma constante', 0, 7);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('Infinito', 0, 7);

insert into opcion (respuesta, es_correcta, id_pregunta) values ('2x', 1, 8);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('x', 0, 8);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('x²', 0, 8);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('2', 0, 8);

insert into opcion (respuesta, es_correcta, id_pregunta) values ('El valor al que se aproxima una función cuando x tiende a un punto', 1, 9);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('El valor exacto de la función en un punto', 0, 9);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('El área bajo la curva entre dos puntos', 0, 9);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('La pendiente de la recta tangente', 0, 9);

insert into opcion (respuesta, es_correcta, id_pregunta) values ('d/dx[f(g(x))] = f\'(g(x))·g\'(x)', 1, 10);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('d/dx[f(x)·g(x)] = f(x)+g(x)', 0, 10);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('d/dx[f(x)+g(x)] = f(x)·g(x)', 0, 10);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('d/dx[f(x)] = f(x)/x', 0, 10);

-- -----------------------------------------------------------
-- Examen 3: Biología Celular (id_examen = 3)
-- -----------------------------------------------------------
insert into pregunta (contenido, id_examen) values ('¿Cuál es la función del núcleo celular?', 3);           -- p11
insert into pregunta (contenido, id_examen) values ('¿Qué organelo produce energía en la célula?', 3);      -- p12
insert into pregunta (contenido, id_examen) values ('¿Qué diferencia a una célula procariota de una eucariota?', 3); -- p13
insert into pregunta (contenido, id_examen) values ('¿Cuál es la función de la membrana celular?', 3);      -- p14
insert into pregunta (contenido, id_examen) values ('¿Qué es la fotosíntesis?', 3);                         -- p15

insert into opcion (respuesta, es_correcta, id_pregunta) values ('Contener y proteger el ADN de la célula', 1, 11);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('Producir energía en forma de ATP', 0, 11);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('Sintetizar proteínas', 0, 11);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('Transportar sustancias dentro de la célula', 0, 11);

insert into opcion (respuesta, es_correcta, id_pregunta) values ('La mitocondria', 1, 12);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('El ribosoma', 0, 12);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('El retículo endoplásmico', 0, 12);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('El aparato de Golgi', 0, 12);

insert into opcion (respuesta, es_correcta, id_pregunta) values ('La procariota carece de núcleo definido', 1, 13);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('La eucariota no tiene mitocondrias', 0, 13);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('La procariota es más grande que la eucariota', 0, 13);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('La eucariota no tiene membrana celular', 0, 13);

insert into opcion (respuesta, es_correcta, id_pregunta) values ('Regular el paso de sustancias dentro y fuera de la célula', 1, 14);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('Producir proteínas para la célula', 0, 14);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('Almacenar el material genético', 0, 14);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('Generar energía en forma de ATP', 0, 14);

insert into opcion (respuesta, es_correcta, id_pregunta) values ('Proceso por el que las plantas convierten luz solar en energía química', 1, 15);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('Proceso de división celular', 0, 15);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('Síntesis de proteínas a partir del ARN', 0, 15);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('Transporte de oxígeno en la sangre', 0, 15);

-- -----------------------------------------------------------
-- Examen 4: Cinemática (id_examen = 4)
-- -----------------------------------------------------------
insert into pregunta (contenido, id_examen) values ('¿Qué estudia la cinemática?', 4);                         -- p16
insert into pregunta (contenido, id_examen) values ('¿Cuál es la unidad de velocidad en el SI?', 4);           -- p17
insert into pregunta (contenido, id_examen) values ('¿Qué es la aceleración?', 4);                             -- p18
insert into pregunta (contenido, id_examen) values ('En un movimiento uniformemente acelerado, ¿qué permanece constante?', 4); -- p19
insert into pregunta (contenido, id_examen) values ('¿Cuál es la fórmula del desplazamiento en MRU?', 4);     -- p20

insert into opcion (respuesta, es_correcta, id_pregunta) values ('El movimiento de los cuerpos sin considerar las causas', 1, 16);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('Las fuerzas que producen el movimiento', 0, 16);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('La energía de los cuerpos en reposo', 0, 16);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('La masa de los cuerpos en movimiento', 0, 16);

insert into opcion (respuesta, es_correcta, id_pregunta) values ('m/s', 1, 17);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('m/s²', 0, 17);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('kg·m/s', 0, 17);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('N', 0, 17);

insert into opcion (respuesta, es_correcta, id_pregunta) values ('La variación de la velocidad en el tiempo', 1, 18);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('La distancia recorrida por unidad de tiempo', 0, 18);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('La fuerza aplicada sobre un cuerpo', 0, 18);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('El cambio de posición de un cuerpo', 0, 18);

insert into opcion (respuesta, es_correcta, id_pregunta) values ('La aceleración', 1, 19);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('La velocidad', 0, 19);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('El desplazamiento', 0, 19);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('La posición inicial', 0, 19);

insert into opcion (respuesta, es_correcta, id_pregunta) values ('d = v · t', 1, 20);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('d = ½ · a · t²', 0, 20);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('d = v² / 2a', 0, 20);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('d = a · t', 0, 20);

-- -----------------------------------------------------------
-- Examen 5: Aritmética (id_examen = 5)
-- -----------------------------------------------------------
insert into pregunta (contenido, id_examen) values ('¿Qué es una razón matemática?', 5);                   -- p21
insert into pregunta (contenido, id_examen) values ('¿Cuánto es el 25% de 200?', 5);                       -- p22
insert into pregunta (contenido, id_examen) values ('Si a/b = c/d, ¿cómo se llama esta igualdad?', 5);    -- p23
insert into pregunta (contenido, id_examen) values ('¿Cuál es el MCM de 4 y 6?', 5);                      -- p24
insert into pregunta (contenido, id_examen) values ('¿Qué es un número primo?', 5);                        -- p25

insert into opcion (respuesta, es_correcta, id_pregunta) values ('La comparación entre dos cantidades por cociente', 1, 21);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('La suma de dos números', 0, 21);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('La diferencia entre dos cantidades', 0, 21);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('El producto de dos valores', 0, 21);

insert into opcion (respuesta, es_correcta, id_pregunta) values ('50', 1, 22);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('25', 0, 22);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('75', 0, 22);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('100', 0, 22);

insert into opcion (respuesta, es_correcta, id_pregunta) values ('Proporción', 1, 23);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('Razón', 0, 23);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('Fracción', 0, 23);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('Identidad', 0, 23);

insert into opcion (respuesta, es_correcta, id_pregunta) values ('12', 1, 24);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('8', 0, 24);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('24', 0, 24);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('2', 0, 24);

insert into opcion (respuesta, es_correcta, id_pregunta) values ('Un número divisible solo entre 1 y él mismo', 1, 25);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('Un número par mayor que dos', 0, 25);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('Un número divisible entre 2', 0, 25);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('Un número mayor que 10', 0, 25);

-- -----------------------------------------------------------
-- Examen 6: Historia de México (id_examen = 6)
-- -----------------------------------------------------------
insert into pregunta (contenido, id_examen) values ('¿En qué año inició la Revolución Mexicana?', 6);                    -- p26
insert into pregunta (contenido, id_examen) values ('¿Quién promulgó la Constitución de 1917?', 6);                      -- p27
insert into pregunta (contenido, id_examen) values ('¿Cuál fue el lema de Francisco I. Madero?', 6);                    -- p28
insert into pregunta (contenido, id_examen) values ('¿En qué siglo consumó la Independencia de México?', 6);            -- p29
insert into pregunta (contenido, id_examen) values ('¿Cómo se llama el documento que proclamó la Independencia?', 6);  -- p30

insert into opcion (respuesta, es_correcta, id_pregunta) values ('1910', 1, 26);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('1900', 0, 26);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('1920', 0, 26);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('1876', 0, 26);

insert into opcion (respuesta, es_correcta, id_pregunta) values ('Venustiano Carranza', 1, 27);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('Francisco Villa', 0, 27);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('Emiliano Zapata', 0, 27);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('Porfirio Díaz', 0, 27);

insert into opcion (respuesta, es_correcta, id_pregunta) values ('Sufragio efectivo, no reelección', 1, 28);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('Tierra y libertad', 0, 28);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('La tierra es de quien la trabaja', 0, 28);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('Viva México independiente', 0, 28);

insert into opcion (respuesta, es_correcta, id_pregunta) values ('Siglo XIX (1821)', 1, 29);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('Siglo XVIII (1776)', 0, 29);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('Siglo XX (1910)', 0, 29);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('Siglo XVII (1650)', 0, 29);

insert into opcion (respuesta, es_correcta, id_pregunta) values ('Acta de Independencia de la Nación Mexicana', 1, 30);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('Constitución de Apatzingán', 0, 30);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('Plan de Iguala', 0, 30);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('Tratado de Córdoba', 0, 30);

-- -----------------------------------------------------------
-- Examen 7: Literatura (id_examen = 7)
-- -----------------------------------------------------------
insert into pregunta (contenido, id_examen) values ('¿Qué es un género literario?', 7);                     -- p31
insert into pregunta (contenido, id_examen) values ('¿Cuál es la característica principal del género épico?', 7); -- p32
insert into pregunta (contenido, id_examen) values ('¿Quién escribió el Quijote?', 7);                     -- p33
insert into pregunta (contenido, id_examen) values ('¿Qué es un soneto?', 7);                              -- p34
insert into pregunta (contenido, id_examen) values ('¿Qué distingue a la novela del cuento?', 7);          -- p35

insert into opcion (respuesta, es_correcta, id_pregunta) values ('Categoría que agrupa obras con rasgos comunes de forma y contenido', 1, 31);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('El idioma en que está escrita una obra', 0, 31);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('El número de páginas de un libro', 0, 31);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('El país de origen del autor', 0, 31);

insert into opcion (respuesta, es_correcta, id_pregunta) values ('Narración de hazañas heroicas de manera objetiva', 1, 32);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('Expresión de sentimientos subjetivos del autor', 0, 32);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('Diálogo entre dos personajes en escena', 0, 32);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('Historia breve con moraleja al final', 0, 32);

insert into opcion (respuesta, es_correcta, id_pregunta) values ('Miguel de Cervantes Saavedra', 1, 33);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('Francisco de Quevedo', 0, 33);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('Lope de Vega', 0, 33);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('Góngora', 0, 33);

insert into opcion (respuesta, es_correcta, id_pregunta) values ('Poema de 14 versos distribuidos en dos cuartetos y dos tercetos', 1, 34);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('Poema de verso libre sin rima', 0, 34);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('Historia corta en prosa', 0, 34);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('Obra de teatro en tres actos', 0, 34);

insert into opcion (respuesta, es_correcta, id_pregunta) values ('La novela es más extensa y tiene mayor desarrollo de personajes', 1, 35);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('El cuento siempre tiene más personajes que la novela', 0, 35);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('La novela siempre es en verso y el cuento en prosa', 0, 35);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('No existe ninguna diferencia entre ambos géneros', 0, 35);

-- -----------------------------------------------------------
-- Examen 8: Genética (id_examen = 8)
-- -----------------------------------------------------------
insert into pregunta (contenido, id_examen) values ('¿Qué es el ADN?', 8);                                        -- p36
insert into pregunta (contenido, id_examen) values ('¿Quiénes describieron la estructura del ADN en 1953?', 8);   -- p37
insert into pregunta (contenido, id_examen) values ('¿Qué son los cromosomas?', 8);                               -- p38
insert into pregunta (contenido, id_examen) values ('¿Qué establece la primera ley de Mendel?', 8);               -- p39
insert into pregunta (contenido, id_examen) values ('¿Cuántos pares de cromosomas tiene el ser humano?', 8);      -- p40

insert into opcion (respuesta, es_correcta, id_pregunta) values ('Molécula que almacena la información genética de los seres vivos', 1, 36);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('Proteína que produce energía en la célula', 0, 36);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('Organelo encargado de la respiración celular', 0, 36);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('Membrana que recubre el núcleo celular', 0, 36);

insert into opcion (respuesta, es_correcta, id_pregunta) values ('Watson y Crick', 1, 37);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('Mendel y Darwin', 0, 37);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('Pasteur y Koch', 0, 37);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('Hooke y Van Leeuwenhoek', 0, 37);

insert into opcion (respuesta, es_correcta, id_pregunta) values ('Estructuras que contienen el ADN dentro del núcleo celular', 1, 38);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('Moléculas de proteína del citoplasma', 0, 38);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('Organelos que producen energía', 0, 38);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('Partes de la membrana celular', 0, 38);

insert into opcion (respuesta, es_correcta, id_pregunta) values ('Principio de la uniformidad: los híbridos de F1 son uniformes', 1, 39);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('Los rasgos se mezclan en proporciones iguales', 0, 39);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('Los genes siempre se heredan juntos', 0, 39);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('Las mutaciones son siempre letales', 0, 39);

insert into opcion (respuesta, es_correcta, id_pregunta) values ('23 pares (46 cromosomas en total)', 1, 40);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('24 pares (48 cromosomas en total)', 0, 40);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('22 pares (44 cromosomas en total)', 0, 40);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('46 pares (92 cromosomas en total)', 0, 40);

-- -----------------------------------------------------------
-- Examen 9: Estequiometría (id_examen = 9)
-- -----------------------------------------------------------
insert into pregunta (contenido, id_examen) values ('¿Qué es una reacción química?', 9);                                     -- p41
insert into pregunta (contenido, id_examen) values ('¿Qué indica el coeficiente estequiométrico?', 9);                      -- p42
insert into pregunta (contenido, id_examen) values ('¿Cuántos gramos hay en un mol de agua (H₂O)?', 9);                    -- p43
insert into pregunta (contenido, id_examen) values ('¿Qué es el número de Avogadro?', 9);                                   -- p44
insert into pregunta (contenido, id_examen) values ('¿Cuál es la ley de conservación de la masa?', 9);                     -- p45

insert into opcion (respuesta, es_correcta, id_pregunta) values ('Proceso en que sustancias se transforman en nuevas sustancias', 1, 41);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('Mezcla de dos líquidos sin cambio de composición', 0, 41);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('Cambio de estado físico de la materia', 0, 41);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('Separación de componentes por filtración', 0, 41);

insert into opcion (respuesta, es_correcta, id_pregunta) values ('La cantidad de moles de cada reactivo o producto', 1, 42);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('La temperatura de reacción', 0, 42);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('El número de átomos de un elemento en la molécula', 0, 42);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('La velocidad de la reacción', 0, 42);

insert into opcion (respuesta, es_correcta, id_pregunta) values ('18 g', 1, 43);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('16 g', 0, 43);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('20 g', 0, 43);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('2 g', 0, 43);

insert into opcion (respuesta, es_correcta, id_pregunta) values ('6.022 × 10²³ entidades por mol', 1, 44);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('9.8 m/s² (aceleración gravitacional)', 0, 44);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('3 × 10⁸ m/s (velocidad de la luz)', 0, 44);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('1.6 × 10⁻¹⁹ C (carga del electrón)', 0, 44);

insert into opcion (respuesta, es_correcta, id_pregunta) values ('La masa total de reactivos es igual a la de los productos', 1, 45);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('La energía se conserva pero la masa puede cambiar', 0, 45);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('Los elementos no cambian en una reacción', 0, 45);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('La temperatura permanece constante en toda reacción', 0, 45);

-- -----------------------------------------------------------
-- Examen 10: Historia de las Matemáticas (id_examen = 10)
-- -----------------------------------------------------------
insert into pregunta (contenido, id_examen) values ('¿Qué civilización desarrolló el sistema de numeración posicional?', 10);  -- p46
insert into pregunta (contenido, id_examen) values ('¿A quién se atribuye el Teorema de Pitágoras?', 10);                      -- p47
insert into pregunta (contenido, id_examen) values ('¿Quién es considerado el padre del álgebra?', 10);                        -- p48
insert into pregunta (contenido, id_examen) values ('¿Cuándo se publicaron los Elementos de Euclides?', 10);                   -- p49
insert into pregunta (contenido, id_examen) values ('¿Qué matemático introdujo el concepto de coordenadas cartesianas?', 10); -- p50

insert into opcion (respuesta, es_correcta, id_pregunta) values ('Mesopotamia (babilonios)', 1, 46);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('Grecia antigua', 0, 46);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('Egipto antiguo', 0, 46);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('China imperial', 0, 46);

insert into opcion (respuesta, es_correcta, id_pregunta) values ('Pitágoras de Samos', 1, 47);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('Arquímedes de Siracusa', 0, 47);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('Euclides de Alejandría', 0, 47);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('Tales de Mileto', 0, 47);

insert into opcion (respuesta, es_correcta, id_pregunta) values ('Al-Juarismi', 1, 48);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('Blaise Pascal', 0, 48);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('Isaac Newton', 0, 48);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('Gottfried Leibniz', 0, 48);

insert into opcion (respuesta, es_correcta, id_pregunta) values ('Alrededor del 300 a.C.', 1, 49);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('Siglo XV d.C.', 0, 49);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('Año 0', 0, 49);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('Siglo X d.C.', 0, 49);

insert into opcion (respuesta, es_correcta, id_pregunta) values ('René Descartes', 1, 50);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('Carl Friedrich Gauss', 0, 50);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('Leonhard Euler', 0, 50);
insert into opcion (respuesta, es_correcta, id_pregunta) values ('Pierre de Fermat', 0, 50);

-- ============================================================
-- 9. PUBLICACIONES
-- ============================================================
insert into publicacion (titulo, descripcion, texto, fecha_creacion, id_usuario, id_estado) values
  ('Consejos para mejorar en cálculo diferencial',
   'Reflexión académica',
   'Una estrategia que me ha funcionado es practicar derivadas todos los días y entender su interpretación gráfica. No solo memoricen fórmulas, intenten comprender qué representa la pendiente en cada punto.',
   '2026-02-12 00:02:25', 1, 3);   -- publicación 1 (usuario admin, estado publicado)

insert into publicacion (titulo, descripcion, texto, fecha_creacion, id_usuario, id_estado) values
  ('Cómo entender mejor la física',
   'Aporte educativo',
   'Para comprender la cinemática recomiendo analizar primero el concepto de movimiento antes de aplicar fórmulas. Entender la relación entre desplazamiento, velocidad y aceleración facilita mucho la resolución de problemas.',
   '2026-02-12 00:02:25', 2, 3);   -- publicación 2

insert into publicacion (titulo, descripcion, texto, fecha_creacion, id_usuario, id_estado) values
  ('Recomendaciones para química general',
   'Experiencia de estudio',
   'Al estudiar estequiometría es fundamental practicar el balanceo de ecuaciones antes de realizar cálculos. Dominar ese paso simplifica todos los ejercicios posteriores.',
   '2026-02-12 00:02:25', 3, 3);   -- publicación 3

-- Etiquetas de publicaciones (coherentes con su contenido)
insert into publicacion_etiqueta (id_publicacion, id_etiqueta) values (1, 4);  -- derivadas
insert into publicacion_etiqueta (id_publicacion, id_etiqueta) values (1, 7);  -- integrales
insert into publicacion_etiqueta (id_publicacion, id_etiqueta) values (1, 1);  -- álgebra

insert into publicacion_etiqueta (id_publicacion, id_etiqueta) values (2, 3);  -- cinemática
insert into publicacion_etiqueta (id_publicacion, id_etiqueta) values (2, 8);  -- leyes de newton

insert into publicacion_etiqueta (id_publicacion, id_etiqueta) values (3, 5);  -- estequiometría
insert into publicacion_etiqueta (id_publicacion, id_etiqueta) values (3, 9);  -- reacciones químicas

-- ============================================================
-- 10. INTENTOS DE EXAMEN
-- Usuario 1 → examen 1 (Álgebra Lineal)
-- Usuario 2 → examen 2 (Cálculo Diferencial)
-- Usuario 3 → examen 3 (Biología Celular)
-- ============================================================
insert into intento (calificacion, fecha, id_usuario, id_examen) values (85, '2026-02-12 00:02:25', 1, 1);  -- intento 1
insert into intento (calificacion, fecha, id_usuario, id_examen) values (90, '2026-02-12 00:02:25', 2, 2);  -- intento 2
insert into intento (calificacion, fecha, id_usuario, id_examen) values (78, '2026-02-12 00:02:25', 3, 3);  -- intento 3

-- Respuestas intento 1 (examen 1 — preguntas 1, 2, 3, 4, 5)
INSERT INTO respuesta_intento (id_intento, id_pregunta, id_opcion, es_correcta) VALUES
  (1, 1, 1,  true),   -- ¿Qué es un vector? → correcta
  (1, 2, 5,  true),   -- ¿Qué es una matriz? → correcta
  (1, 3, 9,  true),   -- ¿Qué es el determinante? → correcta
  (1, 4, 13, true),   -- ¿Qué es una matriz identidad? → correcta
  (1, 5, 18, false);  -- ¿Cuándo tiene solución única? → incorrecta (opción 18 = "Cuando las variables son positivas")

-- Respuestas intento 2 (examen 2 — preguntas 6, 7, 8, 9, 10)
INSERT INTO respuesta_intento (id_intento, id_pregunta, id_opcion, es_correcta) VALUES
  (2, 6,  21, true),  -- ¿Qué representa la derivada? → correcta
  (2, 7,  25, true),  -- ¿Derivada de constante? → correcta (opción: Cero)
  (2, 8,  29, true),  -- ¿Derivada de x²? → correcta (2x)
  (2, 9,  33, true),  -- ¿Qué es un límite? → correcta
  (2, 10, 38, false); -- Regla de la cadena → incorrecta (opción 38 = "d/dx[f+g] = f·g")

-- Respuestas intento 3 (examen 3 — preguntas 11, 12, 13, 14, 15)
INSERT INTO respuesta_intento (id_intento, id_pregunta, id_opcion, es_correcta) VALUES
  (3, 11, 41, true),  -- Función del núcleo → correcta
  (3, 12, 46, false), -- ¿Qué organelo produce energía? → incorrecta (opción 46 = "El ribosoma")
  (3, 13, 49, true),  -- Procariota vs eucariota → correcta
  (3, 14, 53, true),  -- Función membrana celular → correcta
  (3, 15, 57, true);  -- ¿Qué es la fotosíntesis? → correcta

-- ============================================================
-- 11. NOTAS
-- Cada nota referencia un recurso coherente con su contenido
-- ============================================================
insert into nota (titulo, contenido, fecha_creacion, fecha_actualizacion, es_compartida, id_usuario, id_recurso)
values ('Resumen de álgebra lineal',
        'Repasar matrices, determinantes y sistemas de ecuaciones para el examen final.',
        '2026-03-01 22:00:00', '2026-03-01 22:00:00', 1, 1, 5);  -- recurso 5: Compe Álgebra

insert into nota (titulo, contenido, fecha_creacion, fecha_actualizacion, es_compartida, id_usuario, id_recurso)
values ('Fórmulas de cálculo diferencial',
        'Fórmulas importantes de derivadas: regla de la cadena, derivada del producto, cociente.',
        '2026-03-01 22:05:00', '2026-03-01 22:05:00', 0, 2, 2);  -- recurso 2: Cálculo Diferencial

insert into nota (titulo, contenido, fecha_creacion, fecha_actualizacion, es_compartida, id_usuario, id_recurso)
values ('Conceptos clave de biología celular',
        'Mitocondria, núcleo, membrana celular: diferencias entre células procariotas y eucariotas.',
        '2026-03-01 22:10:00', '2026-03-01 22:10:00', 1, 3, 4);  -- recurso 4: Biología Humana

insert into nota (titulo, contenido, fecha_creacion, fecha_actualizacion, es_compartida, id_usuario, id_recurso)
values ('Estequiometría básica',
        'Balanceo de ecuaciones y cálculo de moles. Recordar ley de conservación de la masa.',
        '2026-03-01 22:15:00', '2026-03-01 22:15:00', 0, 4, 10); -- recurso 10: Estequiometría

insert into nota (titulo, contenido, fecha_creacion, fecha_actualizacion, es_compartida, id_usuario, id_recurso)
values ('Notas de Historia de México',
        'Revolución Mexicana 1910-1921: causas, personajes y consecuencias principales.',
        '2026-03-01 22:20:00', '2026-03-01 22:20:00', 1, 5, 9);  -- recurso 9: Historia México I

-- ============================================================
-- 12. RECURSOS GUARDADOS POR USUARIO
-- ============================================================
insert into usuario_recurso (id_usuario, id_recurso) values (1, 1);   -- Jafet → Aritmética
insert into usuario_recurso (id_usuario, id_recurso) values (1, 2);   -- Jafet → Cálculo Diferencial
insert into usuario_recurso (id_usuario, id_recurso) values (1, 5);   -- Jafet → Álgebra Trilce
insert into usuario_recurso (id_usuario, id_recurso) values (2, 2);   -- Carlos → Cálculo Diferencial
insert into usuario_recurso (id_usuario, id_recurso) values (2, 13);  -- Carlos → Historia Matemáticas
insert into usuario_recurso (id_usuario, id_recurso) values (3, 4);   -- Maria → Biología Humana
insert into usuario_recurso (id_usuario, id_recurso) values (3, 7);   -- Maria → Genética Básica
insert into usuario_recurso (id_usuario, id_recurso) values (4, 10);  -- Luis → Estequiometría
insert into usuario_recurso (id_usuario, id_recurso) values (5, 9);   -- Jose → Historia México I
insert into usuario_recurso (id_usuario, id_recurso) values (5, 16);  -- Jose → Historia México II
insert into usuario_recurso (id_usuario, id_recurso) values (8, 1);   -- Laura (premium) → Aritmética
insert into usuario_recurso (id_usuario, id_recurso) values (8, 2);   -- Laura (premium) → Cálculo
insert into usuario_recurso (id_usuario, id_recurso) values (8, 4);   -- Laura (premium) → Biología
insert into usuario_recurso (id_usuario, id_recurso) values (8, 10);  -- Laura (premium) → Química

-- ============================================================
-- 13. VISTAS DE CONTENIDO
-- ============================================================
-- Vistas de recursos
insert into vista_contenido (id_usuario, id_recurso, fecha_vista) values (1, 1,  '2026-03-03 10:00:00');
insert into vista_contenido (id_usuario, id_recurso, fecha_vista) values (2, 1,  '2026-03-03 10:05:00');
insert into vista_contenido (id_usuario, id_recurso, fecha_vista) values (3, 4,  '2026-03-03 10:10:00');
insert into vista_contenido (id_usuario, id_recurso, fecha_vista) values (4, 10, '2026-03-03 10:12:00');
insert into vista_contenido (id_usuario, id_recurso, fecha_vista) values (5, 9,  '2026-03-03 10:15:00');
insert into vista_contenido (id_usuario, id_recurso, fecha_vista) values (6, 5,  '2026-03-03 10:18:00');
insert into vista_contenido (id_usuario, id_recurso, fecha_vista) values (7, 2,  '2026-03-03 10:20:00');
insert into vista_contenido (id_usuario, id_recurso, fecha_vista) values (8, 2,  '2026-03-03 10:22:00');
insert into vista_contenido (id_usuario, id_recurso, fecha_vista) values (9, 11, '2026-03-03 10:25:00');
insert into vista_contenido (id_usuario, id_recurso, fecha_vista) values (10, 7, '2026-03-03 10:28:00');

-- Vistas de publicaciones
insert into vista_contenido (id_usuario, id_publicacion, fecha_vista) values (1, 1, '2026-03-03 11:00:00');
insert into vista_contenido (id_usuario, id_publicacion, fecha_vista) values (2, 1, '2026-03-03 11:02:00');
insert into vista_contenido (id_usuario, id_publicacion, fecha_vista) values (3, 2, '2026-03-03 11:05:00');
insert into vista_contenido (id_usuario, id_publicacion, fecha_vista) values (4, 2, '2026-03-03 11:06:00');
insert into vista_contenido (id_usuario, id_publicacion, fecha_vista) values (5, 3, '2026-03-03 11:10:00');
insert into vista_contenido (id_usuario, id_publicacion, fecha_vista) values (6, 3, '2026-03-03 11:12:00');
insert into vista_contenido (id_usuario, id_publicacion, fecha_vista) values (7, 1, '2026-03-03 11:15:00');
insert into vista_contenido (id_usuario, id_publicacion, fecha_vista) values (8, 2, '2026-03-03 11:18:00');

-- ============================================================
-- 14. PROGRESO DE CONTENIDO
-- ============================================================
-- Progreso en recursos
insert into progreso_contenido (id_usuario, id_recurso, porcentaje_leido, ultima_posicion, completado)
values (1,  1,  100, 5200, true);   -- Jafet completó Aritmética
insert into progreso_contenido (id_usuario, id_recurso, porcentaje_leido, ultima_posicion, completado)
values (2,  2,  65,  3400, false);  -- Carlos 65% en Cálculo
insert into progreso_contenido (id_usuario, id_recurso, porcentaje_leido, ultima_posicion, completado)
values (3,  4,  40,  2100, false);  -- Maria 40% en Biología Humana
insert into progreso_contenido (id_usuario, id_recurso, porcentaje_leido, ultima_posicion, completado)
values (4,  10, 90,  4800, false);  -- Luis 90% en Estequiometría
insert into progreso_contenido (id_usuario, id_recurso, porcentaje_leido, ultima_posicion, completado)
values (5,  9,  100, 6000, true);   -- Jose completó Historia México I
insert into progreso_contenido (id_usuario, id_recurso, porcentaje_leido, ultima_posicion, completado)
values (8,  2,  55,  2900, false);  -- Laura 55% en Cálculo
insert into progreso_contenido (id_usuario, id_recurso, porcentaje_leido, ultima_posicion, completado)
values (9,  11, 30,  1500, false);  -- Miguel 30% en Genética General
insert into progreso_contenido (id_usuario, id_recurso, porcentaje_leido, ultima_posicion, completado)
values (10, 7,  70,  3600, false);  -- Daniela 70% en Genética Básica

-- Progreso en publicaciones
insert into progreso_contenido (id_usuario, id_publicacion, porcentaje_leido, ultima_posicion, completado)
values (1, 1, 100, 1800, true);
insert into progreso_contenido (id_usuario, id_publicacion, porcentaje_leido, ultima_posicion, completado)
values (2, 1, 50,  900,  false);
insert into progreso_contenido (id_usuario, id_publicacion, porcentaje_leido, ultima_posicion, completado)
values (3, 2, 75,  1200, false);
insert into progreso_contenido (id_usuario, id_publicacion, porcentaje_leido, ultima_posicion, completado)
values (4, 3, 30,  500,  false);
insert into progreso_contenido (id_usuario, id_publicacion, porcentaje_leido, ultima_posicion, completado)
values (5, 3, 100, 1600, true);
insert into progreso_contenido (id_usuario, id_publicacion, porcentaje_leido, ultima_posicion, completado)
values (7, 1, 80,  1440, false);
insert into progreso_contenido (id_usuario, id_publicacion, porcentaje_leido, ultima_posicion, completado)
values (8, 2, 60,  1000, false);

-- ============================================================
-- 15. DESCARGAS OFFLINE
-- Solo usuarios con beneficio de descarga (membresías 2, 3, 4)
-- → usuarios 8 (Premium Mensual), 9 (Premium Semestral), 10 (Premium Anual)
-- Usuarios gratuitos (1-7) NO tienen este beneficio
-- ============================================================
insert into offline (id_usuario, id_recurso, fecha_descarga, ultima_sincronizacion, activo)
values (8, 1,  NOW(), NOW(), true);   -- Laura → Aritmética
insert into offline (id_usuario, id_recurso, fecha_descarga, ultima_sincronizacion, activo)
values (8, 2,  NOW(), NOW(), true);   -- Laura → Cálculo Diferencial
insert into offline (id_usuario, id_recurso, fecha_descarga, ultima_sincronizacion, activo)
values (8, 4,  NOW(), NOW(), true);   -- Laura → Biología Humana
insert into offline (id_usuario, id_recurso, fecha_descarga, ultima_sincronizacion, activo)
values (8, 10, NOW(), NOW(), true);   -- Laura → Estequiometría

insert into offline (id_usuario, id_recurso, fecha_descarga, ultima_sincronizacion, activo)
values (9, 5,  NOW(), NOW(), true);   -- Miguel → Álgebra Trilce
insert into offline (id_usuario, id_recurso, fecha_descarga, ultima_sincronizacion, activo)
values (9, 11, NOW(), NOW(), true);   -- Miguel → Genética General
insert into offline (id_usuario, id_recurso, fecha_descarga, ultima_sincronizacion, activo)
values (9, 13, NOW(), NOW(), false);  -- Miguel → Historia Matemáticas (eliminado)

insert into offline (id_usuario, id_recurso, fecha_descarga, ultima_sincronizacion, activo)
values (10, 7,  NOW(), NOW(), true);  -- Daniela → Genética Básica
insert into offline (id_usuario, id_recurso, fecha_descarga, ultima_sincronizacion, activo)
values (10, 14, NOW(), NOW(), true);  -- Daniela → Literatura Pamer
insert into offline (id_usuario, id_recurso, fecha_descarga, ultima_sincronizacion, activo)
values (10, 6,  NOW(), NOW(), true);  -- Daniela → Literatura Trilce