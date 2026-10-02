@echo off
cd /d "%~dp0"
python -m pip install -r requirements_pc.txt
python gerar_pc_exclusivos.py
pause
