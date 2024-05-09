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
    explicacao TEXT NOT NULL,
    usuario_professor_id TEXT NOT NULL,
    fase_jogo_id TEXT NOT NULL,
    updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (usuario_professor_id) REFERENCES usuario_professor (id)
    FOREIGN KEY (fase_jogo_id) REFERENCES fase_jogo (id)
);


CREATE TABLE questoes_verdadeiro_ou_falso(
    id TEXT NOT NULL PRIMARY KEY UNIQUE,
    enunciado TEXT NOT NULL,
    is_correta BLOB NOT NULL DEFAULT 1,
    usuario_professor_id TEXT NOT NULL,
    explicacao TEXT NOT NULL,
    fase_jogo_id TEXT NOT NULL,
    updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (usuario_professor_id) REFERENCES usuario_professor (id)
    FOREIGN KEY (fase_jogo_id) REFERENCES fase_jogo (id)
);

-- SELECIONAR CADA UMA DAS TABELAS PARA SABER SE FORAM CRIADAS
SELECT * FROM usuario_admin;
SELECT * FROM usuario_professor;
SELECT * FROM usuario_estudante;
SELECT * FROM usuarios;
SELECT * FROM score_total;
SELECT * FROM fase_jogo;
SELECT * FROM questoes_choice;

SELECT * FROM questoes_verdadeiro_ou_falso

-- INSERCAO DE DADOS INICIAIS

INSERT INTO fase_jogo (
    id,
    nro_fase,
    score_questao_correta
    ) 
    VALUES 
    (
    "e33461e9-51a6-4dea-abe1-6bcd0ef6d6eb", 
    1, 
    1)
    ,
     (
    "9bb3f773-7595-45bd-969d-15eea515701c", 
    2, 
    2)
    ;

INSERT INTO usuarios  (
    id,
    email_institucional,
    username,
    password,
    recovery_question,
    recovery_answer
    )
    VALUES
    (
        "0032e45d-d3fe-40b8-9a56-055589564264",
        "estudante.teste@estudantespiaget.com.br",
        "estudante-teste",
        "estudante123",
        "Nome do seu PET?",
        "aluno-pet"
    );

INSERT INTO usuarios (
    id,
    email_institucional,
    username,
    password,
    recovery_question,
    recovery_answer,
    role
    )
    VALUES
    (
        "9f2fee76-919d-4b82-8018-fbce5a2c7a69",
        "admin.teste@secretariapiaget.com.br",
        "admin-teste",
        "admin123",
        "Nome do seu PET?",
        "admin-pet",
        "ADMINISTRADORES"
    );

INSERT INTO usuarios (
    id,
    email_institucional,
    username,
    password,
    recovery_question,
    recovery_answer,
    role
    )
    VALUES
    (
        "f9731aa1-ef6c-4a4d-85de-8526d6cdffb1",
        "professor.teste@professorespiaget.com.br",
        "professor-teste",
        "teacher123",
        "Nome do seu PET?",
        "teacher-pet",
        "PROFESSORES"
    );

INSERT INTO usuario_estudante(
    id,
    is_active,
    usuario_id
) VALUES (
    "0a24af74-3182-4802-801a-ea8fafbef689",
    1,
    "0032e45d-d3fe-40b8-9a56-055589564264"
)   ;

INSERT INTO usuario_professor(
    id,
    is_active,
    usuario_id,
    usuario_id_admin
) VALUES (
    "751a319d-1997-4adf-b5ee-585c990726e4",
    1,
    "f9731aa1-ef6c-4a4d-85de-8526d6cdffb1",
    "8f754d1d-d077-4238-925b-a667d5f3fdd4"
)   ;


-- DELETAR TABELAS (PARA DELETAR TODAS AS TABELAS COMECAR DE BAIXO PARA CIMA )
DROP TABLE questoes_verdadeiro_ou_falso;
DROP TABLE usuarios;

DROP TABLE usuario_admin;
DROP TABLE usuario_professor;
DROP TABLE usuario_estudante;
DROP TABLE usuarios;
DROP TABLE score_total;

DROP TABLE fase_jogo;

DROP TABLE questoes_choice;

DROP TABLE questoes_verdadeiro_ou_falso;

SELECT usuario_professor.id from usuario_professor
INNER JOIN usuarios
ON usuario_professor.usuario_id = usuarios.id
WHERE usuarios.email_institucional = "professor.teste@professorespiaget.com.br"