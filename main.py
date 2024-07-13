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
