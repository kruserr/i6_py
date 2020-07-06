import i6

import sys
import subprocess


def test_cli():
    i6.cli(menu=False).run()

def test_cli_subprocess_direct():
    subprocess.run([sys.executable, 'src/i6/cli/main.py'], timeout=5)

def test_cli_subprocess_path():
    subprocess.run(['i6'], timeout=5)

def test_cli_subprocess_python_module():
    subprocess.run([sys.executable, '-m', 'i6'], timeout=5)

def test_cli_subprocess_bin():
    subprocess.run(['bin/i6'], timeout=5)

def test_cli_subprocess_bin_exe():
    subprocess.run(['bin/i6.exe'], timeout=5)

def test_cli_args():
    i6.cli('aiocheck', menu=False).run()
