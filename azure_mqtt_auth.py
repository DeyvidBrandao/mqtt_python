import time
import base64
import hmac
import hashlib
import urllib.parse
from application.configs.broker_configs import mqtt_broker_configs  # Importa as configs

IOT_HUB_HOST = mqtt_broker_configs["HOST"]
SHARED_ACCESS_KEY = "Li0osoLfN8Y5smEbWrp+sn8JdLDQkornMDFc0XWhHrs="  # Certifique-se que é a chave correta

def generate_sas_token(device_id):
    """Gera um token SAS para autenticação no Azure IoT Hub."""
    expiry = int(time.time()) + 3600  # Token válido por 1 hora
    uri = f"{IOT_HUB_HOST}/devices/{device_id}"
    sign_key = f"{uri}\n{expiry}".encode('utf-8')

    key_bytes = base64.b64decode(SHARED_ACCESS_KEY.encode('utf-8'))
    signature = base64.b64encode(hmac.new(key_bytes, sign_key, hashlib.sha256).digest())

    sas_token = (
        f"SharedAccessSignature sr={urllib.parse.quote(uri)}"
        f"&sig={urllib.parse.quote(signature.decode())}&se={expiry}"
    )
    return sas_token


#
#
# Funciona
#
# import time
# import base64
# import hmac
# import hashlib
# import urllib.parse
#
# IOT_HUB_HOST = "py-telemetria.azure-devices.net"
# DEVICE_ID = "teste"
# SHARED_ACCESS_KEY = "Li0osoLfN8Y5smEbWrp+sn8JdLDQkornMDFc0XWhHrs="
#
#
# def generate_sas_token():
#     expiry = int(time.time()) + 3600  # Expira em 1 hora
#     uri = f"{IOT_HUB_HOST}/devices/{DEVICE_ID}"
#     sign_key = f"{uri}\n{expiry}"
#
#     signature = base64.b64encode(
#         hmac.new(base64.b64decode(SHARED_ACCESS_KEY), sign_key.encode('utf-8'), hashlib.sha256).digest()
#     )
#
#     sas_token = f"SharedAccessSignature sr={urllib.parse.quote(uri)}&sig={urllib.parse.quote(signature.decode())}&se={expiry}"
#     return sas_token
#
# print(generate_sas_token())
