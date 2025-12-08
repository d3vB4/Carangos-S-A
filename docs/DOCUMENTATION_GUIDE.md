# 📚 Guia de Documentação e Organização - Módulos

## 🎯 Visão Geral

Este guia contém toda a documentação necessária para organizar o trabalho realizado na pasta `modules/` do Sistema Carangos S/A, incluindo:

- ✅ Documentação completa de todas as funções
- ✅ Templates de cards para Trello
- ✅ Estrutura de commits profissional
- ✅ Template padrão de Pull Request

---

## 📂 Arquivos de Documentação

### 1. 📖 MODULES_DOCUMENTATION.md
**Propósito:** Documentação técnica completa de todos os módulos

**Conteúdo:**
- Documentação detalhada de cada módulo
- Todas as funções com docstrings profissionais
- Estruturas de dados
- Fórmulas e cálculos
- Organização para Trello
- Estrutura de commits sugerida
- Template de Pull Request

**Quando usar:**
- Para entender a arquitetura dos módulos
- Para consultar documentação de funções
- Para planejar cards do Trello
- Para estruturar commits

📄 [Ver Documentação Completa](./MODULES_DOCUMENTATION.md)

---

### 2. 🎴 TRELLO_CARD_TEMPLATE.md
**Propósito:** Templates personalizados de cards para o Trello

**Conteúdo:**
- 5 cards detalhados (um para cada módulo)
- Checklists completas de implementação
- Checklists de documentação
- Checklists de testes
- Estruturas de dados
- Fórmulas e tabelas
- Configuração de labels
- Estrutura de listas
- Métricas de acompanhamento

**Quando usar:**
- Ao criar cards no Trello
- Para organizar tarefas por módulo
- Para rastrear progresso
- Para definir labels e prioridades

📄 [Ver Templates de Cards](./TRELLO_CARD_TEMPLATE.md)

---

### 3. 🚀 .github/PULL_REQUEST_TEMPLATE.md
**Propósito:** Template padrão para Pull Requests no GitHub

**Conteúdo:**
- Seções estruturadas de PR
- Checklist de qualidade
- Seção de testes
- Documentação de breaking changes
- Métricas e estatísticas
- Instruções de deploy

**Quando usar:**
- Ao criar qualquer Pull Request
- Para manter padrão de documentação
- Para facilitar code review
- Para rastrear mudanças

📄 [Ver Template de PR](./.github/PULL_REQUEST_TEMPLATE.md)

---

## 🎴 Como Criar Cards no Trello

### Passo a Passo:

#### 1. Acesse o Template
Abra o arquivo [TRELLO_CARD_TEMPLATE.md](./TRELLO_CARD_TEMPLATE.md)

#### 2. Escolha o Módulo
Selecione o card correspondente ao módulo:
- 📦 Card 1: Data Manager
- 📊 Card 2: Estoque
- 💰 Card 3: Financeiro
- ⚙️ Card 4: Operacional
- 👥 Card 5: RH

#### 3. Copie o Conteúdo
Copie as seguintes seções do template:
- **Título** → Nome do card no Trello
- **Descrição** → Descrição do card
- **Checklist** → Adicione como checklist no Trello

#### 4. Configure o Card
- **Adicione Labels:** Use as labels sugeridas
- **Atribua Membros:** Adicione responsáveis
- **Defina Datas:** Estabeleça prazos
- **Anexe Arquivos:** Adicione os arquivos .py correspondentes

#### 5. Organize nas Listas
Coloque o card na lista apropriada:
- 📥 Backlog
- 📝 To Do
- 🔄 In Progress
- 👀 Code Review
- 🧪 Testing
- ✅ Done

---

## 🔄 Como Estruturar Commits

### Formato Padrão:
```
<tipo>(<escopo>): <descrição curta>

<descrição detalhada opcional>

<referências opcionais>
```

### Tipos de Commit:
- `feat`: Nova funcionalidade
- `fix`: Correção de bug
- `docs`: Documentação
- `refactor`: Refatoração
- `test`: Testes
- `chore`: Manutenção

### Exemplos por Módulo:

#### Data Manager
```bash
feat(data-manager): adicionar função load_data para carregar JSON
feat(data-manager): adicionar função save_data para persistência
docs(data-manager): documentar funções e comportamentos
```

