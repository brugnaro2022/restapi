# Fluxograma - Sistema de Agendamento de Barbearia

## Fluxograma Principal do Sistema

```mermaid
flowchart TD
    A[Cliente acessa o sistema] --> B{Cliente já cadastrado?}
    B -->|Não| C[Cadastro de Cliente]
    B -->|Sim| D[Login do Cliente]
    
    C --> E[Preencher dados pessoais]
    E --> F[Validar dados]
    F -->|Dados inválidos| E
    F -->|Dados válidos| G[Cliente cadastrado]
    G --> D
    
    D --> H[Autenticação]
    H -->|Falha| I[Exibir erro de login]
    I --> D
    H -->|Sucesso| J[Dashboard do Cliente]
    
    J --> K{Cliente quer agendar?}
    K -->|Não| L[Visualizar agendamentos existentes]
    K -->|Sim| M[Selecionar tipo de serviço]
    
    M --> N[Escolher barbeiro]
    N --> O[Selecionar data e horário]
    O --> P{Disponibilidade verificada?}
    P -->|Não| Q[Exibir horários alternativos]
    Q --> O
    P -->|Sim| R[Confirmar agendamento]
    
    R --> S[Gerar confirmação]
    S --> T[Enviar notificação]
    T --> U[Agendamento criado]
    
    L --> V{Cliente quer modificar?}
    V -->|Sim| W[Editar agendamento]
    V -->|Não| X[Logout]
    W --> Y{Data/horário disponível?}
    Y -->|Não| Q
    Y -->|Sim| Z[Atualizar agendamento]
    Z --> AA[Enviar confirmação de alteração]
    AA --> X
    
    U --> X
```

## Fluxograma do Processo de Agendamento

```mermaid
flowchart TD
    A[Cliente solicita agendamento] --> B[Verificar disponibilidade do barbeiro]
    B --> C{Barbeiro disponível?}
    C -->|Não| D[Sugerir horários alternativos]
    C -->|Sim| E[Verificar conflitos de horário]
    
    D --> F[Cliente escolhe novo horário]
    F --> B
    
    E --> G{Conflito detectado?}
    G -->|Sim| H[Notificar conflito]
    G -->|Não| I[Reservar horário temporariamente]
    
    H --> D
    I --> J[Cliente confirma dados]
    J --> K{Dados corretos?}
    K -->|Não| L[Corrigir informações]
    L --> J
    K -->|Sim| M[Processar pagamento]
    
    M --> N{Pagamento aprovado?}
    N -->|Não| O[Exibir erro de pagamento]
    N -->|Sim| P[Confirmar agendamento]
    
    O --> Q[Liberar horário reservado]
    Q --> R[Retornar ao início]
    
    P --> S[Gerar ID do agendamento]
    S --> T[Salvar no banco de dados]
    T --> U[Enviar confirmação por email/SMS]
    U --> V[Adicionar ao calendário do barbeiro]
    V --> W[Agendamento finalizado]
```

## Fluxograma do Dia do Atendimento

```mermaid
flowchart TD
    A[Dia do agendamento] --> B[Cliente chega à barbearia]
    B --> C[Verificar agendamento no sistema]
    C --> D{Cliente presente?}
    D -->|Não| E[Aguardar 15 minutos]
    E --> F{Cliente chegou?}
    F -->|Não| G[Marcar como não compareceu]
    F -->|Sim| H[Iniciar atendimento]
    
    D -->|Sim| H
    H --> I[Barbeiro inicia serviço]
    I --> J[Registrar início do serviço]
    J --> K[Executar serviço]
    K --> L[Finalizar serviço]
    L --> M[Registrar conclusão]
    M --> N[Processar pagamento final]
    N --> O[Gerar recibo]
    O --> P[Atualizar status do agendamento]
    P --> Q[Enviar feedback para cliente]
    Q --> R[Atendimento concluído]
    
    G --> S[Liberar horário para outros clientes]
    S --> T[Notificar cliente sobre não comparecimento]
```

## Fluxograma de Gestão de Barbeiros

```mermaid
flowchart TD
    A[Administrador acessa sistema] --> B[Gerenciar barbeiros]
    B --> C{Adicionar novo barbeiro?}
    C -->|Sim| D[Cadastrar dados do barbeiro]
    C -->|Não| E[Visualizar barbeiros existentes]
    
    D --> F[Definir horários de trabalho]
    F --> G[Configurar serviços oferecidos]
    G --> H[Definir preços]
    H --> I[Salvar no sistema]
    
    E --> J{Modificar barbeiro?}
    J -->|Sim| K[Editar informações]
    J -->|Não| L[Visualizar agenda]
    
    K --> M[Atualizar dados]
    M --> N[Salvar alterações]
    
    L --> O[Ver agendamentos do dia]
    O --> P[Verificar disponibilidade]
    P --> Q[Gerenciar folgas]
    Q --> R[Configurar horários especiais]
```

## Fluxograma de Relatórios e Analytics

```mermaid
flowchart TD
    A[Sistema gera relatórios] --> B{Tipo de relatório?}
    B -->|Financeiro| C[Relatório de vendas]
    B -->|Operacional| D[Relatório de agendamentos]
    B -->|Cliente| E[Relatório de satisfação]
    
    C --> F[Calcular receita diária/mensal]
    F --> G[Analisar serviços mais procurados]
    G --> H[Identificar tendências de preço]
    
    D --> I[Contar agendamentos por período]
    I --> J[Analisar taxa de comparecimento]
    J --> K[Identificar horários de pico]
    
    E --> L[Coletar feedback dos clientes]
    L --> M[Calcular satisfação média]
    M --> N[Identificar áreas de melhoria]
    
    H --> O[Gerar gráficos e estatísticas]
    K --> O
    N --> O
    O --> P[Enviar relatório para administrador]
```

## Funcionalidades Principais do Sistema

### 1. **Gestão de Clientes**
- Cadastro e autenticação
- Histórico de agendamentos
- Preferências de serviços
- Dados de contato

### 2. **Gestão de Agendamentos**
- Criação de novos agendamentos
- Modificação de agendamentos existentes
- Cancelamento de agendamentos
- Verificação de disponibilidade

### 3. **Gestão de Barbeiros**
- Cadastro de profissionais
- Horários de trabalho
- Serviços oferecidos
- Agenda individual

### 4. **Gestão de Serviços**
- Catálogo de serviços
- Preços e duração
- Disponibilidade por barbeiro

### 5. **Sistema de Notificações**
- Confirmação de agendamento
- Lembretes automáticos
- Alterações de horário
- Feedback pós-atendimento

### 6. **Relatórios e Analytics**
- Relatórios financeiros
- Análise de ocupação
- Satisfação do cliente
- Performance dos barbeiros

## Tecnologias Sugeridas

- **Backend**: Flask (já implementado) ou FastAPI
- **Frontend**: React, Vue.js ou Angular
- **Banco de Dados**: PostgreSQL ou MySQL
- **Autenticação**: JWT ou OAuth2
- **Notificações**: Email (SMTP) e SMS (APIs)
- **Pagamentos**: Stripe, PayPal ou PagSeguro
- **Deploy**: Docker + AWS/Azure/GCP

