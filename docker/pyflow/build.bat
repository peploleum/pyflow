xcopy ".\..\..\run.py" "." /Y /F
docker build -f pyflow.Dockerfile -t pyflow-run .
