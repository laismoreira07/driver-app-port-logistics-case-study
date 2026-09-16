# 01. Contexto de negócio

[← Voltar ao README](../README.md)

## Cenário

Uma operação portuária de exportação precisa decidir com antecedência se haverá carga suficiente para cumprir o planejamento de embarque. O estoque fisicamente disponível é apenas parte dessa visão: há cargas programadas, liberadas na origem, em deslocamento ou aguardando em pátios externos.

O desafio consistia em conectar esses marcos ao sistema do terminal sem transformar o motorista em mero mensageiro entre sistemas. O aplicativo deveria orientar sua jornada e, ao mesmo tempo, produzir eventos úteis para a operação.

## Problema central

> Como aumentar a previsibilidade sobre o estoque em trânsito e sincronizar a chegada dos veículos com a capacidade do terminal, oferecendo ao motorista uma jornada digital simples e rastreável?

### Causas observadas

- dados distribuídos entre agendamento, transporte, pátio e terminal;
- atualizações dependentes de ligações, mensagens ou consultas manuais;
- baixa padronização dos marcos da viagem;
- documentos e instruções acessados por canais diferentes;
- fila externa e chamada do terminal nem sempre refletidas em um único fluxo;
- necessidade de validar motorista, veículo, carga e janela antes do acesso.

### Efeitos para o negócio

- menor confiança sobre o volume efetivamente a caminho;
- dificuldade para estimar chegada e organizar descarga;
- maior esforço de acompanhamento operacional;
- risco de veículo chegar antes da capacidade disponível;
- retrabalho para consultar ou reenviar documentos;
- investigação mais lenta quando ocorre uma divergência.

## Objetivos do produto

1. Disponibilizar ao motorista seu agendamento, janela e orientações.
2. Exibir origem, destino e informações de rota.
3. Centralizar documentos associados à operação.
4. Registrar localização e eventos relevantes durante a jornada.
5. Direcionar o motorista ao pátio regulado correspondente.
6. Confirmar check-in e espera de forma digital.
7. Liberar o QR Code somente após a chamada do terminal.
8. Integrar os marcos da jornada ao ecossistema operacional.
9. Apoiar a visão qualificada de estoque em trânsito.
10. Reduzir a dependência de documentos físicos e contatos paralelos.

## Stakeholders

| Grupo | Necessidade principal | Participação no fluxo |
|---|---|---|
| Motoristas | Clareza, praticidade e informações no momento certo | Executam a jornada pelo app |
| Transportadoras | Visibilidade e menor retrabalho | Associam motorista, veículo e carga |
| Operação do pátio | Ordenação de chegadas e registro de permanência | Confirma entrada e saída |
| Operação do terminal | Controle de capacidade, chamada e acesso | Libera veículo e recebe a carga |
| Planejamento logístico/comercial | Visão confiável do físico e do trânsito | Usa eventos para tomada de decisão |
| TI e integrações | Segurança, consistência e suporte | Mantém os fluxos entre sistemas |
| Fornecedor da plataforma | Evolução e funcionamento do produto | Implementa e corrige a solução |
| Business Analyst | Coerência entre problema, requisito e entrega | Orquestra análise e aceite funcional |

## Escopo do case

### Incluído

- jornada do motorista a partir do agendamento;
- acesso a orientações e documentos digitais;
- geolocalização e eventos de viagem;
- integração com pátios regulados;
- check-in, chamada e QR Code;
- integração conceitual com o sistema do terminal;
- testes funcionais, SIT, UAT, piloto e implantação;
- interpretação operacional do estoque em trânsito.

### Fora do escopo

- algoritmos de roteirização;
- contabilidade ou valoração financeira de estoque;
- infraestrutura e código-fonte da plataforma;
- regras aduaneiras completas;
- operação física de balanças, gates ou equipamentos;
- indicadores internos e dados do cliente;
- integração formal com o sistema governamental Porto Sem Papel.

## Princípios de desenho

- **Evento no momento da operação:** registrar cada marco onde ele acontece.
- **Fonte de verdade explícita:** distinguir dado cadastral, status de jornada e recebimento físico.
- **Menor esforço para o motorista:** informação objetiva e acionável.
- **Segurança por padrão:** não expor documentos ou credenciais além do necessário.
- **Tolerância a falhas:** prever conectividade móvel instável e reprocessamento.
- **Rastreabilidade:** correlacionar agendamento, veículo, motorista, carga e eventos.
- **Digital por padrão:** reduzir papel sem eliminar controles e evidências.

## Critérios qualitativos de sucesso

- motorista consegue concluir a jornada sem depender de instruções paralelas;
- operação distingue claramente programado, em trânsito, no pátio e recebido;
- chamada do terminal e habilitação do QR Code permanecem sincronizadas;
- documentos certos aparecem para a operação certa;
- eventos duplicados ou fora de ordem não corrompem o status;
- falhas de integração podem ser identificadas e reprocessadas;
- UAT confirma aderência à rotina dos usuários;
- piloto demonstra funcionamento no aparelho e na rede utilizados em campo.

## Glossário

| Termo | Definição usada no case |
|---|---|
| Agendamento | Reserva de janela para determinada operação, motorista, veículo e carga |
| Estoque em trânsito | Carga comprometida e em deslocamento, ainda não recebida fisicamente |
| Pátio regulado | Área externa utilizada para organizar espera e chamada de veículos |
| Check-in | Registro de chegada do veículo ao ponto previsto |
| Chamada | Liberação operacional emitida pelo terminal para prosseguimento |
| QR Code | Credencial digital de acesso vinculada à jornada e ao estado da operação |
| SIT | Teste integrado entre sistemas |
| UAT | Teste de aceitação conduzido sob a perspectiva do usuário/negócio |
| Hypercare | Período de acompanhamento intensivo após o go-live |
