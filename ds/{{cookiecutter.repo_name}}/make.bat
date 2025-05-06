@ECHO OFF

pushd %~dp0

REM Command file to provide compatability for Windows systems

if "%1" == "setup" (
   python -m venv --upgrade-deps venv
   venv\Scripts\python -m pip install -U pip setuptools wheel
   venv\Scripts\python -m pip install -U -r requirements.txt
   goto end
)

if "%1" == "clean" (
   rmdir /s /q dist
   rmdir /s /q build
   cd docs\01_statistical_analysis_plan
   rmdir /s /q _build
   cd ..\..\
   cd docs\02_initial_data_analysis_report
   rmdir /s /q _build
   cd ..\..\
   cd docs\03_exploratory_data_analysis_report
   rmdir /s /q _build
   cd ..\..\
   goto end
)

if "%1" == "lint" (
   venv\Scripts\python -m flake8 scripts
   goto end
)

if "%1" == "sync_data_to_s3" (
   echo not implemented
   goto end
)

if "%1" == "serve_plan" (
   cd docs\01_statistical_analysis_plan
   set SPHINXBUILD=..\..\venv\Scripts\sphinx-build
   make.bat html
   cd _build\html
   ..\..\..\..\venv\Scripts\python -m http.server -b 127.0.0.1
   cd ..\..\..\..\
   goto end
)

if "%1" == "serve_ida" (
   cd docs\02_initial_data_analysis_report
   set SPHINXBUILD=..\..\venv\Scripts\sphinx-build
   make.bat html
   cd _build\html
   ..\..\..\..\venv\Scripts\python -m http.server -b 127.0.0.1
   cd ..\..\..\..\
   goto end
)

if "%1" == "serve_eda" (
   cd docs\03_exploratory_data_analysis_report
   set SPHINXBUILD=..\..\venv\Scripts\sphinx-build
   make.bat html
   cd _build\html
   ..\..\..\..\venv\Scripts\python -m http.server -b 127.0.0.1
   cd ..\..\..\..\
   goto end
)

if "%1" == "dist" (
   mkdir dist
   mkdir build
   cd docs\01_statistical_analysis_plan
   set SPHINXBUILD=..\..\venv\Scripts\sphinx-build
   make.bat html
   cd _build
   zip ..\..\..\dist\01_statistical_analysis_documentation.zip html
   cd ..\..\..\
   cd docs\02_initial_data_analysis_report
   make.bat html
   cd _build
   zip ..\..\..\dist\02_initial_data_analysis_report.zip html
   cd ..\..\..\
   cd docs\03_exploratory_data_analysis_report
   make.bat html
   cd _build
   zip ..\..\..\dist\03_exploratory_data_analysis_report.zip html
   cd ..\..\..\
   goto end
)

if "%1" == "help" (
:help
   ECHO setup            - Install Python Dependencies and set up the environment
   ECHO clean            - Clean the project temporary files
   ECHO lint             - Run the linter against the scripts
   ECHO sync_data_to_s3  - Update Data to S3
   ECHO serve_plan       - Serve the statistical analysis plan locally
   ECHO serve_ida        - Serve the initial data analysis report locally
   ECHO serve_eda        - Serve the exploratory data analysis report locally
   ECHO dist             - Build the project deliverables
)

:end
popd
