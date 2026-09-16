# Amostra de requisitos funcionais

[← Voltar ao README](../README.md)

> Requisitos reconstruídos para fins de portfólio. Identificadores, redação e critérios não reproduzem documentos internos.

## Agendamento e jornada

### FR-001 — Listar agendamentos

**Como** motorista autenticado, **quero** visualizar meus agendamentos futuros e históricos **para** organizar minha jornada.

**Critérios de aceite**

- exibir somente operações vinculadas ao usuário autorizado;
- distinguir futuros, em andamento, concluídos e cancelados;
- apresentar data e hora no fuso aplicável;
- informar estado vazio e falha de carregamento;
- permitir atualização sem duplicar itens.

### FR-002 — Exibir detalhes da operação

**Como** motorista, **quero** consultar os dados essenciais do agendamento **para** confirmar se estou seguindo a instrução correta.

**Critérios de aceite**

- apresentar janela, tipo de operação, origem, destino e orientações;
- exibir veículo e carga de forma proporcional à necessidade;
- ocultar campos sem autorização;
- refletir alterações confirmadas pela fonte responsável.

### FR-003 — Enviar lembretes

**Como** motorista, **quero** receber lembretes da operação **para** reduzir risco de atraso ou perda da janela.

**Critérios de aceite**

- respeitar configuração e permissão de notificação;
- identificar claramente o agendamento relacionado;
- não enviar lembrete de agendamento cancelado;
- ao tocar, abrir o contexto correto.

## Rota e localização

### FR-004 — Apresentar origem e destino

**Como** motorista, **quero** acessar origem, destino e local intermediário **para** seguir a rota operacional correta.

**Critérios de aceite**

- exibir o local associado ao estado atual da jornada;
- permitir abrir navegação externa quando autorizado;
- tratar endereço indisponível ou alterado;
- não manter destino anterior após redirecionamento confirmado.

### FR-005 — Compartilhar localização

**Como** operação, **quero** receber atualizações de localização durante a jornada **para** acompanhar a recência e apoiar a previsão operacional.

**Critérios de aceite**

- solicitar permissão com finalidade compreensível;
- registrar início e fim do compartilhamento;
- associar cada atualização à jornada correta;
- informar quando a posição estiver indisponível ou desatualizada;
- não inferir recebimento físico apenas pela posição.

## Documentos

### FR-006 — Listar documentos autorizados

**Como** motorista, **quero** encontrar os documentos da operação em um único local **para** apresentá-los quando necessário.

**Critérios de aceite**

- exibir somente documentos vinculados à jornada e ao perfil;
- identificar tipo, versão e validade quando aplicável;
- não expor URL interna ou token de acesso;
- registrar falha de abertura para suporte.

### FR-007 — Visualizar documento

**Como** motorista, **quero** abrir um documento no celular **para** consultar as informações sem depender de papel.

**Critérios de aceite**

- abrir formato homologado no dispositivo;
- preservar legibilidade;
- apresentar alternativa quando o visualizador não estiver disponível;
- impedir acesso após revogação da autorização.

## Pátio e check-in

### FR-008 — Direcionar ao pátio correto

**Como** motorista, **quero** saber em qual pátio devo aguardar **para** não me dirigir antecipadamente ao terminal.

**Critérios de aceite**

- usar o pátio associado ao agendamento vigente;
- refletir redirecionamento confirmado;
- apresentar instrução clara de chegada;
- evitar exibição simultânea de destinos conflitantes.

### FR-009 — Registrar check-in

**Como** motorista/operação do pátio, **quero** confirmar a chegada **para** atualizar a etapa logística.

**Critérios de aceite**

- validar agendamento ativo e contexto elegível;
- gerar um único efeito para reenvios do mesmo evento;
- registrar data/hora de ocorrência e processamento;
- informar sucesso ou motivo funcional da rejeição;
- atualizar o status nos sistemas consumidores.

### FR-010 — Registrar saída do pátio

**Como** operação, **quero** confirmar a saída após a chamada **para** manter a fila e a jornada sincronizadas.

**Critérios de aceite**

- exigir check-in válido ou exceção autorizada;
- correlacionar saída ao mesmo agendamento;
- rejeitar saída duplicada sem criar novo efeito;
- disponibilizar o estado atualizado ao app e ao terminal.

## Chamada e acesso

### FR-011 — Notificar chamada do terminal

**Como** motorista em espera, **quero** ser avisado quando puder prosseguir **para** chegar ao terminal no momento correto.

**Critérios de aceite**

- enviar notificação apenas após evento autorizado;
- abrir o agendamento correspondente;
- diferenciar chamada nova de lembrete;
- refletir revogação ou alteração posterior.

### FR-012 — Habilitar QR Code

**Como** motorista chamado, **quero** visualizar uma credencial digital **para** validar meu acesso ao terminal.

**Critérios de aceite**

- permanecer indisponível antes da chamada;
- vincular-se ao agendamento correto;
- possuir validade e estado verificáveis;
- ser revogado quando a operação perder elegibilidade;
- não revelar conteúdo sensível fora da apresentação necessária.

### FR-013 — Validar QR Code

**Como** controle de acesso, **quero** validar a credencial **para** permitir somente a entrada elegível.

**Critérios de aceite**

- verificar autenticidade, validade, estado e associação;
- rejeitar credencial expirada, revogada ou incompatível;
- impedir segundo uso quando configurado como uso único;
- registrar resultado com correlação e sem dados excessivos;
- retornar mensagem funcional para tratamento operacional.

## Operação e integração

### FR-014 — Atualizar início da descarga

**Como** terminal, **quero** registrar o início da operação **para** atualizar a jornada e o planejamento.

**Critérios de aceite**

- aceitar transição apenas de estado permitido;
- registrar origem e horário do evento;
- refletir o novo status para os consumidores;
- tratar duplicidade sem iniciar duas operações.

### FR-015 — Tratar falha de integração

**Como** suporte, **quero** identificar e reprocessar eventos com falha **para** restabelecer consistência entre os sistemas.

**Critérios de aceite**

- registrar sistema, etapa, correlação e motivo técnico;
- não gravar segredo ou documento sensível no log;
- permitir reprocessamento controlado;
- preservar idempotência;
- disponibilizar resultado final da tentativa.

### FR-016 — Exibir estado reconciliado

**Como** usuário da operação, **quero** distinguir estados consistentes de divergências **para** agir antes que impactem o fluxo físico.

**Critérios de aceite**

- apresentar status vigente e data da última atualização;
- sinalizar atraso ou divergência sem criar status fictício;
- indicar sistema de origem para suporte autorizado;
- permitir consulta ao histórico de eventos relevantes.
