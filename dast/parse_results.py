import json
from datetime import datetime

def parse_zap_report(report_path):
    """Parsea un reporte JSON de ZAP para extraer información clave."""
    with open(report_path, 'r') as f:
        data = json.load(f)
    
    summary = {
        "execution_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "alert_counts_by_severity": {
            "High": 0,
            "Medium": 0,
            "Low": 0,
            "Informational": 0
        },
        "endpoints": []
    }
    
    endpoints = set()
    severity_mapping = {
        "High": "High",
        "Medium": "Medium",
        "Low": "Low",
        "Informational": "Informational"
    }

    for site in data.get('site', []):
        for alert in site.get('alerts', []):
            # Extract severity
            risk_desc = alert.get('riskdesc', '').split(' ')[0]
            severity = "Informational"  # Default
            for level, key in severity_mapping.items():
                if level in risk_desc:
                    severity = key
                    break
            
            if severity in summary["alert_counts_by_severity"]:
                summary["alert_counts_by_severity"][severity] += len(alert.get('instances', []))

            # Extract endpoints
            for instance in alert.get('instances', []):
                endpoints.add(instance.get('uri'))

    summary["endpoints"] = sorted(list(endpoints))
    return summary

def save_summary(summary, output_path):
    """Guarda el resumen en un archivo JSON."""
    with open(output_path, 'w') as f:
        json.dump(summary, f, indent=4)

def update_metrics_doc(summary, doc_path):
    """Actualiza la documentación de métricas con el resumen generado."""
    with open(doc_path, 'w') as f: # Sobrescribe, ya que es un resumen del último escaneo
        f.write("# Métricas DAST\n\n")
        f.write(f"**Fecha de ejecución:** {summary['execution_date']}\n\n")
        
        f.write("## Resumen de hallazgos\n\n")
        f.write("| Severidad     | Cantidad |\n")
        f.write("|--------------|----------|\n")
        for severity, count in summary['alert_counts_by_severity'].items():
            f.write(f"| {severity:<12} | {count:<8} |\n")
        f.write("\n")

        f.write("## Endpoints escaneados\n\n")
        if summary['endpoints']:
            for endpoint in summary['endpoints']:
                f.write(f"- `{endpoint}`\n")
        else:
            f.write("No se encontraron endpoints.\n")

if __name__ == "__main__":
    zap_report_file = 'reports/zap_report.json'
    summary_file = 'reports/summary.json'
    metrics_file = 'docs/metrics.md'

    report_summary = parse_zap_report(zap_report_file)
    save_summary(report_summary, summary_file)
    update_metrics_doc(report_summary, metrics_file)

    print(f"Reporte de ZAP procesado correctamente y '{summary_file}' generado.")
    print(f"La documentación de métricas '{metrics_file}' ha sido actualizada.")
