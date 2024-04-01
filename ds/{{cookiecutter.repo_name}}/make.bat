@ECHO OFF

pushd %~dp0

REM Command file to provide compatability for Windows systems

if "%1" == "setup" (
   python3 -m venv venv
   venv/bin/python3 -m pip install -U pip setuptools wheel
   venv/bin/python3 -m pip install -r requirements.txt
   goto end
)

if "%1" == "clean" (
   goto end
)

if "%1" == "lint" (
   venv/bin/python3 -m flake8 scripts
)

if "%1" == "help" (
:help
   ECHO "Help..."
)

:end
popd
