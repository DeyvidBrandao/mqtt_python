import paho.mqtt.client as mqtt
import ssl
from application.configs.broker_configs import mqtt_broker_configs
from application.main.mqtt_connection.callbacks import on_connect, on_subscribe, on_message
from azure_mqtt_auth import generate_sas_token

class MqttClientConnection:
    def __init__(self, broker_ip: str, port: int, client_name: str, keepalive=60):
        self.__broker_ip = broker_ip
        self.__port = port
        self.__client_name = client_name
        self.__keepalive = keepalive
        self.__mqtt_client = None

    def start_connection(self):
        print("🔄 Iniciando conexão com Azure IoT Hub...")

        mqtt_client = mqtt.Client(client_id=self.__client_name, protocol=mqtt.MQTTv311)

        # Gerar o SAS Token e configurar autenticação
        username = f"{self.__broker_ip}/{self.__client_name}/?api-version=2021-04-12"
        password = generate_sas_token(self.__client_name)  # Gera o token SAS para o dispositivo

        mqtt_client.username_pw_set(username, password)

        # Configurar TLS
        mqtt_client.tls_set(cert_reqs=ssl.CERT_REQUIRED)

        # Definir Callbacks
        mqtt_client.on_connect = on_connect
        mqtt_client.on_subscribe = on_subscribe
        mqtt_client.on_message = on_message

        # Conectar ao Azure IoT Hub
        mqtt_client.connect(host=self.__broker_ip, port=self.__port, keepalive=self.__keepalive)

        self.__mqtt_client = mqtt_client
        self.__mqtt_client.loop_start()

    def end_connection(self):
        try:
            self.__mqtt_client.loop_stop()
            self.__mqtt_client.disconnect()
            print("🔌 Desconectado do Azure IoT Hub.")
            return True
        except Exception as e:
            print(f"⚠ Erro ao desconectar: {e}")
            return False





















class MqttClientConnection:
    def __init__(self, broker_ip: str, port: int, client_name: str, keepalive=60):
        self.__broker_ip = broker_ip
        self.__port = port
        self.__client_name = client_name
        self.__keepalive = keepalive
        self.__mqtt_client = None

    def start_connection(self):
        print("🔄 Iniciando conexão com Azure IoT Hub...")

        mqtt_client = mqtt.Client(client_id=self.__client_name, protocol=mqtt.MQTTv311)

        # Definir autenticação
        username = f"{self.__broker_ip}/{self.__client_name}/?api-version=2021-04-12"
        password = generate_sas_token(self.__client_name)  # Gera o token SAS
        mqtt_client.username_pw_set(username, password)

        # Configurar TLS
        mqtt_client.tls_set(cert_reqs=ssl.CERT_REQUIRED)

        # Definir Callbacks
        mqtt_client.on_connect = on_connect
        mqtt_client.on_subscribe = on_subscribe
        mqtt_client.on_message = on_message

        # Conectar ao Azure IoT Hub
        mqtt_client.connect(host=self.__broker_ip, port=self.__port, keepalive=self.__keepalive)

        self.__mqtt_client = mqtt_client
        self.__mqtt_client.loop_start()

    def end_connection(self):
        try:
            self.__mqtt_client.loop_stop()
            self.__mqtt_client.disconnect()
            print("🔌 Desconectado do Azure IoT Hub.")
            return True
        except Exception as e:
            print(f"⚠ Erro ao desconectar: {e}")
            return False














# import paho.mqtt.client as mqtt
# from .callbacks import on_connect, on_subscribe, on_message
#
# class MqttClientConnection:
#     def __init__(self, broker_ip: str, port: int, client_name: str, keepalive=60):
#         self.__broker_ip = broker_ip
#         self.__port = port
#         self.__client_name = client_name
#         self.__keepalive = keepalive
#         self.__mqtt_client = None
#
#     def start_connection(self):
#         mqtt_client = mqtt.Client(self.__client_name)
#
#         # callbacks
#         mqtt_client.on_connect = on_connect
#         mqtt_client.on_subscribe = on_subscribe
#         mqtt_client.on_message = on_message
#
#         mqtt_client.connect(host=self.__broker_ip, port=self.__port, keepalive=self.__keepalive)
#         self.__mqtt_client = mqtt_client
#         self.__mqtt_client.loop_start()
#
#     def end_connection(self):
#         try:
#             self.__mqtt_client.loop_stop()
#             self.__mqtt_client.disconnect()
#             return True
#         except:
#             return False