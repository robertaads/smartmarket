# SmartMarket — especificação resumida e evidências

## 1. Introdução
O SmartMarket propõe uma aplicação web para aproximar o produto físico do ambiente digital do supermercado. O consumidor lê com a câmera do smartphone um QR Code associado ao produto e é direcionado a uma página web com descrição, preço, informações nutricionais, categorias alimentares, dicas de receitas e localização física.

A solução segue a abordagem SaaS, sem exigir instalação de aplicativo, e uma arquitetura Headless, separando apresentação, backend e fonte de dados. Para fins didáticos, o Google Sheets é a fonte de dados em nuvem.

## 2. Objetivos
Desenvolver uma aplicação web acessível por QR Code que apresente informações detalhadas dos produtos, nichos alimentares e localização no supermercado. O projeto aplica Flask, gspread, Google Sheets, HTML, CSS, JavaScript, Jinja2, QR Codes, Git/GitHub e deploy.

## 3. Público-alvo e jornada
Público-alvo: consumidores de supermercado que desejam consultar informações dos produtos e encontrar sua localização na loja.
Jornada: produto físico → leitura do QR Code → URL dinâmica → consulta do produto → página de informações → mapa com corredor/prateleira destacados.

## 4. Regras de negócio
- Cada produto possui um ID numérico único.
- O ID recebido na rota `/produto/<id>` identifica o registro consultado.
- A página é única e preenchida dinamicamente com Jinja2.
- Produtos inexistentes devem apresentar resposta 404 amigável.
- O mapa destaca o corredor associado ao produto e informa sua prateleira.
- Dados podem ser alterados na planilha sem modificar o código, quando a integração Sheets estiver configurada.

## 5. Estrutura de dados
Campos: `id`, `nome`, `preco`, `descricao`, `categoria`, `nichos`, `informacoes_nutricionais`, `ingredientes`, `corredor`, `prateleira`, `imagem`, `receita`.

## 6. Arquitetura
QR Code → URL `/produto/<id>` → Flask → serviço de produtos → Google Sheets (ou CSV demonstrativo) → template Jinja2 → interface mobile.

## 7. Fases e evidências
### Fase 1 — Concepção, arquitetura e regras
Entregáveis preparados: nome e finalidade, público-alvo, jornada, regras, estrutura de dados, categorias, corredores/prateleiras e fluxo descrito neste documento. O grupo deve confirmar a planilha Google criada e anexar captura de tela.

### Fase 2 — Backend e integração
Entregáveis preparados: aplicação Flask, rota dinâmica, serviço de consulta, estrutura de pastas e dependências. A integração real depende da criação da planilha e credenciais pelo grupo.

### Fase 3 — Frontend e experiência
Entregáveis preparados: página responsiva Mobile-First, apresentação de dados do produto, nichos, informações nutricionais, ingredientes, receita e mapa modal com destaque de corredor/prateleira.

### Fase 4 — Teste de campo
Entregáveis preparados: script independente `gerar_qrcode.py` e roteiro abaixo. O grupo precisa imprimir/exibir os QR Codes e testar em smartphone na rede local ou URL publicada.

### Fase 5 — DevOps e deploy
Entregáveis preparados: `.gitignore`, `requirements.txt`, `Procfile`, `render.yaml` e instruções GitHub/Render. A criação das contas, push e deploy exigem ação do grupo.

## 8. Roteiro mínimo de testes
| Item | Procedimento | Resultado esperado | Status |
|---|---|---|---|
| QR Code | Ler código pela câmera | Abre a URL do produto correto | A executar |
| URL | Abrir `/produto/101` | Exibe o produto de ID 101 | A executar |
| Dados | Conferir nome, preço e nutrição | Informações correspondem à base | A executar |
| Mapa | Abrir localização | Corredor correto fica destacado | A executar |
| Responsividade | Abrir em smartphone | Conteúdo ajusta à tela | A executar |
| Produto inexistente | Abrir `/produto/99999` | Página 404 amigável | A executar |
| Integração | Alterar dado na planilha | Mudança aparece na aplicação | A executar |

## 9. Limitações e próximos passos
O CSV contém dados fictícios para demonstração. Os valores nutricionais não foram inventados: a interface orienta consultar a embalagem. As imagens dos produtos podem ser adicionadas preenchendo a coluna `imagem` com uma URL válida; até lá, a interface mostra uma inicial como marcador visual. A integração Google Sheets só será efetiva após configurar API, conta de serviço, compartilhamento e variáveis. O mapa é uma representação simplificada para demonstração acadêmica, não uma planta arquitetônica real. A publicação depende das contas e configurações do grupo.
