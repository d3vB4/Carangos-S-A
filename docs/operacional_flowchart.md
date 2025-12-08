# ⚙️ Fluxograma do Módulo Operacional

Este documento descreve o fluxo de funcionamento do módulo Operacional (`modules/operacional.py`), responsável pelo controle de produção e relatórios executivos.

## 🔄 Visão Geral do Processo

O módulo segue um fluxo linear de coleta de dados, processamento estatístico e geração de relatórios comparativos.

```mermaid
flowchart TD
    Start([Início]) --> Input[📥 cadastrar_producao]
    
    subgraph Coleta de Dados
        Input -->|Loop 7 dias| Turnos{Turnos}
        Turnos -->|Manhã/Tarde/Noite| Validacao{Validar > 0?}
        Validacao -->|Não| Error[❌ Erro]
        Error --> Input
        Validacao -->|Sim| Save[💾 Salvar em JSON]
    end
    
    Save --> Stats[📊 calcular_estatisticas]
    
    subgraph Processamento
        Stats --> CalcMedia[Média Diária]
        Stats --> CalcTurno[Média por Turno]
        Stats --> Simula[🔮 simular_producao]
        Simula --> Men[Projeção Mensal]
        Simula --> Anu[Projeção Anual]
    end
    
    Processamento --> Ideal[🎯 calcular_capacidade_ideal]
    Ideal --> Report[📝 gerar_relatorio]
    
    subgraph Relatorio
        Report --> ShowStats[Mostrar Estatísticas]
        Report --> ShowProj[Mostrar Projeções]
        Report --> Compare{Comparar com Ideal}
        Compare -->|>= Meta| Green[✅ Acima da Meta]
        Compare -->|< Meta| Red[⚠️ Abaixo da Meta]
    end
    
    Report --> End([Fim])
```

## 📝 Descrição das Etapas

1. **Cadastrar Produção (`cadastrar_producao`)**:
   - Coleta dados de 7 dias da semana.
   - Para cada dia, coleta produção de 3 turnos (Manhã, Tarde, Noite).
   - Valida entradas negativas.
   - Persiste dados em arquivo JSON.

2. **Calcular Estatísticas (`calcular_estatisticas`)**:
   - Consolida total semanal.
   - Calcula média diária.
   - Calcula média específica por turno.

3. **Simular Produção (`simular_producao`)**:
   - Projeta produção mensal (x4 semanas).
   - Projeta produção anual (x52 semanas).

4. **Calcular Capacidade Ideal (`calcular_capacidade_ideal`)**:
   - Define meta baseada em 3 turnos.
   - Meta: 750 unidades/mês (187.5/semana).

5. **Gerar Relatório (`gerar_relatorio`)**:
   - Exibe todos os dados calculados de forma formatada.
   - Compara realizado vs ideal.
   - Indica status visual (✅ ou ⚠️).
