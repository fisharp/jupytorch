#!/opt/venv/bin/python

import os
import sys
import json

#pylint: disable=import-error
from jupyter_server.auth.security import passwd

DEFAULT_CONFIG_FILE_PATH = "~/.jupyter"
CONFIG_FILE_NAME = "jupyter_server_config.json"
DEFAULT_COMMAND = "jupyter lab"

args = sys.argv[1:] or DEFAULT_COMMAND.split()

CONFIG_FILE_PATH = os.environ.get('JUPYTER_CONFIG_DIR') or DEFAULT_CONFIG_FILE_PATH

# Grab the Login Password from environment
# and inmediately remove it (if found)
PWD = os.environ.pop('JUPYTER_PASSWORD', None)

configs, appconf = { }, { }

print ("⚡ Starting Jupytorch Docker Entrypoint")

if PWD:
    print("""⚠️ Plain password was found as environment variable
    Removed already from current environment""")
    print("⛓️ Setting up the proper hash instead...")
    appconf["password"] = passwd(PWD)
    configs['ServerApp'] = appconf
else:
    print("⌨️  No password found")

if configs:
    # Serializing the config object
    json_obj = json.dumps(configs, indent=4)
    # Written onto the proper file/path
    conf_file_path = os.path.join(CONFIG_FILE_PATH, CONFIG_FILE_NAME)
    with open(conf_file_path, "w", encoding="UTF") as config_file:
        config_file.write(json_obj + '\n')
        print("✅ Configuration File properly saved in ", conf_file_path)

print("✨ Entrypoint Completed.")

# Start Jupyter Service or run CMD (if provided)

if args[:2] == ["jupyter", "lab"]:
    print("⌛ Starting Jupyter Lab Server...")
    # system("python -m jupyter lab")

# Replace the current process by requested CMD
# (equivalent to bash: exec "$@")
os.execvp(args[0], args)
