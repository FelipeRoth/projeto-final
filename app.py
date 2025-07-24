import flask as fk
import randomizador as ran

app = fk.Flask(__name__)

@app.get('/')
def casa_claro():
    txt = ran.paragrafo()
    tt = ran.titulo()
    card = ran.cartao()
    for elemento in card:
        print(elemento)
    print(card)
    return fk.render_template('modelo.html', paragrafo = txt, titulo = tt, elemento = card)

@app.get('/en')
def home_light():
    return fk.render_template('template.html')



app.run(host='0.0.0.0', debug=True)