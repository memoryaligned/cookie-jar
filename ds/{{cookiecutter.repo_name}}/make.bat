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
   goto end
)

if %! == "sync_data_to_s3" (
  echo not implemented
  goto end
)

if %! == "serve_doc" (
  (cd docs\_build\html; ..\..\..\venv\Scripts\python -m http.server -b localhost)
  goto end
)

if %! == "dist" (
  mkdir dist
  cd build && zip ..\dist\docs.zip docs
  goto end
)

if "%1" == "help" (
:help
   ECHO setup            - Install Python Dependencies and set up the environment
   ECHO clean            - Clean the project temporary files
   ECHO lint             - Run the linter against the scripts
   ECHO sync_data_to_s3  - Update Data to S3
   ECHO serve_doc        - Serve the documentation locally
   ECHO dist             - Build the project deliverables
)

:end
popd
