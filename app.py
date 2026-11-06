import os
from flask import Flask, render_template, abort, jsonify
from dotenv import load_dotenv
from services.products import get_products, get_product

load_dotenv()
app = Flask(__name__, template_folder='web/templates', static_folder='web/static')

@app.get('/')
def index():
    return render_template('index.html', products=get_products())

@app.get('/produto/<int:produto_id>')
def produto(produto_id):
    item = get_product(produto_id)
    if not item:
        abort(404)
    return render_template('produto.html', produto=item)

@app.get('/api/produtos')
def api_produtos():
    return jsonify(get_products())

@app.errorhandler(404)
def not_found(_error):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)), debug=os.getenv('FLASK_DEBUG') == '1')