#### Estoque
```bash
feat(estoque): implementar cadastro de produtos
feat(estoque): adicionar verificação de duplicidade
feat(estoque): implementar pesquisa de produtos
feat(estoque): adicionar cálculo de custos
docs(estoque): documentar funções e estruturas
```

#### Financeiro
```bash
feat(financeiro): implementar cadastro de despesas fixas
feat(financeiro): adicionar cálculo de custo de produção
feat(financeiro): implementar cálculo de preço de venda
docs(financeiro): documentar funções e fórmulas
```

#### Operacional
```bash
feat(operacional): implementar cadastro de produção semanal
feat(operacional): adicionar cálculo de estatísticas
feat(operacional): implementar simulação de produção
feat(operacional): gerar relatório comparativo
docs(operacional): documentar funções e estruturas
```

#### RH
```bash
feat(rh): implementar cadastro de funcionários
feat(rh): adicionar cálculo de horas extras
feat(rh): implementar cálculo de IRPF progressivo
feat(rh): gerar folha de pagamento completa
docs(rh): documentar funções e tabelas
```

### Commits Detalhados no MODULES_DOCUMENTATION.md
Para ver a lista completa de commits sugeridos para cada módulo, consulte a seção **"Estrutura de Commits"** no arquivo [MODULES_DOCUMENTATION.md](./MODULES_DOCUMENTATION.md).

---

## 🚀 Como Criar uma Pull Request

### Passo a Passo:

#### 1. Prepare sua Branch
```bash
# Certifique-se de estar na branch correta
git checkout -b feature/modules-implementation

# Adicione seus commits
git add modules/
git commit -m "feat(modules): implementar todos os módulos"
```

#### 2. Push para o Repositório
```bash
git push origin feature/modules-implementation
```

#### 3. Abra a PR no GitHub
- Vá para o repositório no GitHub
- Clique em "Pull Requests" → "New Pull Request"
- Selecione sua branch
- O template será carregado automaticamente

#### 4. Preencha o Template
O template em `.github/PULL_REQUEST_TEMPLATE.md` será carregado automaticamente. Preencha:

- ✅ Descrição e objetivo
- ✅ Tipo de mudança
- ✅ Arquivos modificados
- ✅ Detalhes da implementação
- ✅ Testes realizados
- ✅ Checklist de qualidade
- ✅ Screenshots (se aplicável)

#### 5. Solicite Revisão
- Marque revisores sugeridos
- Indique áreas para focar na revisão
- Aguarde aprovação

---

## 📊 Resumo dos Módulos

### Estatísticas Gerais:
| Módulo | Arquivo | Linhas | Funções | Complexidade |
|--------|---------|--------|---------|--------------|
| Data Manager | `data_manager.py` | 37 | 2 | Baixa |
| Estoque | `estoque.py` | 114 | 5 | Média |
| Financeiro | `financeiro.py` | 80 | 4 | Média |
| Operacional | `operacional.py` | 157 | 5 | Alta |
| RH | `rh.py` | 114 | 6 | Alta |
| **TOTAL** | **5 arquivos** | **502** | **22** | - |

### Funcionalidades por Módulo:

#### 📦 Data Manager
- Carregamento de dados JSON
- Salvamento de dados JSON
- Tratamento de erros
- Configuração via ambiente

#### 📊 Estoque
- Cadastro de produtos
- Verificação de duplicidade
- Pesquisa de produtos
- Cálculo de custos
- Listagem de produtos

#### 💰 Financeiro
- Cadastro de despesas fixas
- Cálculo de custo de produção
- Cálculo de custo unitário
- Cálculo de preço de venda

#### ⚙️ Operacional
- Cadastro de produção por turno
- Cálculo de estatísticas
- Simulação de produção
- Cálculo de capacidade ideal
- Geração de relatórios

#### 👥 RH
- Cadastro de funcionários
- Cálculo de salário bruto
- Cálculo de horas extras
- Cálculo de IRPF
- Cálculo de salário líquido
- Geração de folha de pagamento

---

## 🎯 Fluxo de Trabalho Completo

### 1. Planejamento (Trello)
```
📥 Backlog → 📝 To Do
```
- Crie cards usando os templates
- Defina prioridades
- Atribua responsáveis

### 2. Desenvolvimento
```
📝 To Do → 🔄 In Progress
```
- Mova card para "In Progress"
- Implemente funcionalidades
- Faça commits estruturados
- Atualize checklist do card

