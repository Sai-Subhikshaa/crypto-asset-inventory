import os

from cryptography import x509
from cryptography.hazmat.primitives.asymmetric import rsa, ec, dsa

import csv
from datetime import datetime, timezone

folder_path = "/home/iot-qsrg-2/Documents/Crypto-Projects/Project-1/sample-openssl-certs"

with open("digital_cert_inventory.csv", "w", newline="") as csvfile:
            fieldnames = ["Common Name", "Issuer", "Expiry Date", "Key Size", "Algorithm", "Status", "Key Strength"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for filename in os.listdir(folder_path):
                if filename.endswith(".pem"):
                    file_path = os.path.join(folder_path, filename)
                    print(f"Processing {file_path}...")
                    with open(file_path, "rb") as f:
                        cert_data = f.read()
                        try:
                            try:
                                    cert = x509.load_pem_x509_certificate(cert_data)
                            except ValueError:
                                cert_data= cert_data.replace( b"TRUSTED CERTIFICATE",b"CERTIFICATE")
                                cert = x509.load_pem_x509_certificate(cert_data)           
                        except Exception as e:
                            print(f" Skipping {filename} - could not parse : {e}")
                            continue
                        # Parse it
                        cert = x509.load_pem_x509_certificate(cert_data)
                        common_name = cert.subject.get_attributes_for_oid(x509.NameOID.COMMON_NAME)[0].value
                        issuer_name = cert.issuer.get_attributes_for_oid(x509.NameOID.COMMON_NAME)[0].value
                        public_key = cert.public_key()
                        if isinstance(public_key, rsa.RSAPublicKey):
                            algo_name = "RSA"
                            key_strength = "Weak" if public_key.key_size < 2048 else "Strong"
                        elif isinstance(public_key, ec.EllipticCurvePublicKey):
                            algo_name = "ECC"
                            key_strength = "Weak" if public_key.key_size < 256 else "Strong"
                        elif isinstance(public_key, dsa.DSAPublicKey):
                            algo_name = "DSA"
                            key_strength = "Weak" if public_key.key_size < 2048 else "Strong"
                        else:
                            algo_name = "Unknown"
                            key_strength = "Unknown"
                        key_size = public_key.key_size
                        # Determine status
                        now = datetime.now(timezone.utc)
                        expiry = cert.not_valid_after.replace(tzinfo=timezone.utc)
                        if expiry < now:
                            status = "Expired"
                        elif (expiry - now).days <= 30:
                            status = "Expiring Soon"
                        else:
                            status = "Valid"
                        # Write to CSV           
                        writer.writerow({
                            "Common Name": common_name,
                            "Issuer": issuer_name,
                            "Expiry Date": expiry.strftime("%Y-%m-%d"),
                            "Key Size": key_size,
                            "Algorithm": algo_name,
                            "Status": status,
                            "Key Strength": key_strength
                            })

print("Inventory saved to digital_cert_inventory.csv")


# Extract basic fields
#print("Subject:", cert.subject)
#print("Expiry Date:", cert.not_valid_after_utc)
#print("Issuer:", cert.issuer)
#print("Common Name:", common_name)
#print("Issuer:", issuer_name)
#print("Key Size:", key_size, "bits")
#print("Algorithm:", type(public_key).__name__)
