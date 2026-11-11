import requests
import time
from requests.auth import HTTPBasicAuth

# Deshabilitar advertencias SSL
requests.packages.urllib3.disable_warnings()

HOST = "sandbox-iosxe-latest-1.cisco.com"
PORT = "443"
USER = "developer"
PASS = "C1sco12345!"

url = f"https://{HOST}:{PORT}/restconf/data/ietf-interfaces:interfaces"
headers = {"Accept": "application/yang-data+json"}
auth = HTTPBasicAuth(USER, PASS)

# 1. Parámetros SRE / SLO
MAX_LATENCY_MS = 1500  # SLO de tiempo de respuesta
NUM_TESTS = 5

successful_calls = 0
total_latency = 0

print(f"--- INICIANDO MONITOREO DE SALUD Y SLI DE RESTCONF EN {HOST} ---")

for i in range(1, NUM_TESTS + 1):
    start_time = time.time()
    try:
        response = requests.get(
            url,
            headers=headers,
            auth=auth,
            verify=False,
            timeout=5
        )
        latency = (time.time() - start_time) * 1000
        
        if response.status_code == 200 and latency <= MAX_LATENCY_MS:
            successful_calls += 1
            print(f"Prueba {i}: OK | Latencia: {latency:.2f} ms")
        else:
            print(f"Prueba {i}: FALLO | Código: {response.status_code} | Latencia: {latency:.2f} ms")
            
        total_latency += latency

    except requests.exceptions.RequestException as e:
        print(f"Prueba {i}: ERROR DE CONEXIÓN - {e}")

# 2. Cálculo de SLI y evaluación de SLO
sli_availability = (successful_calls / NUM_TESTS) * 100
avg_latency = total_latency / NUM_TESTS

print("\n--- RESULTADOS DE AUDITORÍA SRE ---")
print(f"Disponibilidad SLI: {sli_availability:.1f}%")
print(f"Latencia Promedio: {avg_latency:.2f} ms")

if sli_availability >= 80.0:
    print("ESTADO DE LA RED: SALUDABLE (Dentro del Presupuesto de Error)")
else:
    print("ESTADO DE LA RED: ALERTA (Presupuesto de Error Excedido)")
