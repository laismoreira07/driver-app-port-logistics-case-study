# 02. Jornada do motorista e requisitos

[← Voltar ao README](../README.md)

## Persona primária

**Motorista em operação de descarga portuária**

- utiliza o celular durante uma jornada com restrições de tempo e conectividade;
- precisa saber onde ir, quando chegar e o que apresentar;
- não deve interpretar regras internas do terminal;
- precisa receber alterações e chamadas com clareza;
- deve acessar somente os documentos relacionados à própria operação.

## Jornada detalhada

| Etapa | Necessidade do motorista | Comportamento esperado do produto | Evidência operacional |
|---|---|---|---|
| 1. Convocação | Saber que existe uma operação | Notificar e exibir agendamento ativo | Agendamento visualizado |
| 2. Preparação | Conferir data, janela, origem e destino | Apresentar resumo e orientações | Confirmação de leitura |
| 3. Documentos | Ter acesso ao que será exigido | Disponibilizar arquivos autorizados | Documento acessado |
| 4. Início da viagem | Seguir para o local correto | Exibir rota e solicitar permissão de localização | Jornada iniciada |
| 5. Deslocamento | Receber lembretes e mudanças | Atualizar status e instruções | Posição/evento recente |
| 6. Pré-chegada | Identificar o pátio correto | Direcionar conforme agendamento | Destino operacional definido |
| 7. Check-in | Informar que chegou | Registrar chegada e confirmar espera | Evento de entrada no pátio |
| 8. Aguardar | Saber se já pode prosseguir | Mostrar status e notificar chamada | Chamada recebida |
| 9. Acesso | Apresentar credencial válida | Habilitar QR Code no estado correto | Validação de acesso |
| 10. Descarga | Confirmar início da operação | Atualizar etapa da jornada | Operação iniciada |
| 11. Encerramento | Saber que a etapa foi concluída | Exibir status final e histórico | Evento sincronizado |

## Épicos funcionais

### EP-01 — Agendamentos

- listar agendamentos futuros e históricos;
- abrir detalhes da operação;
- exibir janela no fuso correto;
- refletir cancelamento ou alteração;
- impedir acesso a agendamento de outro usuário.

### EP-02 — Orientações, rota e lembretes

- apresentar origem, destino e local intermediário quando aplicável;
- abrir navegação compatível com o dispositivo;
- lembrar o motorista antes da janela;
- informar mudança de instrução ou destino;
- sinalizar ausência de conectividade ou posição desatualizada.

### EP-03 — Documentos digitais

- disponibilizar somente documentos autorizados;
- identificar tipo, versão e validade;
- permitir visualização em tela;
- registrar falha de abertura/download;
- proteger arquivos contra exposição indevida.

### EP-04 — Localização e eventos

- solicitar consentimento de localização;
- registrar início e término do compartilhamento;
- transmitir posição dentro da janela definida;
- manter marca temporal e qualidade do sinal;
- diferenciar “sem posição” de “veículo parado”.

### EP-05 — Pátio e check-in

- direcionar ao pátio associado à operação;
- validar elegibilidade de check-in;
- registrar chegada sem duplicidade;
- exibir confirmação e próximo passo;
- receber correções de status vindas da integração.

### EP-06 — Chamada e QR Code

- notificar a chamada do terminal;
- liberar QR Code apenas no estado permitido;
- vincular credencial a agendamento e contexto corretos;
- rejeitar QR expirado, revogado ou já utilizado;
- fornecer mensagem orientativa em caso de recusa.

### EP-07 — Integração e observabilidade

- correlacionar eventos ponta a ponta;
- suportar reenvio sem duplicar efeitos;
- registrar sucesso, erro e tentativa de reprocessamento;
- expor status compreensível ao suporte;
- preservar histórico para auditoria.

## Requisitos não funcionais relevantes

| Dimensão | Necessidade |
|---|---|
| Usabilidade | Ações críticas devem ser compreensíveis com baixa carga cognitiva |
| Disponibilidade | Consulta ao agendamento e ao status deve tolerar indisponibilidades transitórias |
| Desempenho | Chamada e liberação precisam chegar dentro de uma janela operacional útil |
| Segurança | Autenticação, autorização e proteção de documentos devem seguir menor privilégio |
| Privacidade | Localização deve ter finalidade, consentimento, retenção e acesso definidos |
| Integridade | Eventos duplicados ou fora de ordem não podem criar estados impossíveis |
| Auditabilidade | Mudanças críticas precisam de autor, data, origem e correlação |
| Compatibilidade | Fluxos principais devem funcionar nos aparelhos homologados |
| Acessibilidade | Contraste, legibilidade e mensagens não devem depender apenas de cor |
| Resiliência | App e integrações devem prever perda de rede, retentativa e sincronização posterior |

## Estados e transições

O status exibido deve refletir uma máquina de estados coerente. A interface não pode oferecer uma ação apenas porque o usuário chegou a determinada tela; a ação depende do estado confirmado pela operação.

Exemplo: o QR Code pode existir tecnicamente, mas permanecer indisponível até que a chamada do terminal altere a elegibilidade de acesso.

## Exceções essenciais

- agendamento cancelado durante o deslocamento;
- motorista ou veículo divergente;
- documento ausente, vencido ou não autorizado;
- localização negada ou indisponível;
- check-in fora do pátio ou fora da janela;
- chegada recebida mais de uma vez;
- chamada emitida e posteriormente revogada;
- QR Code expirado, duplicado ou já utilizado;
- indisponibilidade do pátio, plataforma ou terminal;
- evento recebido fora de ordem;
- celular sem conexão durante mudança de etapa.

Uma amostra estruturada está em [requisitos funcionais](../examples/functional-requirements.md) e [regras de negócio](../examples/business-rules.md).
