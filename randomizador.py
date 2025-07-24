import random

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

def cartao():

    card = [
        ('1',
         'O orçamento para o filme “Titanic” foi maior do que o custo para construir o próprio navio.'),
         ('2',
          'A famosa máscara usada pelo assassino em série Michael Myers não é uma peça original criada para o filme. Na verdade, trata-se de uma máscara do Capitão Kirk, de Star Trek, e custou apenas 2 dólares.'),
         ('3',
          'Em Batman: O Retorno (1992) A roupa de Mulher-Gato usada por Michelle Pfeiffer era tão apertada que fazia a atriz sofrer uma série de desmaios durante as gravações.')
    ]

    return random.choice(card)