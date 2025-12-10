# 📋 Documentação dos Módulos - Sistema Carangos S/A

## 📑 Índice
- [Visão Geral](#visão-geral)
- [Estrutura de Arquivos](#estrutura-de-arquivos)
- [Documentação por Módulo](#documentação-por-módulo)
- [Organização para Trello](#organização-para-trello)
- [Estrutura de Commits](#estrutura-de-commits)
- [Template de Pull Request](#template-de-pull-request)

---

## 🎯 Visão Geral

Este documento apresenta a documentação completa dos módulos do Sistema de Automação Carangos S/A, organizada para facilitar a criação de cards no Trello e estruturação de commits para pull request.

**Módulos Implementados:**
- `data_manager.py` - Gerenciamento de dados em JSON
- `estoque.py` - Gestão de produtos e custos de estoque
- `financeiro.py` - Cálculos financeiros e precificação
- `operacional.py` - Controle de produção e estatísticas
- `rh.py` - Recursos humanos e folha de pagamento

---

## 📂 Estrutura de Arquivos

```
modules/
├── __pycache__/
├── data_manager.py      (37 linhas, 1.1 KB)
├── estoque.py          (114 linhas, 3.9 KB)
├── financeiro.py        (80 linhas, 2.9 KB)
├── operacional.py      (157 linhas, 6.3 KB)
└── rh.py               (114 linhas, 4.0 KB)
```

---

## 📚 Documentação por Módulo

### 1️⃣ data_manager.py

**Descrição:** Módulo responsável pelo gerenciamento centralizado de dados em arquivos JSON.

**Responsabilidades:**
- Carregamento de dados de arquivos JSON
- Salvamento de dados em arquivos JSON
- Gerenciamento do diretório de dados
- Tratamento de erros de I/O

**Funções Implementadas:**

#### `load_data(filename)`
```python
def load_data(filename):
    """
    Carrega dados de um arquivo JSON.
    Retorna uma lista vazia se o arquivo não existir ou for inválido.
    
    Args:
        filename (str): Nome do arquivo JSON a ser carregado
        
    Returns:
        list: Dados carregados do arquivo ou lista vazia em caso de erro
        
    Raises:
        Nenhuma exceção é propagada - erros são tratados internamente
    """
```

**Comportamento:**
- Constrói o caminho completo usando `DATA_DIR`
- Retorna lista vazia se arquivo não existe
- Trata erros de decodificação JSON
- Usa encoding UTF-8 para suporte a caracteres especiais

#### `save_data(filename, data)`
```python
def save_data(filename, data):
    """
    Salva dados em um arquivo JSON.
    
    Args:
        filename (str): Nome do arquivo JSON para salvar
        data (list/dict): Dados a serem salvos no formato JSON
        
    Returns:
        bool: True se salvou com sucesso, False em caso de erro
        
    Raises:
        Nenhuma exceção é propagada - erros são tratados internamente
    """
```

**Comportamento:**
- Salva com indentação de 4 espaços para legibilidade
- Usa `ensure_ascii=False` para preservar caracteres UTF-8
- Imprime mensagem de erro em caso de falha
- Retorna booleano indicando sucesso/falha

**Variáveis Globais:**
- `DATA_DIR`: Diretório configurável via variável de ambiente para armazenamento de dados

---

### 2️⃣ estoque.py

**Descrição:** Módulo de gerenciamento de estoque de produtos com controle de duplicidade e cálculo de custos.

**Responsabilidades:**
- Cadastro de produtos com validação
- Verificação de duplicidade por código
- Pesquisa de produtos
- Cálculo de custos (semanal, mensal, anual)
- Listagem de produtos

**Funções Implementadas:**

#### `cadastrar_produto(codigo, nome, data_fab, fornecedor, quantidade, valor_compra)`
```python
def cadastrar_produto(codigo, nome, data_fab, fornecedor, quantidade, valor_compra):
    """
    Cadastra um novo produto na lista de produtos.
    Verifica duplicidade de código antes de inserir.
    
    Args:
        codigo (int): Código único do produto
        nome (str): Nome do produto
        data_fab (str): Data de fabricação (formato: DD/MM/YYYY)
        fornecedor (str): Nome do fornecedor
        quantidade (int): Quantidade em estoque
        valor_compra (float): Valor unitário de compra
        
    Returns:
        bool: True se cadastrou com sucesso, False se código duplicado
        
    Side Effects:
        - Atualiza a lista global 'produtos'
        - Salva dados em 'produtos.json'
        - Imprime mensagens de sucesso ou erro
    """
```

#### `verificar_duplicidade(codigo)`
```python
def verificar_duplicidade(codigo):
    """
    Verifica se já existe um produto com o código informado.
    Retorna True se existir, False caso contrário.
    
    Args:
        codigo (int): Código do produto a verificar
        
    Returns:
        bool: True se código já existe, False caso contrário
    """
```

#### `pesquisar_produto(termo)`
```python
def pesquisar_produto(termo):
    """
    Pesquisa produto por nome ou código.
    Retorna uma lista de produtos encontrados.
    
    Args:
        termo (str/int): Termo de busca (nome ou código)
        
    Returns:
        list: Lista de dicionários com produtos encontrados
        
    Comportamento:
        - Busca case-insensitive
        - Busca parcial em nome e código
    """
```

#### `calcular_custos(lista_produtos=None)`
```python
def calcular_custos(lista_produtos=None):
    """
    Calcula o custo total do estoque (semanal, mensal, anual).
    Aceita uma lista opcional de produtos. Se não fornecida, usa a global.
    
    Args:
        lista_produtos (list, optional): Lista de produtos para cálculo
        
    Returns:
        dict: {
            'total_atual': float,      # Custo total atual (semanal)
            'mensal_projetado': float, # Projeção mensal (x4)
            'anual_projetado': float   # Projeção anual (x52)
        }
        
    Fórmulas:
        - Total Atual = Σ(quantidade × valor_compra)
        - Mensal = Total Atual × 4
        - Anual = Total Atual × 52
    """
```

#### `listar_produtos()`
```python
def listar_produtos():
    """
    Lista todos os produtos cadastrados.
    
    Side Effects:
        Imprime no console a lista formatada de produtos
    """
```

**Estrutura de Dados:**
```python
produto = {
    "codigo": int,
    "nome": str,
    "data_fabricacao": str,
    "fornecedor": str,
    "quantidade": int,
    "valor_compra": float
}
```

---

### 3️⃣ financeiro.py

**Descrição:** Módulo de gestão financeira com cálculo de custos de produção e precificação.

**Responsabilidades:**
- Cadastro de despesas fixas
- Cálculo de custo total de produção
- Cálculo de custo unitário por produto
- Cálculo de preço de venda com margem de lucro

**Funções Implementadas:**

#### `cadastrar_despesas_fixas()`
```python
def cadastrar_despesas_fixas():
    """
    Solicita a entrada manual de despesas fixas.
    Retorna o valor total das despesas.
    
    Returns:
        float: Soma total das despesas fixas
        
    Despesas Coletadas:
        - Água
        - Luz
        - Salários
        - Impostos
        
    Side Effects:
        - Salva dados em 'despesas.json'
        - Solicita input do usuário
        - Trata erros de entrada inválida
    """
```

#### `calcular_custo_producao(despesas_fixas, custo_insumos_total)`
```python
def calcular_custo_producao(despesas_fixas, custo_insumos_total):
    """
    Calcula o custo total de produção (Fixas + Variáveis/Insumos).
    
    Args:
        despesas_fixas (float): Total de despesas fixas
        custo_insumos_total (float): Total de custos variáveis/insumos
        
    Returns:
        float: Custo total de produção
        
    Fórmula:
        Custo Total = Despesas Fixas + Custo Insumos
    """
```

#### `calcular_custo_por_carro(custo_total_producao, qtd_carros_produzidos)`
```python
def calcular_custo_por_carro(custo_total_producao, qtd_carros_produzidos):
    """
    Calcula o custo unitário por carro.
    
    Args:
        custo_total_producao (float): Custo total de produção
        qtd_carros_produzidos (int): Quantidade de carros produzidos
        
    Returns:
        float: Custo unitário por carro (0.0 se quantidade <= 0)
        
    Fórmula:
        Custo Unitário = Custo Total / Quantidade Produzida
    """
```

#### `calcular_preco_venda(custo_unitario)`
```python
def calcular_preco_venda(custo_unitario):
    """
    Calcula o preço de venda com 50% de lucro sobre o custo unitário.
    
    Args:
        custo_unitario (float): Custo unitário do produto
        
    Returns:
        float: Preço de venda sugerido
        
    Fórmula:
        Preço Venda = Custo Unitário × 1.50 (margem de 50%)
    """
```

**Estrutura de Dados:**
```python
despesa = {
    "tipo": str,    # "Agua", "Luz", "Salarios", "Impostos"
    "valor": float
}
```

---

### 4️⃣ operacional.py

**Descrição:** Módulo de controle operacional com gestão de produção diária e análise estatística.

**Responsabilidades:**
- Cadastro de produção por turno e dia
- Cálculo de estatísticas de produção
- Simulação de produção mensal/anual
- Comparação com capacidade ideal
- Geração de relatórios operacionais

**Funções Implementadas:**

#### `cadastrar_producao()`
```python
def cadastrar_producao():
    """
    Cadastra a produção diária de cada turno por 7 dias.
    Retorna uma lista de dicionários com os dados.
    
    Returns:
        list: Lista com dados de produção semanal estruturados por dia e turno
        
    Estrutura de Entrada:
        - 7 dias da semana
        - 3 turnos por dia (Manhã, Tarde, Noite)
        
    Side Effects:
        - Solicita input do usuário para cada turno
        - Valida entrada numérica
        - Converte dados para formato flat
        - Salva em 'producao.json'
        - Append aos dados existentes
    """
```

#### `calcular_estatisticas(dados)`
```python
def calcular_estatisticas(dados):
    """
    Calcula produção total semanal, média por dia e por turno.
    Retorna um dicionário com as estatísticas.
    
    Args:
        dados (list): Lista de dicionários com produção por dia/turno
        
    Returns:
        dict: {
            'total_semanal': int,
            'media_diaria': float,
            'media_por_turno': dict,  # {turno: média}
            'total_por_turno': dict   # {turno: total}
        }
        
    Cálculos:
        - Total Semanal = Σ todas produções
        - Média Diária = Total Semanal / 7
        - Média por Turno = Total do Turno / 7
    """
```

#### `simular_producao(total_semanal)`
```python
def simular_producao(total_semanal):
    """
    Simula a produção mensal e anual com base na produção semanal.
    
    Args:
        total_semanal (int): Total produzido na semana
        
    Returns:
        tuple: (mensal, anual)
        
    Fórmulas:
        - Mensal = Total Semanal × 4
        - Anual = Total Semanal × 52
    """
```

#### `calcular_capacidade_ideal()`
```python
def calcular_capacidade_ideal():
    """
    Calcula a produção ideal com 100% da capacidade.
    Capacidade padrão: 500 unidades/mês com 2 turnos.
    Terceiro turno aumenta 50%.
    
    Returns:
        dict: {
            'semanal': float,  # 187.5 unidades
            'mensal': float,   # 750 unidades
            'anual': float     # 9000 unidades
        }
        
    Premissas:
        - Capacidade base (2 turnos): 500/mês
        - Com 3 turnos: 750/mês (+50%)
    """
```

#### `gerar_relatorio(dados, estatisticas, ideal)`
```python
def gerar_relatorio(dados, estatisticas, ideal):
    """
    Emite um relatório comparativo entre produção real e ideal.
    
    Args:
        dados (list): Dados de produção
        estatisticas (dict): Estatísticas calculadas
        ideal (dict): Capacidade ideal
        
    Side Effects:
        Imprime relatório formatado com:
        - Produção total e médias
        - Simulações mensal/anual
        - Comparativo com capacidade ideal
        - Diferenças (gaps) de produção
    """
```

**Estrutura de Dados:**
```python
# Formato estruturado (interno)
producao_dia = {
    "dia": str,  # "Segunda", "Terça", etc.
    "turnos": {
        "Manhã": int,
        "Tarde": int,
        "Noite": int
    }
}

# Formato flat (JSON persistido)
producao_registro = {
    "dia": str,
    "turno": str,
    "quantidade": int
}
```

---

### 5️⃣ rh.py

**Descrição:** Módulo de Recursos Humanos com gestão de funcionários e cálculo de folha de pagamento.

**Responsabilidades:**
- Cadastro de funcionários
- Cálculo de salário bruto
- Cálculo de horas extras
- Cálculo de IRPF progressivo
- Geração de folha de pagamento

**Funções Implementadas:**

#### `cadastrar_funcionario(nome, cpf, rg, endereco, telefone, qtd_filhos, cargo, valor_hora)`
```python
def cadastrar_funcionario(nome, cpf, rg, endereco, telefone, qtd_filhos, cargo, valor_hora):
    """
    Cadastra um funcionário na lista.
    
    Args:
        nome (str): Nome completo do funcionário
        cpf (str): CPF do funcionário
        rg (str): RG do funcionário
        endereco (str): Endereço residencial
        telefone (str): Telefone de contato
        qtd_filhos (int): Quantidade de filhos
        cargo (str): Cargo/função
        valor_hora (float): Valor da hora trabalhada
        
    Side Effects:
        - Atualiza lista global 'funcionarios'
        - Salva em 'funcionarios.json'
        - Imprime mensagem de confirmação
    """
```

#### `calcular_salario_bruto(horas_trabalhadas, valor_hora)`
```python
def calcular_salario_bruto(horas_trabalhadas, valor_hora):
    """
    Calcula salário bruto base.
    
    Args:
        horas_trabalhadas (int): Total de horas trabalhadas
        valor_hora (float): Valor por hora
        
    Returns:
        float: Salário bruto
        
    Fórmula:
        Salário Bruto = Horas Trabalhadas × Valor Hora
    """
```

#### `calcular_horas_extras(horas_extras, valor_hora, cargo)`
```python
def calcular_horas_extras(horas_extras, valor_hora, cargo):
    """
    Calcula valor das horas extras.
    Gerentes e Diretores não recebem hora extra.
    
    Args:
        horas_extras (int): Quantidade de horas extras
        valor_hora (float): Valor da hora normal
        cargo (str): Cargo do funcionário
        
    Returns:
        float: Valor total das horas extras (0.0 para Gerente/Diretor)
        
    Regras:
        - Gerentes e Diretores: não recebem hora extra
        - Demais cargos: adicional de 50% (CLT)
        
    Fórmula:
        Valor Extra = Horas Extras × (Valor Hora × 1.5)
    """
```

#### `calcular_irpf(salario_base)`
```python
def calcular_irpf(salario_base):
    """
    Calcula o IRPF com base em tabela progressiva simplificada (2024).
    
    Args:
        salario_base (float): Salário base para cálculo
        
    Returns:
        float: Valor do IRPF a ser retido
        
    Tabela Progressiva:
        - Até R$ 2.259,20: Isento
        - R$ 2.259,21 a R$ 2.826,65: 7,5% - R$ 169,44
        - R$ 2.826,66 a R$ 3.751,05: 15% - R$ 381,44
        - R$ 3.751,06 a R$ 4.664,68: 22,5% - R$ 662,77
        - Acima de R$ 4.664,68: 27,5% - R$ 896,00
    """
```

#### `calcular_liquido(salario_bruto, irpf)`
```python
def calcular_liquido(salario_bruto, irpf):
    """
    Calcula salário líquido (Bruto - IRPF).
    Ignorando INSS para simplificação conforme enunciado foca em IRPF.
    
    Args:
        salario_bruto (float): Salário bruto total
        irpf (float): Valor do IRPF calculado
        
    Returns:
        float: Salário líquido
        
    Fórmula:
        Líquido = Bruto - IRPF
    """
```

#### `gerar_folha_pagamento()`
```python
def gerar_folha_pagamento():
    """
    Gera relatório final com salários líquidos e IRPF.
    
    Side Effects:
        Imprime folha de pagamento com:
        - Funcionários ordenados por nome
        - Salário bruto (base + horas extras)
        - IRPF calculado
        - Indicação se paga IR
        - Salário líquido
        
    Premissas de Simulação:
        - 160 horas mensais padrão
        - 10 horas extras de exemplo
    """
```

**Estrutura de Dados:**
```python
funcionario = {
    "nome": str,
    "cpf": str,
    "rg": str,
    "endereco": str,
    "telefone": str,
    "qtd_filhos": int,
    "cargo": str,
    "valor_hora": float
}
```

---

## 🎴 Organização para Trello

### Card 1: 📦 Módulo Data Manager
**Lista:** Em Desenvolvimento / Concluído

**Descrição:**
Implementação do módulo de gerenciamento centralizado de dados em JSON.

**Checklist:**
- [x] Criar função `load_data()` para carregar arquivos JSON
- [x] Criar função `save_data()` para salvar arquivos JSON
- [x] Implementar tratamento de erros de I/O
- [x] Configurar diretório de dados via variável de ambiente
- [x] Adicionar suporte a encoding UTF-8
- [x] Documentar todas as funções

**Labels:** `backend`, `core`, `data-management`

**Anexos:** `data_manager.py`

---

### Card 2: 📊 Módulo Estoque
**Lista:** Em Desenvolvimento / Concluído

**Descrição:**
Sistema de gerenciamento de estoque com cadastro de produtos, validação e cálculo de custos.

**Checklist:**
- [x] Implementar `cadastrar_produto()` com validação
- [x] Criar `verificar_duplicidade()` para evitar códigos repetidos
- [x] Desenvolver `pesquisar_produto()` com busca parcial
- [x] Implementar `calcular_custos()` com projeções
- [x] Criar `listar_produtos()` para visualização
- [x] Integrar com data_manager para persistência
- [x] Documentar estrutura de dados e funções

**Labels:** `backend`, `estoque`, `business-logic`

**Anexos:** `estoque.py`

---

### Card 3: 💰 Módulo Financeiro
**Lista:** Em Desenvolvimento / Concluído

**Descrição:**
Gestão financeira com cálculo de custos de produção e formação de preço de venda.

**Checklist:**
- [x] Implementar `cadastrar_despesas_fixas()` com input validado
- [x] Criar `calcular_custo_producao()` para custo total
- [x] Desenvolver `calcular_custo_por_carro()` para custo unitário
- [x] Implementar `calcular_preco_venda()` com margem de 50%
- [x] Integrar com módulo de estoque para custos de insumos
- [x] Documentar fórmulas e regras de negócio

**Labels:** `backend`, `financeiro`, `business-logic`

**Anexos:** `financeiro.py`

---

### Card 4: ⚙️ Módulo Operacional
**Lista:** Em Desenvolvimento / Concluído

**Descrição:**
Controle operacional de produção com cadastro por turno, estatísticas e relatórios comparativos.

**Checklist:**
- [x] Implementar `cadastrar_producao()` para 7 dias e 3 turnos
- [x] Criar `calcular_estatisticas()` com médias e totais
- [x] Desenvolver `simular_producao()` para projeções
- [x] Implementar `calcular_capacidade_ideal()` com regras de turnos
- [x] Criar `gerar_relatorio()` com comparativo real vs ideal
- [x] Converter dados estruturados para formato flat JSON
- [x] Documentar estruturas de dados e cálculos

**Labels:** `backend`, `operacional`, `reporting`

**Anexos:** `operacional.py`

---

### Card 5: 👥 Módulo RH
**Lista:** Em Desenvolvimento / Concluído

**Descrição:**
Recursos Humanos com cadastro de funcionários e cálculo completo de folha de pagamento.

**Checklist:**
- [x] Implementar `cadastrar_funcionario()` com dados completos
- [x] Criar `calcular_salario_bruto()` para salário base
- [x] Desenvolver `calcular_horas_extras()` com regras por cargo
- [x] Implementar `calcular_irpf()` com tabela progressiva 2024
- [x] Criar `calcular_liquido()` para salário final
- [x] Desenvolver `gerar_folha_pagamento()` com relatório ordenado
- [x] Documentar tabela de IRPF e regras de horas extras

**Labels:** `backend`, `rh`, `payroll`

---

## 🔄 Estrutura de Commits

### Formato de Commit
```
<tipo>(<escopo>): <descrição curta>

<descrição detalhada opcional>

<referências opcionais>
```

### Commits Sugeridos

#### Módulo Data Manager
```bash
# Commit 1
feat(data-manager): adicionar função load_data para carregar JSON

- Implementa carregamento de arquivos JSON
- Retorna lista vazia em caso de erro
- Adiciona suporte a encoding UTF-8

# Commit 2
feat(data-manager): adicionar função save_data para persistência

- Implementa salvamento de dados em JSON
- Adiciona formatação com indentação
- Trata erros de I/O com retorno booleano

# Commit 3
feat(data-manager): configurar diretório de dados via env

- Adiciona variável DATA_DIR configurável
- Cria diretório automaticamente se não existir
- Permite customização para deploy em nuvem

# Commit 4
docs(data-manager): documentar funções e comportamentos

- Adiciona docstrings completas
- Documenta parâmetros e retornos
- Inclui exemplos de uso
```

#### Módulo Estoque
```bash
# Commit 1
feat(estoque): implementar cadastro de produtos

- Adiciona função cadastrar_produto
- Implementa validação de duplicidade
- Integra com data_manager para persistência

# Commit 2
feat(estoque): adicionar verificação de duplicidade

- Implementa verificar_duplicidade por código
- Previne cadastros duplicados
- Retorna booleano para validação

# Commit 3
feat(estoque): implementar pesquisa de produtos

- Adiciona busca por nome ou código
- Implementa busca case-insensitive
- Retorna lista de produtos encontrados

# Commit 4
feat(estoque): adicionar cálculo de custos

- Implementa cálculo de custo total
- Adiciona projeções mensal e anual
- Aceita lista customizada de produtos

# Commit 5
feat(estoque): adicionar listagem de produtos

- Implementa função listar_produtos
- Formata saída com informações principais
- Exibe código, nome, quantidade e valor

# Commit 6
docs(estoque): documentar funções e estruturas

- Adiciona docstrings completas
- Documenta estrutura de dados
- Inclui fórmulas de cálculo
```

#### Módulo Financeiro
```bash
# Commit 1
feat(financeiro): implementar cadastro de despesas fixas

- Adiciona função cadastrar_despesas_fixas
- Coleta água, luz, salários e impostos
- Valida entrada numérica do usuário

# Commit 2
feat(financeiro): adicionar cálculo de custo de produção

- Implementa calcular_custo_producao
- Soma despesas fixas e variáveis
- Retorna custo total

# Commit 3
feat(financeiro): implementar cálculo de custo unitário

- Adiciona calcular_custo_por_carro
- Divide custo total pela quantidade
- Trata divisão por zero

# Commit 4
feat(financeiro): adicionar cálculo de preço de venda

- Implementa calcular_preco_venda
- Aplica margem de lucro de 50%
- Retorna preço sugerido

# Commit 5
docs(financeiro): documentar funções e fórmulas

- Adiciona docstrings completas
- Documenta fórmulas de cálculo
- Inclui estrutura de dados
```

#### Módulo Operacional
```bash
# Commit 1
feat(operacional): implementar cadastro de produção semanal

- Adiciona função cadastrar_producao
- Coleta dados de 7 dias e 3 turnos
- Valida entrada numérica

# Commit 2
feat(operacional): converter dados para formato flat

- Transforma estrutura aninhada em flat
- Compatibiliza com formato do app web
- Append aos dados existentes

# Commit 3
feat(operacional): adicionar cálculo de estatísticas

- Implementa calcular_estatisticas
- Calcula totais e médias
- Agrupa por turno

# Commit 4
feat(operacional): implementar simulação de produção

- Adiciona simular_producao
- Projeta produção mensal (x4)
- Projeta produção anual (x52)

# Commit 5
feat(operacional): calcular capacidade ideal

- Implementa calcular_capacidade_ideal
- Define capacidade base: 500/mês (2 turnos)
- Adiciona 50% para terceiro turno

# Commit 6
feat(operacional): gerar relatório comparativo

- Implementa gerar_relatorio
- Compara produção real vs ideal
- Calcula gaps de produção

# Commit 7
docs(operacional): documentar funções e estruturas

- Adiciona docstrings completas
- Documenta ambas estruturas de dados
- Inclui fórmulas e premissas
```

#### Módulo RH
```bash
# Commit 1
feat(rh): implementar cadastro de funcionários

- Adiciona função cadastrar_funcionario
- Coleta dados pessoais e profissionais
- Persiste em funcionarios.json

# Commit 2
feat(rh): adicionar cálculo de salário bruto

- Implementa calcular_salario_bruto
- Multiplica horas por valor/hora
- Retorna salário base

# Commit 3
feat(rh): implementar cálculo de horas extras

- Adiciona calcular_horas_extras
- Aplica adicional de 50% (CLT)
- Exclui Gerentes e Diretores

# Commit 4
feat(rh): adicionar cálculo de IRPF progressivo

- Implementa calcular_irpf
- Usa tabela progressiva 2024
- Aplica alíquotas e deduções

# Commit 5
feat(rh): implementar cálculo de salário líquido

- Adiciona calcular_liquido
- Subtrai IRPF do bruto
- Retorna valor final

# Commit 6
feat(rh): gerar folha de pagamento completa

- Implementa gerar_folha_pagamento
- Ordena funcionários por nome
- Exibe bruto, IRPF e líquido

# Commit 7
docs(rh): documentar funções e tabelas

- Adiciona docstrings completas
- Documenta tabela de IRPF
- Inclui regras de horas extras
```

---

## 📝 Template de Pull Request

```markdown
# 🚀 [MÓDULOS] Implementação Completa dos Módulos do Sistema Carangos S/A

## 📋 Descrição

Esta PR implementa os 5 módulos principais do Sistema de Automação Carangos S/A:
- **Data Manager**: Gerenciamento centralizado de dados JSON
- **Estoque**: Gestão de produtos e custos
- **Financeiro**: Cálculos financeiros e precificação
- **Operacional**: Controle de produção e estatísticas
- **RH**: Recursos humanos e folha de pagamento

## 🎯 Objetivos

- [x] Implementar módulo de gerenciamento de dados (data_manager.py)
- [x] Implementar módulo de estoque (estoque.py)
- [x] Implementar módulo financeiro (financeiro.py)
- [x] Implementar módulo operacional (operacional.py)
- [x] Implementar módulo de RH (rh.py)
- [x] Documentar todas as funções profissionalmente
- [x] Adicionar tratamento de erros
- [x] Garantir integração entre módulos

## 📊 Arquivos Modificados/Adicionados

### Novos Arquivos
- `modules/data_manager.py` - 37 linhas
- `modules/estoque.py` - 114 linhas
- `modules/financeiro.py` - 80 linhas
- `modules/operacional.py` - 157 linhas
- `modules/rh.py` - 114 linhas

### Total
- **5 arquivos** adicionados
- **502 linhas** de código
- **25 funções** implementadas

## 🔍 Detalhamento por Módulo

### 1. Data Manager (`data_manager.py`)
**Funções:** 2
- `load_data(filename)` - Carrega dados de JSON
- `save_data(filename, data)` - Salva dados em JSON

**Características:**
- Diretório configurável via variável de ambiente
- Tratamento robusto de erros
- Suporte a UTF-8

### 2. Estoque (`estoque.py`)
**Funções:** 5
- `cadastrar_produto()` - Cadastro com validação
- `verificar_duplicidade()` - Previne duplicatas
- `pesquisar_produto()` - Busca inteligente
- `calcular_custos()` - Projeções financeiras
- `listar_produtos()` - Visualização

**Características:**
- Validação de duplicidade por código
- Busca case-insensitive
- Cálculos de projeção (semanal, mensal, anual)

### 3. Financeiro (`financeiro.py`)
**Funções:** 4
- `cadastrar_despesas_fixas()` - Coleta de despesas
- `calcular_custo_producao()` - Custo total
- `calcular_custo_por_carro()` - Custo unitário
- `calcular_preco_venda()` - Precificação com margem

**Características:**
- Validação de entrada numérica
- Margem de lucro configurável (50%)
- Integração com módulo de estoque

### 4. Operacional (`operacional.py`)
**Funções:** 5
- `cadastrar_producao()` - Registro de produção
- `calcular_estatisticas()` - Análise estatística
- `simular_producao()` - Projeções
- `calcular_capacidade_ideal()` - Benchmarking
- `gerar_relatorio()` - Relatórios comparativos

**Características:**
- Controle por turno (Manhã, Tarde, Noite)
- Estatísticas detalhadas
- Comparativo real vs ideal
- Conversão de formato para compatibilidade

### 5. RH (`rh.py`)
**Funções:** 6
- `cadastrar_funcionario()` - Cadastro completo
- `calcular_salario_bruto()` - Salário base
- `calcular_horas_extras()` - Horas extras com regras
- `calcular_irpf()` - IRPF progressivo
- `calcular_liquido()` - Salário final
- `gerar_folha_pagamento()` - Folha completa

**Características:**
- Tabela IRPF 2024 atualizada
- Regras diferenciadas por cargo
- Ordenação alfabética na folha
- Cálculo completo de proventos e descontos

## 🧪 Testes

Cada módulo possui seção `if __name__ == "__main__"` com:
- Dados de teste mockados
- Validação de funções principais
- Exemplos de uso

**Como testar:**
```bash
# Testar módulo individual
python -m modules.data_manager
python -m modules.estoque
python -m modules.financeiro
python -m modules.operacional
python -m modules.rh
```

## 📚 Documentação

- [x] Todas as funções possuem docstrings
- [x] Parâmetros documentados com tipos
- [x] Retornos documentados
- [x] Comportamentos e side effects descritos
- [x] Fórmulas e regras de negócio explicadas
- [x] Estruturas de dados documentadas

## ⚠️ Breaking Changes

Nenhuma breaking change. Todos os módulos são novos.

## 🔗 Dependências

- **Internas:** Módulos se integram via `data_manager`
- **Externas:** Apenas bibliotecas padrão Python (json, os)

## ✅ Checklist

- [x] Código segue padrões do projeto
- [x] Todas as funções estão documentadas
- [x] Tratamento de erros implementado
- [x] Testes manuais executados
- [x] Integração entre módulos validada
- [x] Encoding UTF-8 configurado
- [x] Variáveis de ambiente documentadas

## 👥 Revisores Sugeridos

@tech-lead @backend-team

## 📎 Referências

- Documentação completa: `MODULES_DOCUMENTATION.md`
- Estrutura de commits detalhada no documento
- Cards do Trello organizados por módulo

## 💬 Observações

Esta implementação estabelece a base do sistema de automação, com todos os módulos principais funcionando de forma integrada e documentada profissionalmente.

---

**Tipo:** Feature
**Prioridade:** Alta
**Estimativa:** 5 módulos × 2-3 horas = 10-15 horas
**Status:** ✅ Pronto para Review
```

---

## 📌 Notas Finais

### Padrões de Código
- **Encoding:** UTF-8 em todos os arquivos
- **Docstrings:** Formato Google Style
- **Nomenclatura:** snake_case para funções e variáveis
- **Idioma:** Português para nomes e comentários

### Boas Práticas Implementadas
✅ Separação de responsabilidades
✅ Funções com propósito único
✅ Tratamento de erros robusto
✅ Validação de entrada de dados
✅ Documentação completa
✅ Código testável
✅ Integração modular

### Próximos Passos Sugeridos
1. Implementar testes unitários automatizados
2. Adicionar validação de tipos com type hints
3. Criar interface CLI unificada
4. Implementar logging estruturado
5. Adicionar configuração via arquivo .env

---

**Documento gerado em:** 2025-12-04
**Versão:** 1.0
**Autor:** Sistema de Documentação Automática
