
import time
import random
import subprocess
from urllib import request


def run_streamlit(script_file, env=None, timeout=15, port=None):
    """
    Run a streamlit service on the background, returns a process and a url to access it
    """
    port = port or random.randint(13000,15000)
    process = subprocess.Popen([
            'streamlit', 
            'run', script_file,
            '--server.port', str(port),
            '--server.headless', 'True',
        ],
        env=env)
    # Wait server to be alive
    url = f'http://localhost:{port}/'
    for i in range(timeout):
        try:
            request.urlopen(url)
        except request.URLError:
            time.sleep(1)
            timeout -= 1
            if timeout < 0:
                raise
        else:
            break
    return process, url
