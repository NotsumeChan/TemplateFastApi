@echo off
setlocal enabledelayedexpansion

:: Configuración
set entorno_virtual=venv
set comando_a_ejecutar=python -m pip install -r requierments.txt

:: Crear entorno virtual
python -m venv %entorno_virtual%

:: Activar entorno virtual
call %entorno_virtual%\Scripts\activate

:: Ejecutar comando dentro del entorno virtual
%comando_a_ejecutar%

:: Desactivar entorno virtual al finalizar
python main.py

deactivate

endlocal
