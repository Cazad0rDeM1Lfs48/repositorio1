import yaml
from jinja2 import Environment, FileSystemLoader

# 1. Cargar las variables desde el archivo YAML
with open("vars_interfaces.yml", "r") as file:
    variables = yaml.safe_load(file)

# 2. Configurar el entorno de Jinja2
env = Environment(loader=FileSystemLoader("."))
template = env.get_template("cisco_ios.j2")

# 3. Renderizar la plantilla pasando los datos
config_final = template.render(variables)

print("--- CONFIGURACIÓN CISCO IOS GENERADA ---")
print(config_final)

# 4. Guardar la configuración resultante en un archivo .txt
with open("config_R1.txt", "w") as out_file:
    out_file.write(config_final)
