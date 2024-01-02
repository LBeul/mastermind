import subprocess
import sys


def install(pckg):
    """
    Install the package via pip
    :param pckg: Package to install
    """
    subprocess.check_call([sys.executable, "-m", "pip", "install", pckg])


# Liste der zu installierenden Pakete
packages = ["jsonschema", "requests"]

for package in packages:
    install(package)
