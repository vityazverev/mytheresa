import os
import subprocess
import sys


def install_dependencies():
    """Install dependencies from requirements.txt."""
    try:
        print("Installing dependencies from requirements.txt...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("Dependencies installed successfully.")
    except subprocess.CalledProcessError:
        print("Failed to install dependencies.")
        sys.exit(1)


def run_tests():
    """Run pytest to execute all tests."""
    try:
        print("Running tests using pytest...")
        subprocess.check_call([sys.executable, "-m", "pytest", "tests/"])
        print("Tests executed successfully.")
    except subprocess.CalledProcessError:
        print("Some tests failed.")
        sys.exit(1)


if __name__ == "__main__":
    install_dependencies()
    run_tests()
