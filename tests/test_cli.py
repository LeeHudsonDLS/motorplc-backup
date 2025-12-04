import subprocess
import sys

from motorplc_backup import __version__


def test_cli_version():
    cmd = [sys.executable, "-m", "motorplc_backup", "--version"]
    assert subprocess.check_output(cmd).decode().strip() == __version__
