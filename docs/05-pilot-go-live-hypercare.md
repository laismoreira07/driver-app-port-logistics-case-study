# 05. Do piloto ao hypercare

[← Voltar ao README](../README.md)

## Por que o piloto foi decisivo

Em uma solução ligada à operação física, homologar apenas por resposta de API ou tela de ambiente controlado é insuficiente. O piloto permite observar a jornada no tipo de aparelho, conexão e sequência de uso que o motorista encontrará.

## Preparação do piloto

- definir jornada e agendamento fictício/controlado;
- validar usuário, aparelho, versão e permissões;
- confirmar disponibilidade dos sistemas integrados;
- alinhar janela e responsáveis pela observação;
- preparar evidências sem dados pessoais desnecessários;
- estabelecer canal de suporte e critério de interrupção;
- separar defeito de produto, dado, integração e ambiente.

## Roteiro principal

1. Instalar/atualizar o aplicativo no dispositivo homologado.
2. Autenticar com perfil autorizado.
3. Confirmar recebimento do agendamento.
4. Revisar janela, origem, destino e instruções.
5. Abrir os documentos associados.
6. Iniciar a jornada e validar permissões de localização.
7. Registrar chegada/check-in no ponto previsto.
8. Confirmar que o QR Code ainda não está liberado.
9. Simular/receber a chamada do terminal.
10. Confirmar notificação e liberação do QR Code.
11. Validar leitura e mudança de etapa.
12. Confirmar sincronização dos eventos nos sistemas envolvidos.

## Evidência sem exposição

Uma boa evidência não precisa revelar dado real. Para cada teste, bastam:

- identificador do cenário;
- versão e ambiente;
- horário da execução;
- resultado esperado e observado;
- captura recortada/sanitizada quando necessária;
- identificador técnico mascarado para correlação;
- conclusão, defeito ou aceite.

## Go/no-go

| Dimensão | Pergunta de decisão |
|---|---|
| Negócio | O fluxo crítico atende à operação? |
| Qualidade | Há defeito crítico ou alto sem mitigação? |
| Integração | Os eventos chegam, correlacionam e podem ser reprocessados? |
| Segurança | Acesso, documentos e QR respeitam autorização? |
| Operação | Usuários, suporte e contingência estão preparados? |
| Dados | Estados iniciais e cadastros necessários foram conferidos? |
| Comunicação | Motoristas e equipes sabem o que muda e onde pedir ajuda? |

## Go-live

Durante a implantação, o Business Analyst funciona como ponte entre relato operacional e diagnóstico técnico:

- acompanha o caminho crítico;
- valida se o sintoma é reproduzível;
- confirma regra e impacto;
- organiza prioridade com operação e fornecedor;
- assegura que correções sejam retestadas;
- mantém registro das decisões;
- evita que workaround temporário se torne regra permanente sem análise.

## Hypercare

O período de estabilização deve ter janela definida, responsáveis e critérios de saída.

### Indicadores operacionais sugeridos

- agendamentos disponibilizados com sucesso;
- tempo entre chamada e notificação no app;
- taxa de check-in integrado;
- QR Codes emitidos e validados;
- erros de leitura ou credencial expirada;
- documentos abertos com sucesso;
- eventos pendentes de reprocessamento;
- divergências entre status dos sistemas;
- incidentes por severidade e tempo de resolução;
- contatos de suporte por etapa da jornada.

Esses indicadores são recomendações de governança. O repositório não publica valores do projeto real.

## Encerramento do hypercare

- estabilidade do caminho crítico por período acordado;
- ausência de incidente crítico aberto;
- backlog residual priorizado;
- documentação e conhecimento transferidos ao suporte;
- dashboards/logs acessíveis aos responsáveis;
- responsáveis por melhoria contínua definidos;
- aceite formal do encerramento da fase intensiva.
