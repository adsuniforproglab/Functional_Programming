from flask import Flask, render_template, request, redirect, url_for # type: ignore
from flask_sqlalchemy import SQLAlchemy # type: ignore
from functools import reduce, partial  # Added partial for partial application
from typing import List, Callable, TypeVar, Any, Tuple

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///usuarios.db'
db = SQLAlchemy(app)

# Type definitions to enhance code clarity
T = TypeVar('T')
U = TypeVar('U')
V = TypeVar('V')

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return '<Usuario %r>' % self.nome

# =========================================================
# SEÇÃO DE PROGRAMAÇÃO FUNCIONAL
# =========================================================

# 1. FUNÇÕES PURAS - não têm efeitos colaterais e sempre retornam o mesmo valor para os mesmos argumentos
def transformar_maiusculo(texto: str) -> str:
    """Função pura que converte texto para maiúsculo"""
    return texto.upper()

def transformar_minusculo(texto: str) -> str:
    """Função pura que converte texto para minúsculo"""
    return texto.lower()

def transformar_titulo(texto: str) -> str:
    """Função pura que capitaliza o texto"""
    return texto.title()

def calcular_tamanho(texto: str) -> int:
    """Função pura que conta caracteres"""
    return len(texto)

def inverter_sequencia(texto: str) -> str:
    """Função pura que inverte o texto"""
    return texto[::-1]

# 2. FUNÇÕES DE ALTA ORDEM - recebem funções como parâmetros ou retornam funções
def compor_funcoes(f: Callable[[U], V], g: Callable[[T], U]) -> Callable[[T], V]:
    """Função de alta ordem para composição de funções (f ∘ g)"""
    return lambda x: f(g(x))

def pipe(valor: T, *funcoes: Callable) -> Any:
    """Pipe de funções - aplica valor através de uma sequência de funções"""
    resultado = valor
    for funcao in funcoes:
        resultado = funcao(resultado)
    return resultado

def aplicar_cada(funcao: Callable[[T], U], colecao: List[T]) -> List[U]:
    """Função de alta ordem que aplica uma função a cada elemento"""
    return list(map(funcao, colecao))

# 3. CURRYING E APLICAÇÃO PARCIAL - transformação de funções para permitir aplicação parcial
def somar(x: int, y: int) -> int:
    """Função simples para demonstrar currying"""
    return x + y

# Usando partial para aplicação parcial
somar_cinco = partial(somar, 5)  # Cria uma nova função onde o primeiro argumento é 5

# 5. MANIPULADORES DE LISTAS FUNCIONAIS
def extrair_iniciais(nomes: List[str]) -> List[str]:
    """Extrai a primeira letra de cada nome"""
    return [nome[0].upper() for nome in nomes if nome]

# 6. FUNÇÕES PARA OPERAÇÕES COM USUÁRIOS
def extrair_nomes(usuarios: List[Usuario]) -> List[str]:
    """Extrai nomes dos usuários de forma funcional"""
    return list(map(lambda u: u.nome, usuarios))

def extrair_emails(usuarios: List[Usuario]) -> List[str]:
    """Extrai emails dos usuários de forma funcional"""
    return list(map(lambda u: u.email, usuarios))

# =========================================================
# ROTAS DA APLICAÇÃO
# =========================================================

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        novo_usuario = Usuario(nome=nome, email=email)
        db.session.add(novo_usuario)
        db.session.commit()
        return redirect(url_for('listar'))
    return render_template('index.html')

@app.route('/listar')
def listar():
    usuarios = Usuario.query.all()
    
    # Extraindo propriedades usando funções funcionais
    nomes = extrair_nomes(usuarios)
    emails = extrair_emails(usuarios)
    
    # Transformações funcionais
    nomes_em_titulo = aplicar_cada(transformar_titulo, nomes)
    
    # Filter - filtrando usuários com nomes longos
    nomes_longos = list(filter(lambda usuario: len(usuario.nome) > 5, usuarios))
    
    # Reduce - somando comprimentos dos nomes
    total_caracteres = reduce(lambda acc, nome: acc + len(nome), nomes, 0)
    
    # Aplicando função pura
    nomes_maiusculos = aplicar_cada(transformar_maiusculo, nomes)
    
    # Composição de funções
    titulo_apos_minusculo = compor_funcoes(transformar_titulo, transformar_minusculo)
    nomes_processados = aplicar_cada(titulo_apos_minusculo, nomes)
    
    # Usando pipe para aplicar múltiplas funções
    nomes_invertidos_maiusculos = [pipe(nome, transformar_minusculo, inverter_sequencia, transformar_maiusculo) for nome in nomes]
    
    # Map e função nomeada
    contagens_caracteres = list(map(calcular_tamanho, nomes))
    
    # Zip para combinar listas
    dados_nome_contagem = list(zip(nomes, contagens_caracteres))
    
    # Extraindo iniciais dos nomes
    iniciais_nomes = extrair_iniciais(nomes)
    
    # Exemplo de currying/aplicação parcial
    numeros = list(range(1, len(nomes) + 1))
    numeros_mais_cinco = list(map(somar_cinco, numeros))
    
    # Ordenação de nomes por tamanho usando função anônima (lambda)
    nomes_ordenados_tamanho = sorted(nomes, key=lambda nome: len(nome))
    
    return render_template('listar.html', 
                           usuarios=usuarios,
                           emails=emails,
                           nomes_em_titulo=nomes_em_titulo,
                           nomes_longos=nomes_longos,
                           total_caracteres=total_caracteres,
                           nomes_maiusculos=nomes_maiusculos,
                           nomes_processados=nomes_processados,
                           nomes_invertidos_maiusculos=nomes_invertidos_maiusculos,
                           dados_nome_contagem=dados_nome_contagem,
                           iniciais_nomes=iniciais_nomes,
                           numeros_originais=numeros,
                           numeros_mais_cinco=numeros_mais_cinco,
                           nomes_ordenados_tamanho=nomes_ordenados_tamanho)

@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    usuario = Usuario.query.get_or_404(id)
    if request.method == 'POST':
        usuario.nome = request.form['nome']
        usuario.email = request.form['email']
        db.session.commit()
        return redirect(url_for('listar'))
    return render_template('editar.html', usuario=usuario)

@app.route('/deletar/<int:id>')
def deletar(id):
    usuario = Usuario.query.get_or_404(id)
    db.session.delete(usuario)
    db.session.commit()
    return redirect(url_for('listar'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)