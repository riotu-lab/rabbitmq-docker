# RabbitMQ Docker
This repo is for RabbitMQ setup with docker compose with MQTT plugin enabled

## Run Docker with Default Config
Run `docker-compose up -d`

## Exporting definitions.json (Optional)
This is an optional step, by default definitions.json is empty.  
`definitions.json` file contains your custom configuration for example, remove default user `guest`. To get `definitions.json` file, follow these steps.
- Run  `docker-compose up`
- From browser access this url [localhost:15672](http://localhost:15672) and use default credintials username `guest` and password `guest`.  
- Make custom changes you want (i.e. create new exchange, add new users, remove default user `guest`, etc...)
- Go to `Overview` tab and then click on `Export definitions` then click on `Download`
- Rename file to `definitions.json` copy file to `rabbitmq/etc/` folder 
- Restart docker-compose

## Configure RabbitMQ
RabbitMQ configuration file can be found in `rabbitmq/etc/rabbitmq.conf`

## RabbitMQ MQTT Plugin
`rabbitmq/etc/enabled_plugins` contains `rabbitmq_mqtt` and `rabbitmq_web_mqtt` to enable RabbitMQ suppport for MQTT.  
The following configuration is required to configure MQTT plugin

**Note: make sure of setting `mqtt.exchange` is the same exchange you are using in the RabbitMQ client (producer/publisher)**.   
```conf
mqtt.listeners.tcp.default = 1883
web_mqtt.tcp.port = 15675

mqtt.allow_anonymous  = true

mqtt.exchange         = psu
# 24 hours by default
mqtt.subscription_ttl = 86400000
mqtt.prefetch         = 10
```

## References

- [Get Started with RabbitMQ on Docker](https://codeburst.io/get-started-with-rabbitmq-on-docker-4428d7f6e46b)
- [MQTT Plugin Docs](https://www.rabbitmq.com/mqtt.html)