# Chatops Plodindo

Projeto de chatops do LAPPIS para monitoramento do bot Taís.

## Utilizando Docker

* Atualize as variáveis de ambiente no `docker-compose.yml`

* `bot`:

```yml
- TELEGRAM_ACCESS_TOKEN
- TELEGRAM_BOT_NAME
- TELEGRAM_WEBHOOK_URL
```

* `actions`:

```
- BOT_USERNAME
- BOT_PASSWORD
- BOT_URL
- BOT_SSL
```

* Execute o container do `rasa-core-sdk` em background:

```shell
sudo docker-compose up -d actions
```

* Execute o container do `plodindo`

```shell
sudo docker-compose up bot
```

## Instalação

```sh
pip install -r requirements.txt
```

## Usando Chatops localmente

* Entre na pasta `bot`

```sh
cd bot/
```

* Instale o ngrok utilizando as instruções do <a href="https://ngrok.com/download">link</a>.

* No terminal, rode o ngrok na porta 5002 pelo seguinte comando:

```sh
ngrok http 5002
```

* Vá ao arquivo `telegram_credentials.yml` e preencha com as informações corretas do seu bot do telegram. Para criar seu bot abra o telegram e converse com o @BotFather.

* Execute o servidor de custom actions:

```sh
make run-actions
```

* Após essas configurações feitas execute os seguintes comandos:

```sh
make train-nlu
make train-core
make run-telegram
```

* O chatops também pode ser usado pelo terminal, pelos seguintes comandos:

```sh
make train-nlu
make train-core
make run-bash
```

## Funcionalidades do Bot:

As funcionalidades extras do chatops se encontram no arquivo `actions.py`

* Verficação se a Taís está online. 

Verifica pela api do livechat do RocketChat, consultando o status do livechat, online ou offline.

## Referências

[RASA Core 11 and Rasa Core SDK](https://www.youtube.com/watch?v=5gSZ_ZcrbRY&t=578s)
