from flask import Flask, jsonify, request
from flask_cors import CORS
import sqlite3
import re

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


# Função para inserir os livros iniciais no banco de dados
def insert_initial_books():
    # Livros pré-definidos
    initial_books = [
        {
            "title": "Iron Flame",
            "url": "https://drive.google.com/file/d/1IMdPhcoec-KNJ-Vo3YCu_ptCX11tpuKJ/view?usp=drivesdk",
            "image": "src/9789189516090.webp"
        },
        {
            "title": "Duna",
            "url": "https://drive.google.com/file/d/1xu8RZFvC19_jHOTyrUhEA-LNTQX6f1ZS/view?usp=drivesdk",
            "image": "src/duna1.webp"
        },
        {
            "title": "Quarta Asa",
            "url": "https://drive.google.com/file/d/1AIj4B6LSFPoH6CBjvYUBD-S208PNg_Ww/view?usp=drivesdk",
            "image": "src/images.jpeg"
        },
        {
            "title": "Adeus as Armas",
            "url": "https://drive.google.com/file/d/1RV0qtjFaPA4oisZ4CrwbJV5x6tvcNwoP/view?usp=drivesdk",
            "image": "https://m.media-amazon.com/images/I/41h6QHlIEtL._SY445_SX342_.jpg"
        },
        {
            "title": "O Senhor dos Anéis",
            "url": "https://drive.google.com/file/d/1iemKbODbnrN6R2-8iqhoufGroQ70keHe/view?usp=sharing",
            "image": "https://m.media-amazon.com/images/I/81EKLXXFDKL._AC_UF1000,1000_QL80_.jpg"
        },
        {
            "title": "O Fabricante de Lágrimas",
            "url": "https://drive.google.com/file/d/16VrSyhES1p4qWfVh_y5nCyWo70soC5Gk/view?usp=drivesdk",
            "image": "src/fabricante.jpg"
        },
        {
            "title": "O Cão dos Baskervilles",
            "url": "https://drive.google.com/file/d/1GbV3dWmQDY8W3LiATFYJ_KX8o_z9Q_b0/view?usp=drivesdk",
            "image": "src/coolen.jpg"
        },
        {
            "title": "O Iluminado",
            "url": "https://drive.google.com/file/d/1mfPGUBLDjjXDuLaEe6Uf24a4cbKFKHqk/view?usp=drivesdk",
            "image": "https://images-na.ssl-images-amazon.com/images/I/71OfY5QkKyL.jpg"
        },
        {
            "title": "A Garota no Trem",
            "url": "https://drive.google.com/file/d/16VrSyhES1p4qWfVh_y5nCyWo70soC5Gk/view?usp=drivesdk",
            "image": "src/girl.jpg"
        },
        {
            "title": "Um Estranho no Ninho",
            "url": "https://drive.google.com/file/d/163C8_BCRtXza0Xs1NoSaYaVAFsKkWTXH/view?usp=drivesdk",
            "image": "src/stranger.jpeg"
        },
        {
            "title": "A Noite dos Mortos-Vivos",
            "url": "https://drive.google.com/file/d/1rx9hHHlCxu2aAqQhMIY0jfLYDyMs8x-m/view?usp=drivesdk",
            "image": "src/noite.jpg"
        },
        {
            "title": "Caim",
            "url": "https://drive.google.com/file/d/1FosiD1fjgvZc-Vp-MFKtuFPhvcxdkzTl/view?usp=drivesdk",
            "image": "src/caim.jpg"
        },
        {
            "title": "Os Sete Maridos de Evelyn Hugo",
            "url": "https://drive.google.com/file/d/1jdR2aWGn3HSGSCOySBOEfRIWMlhWJ3g8/view?usp=drivesdk",
            "image": "src/sete.jpg"
        },
        {
            "title": "Verity",
            "url": "https://drive.google.com/file/d/1xYWAhw-CLXhnqI9I3O0ilkZsAFp4ouCd/view?usp=drivesdk",
            "image": "src/verity_.jpg"
        },
        {
            "title": "O Paraíso",
            "url": "https://drive.google.com/file/d/1jah8P7Nfl3kQIBn_wA5Dryo6CgphK43L/view?usp=drivesdk",
            "image": "src/paraiso.jpg"
        },
        {
            "title": "O Labirinto do Fauno",
            "url": "https://drive.google.com/file/d/1kp-eLJdDwhwh2OUH0Hd8x_WiUnlknOCF/view?usp=drivesdk",
            "image": "src/labirinto.jpg"
        },
        {
            "title": "O Tempo Todo",
            "url": "https://drive.google.com/file/d/1exQ1jCSkufqQ4yEaxcUgHQGCoJQSR7US/view?usp=drivesdk",
            "image": "src/tempo.webp"
        },
        {
            "title": "Tudo Começa com um Sim",
            "url": "https://drive.google.com/file/d/1ZQewIEGASl4txnIi0uauC_Sa4XHTAp2N/view?usp=drivesdk",
            "image": "src/comeca.jpg"
        },
        {
            "title": "Os Sete Maridos de Evelyn Hugo",
            "url": "https://drive.google.com/file/d/1MvUvTA3icOmLsdWv7dAA4YYuEXAHPDte/view?usp=drivesdk",
            "image": "src/six.jpg"
        },
        {
            "title": "O Tirano de Frankenstein",
            "url": "https://drive.google.com/file/d/1sQJ5npwGlXLKBTbUS0Q9SigDw5tL77OG/view?usp=drivesdk",
            "image": "src/tirano.jpg"
        },
        {
            "title": "A Ascensão de Skywalker",
            "url": "https://drive.google.com/file/d/1gABDlip9EPHqDjTM4sSvy6oEOq9fmN4y/view?usp=drivesdk",
            "image": "src/rise.jpg"
        },
        {
            "title": "Duna (Parte 2)",
            "url": "https://drive.google.com/file/d/1WOu3fN4ViXs8tqxfSorPujgZfAWFYdF-/view?usp=drivesdk",
            "image": "src/duna2.jpg"
        },
        {
            "title": "Uma Janela para o Jardim",
            "url": "https://drive.google.com/file/d/1afsv1zoUv-BU4ctydYj464LzCpctU_Id/view",
            "image": "src/page_1.webp"
        },
        {
            "title": "Breve Breve",
            "url": "https://drive.google.com/file/d/1WOu3fN4ViXs8tqxfSorPujgZfAWFYdF-/view?usp=drivesdk",
            "image": "https://img.elo7.com.br/product/zoom/3FE8395/breve-breve.jpg"
        }

    ]

    conn = connect_db()
    cursor = conn.cursor()

    # Verificar se já existem livros no banco de dados
    cursor.execute('SELECT COUNT(*) FROM books')
    count = cursor.fetchone()[0]

    if count == 0:  # Se não houver livros, insira os livros iniciais
        for book in initial_books:
            cursor.execute('INSERT INTO books (title, url, image) VALUES (?, ?, ?)',
                           (book['title'], book['url'], book['image']))
        conn.commit()

    conn.close()


# Inicialização do banco de dados e inserção dos livros iniciais
create_table()
insert_initial_books()


@app.route('/search', methods=['GET'])
def search_books():
    query = request.args.get('query', '').lower()
    conn = connect_db()
    cursor = conn.cursor()

    if query:
        cursor.execute('SELECT * FROM books WHERE LOWER(title) LIKE ?', ('%' + query + '%',))
    else:
        cursor.execute('SELECT * FROM books')

    books = cursor.fetchall()
    conn.close()

    # Convertendo os resultados para um dicionário
    books_list = []
    for book in books:
        books_list.append({
            'title': book[1],
            'url': book[2],
            'image': book[3]
        })

    return jsonify(books_list)


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
