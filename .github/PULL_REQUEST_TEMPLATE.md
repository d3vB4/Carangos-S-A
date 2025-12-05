# 🚀 Pull Request

## 📋 Descrição

<!-- Descreva de forma clara e concisa o que esta PR faz -->

### 🎯 Objetivo
<!-- Qual problema esta PR resolve? Qual funcionalidade adiciona? -->

### 🔗 Issue/Card Relacionado
<!-- Link para issue do GitHub ou card do Trello -->
- Closes #
- Trello: [Card Name](link)

---

## 📊 Tipo de Mudança

<!-- Marque com 'x' o tipo de mudança -->

- [ ] 🐛 Bug fix (correção de bug)
- [ ] ✨ Nova funcionalidade (feature)
- [ ] 💥 Breaking change (mudança que quebra compatibilidade)
- [ ] 📝 Documentação
- [ ] 🎨 Refatoração (sem mudança de funcionalidade)
- [ ] ⚡ Melhoria de performance
- [ ] ✅ Testes
- [ ] 🔧 Configuração/Build

---

## 📁 Arquivos Modificados

### Novos Arquivos
<!-- Liste os arquivos criados -->
- `path/to/new/file.py` - Descrição breve

### Arquivos Modificados
<!-- Liste os arquivos alterados -->
- `path/to/modified/file.py` - Descrição das mudanças

### Arquivos Removidos
<!-- Liste os arquivos deletados -->
- `path/to/deleted/file.py` - Motivo da remoção

---

## 🔍 Detalhes da Implementação

### Módulos Afetados
<!-- Liste os módulos/componentes afetados -->
- [ ] Data Manager
- [ ] Estoque
- [ ] Financeiro
- [ ] Operacional
- [ ] RH
- [ ] Outro: ___________

### Funcionalidades Implementadas
<!-- Descreva as funcionalidades implementadas -->

1. **Funcionalidade 1**
   - Descrição detalhada
   - Comportamento esperado

2. **Funcionalidade 2**
   - Descrição detalhada
   - Comportamento esperado

### Mudanças Técnicas
<!-- Descreva mudanças técnicas importantes -->

- **Arquitetura:** 
- **Dependências:** 
- **Banco de Dados:** 
- **APIs:** 

---

## 🧪 Testes

### Testes Implementados
<!-- Descreva os testes criados/modificados -->

- [ ] Testes unitários
- [ ] Testes de integração
- [ ] Testes end-to-end
- [ ] Testes manuais

### Cobertura de Testes
<!-- Se aplicável, adicione informações de cobertura -->
- Cobertura atual: ___%
- Cobertura anterior: ___%

### Como Testar
<!-- Instruções passo a passo para testar as mudanças -->

```bash
# Passo 1: Clone e instale dependências
git checkout [branch-name]
pip install -r requirements.txt

# Passo 2: Execute os testes
python -m pytest

# Passo 3: Teste manual
python -m modules.[module_name]
```

### Cenários de Teste
<!-- Liste os cenários testados -->

1. **Cenário 1:** Descrição
   - ✅ Resultado esperado
   - ✅ Resultado obtido

2. **Cenário 2:** Descrição
   - ✅ Resultado esperado
   - ✅ Resultado obtido

---

## 📸 Screenshots/Demonstração

<!-- Se aplicável, adicione screenshots ou GIFs demonstrando as mudanças -->

### Antes
<!-- Screenshot do estado anterior -->

### Depois
<!-- Screenshot do novo estado -->

---

## ⚠️ Breaking Changes

<!-- Se houver breaking changes, descreva-as aqui -->

- [ ] Esta PR contém breaking changes

### Descrição das Breaking Changes
<!-- Descreva o que quebra e como migrar -->

**O que muda:**

**Como migrar:**

---

## 📚 Documentação

<!-- Documentação relacionada -->

- [ ] Código está comentado adequadamente
- [ ] Docstrings adicionadas/atualizadas
- [ ] README atualizado
- [ ] Documentação técnica atualizada
- [ ] Changelog atualizado

