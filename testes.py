import paho.mqtt.client as mqtt
from azure_mqtt_auth import generate_sas_token

client.publish("devices/teste/messages/events/", "Sua mensagem para o Azure IoT Hub")





# import base64
#
# SHARED_ACCESS_KEY = "HostName=py-telemetria.azure-devices.net;DeviceId=teste;SharedAccessKey=Li0osoLfN8Y5smEbWrp+sn8JdLDQkornMDFc0XWhHrs="
#
# try:
#     base64.b64decode(SHARED_ACCESS_KEY)  # Testa a conversão
#     print("Chave válida!")
# except Exception as e:
#     print("Erro na chave:", e)


#
# import paho.mqtt.client as mqtt
# from azure_mqtt_auth import generate_sas_token
#
# MQTT_BROKER = "py-telemetria.azure-devices.net"
# MQTT_PORT = 8883
# CLIENT_ID = "teste"
# USERNAME = f"{MQTT_BROKER}/{CLIENT_ID}/?api-version=2021-04-12"
# PASSWORD = generate_sas_token()
# TOPIC = "devices/teste/messages/events/"
#
# client = mqtt.Client(client_id=CLIENT_ID, protocol=mqtt.MQTTv311)
# client.username_pw_set(USERNAME, PASSWORD)
# client.tls_set()
#
# client.connect(MQTT_BROKER, MQTT_PORT, keepalive=60)
#
# client.publish(TOPIC, '{"mensagem": "teste de publicação"}')
# print("Mensagem publicada!")
#
# client.disconnect()
