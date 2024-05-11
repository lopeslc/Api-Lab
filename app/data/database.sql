-- Active: 1715277551910@@127.0.0.1@3306
CREATE TABLE usuarios(  
    id TEXT NOT NULL PRIMARY KEY UNIQUE,
    email_institucional TEXT NOT NULL UNIQUE,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    recovery_question TEXT NOT NULL,
    recovery_answer TEXT NOT NULL,
    role TEXT NOT NULL DEFAULT "ESTUDANTES"
);


INSERT INTO usuarios(
    id, email_institucional, username, password, recovery_question, recovery_answer, role
) VALUES (
    "cdb0660a-ed92-49c8-bb08-f77523428a67", "estudante@estudantes.piaget.com.br", "estudante-teste", "Abc123!", "Nome do seu PET?", "PET-ESTUDANTE", "ESTUDANTES"
),(
    "4ca064c7-3df0-4c27-b670-b8928c431f82", "admin@secretaria.piaget.com.br", "admin-teste", "Abc123!", "Nome do seu PET?", "PET-ADMINISTRADOR", "ADMINISTRADORES"
),(
    "c4697db7-876c-4323-9f21-2bad9d675ba1", "professor@professores.piaget.com.br", "username", "Abc123!", "Nome do seu PET?", "PET-PROFESSOR", "PROFESSORES"
);


CREATE TABLE usuario_admin (
    id TEXT NOT NULL PRIMARY KEY UNIQUE,
    usuario_id TEXT NOT NULL UNIQUE,
    is_active BLOB NOT NULL DEFAULT 1, 
    FOREIGN KEY (usuario_id) REFERENCES usuarios (id) 
        ON UPDATE CASCADE ON DELETE CASCADE
);

