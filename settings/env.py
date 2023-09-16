import os
import environ

# get root
root = environ.Path(__file__) - 2

# get project root
ROOT_DIR = root()
BASE_DIR = ROOT_DIR
PROJECT_ROOT_DIR = ROOT_DIR

# ===============================
# env setup
# -------------------------------
# read the env
env = environ.Env()
client_env = env.str('CLIENT_ENV', 'dev')
client_env_file_path = env.str('ENV_FILE', os.path.join(PROJECT_ROOT_DIR, 'conf', f'{client_env}.conf'))
environ.Env.read_env(client_env_file_path)
