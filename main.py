from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Permitir CORS

# Dados de exemplo
books = [
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
    }
    # Adicione mais livros aqui conforme necessário
]

@app.route('/search', methods=['GET'])
def search_books():
    query = request.args.get('query', '').lower()
    print(f"Received query: {query}")  # Log de depuração
    if query:
        filtered_books = [book for book in books if query in book['title'].lower()]
    else:
        filtered_books = books

    print(f"Filtered books: {filtered_books}")  # Log de depuração
    return jsonify(filtered_books)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
