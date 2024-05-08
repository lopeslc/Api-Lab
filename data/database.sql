-- Active: 1715123445065@@127.0.0.1@3306
CREATE TABLE usuarios(  
    id TEXT NOT NULL PRIMARY KEY UNIQUE,
    email_institucional TEXT NOT NULL UNIQUE,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    recovery_question TEXT NOT NULL,
    recovery_answer TEXT NOT NULL
)