INSERT INTO usuario_admin(
    id, usuario_id, is_active
) VALUES (
    "d42c4228-f405-4363-8cd4-5b2157edf8d7",
    "4ca064c7-3df0-4c27-b670-b8928c431f82",
    1
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

INSERT INTO usuario_professor(
    id, usuario_id, is_active, usuario_id_admin
) VALUES (
    "0ea61737-ad3f-42bd-8735-7f59989970d0",
    "c4697db7-876c-4323-9f21-2bad9d675ba1",
    1,
    "4ca064c7-3df0-4c27-b670-b8928c431f82"
);

CREATE TABLE usuario_estudante (
    id TEXT NOT NULL PRIMARY KEY UNIQUE,
    is_active BLOB NOT NULL DEFAULT 1, 
    usuario_id TEXT NOT NULL UNIQUE,
    FOREIGN KEY (usuario_id) REFERENCES usuarios (id) 
        ON UPDATE CASCADE ON DELETE CASCADE
);

INSERT INTO usuario_estudante(
    id, usuario_id, is_active
) VALUES (
    "ade34344-e1af-49da-89bc-51be535a8efa",
    1,
    "cdb0660a-ed92-49c8-bb08-f77523428a67"
);

CREATE TABLE score_total (
    id TEXT NOT NULL PRIMARY KEY UNIQUE,
    total_score INTEGER NOT NULL DEFAULT 0, 
    usuario_id_estudante TEXT NOT NULL UNIQUE,
    FOREIGN KEY (usuario_id_estudante) REFERENCES usuario_estudante (id) 
        ON UPDATE CASCADE ON DELETE CASCADE
);

INSERT INTO score_total(
    id, total_score, usuario_id_estudante
) VALUES (
    "f9febab1-3e97-4c63-8bbd-11695586518d",d0, "ade34344-e1af-49da-89bc-51be535a8efa"
)


CREATE TABLE fase_jogo (
    id TEXT NOT NULL PRIMARY KEY UNIQUE,
    nro_fase INTEGER NOT NULL DEFAULT 1, 
    score_questao_correta INTEGER NOT NULL DEFAULT 1
);

INSERT INTO fase_jogo(
    id, nro_fase, score_questao_correta
) VALUES (
    "e6c5f402-8a06-462d-aa4d-f179b667d8e2", 1, 1
), (
    "05641c13-852a-46aa-8e26-fb5236cd7467", 2, 2
);

CREATE TABLE questoes_choice(
    id TEXT NOT NULL PRIMARY KEY UNIQUE,
    enunciado TEXT NOT NULL,
    alternativa_a TEXT NOT NULL,
    alternativa_b TEXT NOT NULL,
    alternativa_c TEXT NOT NULL,
    alternativa_d TEXT NOT NULL,
    alternativa_e TEXT NOT NULL,
    correta TEXT NOT NULL DEFAULT "a",
    explicacao TEXT NOT NULL,
    usuario_professor_id TEXT NOT NULL,
    fase_jogo_id TEXT NOT NULL DEFAULT 2,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (usuario_professor_id) REFERENCES usuario_professor (id)
    FOREIGN KEY (fase_jogo_id) REFERENCES fase_jogo (id)
);

INSERT INTO questoes_choice (
    id, 
    enunciado, 
    alternativa_a, 
    alternativa_b, 
    alternativa_c, 
    alternativa_d, 
    alternativa_e, 
    correta, 
    explicacao, 
    usuario_professor_id, 
    fase_jogo_id
) VALUES (
    "5f48a196-e1ad-4569-b3c7-da502fa8149e",
    "O soro e a vacina são substâncias que agem como imunizadores do organismo. A respeito desses produtos, marque a alternativa incorreta:",
    "a) O soro é responsável por uma imunização passiva.",
    "b) As vacinas estimulam o corpo a produzir anticorpos contra determinado antígeno.",
    "c) As vacinas são produzidas injetando-se o antígeno em um animal, que passará a produzir anticorpos. Os anticorpos são posteriormente processados e podem ser usados em humanos.",
    "d) Como exemplo de soro, podemos citar o antiofídico.",
    "e) Podemos dizer que a vacina é usada na prevenção, enquanto o soro é usado para curar.",
    "c",
    " A vacina é produzida utilizando-se o antígeno inativado ou atenuado. Quando se injeta o antígeno em um animal a fim de conseguir anticorpos, é produzido um soro.",
    "0ea61737-ad3f-42bd-8735-7f59989970d0",
    "05641c13-852a-46aa-8e26-fb5236cd7467"
),
(
    "5c3b3df4-c726-43e1-b6cf-f1abb2118194",
    "Quando uma pessoa é picada por uma cobra, é fundamental procurar ajuda médica imediata. Isso se deve ao fato de que algumas espécies produzem venenos tão poderosos que podem levar a pessoa a óbito. Entre as alternativas a seguir, marque aquela que indica corretamente o motivo pelo qual os médicos fazem uso de soro em vez de vacina para tratar o problema.",
    "a) O soro é usado para tratar picada de cobra, pois garante que o corpo produza anticorpos contra o veneno nele injetado.",
    "b) O soro deve ser aplicado porque possui anticorpos já prontos contra o antígeno, garantindo, assim, uma resposta mais rápida.",
    "c) O soro deve ser usado apenas quando uma vacina não está disponível para uso.",
    "d) Em caso de picada de cobra, o soro é usado porque garante uma imunização ativa do paciente.",
    "e) uma imunização de rebanho.",
    "b",
    " Como o veneno de cobra age rapidamente, é importante que os anticorpos estejam disponíveis de maneira imediata. Sendo assim, a terapia utilizada deve ser o soro, que contém anticorpos já prontos.",
    "0ea61737-ad3f-42bd-8735-7f59989970d0",
    "05641c13-852a-46aa-8e26-fb5236cd7467"
), (
    "ce0d1ea5-9607-4cf9-af16-41c09c52084c",
    "(UFMG) A Campanha Nacional de Vacinação do Idoso, instituída pelo Ministério da Saúde do Brasil, vem-se revelando uma das mais abrangentes dirigidas à população dessa faixa etária. Além da vacina contra a gripe, os postos de saúde estão aplicando, também, a vacina contra pneumonia pneumocócica. É correto afirmar que essas vacinas protegem porque:",
    "a) são constituídas de moléculas recombinantes.",
    "b) contêm anticorpos específicos.",
    "c) induzem resposta imunológica.",
    "d) impedem mutações dos patógenos.",
    "e) nao produzem nenhuma imunização.",
    "c",
    "As vacinas estimulam a produção de anticorpos contra o antígeno específico nelas encontrado.",
    "0ea61737-ad3f-42bd-8735-7f59989970d0",
    "05641c13-852a-46aa-8e26-fb5236cd7467"
),
(
    "5d3b3df4-c726-43e1-b6cf-f1abb2118194",
    "Sabemos que as vacinas são capazes de estimular a produção de anticorpos pelo corpo, protegendo-nos, portanto, de doenças. Graças a essa capacidade, dizemos que as vacinas garantem-nos:",
    "a) uma imunização passiva.",
    "b) uma imunização imediata.",
    "c) uma imunização prolongada.",
    "d) uma imunização ativa.",
    "e) uma imunização contínua.",
    "d",
    " Graças à capacidade da vacina de estimular a produção de anticorpos, dizemos que essa é uma forma de imunização ativa.",
    "0ea61737-ad3f-42bd-8735-7f59989970d0",
    "05641c13-852a-46aa-8e26-fb5236cd7467"
),
(
    "c00e7f9d-1fbe-4c06-a266-d9da2be5f8ee",
    "(Enem) A vacina, o soro e os antibióticos submetem os organismos a processos biológicos diferentes. Pessoas que viajam para regiões em que ocorrem altas incidências de febre amarela, de picadas de cobras peçonhentas e de leptospirose e querem evitar ou tratar problemas de saúde relacionados a essas ocorrências devem seguir determinadas orientações. Ao procurar um posto de saúde, um viajante deveria ser orientado por um médico a tomar preventivamente ou como medida de tratamento",
    "a) antibiótico contra o vírus da febre amarela, soro antiofídico caso seja picado por uma cobra e vacina contra a leptospirose.",
    "b) vacina contra o vírus da febre amarela, soro antiofídico caso seja picado por uma cobra e antibiótico caso entre em contato com a Leptospira sp.",
    "c) soro contra o vírus da febre amarela, antibiótico caso seja picado por uma cobra e soro contra toxinas bacterianas.",
    "d) antibiótico ou soro, tanto contra o vírus da febre amarela como para o veneno de cobras, e vacina contra a leptospirose.",
    "e) soro antiofídico e antibiótico contra a Leptospira sp. e vacina contra a febre amarela caso entre em contato com o vírus causador da doença.",
    "b",
    "Como as vacinas são usadas na prevenção de doenças, os soros são usados para tratamentos rápidos e os antibióticos tratam enfermidades causadas por bactérias, podemos concluir que, para prevenir-se contra febre amarela, devemos vacinar o paciente; para o tratamento contra picada de cobra, devemos utilizar o soro; e em caso de leptospirose, devemos administrar antibiótico.",
    "0ea61737-ad3f-42bd-8735-7f59989970d0",
    "05641c13-852a-46aa-8e26-fb5236cd7467"
),
(
    "0189de8c-3831-47ed-943a-c0cf3b9855b5",
    "As vacinas são importantes imunobiológicos que atuam garantindo a prevenção de doenças. As vacinas garantem essa proteção por induzir:",
    "a) a produção de antígenos.",
    "b) a produção de anticorpos.",
    "c) a produção de histamina.",
    "d) a produção de heparina.",
    "e) a produção de toxinas.",
    "b",
    "Vacinas são imunobiológicos que induzem a imunidade específica ativa. Elas são capazes de estimular nosso corpo a produzir anticorpos.",
    "0ea61737-ad3f-42bd-8735-7f59989970d0",
    "05641c13-852a-46aa-8e26-fb5236cd7467"
),
(
    "3d36275d-d081-4ab7-80d0-acc7ef944b6f",
    "A vacinação é uma forma de se garantir:",
    "a) imunidade ativa de forma natural.",
    "b) imunidade ativa de forma artificial.",
    "c) imunidade passiva de forma natural.",
    "d) imunidade passiva de forma artificial.",
    "e) imunidade ativa ou passiva a depender da vacina utilizada.",
    "b",
    "A vacina faz com que nosso corpo produza uma resposta imune, sendo, portanto, responsável por uma imunidade ativa. Chamamos de imunidade natural aquela que ocorre quando ficamos doentes, por exemplo. Já a artificial ocorre como consequência do uso de vacinas.",
    "0ea61737-ad3f-42bd-8735-7f59989970d0",
    "05641c13-852a-46aa-8e26-fb5236cd7467"
),
(
    "d223a224-384d-4c62-aef2-bb2cadcd2801",
    "Das doenças descritas a seguir, qual não possui vacina para uso humano?",
    "a) Rubéola",
    "b) Hepatite B",
    "c) Febre amarela",
    "d) Sarampo",
    "e) Leptospirose",
    "e",
    "A leptospirose é uma doença causada por bactéria que não apresenta vacina, sendo, portanto, fundamentais outras medidas de prevenção contra a doença.",
    "0ea61737-ad3f-42bd-8735-7f59989970d0",
    "05641c13-852a-46aa-8e26-fb5236cd7467"
),
(
    "a7d0e7d7-3808-4dfe-b6bf-374b744752a2",
    "A utilização de soro é uma forma de se garantir:",
    "a) imunidade ativa de forma natural.",
    "b) imunidade ativa de forma artificial.",
    "c) imunidade passiva de forma natural.",
    "d) imunidade passiva de forma artificial.",
    "e) imunidade ativa ou passiva a depender do soro utilizado.",
    "d",
    "A utilização de soros garante uma imunidade passiva, pois o corpo não é estimulado a desenvolver uma resposta imune. É considerada uma imunidade artificial, pois os soros são produzidos pelo ser humano e inoculados a fim de realizar um tratamento rápido contra alguma doença.",
    "0ea61737-ad3f-42bd-8735-7f59989970d0",
    "05641c13-852a-46aa-8e26-fb5236cd7467"
),
(
    "b466230b-a486-48d0-b9e0-9289f87b6ec2",
    "Marque a alternativa que indica corretamente uma situação em que os soros devem ser utilizados:",
    "a) Redução do número de casos de uma doença.",
    "b) Garantia de proteção de um indivíduo contra uma determinada doença.",
    "c) Prevenção de surtos e epidemias.",
    "d) Garantia de tratamento rápido contra toxinas de animais peçonhentos e microrganismos.",
    "e) Proteção do indivíduo contra picadas de cobras e outros animais peçonhentos.",
    "d",
    "Os soros são utilizados em situações em que se necessita de tratamento rápido, uma vez que eles fornecem anticorpos já prontos (imunização passiva).",
    "0ea61737-ad3f-42bd-8735-7f59989970d0",
    "05641c13-852a-46aa-8e26-fb5236cd7467"
),
(
    "c1421adf-cb8f-4f2a-bd45-56f434619f70",
    "(UFF) Desde o surgimento da gripe suína, vacinas têm sido desenvolvidas na tentativa de estabelecer um método de proteção para a população. Assinale a alternativa que apresenta o mecanismo clássico de imunização em que se baseiam as vacinas.",
    "a) Imunização ativa – mecanismo segundo o qual se introduz uma pequena quantidade de antígeno no organismo para produção de anticorpo.",
    "b) Imunização passiva – mecanismo segundo o qual se introduz uma grande quantidade de antígeno no organismo para produção de anticorpo.",
    "c) Imunização ativa – mecanismo segundo o qual se introduz uma grande quantidade de anticorpos no organismo para o combate ao antígeno.",
    "d) Imunização passiva – mecanismo segundo o qual se introduz uma pequena quantidade de anticorpos para o combate ao antígeno.",
    "e) Imunização ativa – mecanismo segundo o qual se inocula o complexo antígeno-anticorpo para o combate à infecção.",
    "a",
    "As vacinas promovem uma imunização ativa, pois o próprio corpo é estimulado a produzir anticorpos devido à introdução de antígenos, incapazes de provocar a doença, no organismo.",
    "0ea61737-ad3f-42bd-8735-7f59989970d0",
    "05641c13-852a-46aa-8e26-fb5236cd7467"
);;


CREATE TABLE questoes_verdadeiro_ou_falso(
    id TEXT NOT NULL PRIMARY KEY UNIQUE,
    enunciado TEXT NOT NULL,
    is_correta BLOB NOT NULL DEFAULT 1,
    explicacao TEXT NOT NULL,
    usuario_professor_id TEXT NOT NULL,
    fase_jogo_id TEXT NOT NULL,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (usuario_professor_id) REFERENCES usuario_professor (id)
    FOREIGN KEY (fase_jogo_id) REFERENCES fase_jogo (id)
);


SELECT * FROM usuarios;

SELECT * FROM usuario_admin;
SELECT * FROM usuario_professor;

SELECT * FROM usuario_estudante;

SELECT * FROM score_total;

DROP TABLE usuarios;

DROP TABLE usuario_admin;
DROP TABLE usuario_professor;
DROP TABLE usuario_estudante;
DROP TABLE usuarios;
DROP TABLE score_total;

DROP TABLE fase_jogo;

DROP TABLE questoes_choice;

DROP TABLE questoes_verdadeiro_ou_falso;


SELECT * FROM questoes_choice ORDER BY updated_at DESC LIMIT 10;


SELECT * FROM usuarios
INNER JOIN usuario_estudante
ON usuario_estudante.usuario_id = usuarios.id
WHERE usuario_estudante.usuario_id
;

SELECT * FROM usuarios;


SELECT * FROM questoes_verdadeiro_ou_falso;