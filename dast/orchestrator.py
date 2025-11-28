import subprocess
import time
import sys
import requests
import os

HOST_TARGET_URL = "http://localhost:5000/health" 
INTERNAL_TARGET_URL = "http://web:5000"
ZAP_CONTAINER_NAME = "dast_zap"

def check_target_availability(url, retries=10, delay=5):
    print(f"[*] Verificando disponibilidad del objetivo en: {url}")
    for i in range(retries):
        try:
            response = requests.get(url, timeout=3)
            if response.status_code == 200:
                print(f"[OK] Objetivo accesible. Status: {response.status_code}")
                return True
        except requests.exceptions.ConnectionError:
            pass
        print(f"[...] Esperando a que el servicio levante (Intento {i+1}/{retries})")
        time.sleep(delay)
    print("[ERROR] El objetivo no respondió.")
    return False

def run_zap_scan():
    print(f"[*] Iniciando escaneo ZAP contra {INTERNAL_TARGET_URL}...")
    
    report_html = "zap_report.html"
    report_json = "zap_report.json"
    
    cmd = [
        "docker", "exec",
        "-u", "0",
        "-w", "/zap/wrk",
        ZAP_CONTAINER_NAME,
        "zap-baseline.py",
        "-t", INTERNAL_TARGET_URL,
        "-r", report_html,
        "-J", report_json,
        "-I"
    ]
    
    try:
        process = subprocess.run(cmd, check=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        print(process.stdout)
        
        if process.returncode in [0, 1, 2]: 
            print("[OK] Escaneo finalizado.")
            print(f"[*] Reportes generados en carpeta reports/: {report_html}, {report_json}")
        else:
            print(f"[ERROR] ZAP falló con código de salida: {process.returncode}")
            print(process.stderr)
            sys.exit(1)

    except Exception as e:
        print(f"[ERROR] Excepción al ejecutar ZAP: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if not check_target_availability(HOST_TARGET_URL):
        sys.exit(1)
    run_zap_scan()