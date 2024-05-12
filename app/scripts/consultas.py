from db import db

def consulta_jogador(email_institucional):
    consulta = f"""SELECT usuarios.id, usuarios.email_institucional, usuarios.username, score_total.total_score
                    FROM usuarios
                    INNER JOIN usuario_estudante
                        ON usuario_estudante.usuario_id = usuarios.id
                    RIGHT JOIN score_total
                        ON score_total.usuario_id_estudante = usuario_estudante.id
                    WHERE  usuarios.email_institucional = '{email_institucional}'
                    ORDER BY score_total.total_score DESC;"""
    return db(consulta)


def consulta_perguntas_vf():
    consulta = f"""SELECT * FROM questoes_verdadeiro_ou_falso ORDER BY updated_at DESC LIMIT 5"""
    result_tupla =  db(consulta, ())
    result = separa_tupla_em_lista(result_tupla)
    return result

def separa_tupla_em_lista(tupla):
    lista=[]
    for i in tupla:
        for el in i:
            lista.append(el)
    return lista