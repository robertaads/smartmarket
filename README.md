# SmartMarket — pacote do Projeto Integrado

## O que está pronto neste pacote
- Aplicação web Flask com listagem e página dinâmica por ID (`/produto/<id>`).
- Interface responsiva Mobile-First em HTML/CSS/JavaScript e templates Jinja2 (com espaço para imagens por URL na coluna `imagem`).
- Mapa modal que destaca o corredor e a prateleira do produto.
- Base inicial em CSV para executar imediatamente sem credenciais externas.
- Integração opcional com Google Sheets via `gspread` e conta de serviço.
- Gerador de QR Codes PNG baseado nos IDs dos produtos.
- Arquivos iniciais para GitHub e Render.
- Modelo de planilha e roteiro de testes/documentação.

## Executar localmente
1. Instale Python 3.10 ou superior.
2. Abra o terminal na pasta do projeto.
3. Crie e ative um ambiente virtual: `python -m venv .venv`.
4. Windows: `.venv\\Scripts\\activate`; Linux/macOS: `source .venv/bin/activate`.
5. Instale: `pip install -r requirements.txt`.
6. Copie `.env.example` para `.env` (opcional; a aplicação usa CSV por padrão).
7. Execute: `python app.py`.
8. Acesse `http://127.0.0.1:5000`.

## Google Sheets (configuração que o grupo precisa concluir)
1. Crie uma planilha Google com uma aba contendo os mesmos cabeçalhos do `data/produtos.csv`.
2. No Google Cloud, habilite Google Sheets API e crie uma Service Account.
3. Baixe o JSON da conta de serviço e compartilhe a planilha com o e-mail `client_email` desse JSON, com permissão de leitor.
4. Configure `SHEET_ID` com o ID entre `/d/` e `/edit` na URL da planilha.
5. Para desenvolvimento local, configure `GOOGLE_APPLICATION_CREDENTIALS` apontando para o JSON local (não o envie ao GitHub), ou use `GOOGLE_CREDENTIALS_JSON`.
6. Em produção, configure a variável `GOOGLE_CREDENTIALS_JSON` no painel do Render com o conteúdo integral do JSON, além de `SHEET_ID`.

Se não houver credenciais, mantenha `SHEET_ID` vazio e o sistema usará o CSV de demonstração.

## QR Codes
- Local: `python gerar_qrcode.py` gera arquivos na pasta `qrcodes/` usando `http://127.0.0.1:5000`.
- Para teste por smartphone na mesma rede Wi-Fi, defina `BASE_URL=http://IP-LOCAL-DO-COMPUTADOR:5000` antes de executar o gerador. O computador e o celular precisam estar na mesma rede e o firewall deve permitir a porta 5000.
- Após publicar no Render, defina `BASE_URL=https://SEU-SERVICO.onrender.com` e gere novamente os QR Codes. Não use localhost nos QR Codes de produção.

## GitHub e Render
1. `git init`, `git add .`, `git commit -m "feat: estrutura inicial do SmartMarket"`.
2. Crie um repositório vazio no GitHub, configure o remoto e faça `git push -u origin main`.
3. No Render, crie um Web Service conectado ao repositório. Build: `pip install -r requirements.txt`; Start: `gunicorn app:app`.
4. Configure `SHEET_ID` e `GOOGLE_CREDENTIALS_JSON` se usar a planilha real.
5. Teste a URL pública e gere os QR Codes novamente com a URL pública.

**Segurança:** nunca publique arquivos JSON de credenciais, `.env`, senhas ou chaves no GitHub. Se uma chave for publicada, revogue-a no Google Cloud.
