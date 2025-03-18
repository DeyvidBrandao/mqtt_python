import json
from application.configs.broker_configs import mqtt_broker_configs


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print(f"✅ Cliente Conectado com sucesso!")
        client.subscribe(mqtt_broker_configs["TOPIC_SUBSCRIBE"])  # 🔹 Agora usa TOPIC_SUBSCRIBE
    else:
        print(f"❌ Erro ao conectar! Código={rc}")


def on_subscribe(client, userdata, mid, granted_qos):
    print(f"📡 Cliente Subscrito no tópico: {mqtt_broker_configs['TOPIC_SUBSCRIBE']}")
    print(f"📊 QoS: {granted_qos}")


def on_message(client, userdata, message):
    """Callback acionado quando uma mensagem é recebida."""
    try:
        payload = message.payload.decode("utf-8").strip()  # Decodifica e remove espaços extras

        # 🔹 Verifica se a mensagem é JSON ou texto simples
        if payload.startswith("{") and payload.endswith("}"):
            data = json.loads(payload)  # Converte para JSON
            print("\n📩 **Nova Mensagem Recebida:**")
            print(f"📜 Payload JSON: {json.dumps(data, indent=2)}")  # Exibe JSON formatado
        else:
            print("\n📩 **Nova Mensagem de Texto Recebida:**")
            print(f"📜 Texto: {payload}")  # Exibe mensagem de texto simples

    except json.JSONDecodeError:
        print(f"⚠ Erro ao processar mensagem recebida: {payload}")

# import json
# from application.configs.broker_configs import mqtt_broker_configs
#
#
# def on_connect(client, userdata, flags, rc):
#     if rc == 0:
#         print(f"✅ Cliente Conectado com sucesso!")
#         client.subscribe(mqtt_broker_configs["TOPIC"])
#     else:
#         print(f"❌ Erro ao conectar! Código={rc}")
#
#
# def on_subscribe(client, userdata, mid, granted_qos):
#     print(f"📡 Cliente Subscrito no tópico: {mqtt_broker_configs['TOPIC']}")
#     print(f"📊 QoS: {granted_qos}")
#
#
# def on_message(client, userdata, message):
#     """Callback acionado quando uma mensagem é recebida."""
#     try:
#         payload = message.payload.decode("utf-8")  # Decodifica a mensagem recebida
#         data = json.loads(payload)  # Tenta converter para JSON
#
#         print("\n📩 **Nova Mensagem Recebida:**")
#         print(f"📜 Payload: {json.dumps(data, indent=2)}")  # Exibe a mensagem formatada
#     except json.JSONDecodeError:
#         print(f"⚠ Mensagem recebida não está em JSON: {payload}")

# funcionou com lixo na exibição
# import json
# from application.configs.broker_configs import mqtt_broker_configs
#
# def on_connect(client, userdata, flags, rc):
#     if rc == 0:
#         print(f"✅ Cliente Conectado com sucesso: {client}")
#         client.subscribe(mqtt_broker_configs["TOPIC"])
#     else:
#         print(f"❌ Erro ao conectar! Código={rc}")
#
# def on_subscribe(client, userdata, mid, granted_qos):
#     print(f"📡 Cliente Subscrito no tópico: {mqtt_broker_configs['TOPIC']}")
#     print(f"📊 QoS: {granted_qos}")
#
# def on_message(client, userdata, message):
#     """Callback acionado quando uma mensagem é recebida."""
#     try:
#         payload = message.payload.decode("utf-8")  # Decodifica a mensagem
#         data = json.loads(payload)  # Tenta converter para JSON
#         print(f"📩 Mensagem Recebida no tópico {message.topic}: {json.dumps(data, indent=2)}")
#     except json.JSONDecodeError:
#         print(f"⚠ Mensagem recebida não está em JSON: {payload}")








# Anterior usando mosquito
# from application.configs.broker_configs import mqtt_broker_configs
#
# def on_connect(client, userdata, flags, rc):
#     if rc == 0:
#         print(f'Cliente Conectado com sucesso: {client}')
#         client.subscribe(mqtt_broker_configs["TOPIC"])
#     else:
#         print(f'Erro ao me conectar! codigo={rc}')
#
#
# def on_subscribe(client, userdata, mid, granted_qos):
#     print(f'Cliente Subscribed at {mqtt_broker_configs["TOPIC"]}')
#     print(f'QOS: {granted_qos}')
#
#
# def on_message(client, userdata, message):
#     print('Mensagem recebida!')
#     print(client)
#     print(message.payload)
