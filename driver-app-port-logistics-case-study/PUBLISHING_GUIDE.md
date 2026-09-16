# Guia de publicação no GitHub

## Identidade recomendada

**Nome do repositório**

`driver-app-port-logistics-case-study`

**Descrição curta**

> Case de Business Analysis em logística portuária: estoque em trânsito, app de motoristas, agendamento, geolocalização, documentos digitais, QR Code, APIs REST, SIT/UAT e go-live.

**Topics**

`business-analysis` `requirements-engineering` `logistics` `supply-chain` `port-operations` `rest-api` `uat` `mobile-testing` `qr-code` `geolocation` `case-study`

## Publicação

1. Crie um repositório público vazio com o nome sugerido.
2. Não marque a criação automática de README, licença ou `.gitignore`.
3. Descompacte este pacote e abra um terminal dentro da pasta do projeto.
4. Execute os comandos abaixo, substituindo a URL pelo endereço do seu repositório.

```bash
git init
git add .
git commit -m "docs: publish anonymized driver app case study"
git branch -M main
git remote add origin https://github.com/SEU-USUARIO/driver-app-port-logistics-case-study.git
git push -u origin main
```

## Revisão obrigatória antes do push

- Execute `python3 tools/privacy_check.py`.
- Confirme que a saída termina com `PUBLICATION CHECK PASSED`.
- Não copie a pasta de fontes originais para o repositório.
- Não adicione PDFs, vídeo original, screenshots reais ou especificações integrais de API.
- Revise o histórico com `git status` e `git diff --cached --stat`.
- Abra o `README.md` na pré-visualização do GitHub e confira os diagramas Mermaid e o GIF.
- Em `Settings > General > Social preview`, use `assets/demo-flow-preview.png` como imagem de compartilhamento.

## Destaque no perfil

Depois da publicação, fixe o repositório no perfil. Uma descrição curta para o card:

> Da necessidade operacional ao go-live: requisitos, integrações, testes e piloto de um app para a jornada rodoviária-portuária.

## Texto curto para compartilhar

> Publiquei um novo case de portfólio sobre minha atuação em um projeto real de logística portuária. O material mostra como traduzi a necessidade de visibilidade do estoque em trânsito em requisitos, regras, integrações e cenários de teste para uma jornada mobile com agendamento, geolocalização, documentos digitais e QR Code. Todo o conteúdo foi reconstruído e anonimizado para preservar o cliente e a propriedade intelectual da solução.
