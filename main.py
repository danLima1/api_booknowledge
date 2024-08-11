from flask import Flask, jsonify, request
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)  # Permitir CORS

# Função para conectar ao banco de dados SQLite
def connect_db():
    conn = sqlite3.connect('books.db')
    return conn

# Função para criar a tabela de livros
def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            url TEXT NOT NULL,
            image TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Inicialização do banco de dados
create_table()

@app.route('/search', methods=['GET'])
def search_books():
    query = request.args.get('query', '').lower()
    page = int(request.args.get('page', 1))  # Página atual (padrão é 1)
    per_page = 24  # Número de livros por página

    conn = connect_db()
    cursor = conn.cursor()

    if query:
        cursor.execute('SELECT * FROM books WHERE LOWER(title) LIKE ?', ('%' + query + '%',))
    else:
        cursor.execute('SELECT * FROM books')

    books = cursor.fetchall()
    conn.close()

    total_books = len(books)
    total_pages = (total_books + per_page - 1) // per_page  # Calcular o número total de páginas

    # Paginação: Selecionar os livros da página atual
    start = (page - 1) * per_page
    end = start + per_page
    books_on_page = books[start:end]

    # Convertendo os resultados para um dicionário
    books_list = []
    for book in books_on_page:
        books_list.append({
            'title': book[1],
            'url': book[2],
            'image': book[3]
        })

    return jsonify({
        'books': books_list,
        'total_pages': total_pages,
        'current_page': page
    })

@app.route('/add-book', methods=['POST'])
def add_book():
    data = request.json
    title = data.get('title')
    url = data.get('url')
    image = data.get('image')

    # Validar que o link começa com https://drive.google.com/
    if not url.startswith('https://drive.google.com/'):
        return jsonify({'error': 'O link do livro deve ser um link válido do Google Drive.'}), 400

    # Verificar se os campos necessários estão presentes
    if not all([title, url, image]):
        return jsonify({'error': 'Campos title, url e image são obrigatórios.'}), 400

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO books (title, url, image) VALUES (?, ?, ?)', (title, url, image))
    conn.commit()
    conn.close()

    return jsonify({'message': 'Livro adicionado com sucesso!'}), 201

if __name__ == '__main__':
    app.run(debug=True, port=5000)
