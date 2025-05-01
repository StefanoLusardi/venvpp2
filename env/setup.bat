@echo off

:: Create a virtual environment
python -m venv .venv

:: Set CONAN_HOME environment variable in the activate script
echo set CONAN_HOME=%CD%\.conan2>>.venv\Scripts\activate.bat

:: Activate the virtual environment
call .venv\Scripts\activate.bat

:: Upgrade pip
pip install --upgrade pip

:: Install the required packages
pip install -r scripts/requirements.txt

:: Install pre-commit hooks
pre-commit install
