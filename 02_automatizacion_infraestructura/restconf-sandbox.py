import requests
import json
from requests.auth import HTTPBasicAuth

# Deshabilitar advertencias de certificados SSL autofirmados
requests.packages.urllib3.disable_warnings()

# 1. Credenciales y Endpoint del Sandbox de Cisco DevNet
HOST = "sandbox-iosxe-latest-1.cisco.com"
PORT = "443"
USER = "developer"
PASS = "C1sco12345!"

url = f"https://{HOST}:{PORT}/restconf/data/ietf-interfaces:interfaces"

headers = {
    "Accept": "application/yang-data+json",
    "Content-Type": "application/yang-data+json"
}

try:
    # 2. Realizar la petición GET
    response = requests.get(
        url,
        headers=headers,
        auth=HTTPBasicAuth(USER, PASS),
        verify=False
    )

    # 3. Validar y procesar la respuesta en formato JSON
    if response.status_code == 200:
        data = response.json()
        print("--- CONFIGURACIÓN DE INTERFACES OBTENIDA VIA RESTCONF ---")
        print(json.dumps(data, indent=4))
    else:
        print(f"Error en la petición: Código {response.status_code}")
        print(response.text)

except requests.exceptions.RequestException as err:
    print(f"Error de conexión con el Sandbox: {err}")
