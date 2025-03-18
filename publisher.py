import paho.mqtt.client as mqtt
import json
from azure_mqtt_auth import generate_sas_token
from application.configs.broker_configs import mqtt_broker_configs

# Configuração do IoT Hub
MQTT_BROKER = mqtt_broker_configs["HOST"]
MQTT_PORT = mqtt_broker_configs["PORT"]
CLIENT_ID = mqtt_broker_configs["CLIENT_NAME"]
MQTT_TOPIC = mqtt_broker_configs["TOPIC_PUBLISH"]  # 🔹 Agora usa TOPIC_PUBLISH

# Gerar o token de autenticação
USERNAME = f"{MQTT_BROKER}/{CLIENT_ID}/?api-version=2021-04-12"
PASSWORD = generate_sas_token(CLIENT_ID)

def on_publish(client, userdata, mid):
    print(f"📤 Mensagem enviada com sucesso! MID: {mid}")

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("✅ Conectado ao Azure IoT Hub!")
    else:
        print(f"❌ Falha na conexão. Código de retorno: {rc}")

# Criar cliente MQTT
mqtt_client = mqtt.Client(client_id=CLIENT_ID, protocol=mqtt.MQTTv311)
mqtt_client.username_pw_set(USERNAME, PASSWORD)
mqtt_client.tls_set()

# Definir callbacks
mqtt_client.on_connect = on_connect
mqtt_client.on_publish = on_publish

# Conectar ao Azure IoT Hub
print("🔄 Conectando ao Azure IoT Hub...")
mqtt_client.connect(MQTT_BROKER, MQTT_PORT, keepalive=60)

# Criar mensagem JSON
mensagem = {
    "temperatura": 22.5,
    "umidade": 60,
    "status": "ok"
}

# Publicar mensagem no Azure IoT Hub
payload = json.dumps(mensagem)
result = mqtt_client.publish(MQTT_TOPIC, payload, qos=1)

print(f"✅ Tentando publicar mensagem: {payload}")
print(f"📌 Status da publicação: {result.rc}")

# Loop para garantir envio antes de encerrar
mqtt_client.loop_start()
mqtt_client.loop_stop()
mqtt_client.disconnect()








# import paho.mqtt.client as mqtt
# import json
# from application.configs.broker_configs import mqtt_broker_configs
# from azure_mqtt_auth import generate_sas_token
# import logging
#
# # Configuração do log detalhado
# logging.basicConfig(level=logging.DEBUG)
#
# # Configuração do IoT Hub
# MQTT_BROKER = mqtt_broker_configs["HOST"]
# MQTT_PORT = mqtt_broker_configs["PORT"]
# CLIENT_ID = mqtt_broker_configs["CLIENT_NAME"]
# MQTT_TOPIC = mqtt_broker_configs["TOPIC"]
#
# # Gerar o token de autenticação
# USERNAME = f"{MQTT_BROKER}/{CLIENT_ID}/?api-version=2021-04-12"
# PASSWORD = generate_sas_token(CLIENT_ID)
#
# def on_publish(client, userdata, mid):
#     print(f"📤 Mensagem enviada com sucesso! MID: {mid}")
#
# def on_connect(client, userdata, flags, rc):
#     if rc == 0:
#         print("✅ Conectado ao Azure IoT Hub!")
#     else:
#         print(f"❌ Falha na conexão. Código de retorno: {rc}")
#
# # Criar cliente MQTT
# mqtt_client = mqtt.Client(client_id=CLIENT_ID, protocol=mqtt.MQTTv311)
# mqtt_client.username_pw_set(USERNAME, PASSWORD)
# mqtt_client.tls_set()
#
# # Definir callbacks
# mqtt_client.on_connect = on_connect
# mqtt_client.on_publish = on_publish
#
# # Conectar ao Azure IoT Hub
# print("🔄 Conectando ao Azure IoT Hub...")
# mqtt_client.connect(MQTT_BROKER, MQTT_PORT, keepalive=60)
#
# # Criar mensagem JSON
# mensagem = {
#     "temperatura": 22.5,
#     "umidade": 60,
#     "status": "ok"
# }
#
# # Publicar mensagem no Azure IoT Hub
# payload = json.dumps(mensagem)
# result = mqtt_client.publish(MQTT_TOPIC, payload, qos=1)
#
# print(f"✅ Tentando publicar mensagem: {payload}")
# print(f"📌 Status da publicação: {result.rc}")
#
# # Loop para garantir que a mensagem é enviada antes de encerrar
# mqtt_client.loop_start()
# mqtt_client.loop_stop()
# mqtt_client.disconnect()
