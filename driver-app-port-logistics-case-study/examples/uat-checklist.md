# Checklist demonstrativo de UAT

[← Voltar ao README](../README.md)

> Modelo reconstruído para portfólio. Deve ser adaptado aos papéis, parâmetros e ambientes de cada organização.

## Identificação

- [ ] Versão/build registrado.
- [ ] Ambiente de homologação confirmado.
- [ ] Dispositivo e sistema operacional registrados.
- [ ] Jornada/agendamento de teste identificado.
- [ ] Papéis dos participantes definidos.
- [ ] Dados de teste fictícios ou autorizados.
- [ ] Sistemas integrados disponíveis.

## Agendamento

- [ ] Agendamento correto aparece para o motorista.
- [ ] Data, hora e fuso estão corretos.
- [ ] Origem, destino e tipo de operação são compreensíveis.
- [ ] Alteração reflete no aplicativo.
- [ ] Cancelamento impede continuidade indevida.
- [ ] Histórico permanece distinguível da jornada ativa.

## Orientações e rota

- [ ] Próximo destino corresponde ao estado atual.
- [ ] Instruções não são ambíguas.
- [ ] Navegação externa abre o local esperado.
- [ ] Redirecionamento substitui a orientação anterior.
- [ ] Lembrete abre o agendamento correto.

## Localização

- [ ] Solicitação de permissão explica a finalidade.
- [ ] Compartilhamento inicia no momento previsto.
- [ ] Posição recente é distinguível de posição desatualizada.
- [ ] Negativa de permissão possui tratamento conhecido.
- [ ] Compartilhamento é encerrado conforme a regra.

## Documentos

- [ ] Lista contém apenas documentos da operação.
- [ ] Tipo e versão são identificáveis.
- [ ] Arquivos abrem no aparelho homologado.
- [ ] Documento revogado deixa de ser acessível.
- [ ] Falha de abertura apresenta mensagem útil.
- [ ] Conteúdo sensível não aparece em logs ou notificações.

## Pátio e check-in

- [ ] Pátio correto é apresentado.
- [ ] Check-in válido é confirmado.
- [ ] Reenvio não duplica a chegada.
- [ ] Status é atualizado nos sistemas consumidores.
- [ ] Check-in inválido apresenta motivo funcional.
- [ ] Saída do pátio permanece vinculada à mesma jornada.

## Chamada e QR Code

- [ ] QR Code permanece indisponível antes da chamada.
- [ ] Chamada válida gera notificação.
- [ ] QR Code é liberado para o agendamento correto.
- [ ] Leitura funciona no equipamento homologado.
- [ ] Credencial expirada é rejeitada.
- [ ] Credencial revogada é rejeitada.
- [ ] Segundo uso é bloqueado quando aplicável.
- [ ] Resultado de validação atualiza o estado da jornada.

## Encerramento da operação

- [ ] Início da descarga ocorre somente após estado permitido.
- [ ] Evento chega ao planejamento.
- [ ] Recebimento físico não é antecipado por geolocalização.
- [ ] Conclusão é exibida ao motorista.
- [ ] Histórico conserva os marcos essenciais.

## Exceções e resiliência

- [ ] Perda e retorno da conexão foram exercitados.
- [ ] Timeout possui tratamento e reprocessamento.
- [ ] Evento duplicado não cria efeito duplicado.
- [ ] Evento fora de ordem não regride o estado.
- [ ] Mensagens de erro não expõem detalhes internos.
- [ ] Suporte consegue localizar a jornada pela correlação.

## Aceite

- [ ] Cenários críticos aprovados.
- [ ] Nenhum defeito crítico aberto.
- [ ] Defeitos altos corrigidos ou com mitigação aprovada.
- [ ] Evidências anexadas e sanitizadas.
- [ ] Pendências residuais registradas e priorizadas.
- [ ] Responsável de negócio aprovou o resultado.
- [ ] Decisão de go/no-go registrada.

### Resultado

- [ ] Aprovado.
- [ ] Aprovado com ressalvas.
- [ ] Reprovado.

**Observações:**<br>
**Responsável pelo aceite:**<br>
**Data:**
