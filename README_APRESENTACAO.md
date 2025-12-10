# 🎓 Guia de Apresentação - Sistema Carangos S/A

## 📋 Opções de Apresentação

Você tem **3 formas** de apresentar o sistema em sala de aula:

---

## 1️⃣ Apresentação Unificada (Recomendado para Iniciantes)

**Arquivo:** `apresentacao_completa.py`

### ✨ Características:
- ✅ Apresentação **controlada manualmente**
- ✅ Pausa entre cada módulo (pressione ENTER)
- ✅ Tabelas e gráficos visuais
- ✅ 100% em português
- ✅ Não requer interação com o sistema

### 🚀 Como Executar:
```bash
python apresentacao_completa.py
```

### 📊 Fluxo:
1. Cabeçalho do sistema
2. **Módulo 1:** Gestão de Estoque (pressione ENTER)
3. **Módulo 2:** Controle de Produção (pressione ENTER)
4. **Módulo 3:** Gestão Financeira (pressione ENTER)
5. **Módulo 4:** Recursos Humanos (pressione ENTER)
6. Dashboard Executivo Final

**⏱️ Duração:** ~5-10 minutos (controlado por você)

---

## 2️⃣ Apresentação Automatizada do Main.py

**Arquivo:** `apresentacao_automatizada.py`

### ✨ Características:
- ✅ Navega **automaticamente** pelo `main.py`
- ✅ Demonstra todos os módulos em ação
- ✅ Usa `pyautogui` para simular digitação
- ✅ Mostra o sistema real funcionando

### 🚀 Como Executar:
```bash
python apresentacao_automatizada.py
```

### ⚠️ IMPORTANTE:
1. **Não mova o mouse** durante a apresentação
2. A janela do `main.py` deve estar **visível**
3. Aguarde 5 segundos para posicionar as janelas
4. Clique na janela do main.py quando solicitado

### 📊 Fluxo:
1. Inicia o `main.py` automaticamente
2. Navega pelo menu Operacional
3. Navega pelo menu de Estoque
4. Navega pelo menu Financeiro
5. Navega pelo menu de RH
6. Encerra o sistema

**⏱️ Duração:** ~3-5 minutos (automático)

---

## 3️⃣ Teste de Integração Completo

**Arquivo:** `tests/test_integracao_completa.py`

### ✨ Características:
- ✅ Demonstra o **fluxo completo** do sistema
- ✅ Cadastra produtos, registra produção, calcula finanças e RH
- ✅ Mostra dados reais sendo processados
- ✅ Ideal para demonstração técnica

### 🚀 Como Executar:
```bash
python tests/test_integracao_completa.py
```

### 📊 O que faz:
1. **Cadastra 4 produtos** no estoque (R$ 1.980.500,00)
2. **Registra produção semanal** (491 carros)
3. **Calcula indicadores financeiros** (Lucro: R$ 1.852,51)
4. **Gerencia 4 funcionários** (Folha: R$ 9.350,00)
5. Exibe **Dashboard Final**

**⏱️ Duração:** ~2-3 minutos (automático)

---

## 4️⃣ Testes Unitários (Para Validação)

**Arquivo:** `tests/test_robot.py`

### ✨ Características:
- ✅ Testa **todos os módulos** individualmente
- ✅ Valida **100% das funcionalidades**
- ✅ Mostra taxa de sucesso
- ✅ Interface visual com Rich

### 🚀 Como Executar:
```bash
python tests/test_robot.py
```

### 📊 Resultado:
```
📊 Resultados dos Testes Unitários
┌──────────────┬─────────────┐
│ Módulo       │ Status      │
├──────────────┼─────────────┤
│ IMPORTS      │ ✅ APROVADO │
│ DATA_MANAGER │ ✅ APROVADO │
│ OPERACIONAL  │ ✅ APROVADO │
│ ESTOQUE      │ ✅ APROVADO │
│ FINANCEIRO   │ ✅ APROVADO │
│ RH           │ ✅ APROVADO │
└──────────────┴─────────────┘

Taxa de Sucesso: 100.0%
```

**⏱️ Duração:** ~30 segundos

---

## 📌 Recomendações por Cenário

### 🎓 Apresentação em Sala de Aula (Primeira Vez)
**Use:** `apresentacao_completa.py`
- Você controla o ritmo
- Pode explicar cada módulo
- Sem riscos de erro

### 🚀 Demonstração Rápida e Impactante
**Use:** `apresentacao_automatizada.py`
- Mostra o sistema real funcionando
- Impressiona com automação
- Demonstra integração completa

### 🔬 Validação Técnica
**Use:** `tests/test_robot.py` + `tests/test_integracao_completa.py`
- Prova que tudo funciona
- Mostra qualidade do código
- Demonstra testes automatizados

### 💼 Apresentação para Cliente/Professor
**Use:** `apresentacao_completa.py` → `tests/test_integracao_completa.py`
1. Mostre a apresentação visual
2. Execute o teste de integração
3. Mostre os testes unitários passando

---

## 🎯 Dicas para uma Boa Apresentação

### ✅ Antes de Apresentar:
1. **Teste tudo** antes da apresentação
2. **Feche outros programas** para evitar distrações
3. **Aumente o zoom** do terminal (Ctrl + +)
4. **Prepare um backup** (grave um vídeo da apresentação)

### ✅ Durante a Apresentação:
1. **Explique o contexto** antes de cada módulo
2. **Destaque os números** importantes
3. **Mostre a integração** entre módulos
4. **Responda perguntas** ao final de cada seção

### ✅ Ordem Sugerida:
1. Introdução ao projeto
2. `apresentacao_completa.py` (explicando cada módulo)
3. `tests/test_integracao_completa.py` (mostrando dados reais)
4. `tests/test_robot.py` (validando qualidade)
5. Conclusão e perguntas

---

## 🆘 Solução de Problemas

### Problema: "ModuleNotFoundError"
**Solução:** Instale as dependências
```bash
pip install -r requirements.txt
```

### Problema: Apresentação automatizada não funciona
**Solução:** 
1. Verifique se `pyautogui` está instalado
2. Certifique-se de que a janela do main.py está visível
3. Não mova o mouse durante a execução

### Problema: Testes falhando
**Solução:**
1. Verifique se os arquivos JSON existem em `data/`
2. Execute `python main.py` manualmente primeiro
3. Verifique se não há processos travados

---

## 📞 Suporte

Se tiver problemas, verifique:
1. ✅ Python 3.14 instalado
2. ✅ Todas as dependências instaladas (`pip install -r requirements.txt`)
3. ✅ Arquivos JSON em `data/` existem
4. ✅ Terminal com encoding UTF-8

---

**Boa apresentação! 🎓✨**
