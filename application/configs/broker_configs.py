mqtt_broker_configs = {
    "HOST": "py-telemetria.azure-devices.net",  # Nome do IoT Hub
    "PORT": 8883,  # Porta obrigatória para o Azure IoT Hub
    "CLIENT_NAME": "teste",  # Deve ser o ID exato do dispositivo cadastrado no Azure IoT Hub
    "KEEPALIVE": 60,  # Tempo de keepalive
    "TOPIC_PUBLISH": "devices/teste/messages/events/",  # 🔹 Tópico correto para enviar mensagens
    "TOPIC_SUBSCRIBE": "devices/teste/messages/devicebound/#",  # 🔹 Tópico correto para receber mensagens
    "API_VERSION": "2021-04-12"  # Mantém compatibilidade com a API do Azure IoT Hub
}






# mqtt_broker_configs = {
#     "HOST": "py-telemetria.azure-devices.net",
#     "PORT": 8883,
#     "CLIENT_NAME": "teste",
#     "KEEPALIVE": 60,
#     "TOPIC": "devices/teste/messages/devicebound/#",
#     "API_VERSION": "2021-04-12"
# }

# mqtt_broker_configs = {
#     "HOST": "py-telemetria.azure-devices.net",
#     "PORT": 8883,
#     "CLIENT_NAME": "teste",
#     "KEEPALIVE": 60,
#     "TOPIC": "devices/teste/messages/events/",
#     "API_VERSION": "2021-04-12"
# }




# mqtt_broker_configs = {
#     "HOST": "py-telemetria.azure-devices.net",  # Nome do seu IoT Hub
#     "PORT": 8883,  # Porta obrigatória para MQTT no Azure
#     "CLIENT_NAME": "teste",  # Deve ser o ID exato do dispositivo cadastrado no IoT Hub
#     "KEEPALIVE": 60,  # Corrigido o nome do parâmetro (antes estava "KEPPALIVE")
#     "TOPIC": "devices/teste/messages/events/",  # Tópico correto para envio de mensagens
#     "API_VERSION": "2021-04-12"  # Mantém compatibilidade com a versão mais recente da API do Azure IoT Hub
# }
