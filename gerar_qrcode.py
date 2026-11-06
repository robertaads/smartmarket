"""Gera QR Codes PNG para os produtos cadastrados no CSV."""
import csv, os
from pathlib import Path
import qrcode
BASE=Path(__file__).resolve().parent
BASE_URL=os.getenv('BASE_URL','http://127.0.0.1:5000').rstrip('/')
OUT=BASE/'qrcodes'; OUT.mkdir(exist_ok=True)
with (BASE/'data'/'produtos.csv').open(encoding='utf-8-sig',newline='') as f:
    for row in csv.DictReader(f):
        url=f"{BASE_URL}/produto/{row['id']}"
        img=qrcode.make(url)
        path=OUT/f"produto_{row['id']}.png"
        img.save(path)
        print(f"Gerado: {path.name} -> {url}")
