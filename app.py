import flask as fk
import randomizador as ran
import random
import sqlite3 as sql

app = fk.Flask(__name__)

@app.get('/')
def casa_claro():
    # conn = sql.Connection('./curiosidades.db')
    # id = '''
    #     SELECT id
    #     FROM curiosidades
    # '''

    # id = conn.execute(id)
    # quantos_id = 0
    # for _ in id:
    #     quantos_id = quantos_id + 1

    # id_aleatorio = random.randrange(1, quantos_id+1)

    # print(id_aleatorio)

    # sql_select_a_curiosidade = f'''
    #     SELECT filme, fato, img, nome AS nome_categoria
    #     FROM curiosidades
    #     JOIN categorias ON id_categoria == categorias.id
    #     WHERE curiosidades.id LIKE {id_aleatorio};
    # '''
    # a_curiosidade = conn.execute(sql_select_a_curiosidade)

    return fk.render_template('br/index.html', 
                       paragrafo = ran.paragrafo(),
                       titulo = ran.titulo(),
                       elementos = ran.curisidade_aleatoria())

@app.get('/curiosidades')
def cards_curiosidades():
    with sql.Connection('./curiosidades.db') as conn:
        sql_select_curiosidades = '''
        SELECT filme, fato, img, nome AS nome_categoria
        FROM curiosidades
        JOIN categorias ON id_categoria == categorias.id;
    '''
        lista_de_curiosidades = conn.execute(sql_select_curiosidades)
        
    return fk.render_template('br/curiosities.html', curiosidades = lista_de_curiosidades)

@app.get('/en')
def home_light():
    return fk.render_template('en/template.html')

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

app.run(host='0.0.0.0', debug=True)