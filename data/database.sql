-- Active: 1715123445065@@127.0.0.1@3306
CREATE TABLE usuarios(  
    id TEXT NOT NULL PRIMARY KEY UNIQUE,
    email_institucional TEXT NOT NULL UNIQUE,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    recovery_question TEXT NOT NULL,
    recovery_answer TEXT NOT NULL,
    role TEXT NOT NULL DEFAULT "ESTUDANTES"
);

CREATE TABLE usuario_admin (
    id TEXT NOT NULL PRIMARY KEY UNIQUE,
    usuario_id TEXT NOT NULL UNIQUE,
    is_active BLOB NOT NULL DEFAULT 1, 
    FOREIGN KEY (usuario_id) REFERENCES usuarios (id) 
        ON UPDATE CASCADE ON DELETE CASCADE
);


CREATE TABLE usuario_professor (
    id TEXT NOT NULL PRIMARY KEY UNIQUE,
    is_active BLOB NOT NULL DEFAULT 1, 
    usuario_id TEXT NOT NULL UNIQUE,
    usuario_id_admin TEXT NOT NULL UNIQUE,
    FOREIGN KEY (usuario_id) REFERENCES usuarios (id) 
        ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (usuario_id_admin) REFERENCES usuario_admin (id) 
);

CREATE TABLE usuario_estudante (
    id TEXT NOT NULL PRIMARY KEY UNIQUE,
    is_active BLOB NOT NULL DEFAULT 1, 
    usuario_id TEXT NOT NULL UNIQUE,
    FOREIGN KEY (usuario_id) REFERENCES usuarios (id) 
        ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE score_total (
    id TEXT NOT NULL PRIMARY KEY UNIQUE,
    total_score INTEGER NOT NULL DEFAULT 0, 
    usuario_id_estudante TEXT NOT NULL UNIQUE,
    FOREIGN KEY (usuario_id_estudante) REFERENCES usuario_estudante (id) 
        ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE fase_jogo (
    id TEXT NOT NULL PRIMARY KEY UNIQUE,
    nro_fase INTEGER NOT NULL DEFAULT 1, 
    score_questao_correta INTEGER NOT NULL DEFAULT 1
);

CREATE TABLE questoes_choice(
    id TEXT NOT NULL PRIMARY KEY UNIQUE,
    enunciado TEXT NOT NULL,
    alternativa_a TEXT NOT NULL,
    alternativa_b TEXT NOT NULL,
    alternativa_c TEXT NOT NULL,
    alternativa_d TEXT NOT NULL,
    alternativa_e TEXT NOT NULL,
    correta TEXT NOT NULL DEFAULT "A",
    usuario_professor_id TEXT NOT NULL,
    fase_jogo_id TEXT NOT NULL,
    FOREIGN KEY (usuario_professor_id) REFERENCES usuario_professor (id)
    FOREIGN KEY (fase_jogo_id) REFERENCES fase_jogo (id)
);


CREATE TABLE questoes_verdadeiro_ou_falso(
    id TEXT NOT NULL PRIMARY KEY UNIQUE,
    enunciado TEXT NOT NULL,
    is_correta BLOB NOT NULL DEFAULT 1,
    usuario_professor_id TEXT NOT NULL,
    fase_jogo_id TEXT NOT NULL,
    FOREIGN KEY (usuario_professor_id) REFERENCES usuario_professor (id)
    FOREIGN KEY (fase_jogo_id) REFERENCES fase_jogo (id)
);


SELECT * FROM usuarios;

SELECT * FROM usuario_admin;
SELECT * FROM usuario_professor;

SELECT * FROM usuario_estudante;

DROP TABLE usuarios;

DROP TABLE usuario_admin;
DROP TABLE usuario_professor;
DROP TABLE usuario_estudante;
DROP TABLE usuarios;
DROP TABLE score_total;

DROP TABLE fase_jogo;

DROP TABLE questoes_choice;

DROP TABLE questoes_verdadeiro_ou_falso;