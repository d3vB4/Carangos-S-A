# 🚀 Guia de Deploy - Sistema Carangos S/A

Este guia fornece instruções passo a passo para fazer deploy do Sistema de Gestão Integrada da Carangos S/A nas principais plataformas cloud.

## 📋 Pré-requisitos

Antes de fazer o deploy, certifique-se de:

1. ✅ Ter uma conta na plataforma escolhida (Render, Railway ou Northflank)
2. ✅ Ter Git instalado e o projeto versionado
3. ✅ Ter configurado as variáveis de ambiente necessárias

## 🔑 Variáveis de Ambiente Necessárias

Todas as plataformas precisam das seguintes variáveis de ambiente:

| Variável | Descrição | Exemplo |
|----------|-----------|---------|
| `SECRET_KEY` | Chave secreta do Flask (gere uma aleatória) | `sua-chave-super-secreta-aqui` |
| `FLASK_ENV` | Ambiente de execução | `production` |
| `PORT` | Porta do servidor (geralmente auto-configurada) | `5000` |

### Como Gerar uma SECRET_KEY Segura

Execute no Python:
```python
import secrets
print(secrets.token_hex(32))
```

---

## 1️⃣ Deploy no Render

**Render** é uma plataforma moderna e fácil de usar, com plano gratuito generoso.

### Passo a Passo:

