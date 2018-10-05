# Chatops Plodindo

Projeto de chatops do LAPPIS para monitoramento do bot Taís.

#### Para rodar o Chatops
 * Entre na pasta rasa
 * Instale o rasa e suas dependencias, em caso de dúvidas, siga o <a href="http://rasa.com/docs/core/installation/">link</a>
 * No terminal, rode o ngrok na porta 5002 pelo seguinte comando:
 ```
 $ ngrok http 5002
 ```
Para instalar o ngrok siga as instruções do <a href="https://ngrok.com/download">link</a>.

* Vá ao arquivo telegram_credentials.yml e preencha com as informações corretas do seu bot do telegram. Para criar seu bot abra o telegram e converse com o @BotFather.

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

As funcionalidades do chatops se encontram no arquivo actions.py.

Até o momento o Plodindo somente faz a verificação se a Taís está online. Verifica pela api do livechat do RocketChat, consultando o status do livechat, online ou offline.


