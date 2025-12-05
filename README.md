# Sistema de Gestão Integrada - Carangos S/A

Bem-vindo ao repositório do **Sistema de Gestão Integrada da Carangos S/A**. Este projeto é uma solução completa para o gerenciamento de uma fábrica de automóveis, integrando os setores Operacional, de Estoque, Financeiro e de Recursos Humanos.

O sistema foi desenvolvido em **Python** e oferece duas interfaces de uso: uma **Aplicação Web** moderna (Flask) e uma **Interface de Terminal** robusta.

## 🚀 Funcionalidades Principais

O sistema é dividido em 4 módulos principais, todos integrados e com persistência de dados em JSON:

### 1. 🏭 Módulo Operacional
*   **Registro de Produção**: Controle diário de produção por turno (Manhã, Tarde, Noite).
*   **Estatísticas**: Cálculo de médias, totais semanais e simulações mensais/anuais.
*   **Relatórios**: Comparativo visual entre Produção Real vs Capacidade Ideal.

### 2. 📦 Módulo de Estoque
*   **Gestão de Produtos**: Cadastro de peças e insumos com verificação de duplicidade.
*   **Busca Inteligente**: Pesquisa por código ou nome do produto.
*   **Análise de Custos**: Projeção de custos de estoque (Mensal/Anual).

### 3. 💰 Módulo Financeiro
*   **Despesas Fixas**: Gerenciamento de custos operacionais (Água, Luz, Salários, Impostos).
*   **Precificação**: Cálculo automático do **Custo de Produção** e sugestão de **Preço de Venda** com margem de lucro configurável.

### 4. 👥 Módulo de Recursos Humanos (RH)
*   **Gestão de Funcionários**: Cadastro completo com cargo e valor hora.
*   **Folha de Pagamento**: Cálculo automatizado de Salário Bruto, Horas Extras, Descontos de IRPF e Salário Líquido.

---

## 🔐 Segurança e Acesso (RBAC)

O sistema implementa um **Controle de Acesso Baseado em Funções (RBAC)** hierárquico, refletindo o organograma da empresa:

*   **Nível Global** (`presidente`, `conselho`, `admin`): Acesso total a todos os módulos e ao Dashboard Executivo.
*   **Diretoria Operacional**: Acesso aos módulos **Operacional** e **Estoque**.
*   **Diretoria Financeira**: Acesso exclusivo ao módulo **Financeiro**.
*   **Diretoria de RH**: Acesso exclusivo ao módulo de **RH**.
*   **Gerentes/Funcionários**: Acesso restrito às funções do seu departamento específico.

---

## 📂 Estrutura do Projeto

A arquitetura do projeto foi organizada para garantir modularidade e facilidade de manutenção:

```
Sistema Aut Carangos SA/
├── app.py                 # Aplicação Web (Flask)
├── main.py                # Aplicação Terminal (CLI)
├── modules/               # Lógica de Negócio (Core)
│   ├── data_manager.py    # Gerenciador de Persistência (JSON)
│   ├── operacional.py
│   ├── estoque.py
│   ├── financeiro.py
│   └── rh.py
├── data/                  # Banco de Dados (Arquivos JSON)
│   ├── users.json         # Usuários e Senhas (Hash)
│   ├── producao.json
│   ├── produtos.json
│   ├── despesas.json
│   └── funcionarios.json
├── scripts/               # Scripts Utilitários
│   └── seed_users.py      # Populador de Usuários Iniciais
├── tests/                 # Testes Automatizados
│   ├── test_app.py        # Testes da Web App
│   └── test_terminal_flow.py # Testes do Terminal (E2E)
├── templates/             # Templates HTML (Jinja2)
└── static/                # Arquivos Estáticos (CSS, Imagens)
```

---

## 📚 Documentação

O projeto possui documentação completa e organizada para facilitar o desenvolvimento e manutenção:

### 📖 Documentação dos Módulos
- **[README_MODULES.md](./README_MODULES.md)** - Resumo executivo da documentação dos módulos
- **[MODULES_DOCUMENTATION.md](./MODULES_DOCUMENTATION.md)** - Documentação técnica completa (22 funções documentadas)
- **[DOCUMENTATION_GUIDE.md](./DOCUMENTATION_GUIDE.md)** - Guia de uso de toda a documentação

