# 🎴 Templates Personalizados de Cards do Trello

## 📋 Índice
- [Como Usar Este Template](#como-usar-este-template)
- [Card 1: Data Manager](#card-1-data-manager)
- [Card 2: Estoque](#card-2-estoque)
- [Card 3: Financeiro](#card-3-financeiro)
- [Card 4: Operacional](#card-4-operacional)
- [Card 5: RH](#card-5-rh)
- [Configuração de Labels](#configuração-de-labels)
- [Estrutura de Listas](#estrutura-de-listas)

---

## 📖 Como Usar Este Template

### Passo a Passo:
1. **Copie** o conteúdo de cada card abaixo
2. **Cole** no Trello ao criar um novo card
3. **Personalize** as datas e responsáveis
4. **Marque** os checkboxes conforme o progresso
5. **Anexe** os arquivos correspondentes

### Formato de Cada Card:
- **Título**: Nome do módulo
- **Descrição**: Objetivo e contexto
- **Checklist**: Tarefas detalhadas
- **Labels**: Categorização
- **Membros**: Responsáveis
- **Data**: Prazo de entrega
- **Anexos**: Arquivos relacionados

---

## 🎴 Card 1: Data Manager

### 📌 Título
```
📦 Módulo Data Manager - Gerenciamento de Dados JSON
```

### 📝 Descrição
```markdown
## 🎯 Objetivo
Implementar módulo centralizado para gerenciamento de dados em arquivos JSON, fornecendo interface consistente para todos os outros módulos.

## 📊 Escopo
- Carregamento de dados de arquivos JSON
- Salvamento de dados em arquivos JSON
- Tratamento robusto de erros de I/O
- Configuração flexível de diretório de dados

## 🔗 Dependências
- Nenhuma (módulo base)

## 📁 Arquivo
`modules/data_manager.py` (37 linhas)

## 🔢 Estatísticas
- **Funções:** 2
- **Complexidade:** Baixa
- **Prioridade:** Alta (módulo base)
```

### ✅ Checklist
```markdown
## Implementação
- [ ] Criar arquivo `modules/data_manager.py`
- [ ] Implementar função `load_data(filename)`
  - [ ] Construir caminho completo com DATA_DIR
  - [ ] Retornar lista vazia se arquivo não existe
  - [ ] Tratar JSONDecodeError
  - [ ] Tratar IOError
  - [ ] Usar encoding UTF-8
- [ ] Implementar função `save_data(filename, data)`
  - [ ] Salvar com indentação de 4 espaços
  - [ ] Usar ensure_ascii=False
  - [ ] Retornar booleano de sucesso
  - [ ] Imprimir erro em caso de falha
- [ ] Configurar variável DATA_DIR
  - [ ] Ler de variável de ambiente
  - [ ] Fallback para diretório padrão
  - [ ] Criar diretório se não existir

## Documentação
- [ ] Adicionar docstring em `load_data()`
  - [ ] Descrever parâmetros
  - [ ] Descrever retorno
  - [ ] Documentar comportamento de erro
- [ ] Adicionar docstring em `save_data()`
  - [ ] Descrever parâmetros
  - [ ] Descrever retorno
  - [ ] Documentar side effects
- [ ] Adicionar comentários no código
- [ ] Documentar variável DATA_DIR

## Testes
- [ ] Testar carregamento de arquivo existente
- [ ] Testar carregamento de arquivo inexistente
- [ ] Testar carregamento de JSON inválido
- [ ] Testar salvamento com sucesso
- [ ] Testar salvamento com erro de I/O
- [ ] Testar criação automática de diretório

## Integração
- [ ] Validar uso em módulo estoque
- [ ] Validar uso em módulo financeiro
- [ ] Validar uso em módulo operacional
- [ ] Validar uso em módulo RH
```

### 🏷️ Labels
```
backend, core, data-management, high-priority
```

### 👥 Membros
```
@desenvolvedor-backend
```

### 📅 Datas
```
Início: [DATA]
Prazo: [DATA]
```

### 📎 Anexos
```
- modules/data_manager.py
```

---

## 🎴 Card 2: Estoque

### 📌 Título
```
📊 Módulo Estoque - Gestão de Produtos e Custos
```

### 📝 Descrição
```markdown
## 🎯 Objetivo
Implementar sistema completo de gerenciamento de estoque com cadastro de produtos, validação de duplicidade, pesquisa e cálculo de custos com projeções.

## 📊 Escopo
- Cadastro de produtos com validação
- Verificação de duplicidade por código
- Pesquisa inteligente (nome ou código)
- Cálculo de custos (atual, mensal, anual)
- Listagem formatada de produtos

## 🔗 Dependências
- `data_manager.py` (load_data, save_data)

## 📁 Arquivo
`modules/estoque.py` (114 linhas)

## 🔢 Estatísticas
- **Funções:** 5
- **Complexidade:** Média
- **Prioridade:** Alta

## 📐 Fórmulas
- **Custo Total Atual:** Σ(quantidade × valor_compra)
- **Projeção Mensal:** Custo Atual × 4
- **Projeção Anual:** Custo Atual × 52
```

### ✅ Checklist
```markdown
## Implementação
- [ ] Criar arquivo `modules/estoque.py`
- [ ] Importar data_manager
- [ ] Inicializar lista global de produtos
- [ ] Implementar `cadastrar_produto(codigo, nome, data_fab, fornecedor, quantidade, valor_compra)`
  - [ ] Recarregar dados para garantir atualização
  - [ ] Verificar duplicidade antes de inserir
  - [ ] Criar dicionário de produto
  - [ ] Adicionar à lista
  - [ ] Salvar via data_manager
  - [ ] Retornar booleano de sucesso
- [ ] Implementar `verificar_duplicidade(codigo)`
  - [ ] Iterar sobre produtos
  - [ ] Comparar códigos
  - [ ] Retornar True se encontrar
- [ ] Implementar `pesquisar_produto(termo)`
  - [ ] Converter termo para lowercase
  - [ ] Buscar em código e nome
  - [ ] Retornar lista de resultados
- [ ] Implementar `calcular_custos(lista_produtos=None)`
  - [ ] Usar lista global se não fornecida
  - [ ] Calcular custo total atual
  - [ ] Calcular projeção mensal (×4)
  - [ ] Calcular projeção anual (×52)
  - [ ] Retornar dicionário com valores
- [ ] Implementar `listar_produtos()`
  - [ ] Iterar sobre produtos
  - [ ] Formatar saída
  - [ ] Imprimir informações principais

## Estrutura de Dados
- [ ] Definir estrutura do produto:
  ```python
  {
    "codigo": int,
    "nome": str,
    "data_fabricacao": str,
    "fornecedor": str,
    "quantidade": int,
    "valor_compra": float
  }
  ```

## Documentação
- [ ] Docstring em `cadastrar_produto()`
- [ ] Docstring em `verificar_duplicidade()`
- [ ] Docstring em `pesquisar_produto()`
- [ ] Docstring em `calcular_custos()`
- [ ] Docstring em `listar_produtos()`
- [ ] Documentar fórmulas de cálculo
- [ ] Comentar lógica de validação

## Testes
- [ ] Testar cadastro com sucesso
- [ ] Testar cadastro duplicado (deve falhar)
- [ ] Testar pesquisa por código
- [ ] Testar pesquisa por nome
- [ ] Testar pesquisa case-insensitive
- [ ] Testar cálculo de custos com produtos
- [ ] Testar cálculo de custos sem produtos
- [ ] Testar listagem

## Integração
- [ ] Validar integração com data_manager
- [ ] Validar uso no módulo financeiro
- [ ] Testar persistência de dados
```

### 🏷️ Labels
```
backend, estoque, business-logic, high-priority
```

### 👥 Membros
```
@desenvolvedor-backend
```

### 📅 Datas
```
Início: [DATA]
Prazo: [DATA]
```

### 📎 Anexos
```
- modules/estoque.py
- data/produtos.json (gerado)
```

---

## 🎴 Card 3: Financeiro

### 📌 Título
```
💰 Módulo Financeiro - Custos e Precificação
```

### 📝 Descrição
```markdown
## 🎯 Objetivo
Implementar sistema de gestão financeira com cadastro de despesas fixas, cálculo de custos de produção e formação de preço de venda com margem de lucro.

## 📊 Escopo
- Cadastro de despesas fixas (água, luz, salários, impostos)
- Cálculo de custo total de produção
- Cálculo de custo unitário por produto
- Cálculo de preço de venda com margem

## 🔗 Dependências
- `data_manager.py` (save_data)
- `estoque.py` (custos de insumos)

## 📁 Arquivo
`modules/financeiro.py` (80 linhas)

## 🔢 Estatísticas
- **Funções:** 4
- **Complexidade:** Média
- **Prioridade:** Alta

## 📐 Fórmulas
- **Custo Total:** Despesas Fixas + Custo Insumos
- **Custo Unitário:** Custo Total ÷ Quantidade Produzida
- **Preço Venda:** Custo Unitário × 1.50 (margem 50%)
```

### ✅ Checklist
```markdown
## Implementação
- [ ] Criar arquivo `modules/financeiro.py`
- [ ] Importar data_manager
- [ ] Implementar `cadastrar_despesas_fixas()`
  - [ ] Solicitar input de água
  - [ ] Solicitar input de luz
  - [ ] Solicitar input de salários
  - [ ] Solicitar input de impostos
  - [ ] Validar entrada numérica (try/except)
  - [ ] Criar lista de despesas
  - [ ] Salvar via data_manager
  - [ ] Calcular e retornar total
- [ ] Implementar `calcular_custo_producao(despesas_fixas, custo_insumos_total)`
  - [ ] Somar despesas fixas e variáveis
  - [ ] Retornar custo total
- [ ] Implementar `calcular_custo_por_carro(custo_total_producao, qtd_carros_produzidos)`
  - [ ] Validar quantidade > 0
  - [ ] Dividir custo total pela quantidade
  - [ ] Retornar 0.0 se quantidade inválida
- [ ] Implementar `calcular_preco_venda(custo_unitario)`
  - [ ] Definir margem de lucro (50%)
  - [ ] Calcular preço com margem
  - [ ] Retornar preço de venda

## Estrutura de Dados
- [ ] Definir estrutura de despesa:
  ```python
  {
    "tipo": str,  # "Agua", "Luz", "Salarios", "Impostos"
    "valor": float
  }
  ```

## Documentação
- [ ] Docstring em `cadastrar_despesas_fixas()`
- [ ] Docstring em `calcular_custo_producao()`
- [ ] Docstring em `calcular_custo_por_carro()`
- [ ] Docstring em `calcular_preco_venda()`
- [ ] Documentar fórmulas
- [ ] Documentar margem de lucro

## Testes
- [ ] Testar cadastro de despesas com valores válidos
- [ ] Testar cadastro com entrada inválida
- [ ] Testar cálculo de custo de produção
- [ ] Testar cálculo de custo unitário normal
- [ ] Testar cálculo com quantidade zero
- [ ] Testar cálculo de preço de venda
- [ ] Validar margem de 50%

## Integração
- [ ] Integrar com módulo estoque (custo insumos)
- [ ] Integrar com módulo operacional (quantidade produzida)
- [ ] Validar persistência de despesas
```

### 🏷️ Labels
```
backend, financeiro, business-logic, high-priority
```

### 👥 Membros
```
@desenvolvedor-backend
```

### 📅 Datas
```
Início: [DATA]
Prazo: [DATA]
```

### 📎 Anexos
```
- modules/financeiro.py
- data/despesas.json (gerado)
```

---

## 🎴 Card 4: Operacional

### 📌 Título
```
⚙️ Módulo Operacional - Controle de Produção
```

### 📝 Descrição
```markdown
## 🎯 Objetivo
Implementar sistema de controle operacional com cadastro de produção por turno, cálculo de estatísticas, simulações e relatórios comparativos com capacidade ideal.

## 📊 Escopo
- Cadastro de produção semanal (7 dias × 3 turnos)
- Cálculo de estatísticas (totais e médias)
- Simulação de produção mensal e anual
- Cálculo de capacidade ideal
- Geração de relatórios comparativos

## 🔗 Dependências
- `data_manager.py` (load_data, save_data)

## 📁 Arquivo
`modules/operacional.py` (157 linhas)

## 🔢 Estatísticas
- **Funções:** 5
- **Complexidade:** Alta
- **Prioridade:** Alta

## 📐 Fórmulas
- **Total Semanal:** Σ(todas produções)
- **Média Diária:** Total Semanal ÷ 7
- **Média por Turno:** Total do Turno ÷ 7
- **Projeção Mensal:** Total Semanal × 4
- **Projeção Anual:** Total Semanal × 52
- **Capacidade Ideal:** 750/mês (3 turnos) = 187.5/semana
```

### ✅ Checklist
```markdown
## Implementação
- [ ] Criar arquivo `modules/operacional.py`
- [ ] Importar data_manager
- [ ] Implementar `cadastrar_producao()`
  - [ ] Definir dias da semana
  - [ ] Definir turnos (Manhã, Tarde, Noite)
  - [ ] Loop por 7 dias
  - [ ] Loop por 3 turnos em cada dia
  - [ ] Solicitar input com validação
  - [ ] Validar número não-negativo
  - [ ] Criar estrutura de dados aninhada
  - [ ] Converter para formato flat
  - [ ] Carregar dados existentes
  - [ ] Append novos dados
  - [ ] Salvar via data_manager
  - [ ] Retornar dados estruturados
- [ ] Implementar `calcular_estatisticas(dados)`
  - [ ] Calcular total semanal
  - [ ] Calcular total por turno
  - [ ] Calcular média diária (÷7)
  - [ ] Calcular média por turno (÷7)
  - [ ] Retornar dicionário com estatísticas
- [ ] Implementar `simular_producao(total_semanal)`
  - [ ] Calcular projeção mensal (×4)
  - [ ] Calcular projeção anual (×52)
  - [ ] Retornar tupla (mensal, anual)
- [ ] Implementar `calcular_capacidade_ideal()`
  - [ ] Definir capacidade mensal: 750
  - [ ] Calcular semanal: 750÷4
  - [ ] Calcular anual: 750×12
  - [ ] Retornar dicionário
- [ ] Implementar `gerar_relatorio(dados, estatisticas, ideal)`
  - [ ] Imprimir cabeçalho formatado
  - [ ] Exibir totais e médias
  - [ ] Exibir médias por turno
  - [ ] Chamar simular_producao
  - [ ] Exibir simulações
  - [ ] Comparar real vs ideal
  - [ ] Calcular diferenças (gaps)

## Estruturas de Dados
- [ ] Estrutura aninhada (interna):
  ```python
  {
    "dia": str,
    "turnos": {
      "Manhã": int,
      "Tarde": int,
      "Noite": int
    }
  }
  ```
- [ ] Estrutura flat (JSON):
  ```python
  {
    "dia": str,
    "turno": str,
    "quantidade": int
  }
  ```

## Documentação
- [ ] Docstring em `cadastrar_producao()`
- [ ] Docstring em `calcular_estatisticas()`
- [ ] Docstring em `simular_producao()`
- [ ] Docstring em `calcular_capacidade_ideal()`
- [ ] Docstring em `gerar_relatorio()`
- [ ] Documentar ambas estruturas de dados
- [ ] Documentar premissas de capacidade
- [ ] Documentar fórmulas

## Testes
- [ ] Testar cadastro de produção completo
- [ ] Testar validação de entrada
- [ ] Testar cálculo de estatísticas
- [ ] Validar totais e médias
- [ ] Testar simulação de produção
- [ ] Testar cálculo de capacidade ideal
- [ ] Testar geração de relatório
- [ ] Validar conversão de formato

## Integração
- [ ] Validar integração com data_manager
- [ ] Validar uso no módulo financeiro
- [ ] Testar persistência de dados
- [ ] Validar compatibilidade com app web
```

### 🏷️ Labels
```
backend, operacional, reporting, high-priority
```

### 👥 Membros
```
@desenvolvedor-backend
```

### 📅 Datas
```
Início: [DATA]
Prazo: [DATA]
```

### 📎 Anexos
```
- modules/operacional.py
- data/producao.json (gerado)
```

---

## 🎴 Card 5: RH

### 📌 Título
```
👥 Módulo RH - Recursos Humanos e Folha de Pagamento
```

### 📝 Descrição
```markdown
## 🎯 Objetivo
Implementar sistema completo de Recursos Humanos com cadastro de funcionários e cálculo detalhado de folha de pagamento incluindo horas extras e IRPF progressivo.

## 📊 Escopo
- Cadastro completo de funcionários
- Cálculo de salário bruto
- Cálculo de horas extras com regras por cargo
- Cálculo de IRPF com tabela progressiva 2024
- Cálculo de salário líquido
- Geração de folha de pagamento ordenada

## 🔗 Dependências
- `data_manager.py` (load_data, save_data)

## 📁 Arquivo
`modules/rh.py` (114 linhas)

## 🔢 Estatísticas
- **Funções:** 6
- **Complexidade:** Alta
- **Prioridade:** Alta

## 📐 Fórmulas
- **Salário Bruto:** Horas × Valor/Hora
- **Horas Extras:** Horas Extra × (Valor/Hora × 1.5)
- **IRPF:** Tabela progressiva 2024
- **Salário Líquido:** Bruto - IRPF

## 📊 Tabela IRPF 2024
| Faixa Salarial | Alíquota | Dedução |
|----------------|----------|---------|
| Até R$ 2.259,20 | Isento | - |
| R$ 2.259,21 - R$ 2.826,65 | 7,5% | R$ 169,44 |
| R$ 2.826,66 - R$ 3.751,05 | 15% | R$ 381,44 |
| R$ 3.751,06 - R$ 4.664,68 | 22,5% | R$ 662,77 |
| Acima de R$ 4.664,68 | 27,5% | R$ 896,00 |
```

### ✅ Checklist
```markdown
## Implementação
- [ ] Criar arquivo `modules/rh.py`
- [ ] Importar data_manager
- [ ] Inicializar lista global de funcionários
- [ ] Implementar `cadastrar_funcionario(nome, cpf, rg, endereco, telefone, qtd_filhos, cargo, valor_hora)`
  - [ ] Recarregar dados
  - [ ] Criar dicionário de funcionário
  - [ ] Adicionar à lista
  - [ ] Salvar via data_manager
  - [ ] Imprimir confirmação
- [ ] Implementar `calcular_salario_bruto(horas_trabalhadas, valor_hora)`
  - [ ] Multiplicar horas por valor
  - [ ] Retornar salário bruto
- [ ] Implementar `calcular_horas_extras(horas_extras, valor_hora, cargo)`
  - [ ] Verificar se cargo é Gerente ou Diretor
  - [ ] Retornar 0.0 se for
  - [ ] Calcular com adicional de 50%
  - [ ] Retornar valor das extras
- [ ] Implementar `calcular_irpf(salario_base)`
  - [ ] Implementar faixa 1: até 2259.20 → 0%
  - [ ] Implementar faixa 2: até 2826.65 → 7.5% - 169.44
  - [ ] Implementar faixa 3: até 3751.05 → 15% - 381.44
  - [ ] Implementar faixa 4: até 4664.68 → 22.5% - 662.77
  - [ ] Implementar faixa 5: acima → 27.5% - 896.00
  - [ ] Retornar IRPF calculado
- [ ] Implementar `calcular_liquido(salario_bruto, irpf)`
  - [ ] Subtrair IRPF do bruto
  - [ ] Retornar líquido
- [ ] Implementar `gerar_folha_pagamento()`
  - [ ] Ordenar funcionários por nome
  - [ ] Loop por funcionários
  - [ ] Simular horas trabalhadas (160)
  - [ ] Simular horas extras (10)
  - [ ] Calcular salário bruto
  - [ ] Calcular horas extras
  - [ ] Somar bruto + extras
  - [ ] Calcular IRPF
  - [ ] Calcular líquido
  - [ ] Determinar se paga IR
  - [ ] Imprimir folha formatada

## Estrutura de Dados
- [ ] Definir estrutura de funcionário:
  ```python
  {
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

## Documentação
- [ ] Docstring em `cadastrar_funcionario()`
- [ ] Docstring em `calcular_salario_bruto()`
- [ ] Docstring em `calcular_horas_extras()`
  - [ ] Documentar regra de Gerente/Diretor
  - [ ] Documentar adicional de 50%
- [ ] Docstring em `calcular_irpf()`
  - [ ] Documentar tabela completa
  - [ ] Incluir valores de 2024
- [ ] Docstring em `calcular_liquido()`
- [ ] Docstring em `gerar_folha_pagamento()`
- [ ] Comentar lógica de cálculo

## Testes
- [ ] Testar cadastro de funcionário
- [ ] Testar cálculo de salário bruto
- [ ] Testar horas extras para Operário (deve calcular)
- [ ] Testar horas extras para Gerente (deve retornar 0)
- [ ] Testar horas extras para Diretor (deve retornar 0)
- [ ] Testar IRPF faixa 1 (isento)
- [ ] Testar IRPF faixa 2 (7.5%)
- [ ] Testar IRPF faixa 3 (15%)
- [ ] Testar IRPF faixa 4 (22.5%)
- [ ] Testar IRPF faixa 5 (27.5%)
- [ ] Testar cálculo de líquido
- [ ] Testar geração de folha completa
- [ ] Validar ordenação alfabética

## Integração
- [ ] Validar integração com data_manager
- [ ] Testar persistência de funcionários
- [ ] Validar cálculos com valores reais
```

### 🏷️ Labels
```
backend, rh, payroll, high-priority
```

### 👥 Membros
```
@desenvolvedor-backend
```

### 📅 Datas
```
Início: [DATA]
Prazo: [DATA]
```

### 📎 Anexos
```
- modules/rh.py
- data/funcionarios.json (gerado)
```

---

## 🏷️ Configuração de Labels

### Labels Sugeridas para o Board:

#### Por Categoria
- 🔵 `backend` - Desenvolvimento backend
- 🟢 `frontend` - Desenvolvimento frontend
- 🟡 `core` - Funcionalidades core/base
- 🟠 `business-logic` - Lógica de negócio

#### Por Módulo
- 📦 `data-management` - Gerenciamento de dados
- 📊 `estoque` - Módulo de estoque
- 💰 `financeiro` - Módulo financeiro
- ⚙️ `operacional` - Módulo operacional
- 👥 `rh` - Módulo RH
- 💼 `payroll` - Folha de pagamento
- 📈 `reporting` - Relatórios

#### Por Prioridade
- 🔴 `high-priority` - Alta prioridade
- 🟡 `medium-priority` - Média prioridade
- 🟢 `low-priority` - Baixa prioridade

#### Por Status
- ⏳ `in-progress` - Em andamento
- ✅ `ready-for-review` - Pronto para revisão
- 🐛 `bug` - Bug/Correção
- ✨ `enhancement` - Melhoria

---

## 📋 Estrutura de Listas

### Listas Sugeridas:

1. **📥 Backlog**
   - Cards ainda não iniciados
   - Ideias futuras

2. **📝 To Do**
   - Cards prontos para iniciar
   - Prioridades definidas

3. **🔄 In Progress**
   - Cards em desenvolvimento ativo
   - Limite WIP: 3-5 cards

4. **👀 Code Review**
   - Cards aguardando revisão
   - Pull requests abertos

5. **🧪 Testing**
   - Cards em fase de testes
   - Validação de qualidade

6. **✅ Done**
   - Cards concluídos
   - Merged e deployed

---

## 📊 Métricas de Acompanhamento

### Por Card, Rastrear:
- ⏱️ **Tempo estimado:** [X horas]
- ⏰ **Tempo real:** [Y horas]
- 📈 **Progresso:** [X/Y tarefas]
- 🐛 **Bugs encontrados:** [N]
- ✅ **Testes passando:** [X/Y]

### Exemplo de Comentário de Progresso:
```markdown
## 📊 Update [DATA]

### ✅ Concluído
- Implementação da função load_data
- Testes unitários básicos

### 🔄 Em Andamento
- Implementação da função save_data
- Tratamento de erros

### ⏭️ Próximos Passos
- Finalizar documentação
- Testes de integração

### ⚠️ Bloqueios
- Nenhum
```

---

## 🎨 Customização Visual

### Cores de Capa Sugeridas:
- **Data Manager:** 🟦 Azul (módulo base)
- **Estoque:** 🟩 Verde (gestão)
- **Financeiro:** 🟨 Amarelo (dinheiro)
- **Operacional:** 🟧 Laranja (produção)
- **RH:** 🟪 Roxo (pessoas)

### Emojis por Tipo de Tarefa:
- 🔨 Implementação
- 📝 Documentação
- 🧪 Testes
- 🔗 Integração
- 🐛 Bug fix
- ✨ Enhancement

---

**Template criado em:** 2025-12-04
**Versão:** 1.0
**Compatível com:** Trello, Jira, Azure DevOps
