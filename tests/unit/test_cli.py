import i6

import subprocess


def test_cli():
    i6.cli(menu=False).run()

def test_cli_subprocess_direct():
    subprocess.run(['python', 'src/i6/cli/main.py'], timeout=1)

def test_cli_subprocess_path():
    subprocess.run(['i6'], timeout=1)

def test_cli_subprocess_python_module():
    subprocess.run(['python', '-m', 'i6'], timeout=1)

def test_cli_args():
    i6.cli('aiocheck', menu=False).run()
