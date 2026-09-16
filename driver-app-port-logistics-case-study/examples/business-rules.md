# Regras de negócio conceituais

[← Voltar ao README](../README.md)

> Regras reconstruídas e parametrizações omitidas. O objetivo é demonstrar raciocínio de análise, não reproduzir a configuração do cliente.

| ID | Regra | Justificativa |
|---|---|---|
| BR-001 | Somente agendamento ativo e confirmado pode iniciar a jornada. | Evitar rastreamento ou acesso associado a operação cancelada. |
| BR-002 | Motorista e veículo devem estar vinculados ao agendamento vigente. | Preservar identidade e rastreabilidade. |
| BR-003 | Alteração de motorista ou veículo exige nova validação antes do acesso. | Impedir uso de credencial emitida para outro contexto. |
| BR-004 | Localização representa posição reportada, não recebimento físico da carga. | Evitar antecipação indevida de estoque. |
| BR-005 | Posição deve carregar recência e qualidade; ausência de atualização não equivale a veículo parado. | Diferenciar falta de sinal de comportamento operacional. |
| BR-006 | O check-in deve estar associado ao pátio e à jornada corretos. | Evitar entrada registrada no local incorreto. |
| BR-007 | Reenvio do mesmo check-in não pode gerar uma segunda chegada. | Garantir idempotência. |
| BR-008 | O QR Code só pode ser disponibilizado após chamada válida do terminal. | Sincronizar acesso com capacidade operacional. |
| BR-009 | Cancelamento ou revogação posterior deve invalidar a credencial ainda não consumida. | Impedir acesso fora do estado autorizado. |
| BR-010 | Credencial expirada, incompatível ou já consumida deve ser rejeitada. | Preservar segurança e unicidade do acesso. |
| BR-011 | Documento deve ser exibido somente a usuário autorizado e à jornada correspondente. | Proteger informação operacional e pessoal. |
| BR-012 | Nova versão válida de documento deve ser distinguível da anterior. | Evitar apresentação de informação desatualizada. |
| BR-013 | Evento crítico deve possuir identificador único e correlação da jornada. | Permitir auditoria e reprocessamento seguro. |
| BR-014 | Data de ocorrência e data de processamento devem ser preservadas separadamente. | Tratar atraso de rede e eventos fora de ordem. |
| BR-015 | Transição de estado deve respeitar a sequência permitida ou uma exceção autorizada. | Evitar estados impossíveis. |
| BR-016 | A carga só compõe o estoque físico após confirmação do marco de recebimento definido pelo terminal. | Separar trânsito de disponibilidade física. |
| BR-017 | Agendamento cancelado ou encerrado não compõe a visão ativa de estoque em trânsito. | Evitar superestimação do volume esperado. |
| BR-018 | Falha de integração deve manter o último estado confirmado e gerar pendência; não deve inventar sucesso. | Preservar consistência e transparência. |
| BR-019 | Logs funcionais não devem registrar tokens, documentos completos ou dados pessoais desnecessários. | Aplicar segurança e minimização de dados. |
| BR-020 | Permissão de localização deve ter finalidade, período e alternativa operacional definidos. | Tratar privacidade e consentimento. |

## Matriz de elegibilidade do QR Code

| Agendamento | Check-in | Chamada | Credencial | Resultado esperado |
|---|---|---|---|---|
| Ativo | Confirmado | Não emitida | Inexistente | Aguardar; QR indisponível |
| Ativo | Confirmado | Emitida | Válida | Permitir apresentação/validação |
| Cancelado | Qualquer | Qualquer | Qualquer | Bloquear e revogar |
| Ativo | Não confirmado | Emitida por exceção | Válida | Aplicar regra de exceção autorizada e auditada |
| Ativo | Confirmado | Revogada | Válida anteriormente | Bloquear e atualizar app |
| Ativo | Confirmado | Emitida | Expirada | Bloquear e orientar tratamento |
| Ativo | Confirmado | Emitida | Já consumida | Bloquear segundo uso |

## Regras de composição da visão de estoque

- **Programado:** possui agendamento válido, mas ainda sem evidência de viagem iniciada.
- **Em trânsito:** jornada iniciada com atualização válida ou marco equivalente.
- **No pátio:** chegada confirmada pelo sistema responsável.
- **Chamado:** liberação emitida pelo terminal.
- **Em descarga:** acesso validado e operação iniciada.
- **Recebido:** marco físico confirmado pelo sistema do terminal.
- **Exceção:** estado não confiável para consolidação automática sem análise.

Parâmetros de tempo, tolerância, volume e exceção não são publicados.
