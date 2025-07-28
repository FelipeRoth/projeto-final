import sqlite3 as sql

conn = sql.Connection('curiosidades.db')

sql_criar_tabela_curiosidades = '''
CREATE TABLE IF NOT EXISTS curiosidades (
    id INTEGER PRIMARY KEY,
    filme TEXT NOT NULL,
    fato TEXT NOT NULL,
    img TEXT NOT NULL,
    id_categoria INTEGER NOT NULL,
    FOREIGN KEY(id_categoria) REFERENCES categorias(id)
);
'''

sql_criar_tabela_categoria = '''
CREATE TABLE IF NOT EXISTS categorias (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL
);
'''

conn.execute(sql_criar_tabela_curiosidades)
conn.execute(sql_criar_tabela_categoria)
conn.commit()

# 
# CADASTROS INICIAIS
# 

# CADASTRAR CATEGORIAS INICIAIS

sql_insert_categorias = '''
INSERT INTO categorias (nome) VALUES (?);
'''
lista_insert_categorias = [
    ('bobinha',),
    ('chocante',),
    ('surprendente',)
]

conn.executemany(sql_insert_categorias, lista_insert_categorias)

# CADASTRAR CURIOSIDADES INICIAIS

sql_insert_curiosidades = '''
INSERT INTO curiosidades (filme, fato, img, id_categoria) VALUES (?, ?, ?, ?);
'''

lista_insert_curiosidades = [
    (
        'Titanic (1997)',
        'O orçamento para do filme foi maior do que o custo para construir o próprio navio.',
        '1.jpg',
        '3'
    ),

    (
        'Halloween (1978)',
        'A famosa máscara usada pelo assassino em série Michael Myers não é uma peça original criada para o filme. Na verdade, trata-se de uma máscara do Capitão Kirk, de Star Trek, e custou apenas 2 dólares.',
        '2.jpg',
        '1'
    ),

    (
        'Batman: O Retorno (1992)',
        'A roupa de Mulher-Gato usada por Michelle Pfeiffer era tão apertada que fazia a atriz sofrer uma série de desmaios durante as gravações.',
        '3.jpg',
        '2'
    )
]

conn.executemany(sql_insert_curiosidades, lista_insert_curiosidades)

conn.commit()
conn.close()