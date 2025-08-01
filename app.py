import flask as fk
import randomizador as ran
import random
import sqlite3 as sql

app = fk.Flask(__name__)

@app.get('/')
def casa_br():
    return fk.render_template('br/index.html', 
                       paragrafo = ran.paragrafo(),
                       titulo = ran.titulo(),
                       elementos = ran.curisidade_aleatoria())

@app.get('/adm')
def adm():
    with sql.Connection('./curiosidades.db') as conn:
        sql_select_curiosidades = '''
        SELECT filme, fato, img, nome AS nome_categoria
        FROM curiosidades
        JOIN categorias ON id_categoria == categorias.id;
    '''
        lista_de_curiosidades = conn.execute(sql_select_curiosidades)
    
    adm = True

    return fk.render_template('br/curiosities.html', curiosidades = lista_de_curiosidades, adm = adm)

@app.get('/curiosidades')
def cards_curiosidades():
    with sql.Connection('./curiosidades.db') as conn:
        sql_select_curiosidades = '''
        SELECT filme, fato, img, nome AS nome_categoria
        FROM curiosidades
        JOIN categorias ON id_categoria == categorias.id;
    '''
        lista_de_curiosidades = conn.execute(sql_select_curiosidades)

    adm = False
    
    return fk.render_template('br/curiosities.html', curiosidades = lista_de_curiosidades, adm = adm)

@app.get('/buscar')
def get_buscar():
    return fk.render_template('br/search.html')

@app.post('/buscar')
def post_buscar():
    filme = fk.request.form['filme']
    
    sql_select_filme_por_nome = f'''
    SELECT filme, fato, img, nome AS nome_categoria
    FROM curiosidades
    JOIN categorias ON id_categoria == categorias.id
    WHERE filme LIKE '%{filme}%' ORDER BY nome ASC;
'''
    with sql.Connection('curiosidades.db') as conn:
        # if filme:
        lista_de_filmes = conn.execute(sql_select_filme_por_nome)
        # else:
        #     lista_de_filmes = [('a', 'b', 'c', 'd')]

    return fk.render_template('br/curiosities.html', curiosidades = lista_de_filmes)

@app.get('/editar/<id_filme>')
def buscar(id_filme):
    with sql.Connection('curiosidades.db') as conn:
        sql_select_categorias = "SELECT id, nome FROM categorias;"
        sql_dados_curiosidade = f'''
            SELECT filme, fato, img, nome AS nome_categoria
            FROM curiosidades
            JOIN categorias ON id_categoria == categorias.id;
            WHERE id = {id_filme}
            '''
        lista_categorias = conn.execute(sql_select_categorias)    
        registro_curiosidade = conn.execute(sql_dados_curiosidade)

        filme, fato, img, nome_categoria = next(registro_curiosidade)
        dados_curiosidade = {
            "id": id,
            "nome": filme,
            "preco": fato,
            "img": img,
            "id_categoria": nome_categoria
        }

        return fk.render_template('br/edit.html',
                                     categorias = lista_categorias,
                                     curiosidade = dados_curiosidade)

@app.get("/cadastrar")
def get_cadastrar():
    with sql.Connection('curiosidades.db') as conn:
        sql_select_categorias = "SELECT id, nome FROM categorias;"
        
        lista_categorias = conn.execute(sql_select_categorias)
        #retorno: [(1,'bobinha'), (2, 'chocante'), (3, 'surprendente')] 
    return fk.render_template("br/register.html", categorias = lista_categorias)

@app.post('/cadastrar')
def fazer_cadastro():
    filme = fk.request.form.get('filme')
    curiosidade = fk.request.form.get('curiosidade')
    arquivo_imagem = fk.request.files['img']
    categoria = fk.request.form.get("categoria")

    arquivo_imagem.save(f"./static/img/{arquivo_imagem.filename}")
    nome_imagem = arquivo_imagem.filename

    print(f'este é o arquivo de imagem: {nome_imagem}')


    with sql.Connection("curiosidades.db") as conn:
        sql_inserir_curiosidade = '''
        INSERT INTO curiosidades (filme, fato, img, id_categoria) VALUES (?,?,?,?);
        ''' 
        conn.execute(sql_inserir_curiosidade, (filme, curiosidade, nome_imagem, categoria))

    return fk.redirect("/curiosidades")

@app.get('/en')
def home_light():
    return fk.render_template('en/template.html')

app.run(host='0.0.0.0', debug=True)
