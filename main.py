from flask import Flask, render_template, request, redirect, url_for # type: ignore
from flask_sqlalchemy import SQLAlchemy # type: ignore

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///usuarios.db'
db = SQLAlchemy(app)

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return '<Usuario %r>' % self.nome

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
    emails_usuarios = [usuario.email for usuario in usuarios]  # List Comprehension
    nomes_em_titulo = list(map(lambda nome: nome.title(), [usuario.nome for usuario in usuarios]))  # Função Lambda e Alta Ordem
    return render_template('listar.html', usuarios=usuarios, emails=emails_usuarios, nomes_em_titulo=nomes_em_titulo)

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