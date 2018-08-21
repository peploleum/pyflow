echo "Building for environment" %1

rd /s /q deployment


REM vortex --template templates --output deployment -varpath .\environments\$1.yaml