### 3. Documentação
```
Durante o desenvolvimento
```
- Adicione docstrings
- Comente código complexo
- Atualize README se necessário

### 4. Testes
```
🔄 In Progress → 🧪 Testing
```
- Execute testes manuais
- Valide funcionalidades
- Marque itens da checklist

### 5. Code Review
```
🧪 Testing → 👀 Code Review
```
- Crie Pull Request
- Use template padrão
- Solicite revisão
- Responda comentários

### 6. Conclusão
```
👀 Code Review → ✅ Done
```
- Merge da PR
- Mova card para "Done"
- Atualize documentação final

---

## 📋 Checklists Rápidas

### ✅ Antes de Criar Card no Trello
- [ ] Li a documentação do módulo
- [ ] Entendi as funcionalidades
- [ ] Identifiquei dependências
- [ ] Defini prioridade

### ✅ Antes de Fazer Commit
- [ ] Código está funcionando
- [ ] Testes manuais executados
- [ ] Docstrings adicionadas
- [ ] Código segue padrões
- [ ] Mensagem de commit descritiva

### ✅ Antes de Criar Pull Request
- [ ] Todos os commits feitos
- [ ] Branch atualizada com main
- [ ] Testes passando
- [ ] Documentação atualizada
- [ ] Template de PR preenchido

### ✅ Antes de Marcar Card como Done
- [ ] PR merged
- [ ] Testes validados
- [ ] Documentação completa
- [ ] Sem bugs conhecidos

---

## 🔗 Links Rápidos

### Documentação
- 📖 [Documentação Completa dos Módulos](./MODULES_DOCUMENTATION.md)
- 🎴 [Templates de Cards do Trello](./TRELLO_CARD_TEMPLATE.md)
- 🚀 [Template de Pull Request](./.github/PULL_REQUEST_TEMPLATE.md)

### Arquivos dos Módulos
- 📦 [data_manager.py](./modules/data_manager.py)
- 📊 [estoque.py](./modules/estoque.py)
- 💰 [financeiro.py](./modules/financeiro.py)
- ⚙️ [operacional.py](./modules/operacional.py)
- 👥 [rh.py](./modules/rh.py)

---

## 💡 Dicas e Boas Práticas

### Para Trello:
- ✅ Use cores diferentes para cada módulo
- ✅ Atualize cards diariamente
- ✅ Comente progresso nos cards
- ✅ Anexe screenshots quando relevante
- ✅ Use labels para filtrar facilmente

### Para Commits:
- ✅ Commits pequenos e focados
- ✅ Uma funcionalidade por commit
- ✅ Mensagens descritivas
- ✅ Referências a issues/cards
- ✅ Commits em português

### Para Pull Requests:
- ✅ Preencha todo o template
- ✅ Adicione screenshots
- ✅ Liste breaking changes
- ✅ Documente decisões importantes
- ✅ Responda comentários rapidamente

### Para Documentação:
- ✅ Docstrings em todas as funções
- ✅ Comentários em código complexo
- ✅ Exemplos de uso
- ✅ Documentar fórmulas
- ✅ Manter atualizado

---

## 🆘 Troubleshooting

### Problema: Template de PR não aparece
**Solução:** Certifique-se de que o arquivo está em `.github/PULL_REQUEST_TEMPLATE.md`

### Problema: Commits muito grandes
**Solução:** Consulte a seção "Estrutura de Commits" e divida em commits menores

### Problema: Card do Trello muito complexo
**Solução:** Divida em sub-cards ou use checklists aninhadas

### Problema: Documentação incompleta
**Solução:** Use os templates como guia e preencha todas as seções

---

## 📞 Suporte

Para dúvidas sobre:
- **Documentação:** Consulte [MODULES_DOCUMENTATION.md](./MODULES_DOCUMENTATION.md)
- **Trello:** Consulte [TRELLO_CARD_TEMPLATE.md](./TRELLO_CARD_TEMPLATE.md)
- **Pull Requests:** Consulte [.github/PULL_REQUEST_TEMPLATE.md](./.github/PULL_REQUEST_TEMPLATE.md)

---

**Última Atualização:** 2025-12-04
**Versão:** 1.0
**Mantido por:** Equipe de Desenvolvimento Carangos S/A
