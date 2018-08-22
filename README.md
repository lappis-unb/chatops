# Chatops

Projeto de chatops do LAPPIS.

#### Para rodar o Chatops
 * Entre na pasta rasa
 * Instale o rasa e suas dependencias, em caso de dúvidas, siga o <a href="http://rasa.com/docs/core/installation/">link</a>
 * Vá ao arquivo actions.py e coloque o seu token do github na linha 38, no lugar de '[PLACE HERE YOUR GITHUB TOKEN]'. Para gerar um token acesse o <a href="https://github.com/settings/tokens">link</a>.

 * No terminal, rode o ngrok na porta 5002 pelo seguinte comando:
 ```
 $ ngrok http 5002
 ```
Para instalar o ngrok siga as instruções do <a href="https://ngrok.com/download">link</a>.

* Vá ao arquivo telegram_credentials.yml e descomente as 3 primeiras linhas e preencha com as informações corretas do seu bot do telegram. Para criar seu bot abra o telegram e converse com o @BotFather.

* Após essas configurações feitas rode os seguintes comandos:
```
$ make train-nlu
$ make train-core
$ make run-telegram
```

O chatops também pode ser usado pelo terminal, pelos seguintes comandos:
```
$ make train-nlu
$ make train-core
$ make run-bash
```

### Funcionalidades do Bot:

Até o momento foram criadas 2 funcionalidades, a de listar issues do github e de criar issues no github. Essas funções estão no arquivo actions.py.

* Listar issues:  
Para listar as issues o usuário teria apenas que solicitar ao bot 'list issues' após o cumprimento.  
Esta funcionalidade lista as issues do repositorio da <a href="https://github.com/lappis-unb/rouana">Rouana</a>.

* Criar issues:  
Para criar uma issue o usuário teria que, após o cumprimento solicitar ao bot 'create issue', dessa forma o bot pergunta o nome da issue e o usuário deveria responder com '/name Nome da Issue' e em resposta o bot pergunta o corpo da issue e o usuário deve responder com '/body Conteúdo da issue'. Após o corpo e nome estabelecidos o bot deve criar a issue e responder com o link da nova issue.  
Esta funcionalidade cria issues em um repositório <a href="https://github.com/gabibguedes/teste">teste</a>.

### Problemas:

O chatops ainda apresenta muitos erros para seguir um fluxo, especialmente o de criar issue que necessita de varias actions sendo chamadas uma após a outra.
