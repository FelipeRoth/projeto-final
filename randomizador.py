import random
import sqlite3 as sql

def paragrafo():
    txt = random.choice([
        'Essa curiosidades poucos sabem',
        'Levou anos para descobrirem',
        'Você é um dos poucos que sabe',
    ])
    return txt

def titulo():
    tt = random.choice([
        'Curiosidades sobre filmes',
        'Você vai ficar de queixo caido',
        'Você sabia?',
    ])
    return tt

def curisidade_aleatoria():
    conn = sql.Connection('./curiosidades.db')
    id = '''
        SELECT id
        FROM curiosidades
    '''

    id = conn.execute(id)
    quantos_id = 0
    for _ in id:
        quantos_id = quantos_id + 1

    id_aleatorio = random.randrange(1, quantos_id+1)

    print(id_aleatorio)

    sql_select_a_curiosidade = f'''
        SELECT filme, fato, img, nome AS nome_categoria
        FROM curiosidades
        JOIN categorias ON id_categoria == categorias.id
        WHERE curiosidades.id LIKE {id_aleatorio};
    '''
    a_curiosidade = conn.execute(sql_select_a_curiosidade)
    return a_curiosidade
