import requests
import json
from requests.auth import HTTPBasicAuth

# Deshabilitar advertencias de certificados SSL autofirmados
requests.packages.urllib3.disable_warnings()

# 1. Parámetros de la API RESTCONF
url = "https://192.168.1.1/restconf/data/ietf-interfaces:interfaces"
headers = {
    "Accept": "application/yang-data+json",
    "Content-Type": "application/yang-data+json"
}
auth = HTTPBasicAuth("admin", "C1scoPassword12345!")

try:
    # 2. Petición GET HTTP
    response = requests.get(
        url,
        headers=headers,
        auth=auth,
        verify=False  # Ignorar verificación SSL en entorno de lab
    )

    # 3. Validación del código de respuesta
    if response.status_code == 200:
        data = response.json()
        interfaces = data["ietf-interfaces:interfaces"]["interface"]
        
        print(f"{'Nombre':<20} {'Tipo':<30} {'Habilitada':<10}")
        print("-" * 60)
        for iface in interfaces:
            name = iface.get("name", "N/A")
            if_type = iface.get("type", "N/A")
            enabled = iface.get("enabled", False)
            print(f"{name:<20} {if_type:<30} {str(enabled):<10}")
    else:
        print(f"Error HTTP {response.status_code}: {response.text}")

except requests.exceptions.RequestException as e:
    print(f"Error de conexión: {e}")
