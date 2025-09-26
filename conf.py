import yaml
import time
import sys
from jinja2 import Environment, FileSystemLoader

def generate_apache_config(template_path, data_path, output_path):
    env = Environment(loader=FileSystemLoader('.'), trim_blocks=True, lstrip_blocks=True)
    template = env.get_template(template_path)

    with open(data_path, 'r') as f:
        data = yaml.safe_load(f)

    rendered_config = template.render(data)

    with open(output_path, 'w') as f:
        return f.write(rendered_config)

if __name__ == "__main__":
    try:
        generate_apache_config('vhosts.j2', 'data.yml', 'vhosts.conf')
        print("Configuration file 'vhosts.conf' generated successfully.")
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)
        sys.exit(1)