1. **Acesse [render.com](https://render.com)** e faça login

2. **Crie um novo Web Service**:
   - Clique em "New +" → "Web Service"
   - Conecte seu repositório GitHub/GitLab

3. **Configure o serviço**:
   - **Name**: `carangos-sa`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Instance Type**: Free (ou pago conforme necessidade)

4. **Configure as variáveis de ambiente**:
   - Vá em "Environment" → "Add Environment Variable"
   - Adicione:
     - `SECRET_KEY`: [sua chave gerada]
     - `FLASK_ENV`: `production`

5. **Configure persistência de dados** (IMPORTANTE):
   - Vá em "Disks" → "Add Disk"
   - **Name**: `data`
   - **Mount Path**: `/app/data`
   - **Size**: 1GB (ou conforme necessidade)

6. **Deploy**:
   - Clique em "Create Web Service"
   - Aguarde o build e deploy (5-10 minutos)

7. **Acesse sua aplicação**:
   - URL será algo como: `https://carangos-sa.onrender.com`

### Comandos Úteis Render:

```bash
# Ver logs em tempo real
render logs -f

# Fazer redeploy manual
render deploy
```

---

## 2️⃣ Deploy no Railway

**Railway** oferece deploy extremamente simples com CLI poderosa.

### Passo a Passo:

1. **Acesse [railway.app](https://railway.app)** e faça login

2. **Instale a CLI do Railway** (opcional, mas recomendado):
   ```bash
   npm install -g @railway/cli
   railway login
   ```

3. **Deploy via Dashboard**:
   - Clique em "New Project" → "Deploy from GitHub repo"
   - Selecione seu repositório
   - Railway detectará automaticamente o `Procfile`

4. **Configure as variáveis de ambiente**:
   - Vá em "Variables"
   - Adicione:
     - `SECRET_KEY`: [sua chave gerada]
     - `FLASK_ENV`: `production`

5. **Configure Volume para persistência**:
   - Vá em "Settings" → "Volumes"
   - Clique em "New Volume"
   - **Mount Path**: `/app/data`
   - **Size**: 1GB

6. **Deploy automático**:
   - Railway faz deploy automaticamente a cada push no GitHub

7. **Acesse sua aplicação**:
   - Vá em "Settings" → "Generate Domain"
   - URL será algo como: `https://carangos-sa.up.railway.app`

### Comandos Úteis Railway:

```bash
# Deploy via CLI
cd "Sistema-Aut-Carangos-SA"
railway up

# Ver logs
railway logs

# Abrir aplicação no navegador
railway open

# Adicionar variáveis de ambiente via CLI
railway variables set SECRET_KEY=sua-chave-aqui
railway variables set FLASK_ENV=production
```

---

## 3️⃣ Deploy no Northflank

**Northflank** é uma plataforma robusta com excelente suporte a containers.

### Passo a Passo:

1. **Acesse [northflank.com](https://northflank.com)** e faça login

2. **Crie um novo Service**:
   - Clique em "Create Service" → "Combined Service"
   - Conecte seu repositório GitHub/GitLab

3. **Configure o build**:
   - **Build Type**: Buildpack
   - **Buildpack**: Heroku Python
   - **Port**: 5000

4. **Configure as variáveis de ambiente**:
   - Vá em "Environment Variables"
   - Adicione:
     - `SECRET_KEY`: [sua chave gerada]
     - `FLASK_ENV`: `production`
     - `PORT`: `5000`

5. **Configure persistência de dados**:
   - Vá em "Volumes" → "Add Volume"
   - **Mount Path**: `/app/data`
   - **Size**: 1GB
   - **Type**: SSD

6. **Configure Health Check**:
   - **Path**: `/`
   - **Port**: 5000
   - **Initial Delay**: 30s

7. **Deploy**:
   - Clique em "Create & Deploy"
   - Aguarde o build (5-10 minutos)

8. **Acesse sua aplicação**:
   - Vá em "Networking" → "Add Domain"
   - URL será algo como: `https://carangos-sa.northflank.app`

### Recursos do Northflank:

- **Auto-scaling**: Configure para escalar automaticamente
- **Backups**: Configure backups automáticos do volume
- **Monitoring**: Métricas detalhadas de CPU, memória e requests

---

## 🐳 Deploy com Docker (Genérico)

Para qualquer plataforma que suporte Docker (AWS ECS, Google Cloud Run, Azure Container Apps, etc.):

### Build Local:

```bash
cd "Sistema-Aut-Carangos-SA"

# Build da imagem
docker build -t carangos-sa:latest .

# Testar localmente
docker run -p 5000:5000 \
  -e SECRET_KEY=sua-chave-aqui \
  -e FLASK_ENV=production \
  -v $(pwd)/data:/app/data \
  carangos-sa:latest

# Acesse http://localhost:5000
```

### Push para Registry:

```bash
# Docker Hub
docker tag carangos-sa:latest seu-usuario/carangos-sa:latest
docker push seu-usuario/carangos-sa:latest

# Google Container Registry
docker tag carangos-sa:latest gcr.io/seu-projeto/carangos-sa:latest
docker push gcr.io/seu-projeto/carangos-sa:latest

# AWS ECR
docker tag carangos-sa:latest 123456789.dkr.ecr.us-east-1.amazonaws.com/carangos-sa:latest
docker push 123456789.dkr.ecr.us-east-1.amazonaws.com/carangos-sa:latest
```

---

## 🧪 Teste Local com Docker Compose

Antes de fazer deploy, teste localmente:

```bash
cd "Sistema-Aut-Carangos-SA"

# Iniciar aplicação
docker-compose up --build

# Acesse http://localhost:5000

# Parar aplicação
docker-compose down
```

---

## 📊 Inicialização de Dados

Após o primeiro deploy, você precisa inicializar os usuários:

### Opção 1: Via SSH/Console da Plataforma

```bash
# Conecte via SSH/console da plataforma
python scripts/seed_users.py
```

### Opção 2: Adicionar ao Procfile (Automático)

Edite o `Procfile`:
```
release: python scripts/seed_users.py
web: gunicorn app:app
```

---

## 🔒 Checklist de Segurança

Antes de ir para produção:

- [ ] ✅ SECRET_KEY configurada com valor aleatório forte
- [ ] ✅ FLASK_ENV definida como `production`
- [ ] ✅ Debug mode desabilitado (automático em produção)
- [ ] ✅ Arquivo `.env` NÃO commitado no Git
- [ ] ✅ HTTPS habilitado (geralmente automático nas plataformas)
- [ ] ✅ Volume/disco persistente configurado para `/app/data`
- [ ] ✅ Backups configurados (se disponível na plataforma)

---

## 🐛 Troubleshooting

### Aplicação não inicia:

1. Verifique os logs da plataforma
2. Confirme que todas as variáveis de ambiente estão configuradas
3. Verifique se o `requirements.txt` está correto
4. Confirme que a porta está correta (geralmente auto-configurada)

### Dados não persistem após redeploy:

1. Verifique se o volume está montado em `/app/data`
2. Confirme que a variável `DATA_DIR` aponta para o volume (se customizada)
3. Verifique permissões de escrita no volume

### Erro 500 Internal Server Error:

1. Verifique os logs da aplicação
2. Confirme que `SECRET_KEY` está definida
3. Verifique se o diretório `data/` existe e tem permissões de escrita
4. Execute `python scripts/seed_users.py` se os usuários não existirem

### Erro de módulo não encontrado:

1. Verifique se todas as dependências estão no `requirements.txt`
2. Force um rebuild/redeploy
3. Limpe o cache de build da plataforma

---

## 📞 Suporte

Para problemas específicos de cada plataforma:

- **Render**: [docs.render.com](https://docs.render.com)
- **Railway**: [docs.railway.app](https://docs.railway.app)
- **Northflank**: [northflank.com/docs](https://northflank.com/docs)

---

## 🎉 Próximos Passos

Após o deploy bem-sucedido:

1. Configure um domínio customizado (se disponível)
2. Configure backups automáticos
3. Configure monitoramento e alertas
4. Considere migrar de JSON para PostgreSQL para maior robustez
5. Configure CI/CD para deploys automáticos

**Boa sorte com seu deploy! 🚀**
