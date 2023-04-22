# pylint: disable=undefined-variable
# Configuration file for jupyter-lab.
c = get_config()   #noqa

## Set the Access-Control-Allow-Credentials: true header
c.ServerApp.allow_credentials = True
c.ServerApp.allow_origin = '*'
c.ServerApp.allow_remote_access = True
c.ServerApp.password_required = False
c.ServerApp.allow_password_change = True
# c.ServerApp.disable_check_xsrf = True
# c.ServerApp.local_hostnames = ['localhost']

c.ServerApp.ip = '0.0.0.0'
# c.ServerApp.port = 8888

c.ServerApp.notebook_dir = '/var/data'

c.ServerApp.webbrowser_open_new = 0

c.ExtensionApp.open_browser = False
