@ECHO OFF

pushd %~dp0

REM Command file to provide compatability for Windows systems

if "%1" == "setup" (
   python -m venv venv
   venv\Scripts\python -m pip install -U pip setuptools wheel
   venv\Scripts\python -m pip install -U -r requirements.txt
   goto end
)

if "%1" == "clean" (
   goto end
)

if "%1" == "lint" (
   venv\Scripts\python -m flake8 scripts
)

if "%1" == "help" (
:help
   ECHO "Help..."
)

:end
popd
