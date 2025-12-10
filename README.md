# 🚗 Carangos S/A - Sistema Integrado de Gestão

Sistema completo de gestão para montadoras de veículos com interface Web e Terminal CLI.

## 📋 Índice

- [Sobre](#sobre)
- [Funcionalidades](#funcionalidades)
- [Instalação](#instalação)
- [Uso](#uso)
- [Testes Automatizados](#testes-automatizados)
- [Apresentação](#apresentação)
- [Módulos](#módulos)
- [Tecnologias](#tecnologias)

## 🎯 Sobre

O Carangos S/A é um sistema integrado de gestão desenvolvido especificamente para montadoras de veículos. Oferece controle completo de produção, estoque, finanças e recursos humanos através de uma interface web moderna e um terminal CLI poderoso.

## ✨ Funcionalidades

### 🏭 Módulo Operacional
- Registro de produção semanal por turno
- Cálculo de estatísticas e eficiência
- Relatórios de capacidade ideal
- Análise de performance por dia/turno

### 📦 Módulo de Estoque
- Cadastro e busca de produtos
- Gestão de fornecedores
- Cálculo de custos (atual, mensal, anual)
- Controle de quantidades

### 💰 Módulo Financeiro
- Gestão de despesas fixas
- Cálculo de custo de produção
- Indicadores financeiros (custo/carro, margem)
- Cálculo de impostos (CSLL)
- Relatórios de água, luz e salários

### 👥 Módulo de RH
- Cadastro de funcionários
- Gestão de setores e cargos
- Folha de pagamento automática
- Cálculo de benefícios e encargos

## 🚀 Instalação

### Pré-requisitos
- Python 3.12+
- pip

### Passos

1. Clone o repositório:
```bash
git clone <repository-url>
cd Carangos-S-A
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Configure o ambiente (opcional):
```bash
cp .env.example .env
# Edite .env conforme necessário
```

## 💻 Uso

### Interface Web

Execute o servidor Flask:
```bash
python app.py
```

Acesse no navegador: `http://localhost:5000`

### Terminal CLI

Execute o sistema em modo terminal:
```bash
python main.py
```

**Dica:** Pressione Enter sem digitar nada para entrar em modo teste (sem autenticação).

## 🧪 Testes Automatizados

O sistema inclui uma suite completa de testes automatizados com demonstração visual usando Rich, pytest-sugar e doitlive.

### Executar Todos os Testes

**Windows:**
```bash
demo.bat
```

**Linux/Mac:**
```bash
bash demo.sh
```

### Executar Testes Individuais

**Robô de Testes Automatizado:**
```bash
python tests/test_robot.py
```
- Testa todos os módulos automaticamente
- Output visual com Rich
- Relatório detalhado de resultados

**Demonstração ao Vivo:**
```bash
python tests/test_live_demo.py
```
- Demonstração interativa de todos os módulos
- Tabelas e gráficos com Rich
- Navegação passo a passo

**Master Test Runner:**
```bash
python tests/run_all_tests.py
```
- Executa toda a suite de testes
- Gera relatório HTML
- Mostra cobertura de código

### Testes com Pytest

**Todos os testes:**
```bash
pytest tests/ -v --cov=modules --cov-report=html
```

**Testes específicos:**
```bash
pytest tests/test_modules.py -v
pytest tests/test_operacional.py -v
pytest tests/test_terminal_flow.py -v
```

**Com pytest-sugar (output bonito):**
```bash
pytest tests/ --sugar
```

### Cobertura de Testes

Gerar relatório de cobertura:
```bash
pytest tests/ --cov=modules --cov-report=html --cov-report=term
```

O relatório HTML será gerado em `htmlcov/index.html`

## 🎬 Apresentação

O sistema inclui uma página de apresentação moderna e interativa.

### Acessar Apresentação

1. Abra o arquivo no navegador:
```
apresentacao/index_apresentacao.html
```

2. Ou através do servidor web:
```bash
python app.py
# Acesse: http://localhost:5000/apresentacao
```

### Conteúdo da Apresentação

- **Sobre o Produto:** Visão, missão e valores
- **Arquitetura do Sistema:** Tecnologias e design
- **Benefícios:** Por que escolher o Carangos S/A
- **Módulos:** Detalhes de cada módulo
- **Recursos:** Funcionalidades principais

## 📦 Módulos

### Estrutura de Diretórios

```
Carangos-S-A/
├── app.py                  # Aplicação Flask (Web)
├── main.py                 # Sistema CLI (Terminal)
├── modules/                # Módulos do sistema
│   ├── operacional.py
│   ├── estoque.py
│   ├── financeiro.py
│   ├── rh.py
│   └── data_manager.py
├── tests/                  # Testes automatizados
│   ├── test_robot.py       # Robô de testes
│   ├── test_live_demo.py   # Demo ao vivo
│   ├── run_all_tests.py    # Runner principal
│   └── ...
├── templates/              # Templates HTML
├── static/                 # Arquivos estáticos
├── apresentacao/           # Páginas de apresentação
│   └── index_apresentacao.html
├── data/                   # Dados JSON
├── docs/                   # Documentação
└── requirements.txt        # Dependências
```

## 🛠️ Tecnologias

### Backend
- **Python 3.12**
- **Flask 3.0** - Framework web
- **Werkzeug 3.0** - Utilitários WSGI
- **python-dotenv** - Variáveis de ambiente

### Frontend
- **HTML5/CSS3**
- **JavaScript (Vanilla)**
- **Font Awesome** - Ícones
- **Google Fonts** - Tipografia

### Testes
- **pytest** - Framework de testes
- **pytest-sugar** - Output bonito
- **pytest-cov** - Cobertura de código
- **Rich** - Terminal formatado
- **pyautogui** - Automação GUI
- **pynput** - Controle de teclado
- **doitlive** - Apresentações ao vivo

### Deploy
- **Docker** - Containerização
- **Gunicorn** - Servidor WSGI
- **Heroku/Northflank** - Cloud hosting

## 📊 Estrutura de Dados

Os dados são armazenados em arquivos JSON na pasta `data/`:

- `producao.json` - Dados de produção
- `produtos.json` - Estoque de produtos
- `despesas.json` - Despesas fixas
- `funcionarios.json` - Cadastro de funcionários
- `users.json` - Usuários do sistema

## 🔐 Autenticação

O sistema possui autenticação de usuários com:
- Login/senha criptografada (Werkzeug)
- Controle de acesso por roles
- Modo teste (sem autenticação)

## 🎨 Interface

### Web
- Design moderno com glassmorphism
- Tema escuro
- Responsivo (mobile-friendly)
- Animações suaves

### Terminal
- Interface CLI interativa
- Menus navegáveis
- Cores e formatação
- Feedback visual

## 📈 Relatórios

O sistema gera diversos relatórios:

1. **Produção Semanal**
   - Por dia e turno
   - Estatísticas e médias
   - Eficiência vs. capacidade ideal

2. **Custos de Estoque**
   - Custo total atual
   - Projeções mensais/anuais
   - Por produto e fornecedor

3. **Indicadores Financeiros**
   - Custo unitário
   - Preço de venda
   - Lucro bruto/líquido
   - Impostos (CSLL)

4. **Folha de Pagamento**
   - Salários base
   - Horas extras
   - Benefícios
   - Encargos

## 🤝 Contribuindo

1. Fork o projeto
2. Crie uma branch (`git checkout -b feature/nova-funcionalidade`)
3. Commit suas mudanças (`git commit -am 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/nova-funcionalidade`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está sob a licença GPL-3.0. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 👥 Autores

- **Equipe Carangos S/A**

## 🙏 Agradecimentos

- Flask community
- Python community
- Todos os contribuidores

---

**Carangos S/A** - Transformando a gestão de montadoras de veículos 🚗✨
