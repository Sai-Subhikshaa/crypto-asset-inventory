import csv
import json
from datetime import datetime

# ── Read CSV from Project-1 ───────────────────────────────────────────────────
certs = []
with open("/home/iot-qsrg-2/Documents/Crypto-Projects/Project-1/digital_cert_inventory.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        certs.append({
            "name":     row["Common Name"],
            "issuer":   row["Issuer"],
            "expiry":   row["Expiry Date"],
            "keySize":  int(row["Key Size"]),
            "algo":     row["Algorithm"],
            "status":   row["Status"],
            "strength": row["Key Strength"]
        })

# ── Generate JS data block ────────────────────────────────────────────────────
cert_js = f"const certs = {json.dumps(certs, indent=2)};"

# ── Read dashboard template from Project-2 ────────────────────────────────────
with open("/home/iot-qsrg-2/Documents/Crypto-Projects/Project-2/dashboard_template.html", "r") as f:
    template = f.read()

# ── Inject data into template ─────────────────────────────────────────────────
output = template.replace("/* __CERT_DATA__ */", cert_js)

# ── Write output dashboard to Project-2 ──────────────────────────────────────
with open("/home/iot-qsrg-2/Documents/Crypto-Projects/Project-2/dashboard.html", "w") as f:
    f.write(output)

print(f" Dashboard generated successfully — dashboard.html")
print(f" {len(certs)} certificates loaded from inventory")