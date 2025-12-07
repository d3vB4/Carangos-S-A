# ✅ Atualização do Módulo Financeiro - Cálculos da Fábrica 24/7

## 🎯 Mudanças Implementadas

O módulo `financeiro.py` foi atualizado com as novas regras de cálculo de água e energia baseadas na operação contínua da fábrica.

---

## 📊 Novas Regras de Cálculo

### 💧 Água
- **Custo**: R$ 1,50 por hora por trabalhador
- **Operação**: 24 horas/dia (fábrica nunca desliga)
- **Fórmula**: `24h × 22 dias × qtd_funcionários × R$ 1,50`

### ⚡ Energia Elétrica

A fábrica opera 24h/dia com dois tipos de fornecimento:

#### 🔋 Gerador (8 horas/dia)
- **Custo**: R$ 1,60 por hora por trabalhador
- **Período**: 8 horas/dia
- **Fórmula**: `8h × 22 dias × qtd_funcionários × R$ 1,60`

#### 🔌 Rede Elétrica (16 horas/dia)
- **Custo**: R$ 2,40 por hora por trabalhador
- **Período**: 16 horas/dia
- **Fórmula**: `16h × 22 dias × qtd_funcionários × R$ 2,40`

---

## 🔧 Novas Funções Criadas

### 1. `calcular_custo_agua_fabrica(dias_trabalhados=22)`
Calcula o custo de água baseado na operação 24/7 da fábrica.

**Retorna**:
```python
{
    'tipo': 'Água',
    'custo_por_hora_trabalhador': 1.50,
    'horas_por_dia': 24,
    'dias_trabalhados': 22,
    'qtd_funcionarios': 5,
    'total_horas_fabrica': 528,  # 24h × 22 dias
    'custo_total': 3960.00  # 528h × 5 × R$ 1,50
}
```

### 2. `calcular_custo_luz_fabrica(dias_trabalhados=22)`
Calcula o custo de energia separando gerador e rede elétrica.

**Retorna**:
```python
{
    'tipo': 'Energia',
    'horas_gerador_dia': 8,
    'custo_gerador_hora': 1.60,
    'horas_rede_dia': 16,
    'custo_rede_hora': 2.40,
    'dias_trabalhados': 22,
    'qtd_funcionarios': 5,
    'custo_gerador': 1408.00,  # 8h × 22 × 5 × R$ 1,60
    'custo_rede': 4224.00,     # 16h × 22 × 5 × R$ 2,40
    'custo_total': 5632.00
}
```

### 3. `calcular_despesas_fabrica(dias_trabalhados=22)`
Calcula todas as despesas (água + energia).

### 4. `gerar_relatorio_fabrica(dias_trabalhados=22)`
Gera relatório detalhado formatado com todas as informações.

---

## 📋 Exemplo de Relatório Gerado

```
================================================================================
              RELATÓRIO DE CUSTOS DE UTILIDADES - FÁBRICA 24/7
================================================================================

📊 INFORMAÇÕES GERAIS
--------------------------------------------------------------------------------
Quantidade de funcionários: 5
Dias trabalhados no mês: 22
Operação da fábrica: 24 horas/dia (nunca desliga)
Total de horas da fábrica no mês: 528h

--------------------------------------------------------------------------------
💧 ÁGUA
--------------------------------------------------------------------------------
Custo por hora por trabalhador: R$ 1.50
Horas de operação por dia: 24h
Cálculo: 528h × 5 funcionários × R$ 1.50

💰 CUSTO TOTAL DE ÁGUA: R$ 3960.00

--------------------------------------------------------------------------------
⚡ ENERGIA ELÉTRICA
--------------------------------------------------------------------------------

🔋 Período com GERADOR (8h/dia):
   Custo por hora por trabalhador: R$ 1.60
   Cálculo: 8h × 22 dias × 5 funcionários × R$ 1.60
   Subtotal Gerador: R$ 1408.00

🔌 Período com REDE ELÉTRICA (16h/dia):
   Custo por hora por trabalhador: R$ 2.40
   Cálculo: 16h × 22 dias × 5 funcionários × R$ 2.40
   Subtotal Rede: R$ 4224.00

💰 CUSTO TOTAL DE ENERGIA: R$ 5632.00

================================================================================
📊 RESUMO TOTAL - DESPESAS MENSAIS
================================================================================
Água:                    R$      3960.00
Energia (Gerador):       R$      1408.00
Energia (Rede):          R$      4224.00
Energia (Total):         R$      5632.00
--------------------------------------------------------------------------------
TOTAL UTILIDADES:        R$      9592.00
================================================================================
```

---

## 🧮 Exemplo de Cálculo (5 Funcionários)

### Água
- 24h/dia × 22 dias = 528 horas/mês
- 528h × 5 funcionários × R$ 1,50 = **R$ 3.960,00**

### Energia - Gerador
- 8h/dia × 22 dias = 176 horas/mês
- 176h × 5 funcionários × R$ 1,60 = **R$ 1.408,00**

### Energia - Rede
- 16h/dia × 22 dias = 352 horas/mês
- 352h × 5 funcionários × R$ 2,40 = **R$ 4.224,00**

### Total Energia
- R$ 1.408,00 + R$ 4.224,00 = **R$ 5.632,00**

### **TOTAL GERAL**
- R$ 3.960,00 + R$ 5.632,00 = **R$ 9.592,00/mês**

---

## 🚀 Como Usar

### Via Código Python
```python
from modules.financeiro import gerar_relatorio_fabrica

# Gerar relatório com 22 dias trabalhados (padrão)
gerar_relatorio_fabrica()

# Ou especificar dias diferentes
gerar_relatorio_fabrica(dias_trabalhados=20)
```

### Via Main.py
```bash
python main.py
# Menu → 3. Módulo Financeiro → 3. Calcular Custos de Água e Luz
```

---

## ✅ Compatibilidade

As funções antigas foram mantidas para compatibilidade:
- `calcular_custo_agua()` → chama `calcular_custo_agua_fabrica()`
- `calcular_custo_luz()` → chama `calcular_custo_luz_fabrica()`

**Recomendação**: Use as novas funções `*_fabrica()` para cálculos precisos!

---

## 📁 Arquivos Modificados

- ✅ `modules/financeiro.py` - Novas funções de cálculo implementadas
- ✅ Testado e funcionando corretamente

**Sistema atualizado e pronto para uso! 🎉**
