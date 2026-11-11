from netmiko import ConnectHandler
from netmiko.exceptions import NetmikoTimeoutException, NetmikoAuthenticationException

# 1. Definición de parámetros de conexión
device = {
    'device_type': 'cisco_ios',
    'host': '192.168.1.1',
    'username': 'admin',
    'password': 'CiscoPassword123!',
    'port': 22,
}

try:
    # 2. Establecer la conexión SSH
    net_connect = ConnectHandler(**device)
    print(f"Conectado exitosamente a {device['host']}")

    # 3. Ejecución de comandos de lectura
    output_show = net_connect.send_command("show ip interface brief")
    print("--- Estado de Interfaces ---")
    print(output_show)

    # 4. Envío de comandos de configuración
    config_commands = [
        'interface Loopback100',
        'description Interface creada via Python Netmiko',
        'ip address 10.100.100.1 255.255.255.255',
        'no shutdown'
    ]
    output_config = net_connect.send_config_set(config_commands)
    print("--- Aplicando Configuración ---")
    print(output_config)

    # 5. Cierre de sesión
    net_connect.disconnect()

except NetmikoTimeoutException:
    print(f"Error: Tiempo de espera agotado al conectar a {device['host']}")
except NetmikoAuthenticationException:
    print(f"Error: Credenciales incorrectas para {device['host']}")
