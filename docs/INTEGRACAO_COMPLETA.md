# ✅ Integração Completa: Financeiro.py + Main.py

## 📋 Resumo das Alterações

O módulo `financeiro.py` foi atualizado para funcionar perfeitamente com a `main.py`, mantendo TODAS as funcionalidades anteriores e adicionando compatibilidade total.

---

## 🔧 Funções Adicionadas ao Financeiro.py

### 1. **Funções para Main.py (Compatibilidade)**

#### `cadastrar_despesas_fixas()`
- Solicita entrada manual de: Água, Luz, Salários, Impostos
- Salva em `despesas.json`
- Retorna o total de despesas fixas

#### `calcular_custo_producao(despesas_fixas, custo_insumos_total)`
- Calcula: Custo Total = Despesas Fixas + Insumos

#### `calcular_custo_por_carro(custo_total_producao, qtd_carros_produzidos)`
- Calcula: Custo Unitário = Custo Total / Quantidade de Carros

#### `calcular_preco_venda(custo_unitario)`
- Calcula: Preço de Venda = Custo Unitário × 1.5 (50% de lucro)

### 2. **Funções de Cálculo de Utilidades (Nova Funcionalidade)**

#### `calcular_custo_agua(custo_por_hora, horas_extras_mes=10)`
- Calcula custo de água baseado em horas trabalhadas
- Usa dados de funcionários do RH

#### `calcular_custo_luz(custo_por_hora, horas_extras_mes=10)`
- Calcula custo de luz baseado em horas trabalhadas
- Usa dados de funcionários do RH

#### `gerar_relatorio_utilidades(custo_agua_hora, custo_luz_hora, horas_extras_mes=10)`
- Gera relatório completo e formatado
- Mostra detalhamento por funcionário e totais

#### `cadastrar_custos_utilidades()`
- Interface interativa para entrada de custos
- Gera relatório automaticamente

---

## 📊 Menu Financeiro Atualizado

```
MÓDULO FINANCEIRO
==================
1. Gerenciar Despesas Fixas
2. Ver Relatório Financeiro
3. Calcular Custos de Água e Luz  ← NOVO!
0. Voltar
```

### Opção 1: Gerenciar Despesas Fixas
- Cadastra: Água, Luz, Salários, Impostos (valores fixos)
- Salva em `despesas.json`

### Opção 2: Ver Relatório Financeiro
- Mostra custo total de produção
- Calcula custo por carro
- Sugere preço de venda

### Opção 3: Calcular Custos de Água e Luz ⭐ NOVO
- Calcula água e luz baseado em **horas trabalhadas**
- Integra com dados de funcionários do RH
- Considera:
  - 8h/dia × 22 dias = 176h normais
  - 8-10h extras por mês
  - Total por funcionário: ~186h/mês

---

## 🔄 Fluxo de Trabalho Completo

### 1. Cadastrar Funcionários (Módulo RH)
```python
# No menu RH
1. Cadastrar Funcionário
   - Nome, CPF, RG, etc.
   - Cargo e valor/hora
```

### 2. Calcular Custos de Utilidades (Módulo Financeiro - Opção 3)
```python
# No menu Financeiro > Opção 3
Custo de água por hora: 0.50
Custo de luz por hora: 1.20
Horas extras/mês: 10

# Resultado:
- 5 funcionários × 186h = 930h totais
- Água: 930h × R$ 0.50 = R$ 465.00
- Luz: 930h × R$ 1.20 = R$ 1,116.00
- TOTAL: R$ 1,581.00
```

### 3. Gerenciar Despesas Fixas (Opção 1)
```python
# Valores fixos mensais
Água: R$ 500.00
Luz: R$ 1200.00
Salários: R$ 15000.00
Impostos: R$ 3000.00
```

### 4. Ver Relatório Completo (Opção 2)
```python
# Combina tudo:
- Despesas fixas
- Custo de insumos (do estoque)
- Produção (do operacional)
- Calcula preço de venda
```

---

## 💡 Diferença Entre as Opções

### Opção 1 vs Opção 3 (Água e Luz)

| Aspecto | Opção 1 (Despesas Fixas) | Opção 3 (Custos por Horas) |
|---------|-------------------------|---------------------------|
| **Tipo** | Valor fixo mensal | Calculado dinamicamente |
| **Base** | Entrada manual | Horas trabalhadas |
| **Depende de** | Nada | Funcionários cadastrados |
| **Uso** | Custo total da empresa | Custo proporcional ao uso |

**Recomendação**: Use a **Opção 3** para cálculos mais precisos baseados em horas reais de trabalho!

---

## ✅ Compatibilidade Total

- ✅ Todas as funções antigas da main.py funcionam
- ✅ Nova funcionalidade de cálculo por horas adicionada
- ✅ Integração perfeita com módulo RH
- ✅ Sem quebra de código existente

---

## 🧪 Como Testar

### Teste Rápido
```bash
# 1. Cadastrar funcionários
python modules/rh.py

# 2. Testar módulo financeiro
python modules/financeiro.py

# 3. Testar integração completa
python teste_integracao.py
```

### Teste via Main.py
```bash
python main.py
# Login necessário
# Ir em: 3. Módulo Financeiro > 3. Calcular Custos de Água e Luz
```

---

## 📝 Arquivos Modificados

1. ✅ `modules/financeiro.py` - Funções adicionadas
2. ✅ `main.py` - Menu atualizado com opção 3
3. ✅ `modules/rh.py` - Restaurado e funcionando

---

## 🎯 Resultado Final

O sistema agora possui:
- **Cálculo tradicional**: Despesas fixas manuais
- **Cálculo inteligente**: Custos baseados em horas trabalhadas
- **Integração total**: RH ↔ Financeiro
- **Compatibilidade**: 100% com código existente