### Links de Documentação
<!-- Links para documentação relevante -->
- [Documentação dos Módulos](./MODULES_DOCUMENTATION.md)
- [Cards do Trello](./TRELLO_CARD_TEMPLATE.md)

---

## ✅ Checklist de Qualidade

### Code Quality
- [ ] Código segue os padrões do projeto
- [ ] Não há código comentado/debug desnecessário
- [ ] Variáveis e funções têm nomes descritivos
- [ ] Funções são pequenas e focadas
- [ ] Não há duplicação de código
- [ ] Tratamento de erros implementado

### Segurança
- [ ] Não há credenciais hardcoded
- [ ] Inputs são validados
- [ ] Não há vulnerabilidades conhecidas
- [ ] Dados sensíveis são protegidos

### Performance
- [ ] Não há loops desnecessários
- [ ] Queries são otimizadas
- [ ] Não há memory leaks
- [ ] Recursos são liberados adequadamente

### Compatibilidade
- [ ] Testado no Python 3.x
- [ ] Compatível com Windows
- [ ] Compatível com Linux/Mac (se aplicável)
- [ ] Encoding UTF-8 configurado

---

## 🔗 Dependências

### Novas Dependências
<!-- Liste novas dependências adicionadas -->
- `package-name==version` - Motivo

### Dependências Removidas
<!-- Liste dependências removidas -->
- `package-name` - Motivo

### Dependências Atualizadas
<!-- Liste dependências atualizadas -->
- `package-name`: `old-version` → `new-version` - Motivo

---

## 🚀 Deploy

### Instruções de Deploy
<!-- Instruções especiais para deploy, se necessário -->

```bash
# Comandos de deploy
```

### Variáveis de Ambiente
<!-- Novas variáveis de ambiente necessárias -->
- `VAR_NAME` - Descrição

### Migrations
<!-- Se houver migrations de banco de dados -->
- [ ] Migrations criadas
- [ ] Migrations testadas
- [ ] Rollback testado

---

## 📝 Notas Adicionais

<!-- Qualquer informação adicional relevante -->

### Decisões de Design
<!-- Explique decisões importantes de design -->

### Limitações Conhecidas
<!-- Liste limitações conhecidas desta implementação -->

### Trabalho Futuro
<!-- O que pode ser melhorado no futuro -->

---

## 👥 Revisores

<!-- Marque os revisores sugeridos -->
@reviewer1 @reviewer2

### Áreas para Focar na Revisão
<!-- Áreas específicas que precisam de atenção especial -->
- [ ] Lógica de negócio em `module_name.py`
- [ ] Tratamento de erros
- [ ] Performance de queries
- [ ] Segurança

---

## 📊 Métricas

<!-- Se aplicável, adicione métricas relevantes -->

| Métrica | Antes | Depois | Melhoria |
|---------|-------|--------|----------|
| Tempo de execução | - | - | - |
| Uso de memória | - | - | - |
| Linhas de código | - | - | - |
| Cobertura de testes | - | - | - |

---

## ✨ Commits

<!-- Lista de commits principais (gerada automaticamente pelo GitHub) -->

### Estrutura de Commits
<!-- Se seguiu uma estrutura específica, descreva aqui -->

Commits seguem o padrão:
```
<tipo>(<escopo>): <descrição>

<corpo opcional>
```

**Tipos usados:**
- `feat`: Nova funcionalidade
- `fix`: Correção de bug
- `docs`: Documentação
- `refactor`: Refatoração
- `test`: Testes
- `chore`: Tarefas de manutenção

---

## 🎉 Pronto para Merge?

<!-- Marque quando estiver pronto -->
- [ ] Todos os testes passando
- [ ] Code review aprovado
- [ ] Documentação atualizada
- [ ] Sem conflitos com a branch principal
- [ ] CI/CD passando

---

**Data de Criação:** <!-- Será preenchido automaticamente -->
**Autor:** @<!-- seu-usuario -->
**Branch:** `feature/` ou `fix/` ou `docs/`
**Target Branch:** `main` ou `develop`