### 🎴 Organização e Workflow
- **[TRELLO_CARD_TEMPLATE.md](./TRELLO_CARD_TEMPLATE.md)** - Templates de cards para Trello (5 cards prontos)
- **[PULL_REQUEST_TEMPLATE.md](./.github/PULL_REQUEST_TEMPLATE.md)** - Template padrão de Pull Request

### 🚀 Deploy
- **[DEPLOY.md](./DEPLOY.md)** - Guia completo de deploy em nuvem

**💡 Comece por aqui:** [README_MODULES.md](./README_MODULES.md) para ter uma visão geral rápida!

---

## 🛠️ Instalação e Configuração

### Pré-requisitos
*   Python 3.8 ou superior.

### Passo a Passo

1.  **Clone o repositório** (ou extraia os arquivos):
    ```bash
    cd "Sistema Aut Carangos SA"
    ```

2.  **Instale as dependências**:
    ```bash
    pip install -r requirements.txt
    ```
    
    Ou manualmente:
    ```bash
    pip install flask werkzeug python-dotenv
    ```

3.  **Inicialize o Banco de Dados de Usuários**:
    Execute o script para criar os usuários padrão e as estruturas de dados:
    ```bash
    python scripts/seed_users.py
    ```

---

## ☁️ Deploy na Nuvem

O sistema está pronto para deploy em plataformas cloud modernas. Suportamos:

*   **Render** - Deploy simples com plano gratuito
*   **Railway** - Deploy automático via Git
*   **Northflank** - Plataforma robusta com containers

### Deploy Rápido

1.  **Configure as variáveis de ambiente**:
    *   `SECRET_KEY`: Chave secreta (gere com `python -c "import secrets; print(secrets.token_hex(32))"`)
    *   `FLASK_ENV`: `production`

2.  **Configure volume persistente** para `/app/data` (para manter os dados JSON)

3.  **Faça deploy** seguindo o guia detalhado: **[DEPLOY.md](DEPLOY.md)**

### Teste Local com Docker

```bash
# Build e execute
docker-compose up --build

# Acesse http://localhost:5000
```

📖 **Guia Completo**: Veja [DEPLOY.md](DEPLOY.md) para instruções detalhadas de cada plataforma.

---

## 🖥️ Como Usar

### Opção 1: Aplicação Web (Recomendado)

Interface gráfica moderna, responsiva e com dashboards visuais.

1.  Inicie o servidor:
    ```bash
    python app.py
    ```
2.  Acesse no navegador: `http://127.0.0.1:5000`
3.  Faça login com as credenciais abaixo.

### Opção 2: Interface de Terminal

Interface rápida via linha de comando para operações diretas.

1.  Execute o menu principal:
    ```bash
    python main.py
    ```
2.  Navegue pelos menus numéricos.

---

## 🔑 Credenciais de Acesso

Para testes, utilize os seguintes usuários (Senha padrão: `123456`, exceto Admin/Presidente):

| Cargo | Usuário | Senha | Acesso |
| :--- | :--- | :--- | :--- |
| **Admin** | `admin` | `admin123` | Total |
| **Presidente** | `presidente` | `admin123` | Total |
| **Dir. Operacional** | `dir_operacional` | `123456` | Operacional, Estoque |
| **Dir. Financeiro** | `dir_financeira` | `123456` | Financeiro |
| **Dir. RH** | `dir_rh` | `123456` | RH |
| **Ger. Montagem** | `ger_montagem` | `123456` | Operacional |

---

## ✅ Testes Automatizados

O projeto conta com uma suíte de testes robusta para garantir a estabilidade.

Para rodar os testes do fluxo do terminal (incluindo cenários End-to-End):

```bash
python tests/test_terminal_flow.py
```

Para rodar os testes da aplicação web:

```bash
python tests/test_app.py
```

---

## 👨‍💻 Autor

Desenvolvido por **Antigravity** (Google DeepMind) em colaboração com **Alexandre Junior**.
Projeto focado em **Clean Code**, **Arquitetura Modular** e **Automação**.
