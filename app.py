import flask as fk
import randomizador as ran
import random
import sqlite3 as sql

app = fk.Flask(__name__)

@app.get('/')
def casa_claro():
    sql_select_curiosidades = '''
    SELECT filme, fato, img, nome AS nome_categoria
    FROM curiosidades
    JOIN categorias ON id_categoria == categorias.id;
'''
    with sql.Connection('curiosidades.db') as conn:
        lista_de_curiosidades = conn.execute(sql_select_curiosidades)

    voltas = [1, 2]
    for volta in voltas:
        print(f'volta {volta}')
        for curiosidade in lista_de_curiosidades:
            filme = curiosidade[0]
            fato = curiosidade[1]
            img = curiosidade[2]
            nome_categoria = curiosidade[3]
    print(f'{filme}, {fato}, {img}, {nome_categoria}')
            

        
    return fk.render_template('br/index.html', 
                       paragrafo = ran.paragrafo(),
                       titulo = ran.titulo())

@app.get('/curiosidades')
def cards_curiosidades():
    
    sql_select_curiosidades = '''
    SELECT filme, fato, img, nome AS nome_categoria
    FROM curiosidades
    JOIN categorias ON id_categoria == categorias.id;
'''
    with sql.Connection('curiosidades.db') as conn:
        lista_de_curiosidades = conn.execute(sql_select_curiosidades)
    
    return fk.render_template('br/curiosities.html', curiosidades = lista_de_curiosidades)

@app.get('/en')
def home_light():
    return fk.render_template('en/template.html')



app.run(host='0.0.0.0', debug=True)