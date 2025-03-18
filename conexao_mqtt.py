import paho.mqtt.client as mqtt
from azure_mqtt_auth import generate_sas_token

MQTT_BROKER = "py-telemetria.azure-devices.net"
MQTT_PORT = 8883
MQTT_TOPIC = "devices/teste/messages/events/"
CLIENT_ID = "teste"
USERNAME = f"{MQTT_BROKER}/{CLIENT_ID}/?api-version=2021-04-12"
PASSWORD = generate_sas_token()

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Conectado ao Azure IoT Hub!")
        client.publish(MQTT_TOPIC, "Nova Mensagem de TEXTO")
    else:
        print(f"Falha na conexão. Código de retorno: {rc}")

client = mqtt.Client(client_id=CLIENT_ID, protocol=mqtt.MQTTv311)
client.username_pw_set(USERNAME, PASSWORD)
client.tls_set()  # Necessário para conexão segura com a porta 8883
client.on_connect = on_connect

client.publish("devices/teste/messages/events/", "Sua mensagem para o Azure IoT Hub")


client.connect(MQTT_BROKER, MQTT_PORT, keepalive=60)
client.loop_forever()
