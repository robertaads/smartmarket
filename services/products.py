"""Leitura de produtos no Google Sheets ou em CSV local para demonstração."""
import csv, json, os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
CSV_PATH = BASE_DIR / 'data' / 'produtos.csv'

def _normalizar(row):
    return {
        'id': int(row.get('id', 0)), 'nome': row.get('nome',''),
        'preco': row.get('preco',''), 'descricao': row.get('descricao',''),
        'categoria': row.get('categoria',''), 'nichos': row.get('nichos',''),
        'informacoes_nutricionais': row.get('informacoes_nutricionais',''),
        'ingredientes': row.get('ingredientes',''), 'corredor': str(row.get('corredor','')),
        'prateleira': str(row.get('prateleira','')), 'imagem': row.get('imagem',''),
        'receita': row.get('receita','')
    }

def _from_csv():
    with CSV_PATH.open(encoding='utf-8-sig', newline='') as f:
        return [_normalizar(r) for r in csv.DictReader(f)]

def _from_sheets():
    import gspread
    raw = os.getenv('GOOGLE_CREDENTIALS_JSON')
    if raw:
        credentials = json.loads(raw)
        client = gspread.service_account_from_dict(credentials)
    else:
        path = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
        if not path:
            raise RuntimeError('Configure GOOGLE_CREDENTIALS_JSON ou GOOGLE_APPLICATION_CREDENTIALS.')
        client = gspread.service_account(filename=path)
    sheet = client.open_by_key(os.environ['SHEET_ID']).sheet1
    return [_normalizar(r) for r in sheet.get_all_records()]

def get_products():
    if os.getenv('SHEET_ID'):
        try:
            return _from_sheets()
        except Exception as exc:
            app_mode = os.getenv('DATA_MODE', 'csv').lower()
            if app_mode != 'csv':
                raise
    return _from_csv()

def get_product(product_id):
    return next((p for p in get_products() if p['id'] == product_id), None)
