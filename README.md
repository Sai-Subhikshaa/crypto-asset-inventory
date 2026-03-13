# crypto-asset-inventory
A Python tool to scan, inventory and assess enterprise digital certificates for cryptographic risk.
# 🔐 Crypto Asset Inventory - Phase 1: Digital Certificate Inventory

## Overview
In large enterprises, digital certificates are scattered across hundreds 
of systems with no centralised visibility. Without a structured inventory, 
organisations risk undetected expired certificates, weak cryptographic 
algorithms, and key compromise, all of which can lead to authentication 
failures, service outages, and security breaches.

This tool automatically scans certificate files enterprise-wide, extracts 
key security attributes, and produces a structured inventory that enables 
security teams to assess risk and act accordingly.

---

## 🎯 What This Tool Does
- Scans a folder of PEM certificate files automatically
- Extracts key inventory fields from each certificate
- Assesses cryptographic strength based on algorithm and key size
- Assigns risk status (Valid / Expiring Soon / Expired)
- Exports a structured CSV inventory ready for dashboard visualisation

---

## 📋 Inventory Fields Captured

| Field | Description |
|---|---|
| Common Name | Identity the certificate is issued to |
| Issuer | Certificate Authority that issued it |
| Expiry Date | Date the certificate expires |
| Key Size | Size of the cryptographic key in bits |
| Algorithm | Cryptographic algorithm used (RSA, ECC, DSA) |
| Status | Valid / Expiring Soon / Expired |
| Key Strength | Strong / Weak based on NIST standards |

---

## 🔑 Key Strength Assessment Criteria

| Algorithm | Minimum Strong Key Size |
|---|---|
| RSA | 2048 bits |
| ECC | 256 bits |
| DSA | 2048 bits |

*Based on NIST SP 800-57 recommendations.*

---

## 🚀 How To Run

### Prerequisites
```bash
pip install cryptography
```

### Usage
1. Place your `.pem` certificate files in a folder
2. Update `folder_path` in the script to point to your folder
3. Run the script:
```bash
python cert-asset-inventory.py
```
4. Output will be saved to `digital_cert_inventory.csv`

---

## 📊 Sample Output

| Common Name | Issuer | Expiry Date | Key Size | Algorithm | Status | Key Strength |
|---|---|---|---|---|---|---|
| payments.company.com | DigiCert | 2025-06-15 | 2048 | RSA | Expiring Soon | Strong |
| legacy.company.com | Internal CA | 2018-03-18 | 1024 | RSA | Expired | Weak |
| api.company.com | DigiCert | 2120-10-31 | 256 | ECC | Valid | Strong |

---

## ⚠️ Security Note
Never commit private keys to this repository. 
This tool requires certificate (`.pem`) files only, 
not private key files.

---

## 🗺️ Roadmap - Broader Crypto Asset Inventory

This project is Phase 1 of a broader enterprise cryptographic 
inventory program:

| Phase | Scope | Status |
|---|---|---|
| Phase 1 | Digital Certificate Inventory | ✅ Complete |
| Phase 2 | Crypto Posture Dashboard (KPIs/KRIs) | 🔜 In Progress |
| Phase 3 | Threat & Vulnerability Analysis Report | 🔜 Planned |
| Phase 4 | Key Stores & HSM Inventory | 🔜 Planned |
| Phase 5 | Protocol & Library Inventory | 🔜 Planned |

---

## 📚 References
- [NIST SP 800-57 — Recommendation for Key Management](https://csrc.nist.gov/publications/detail/sp/800-57-part-1/rev-5/final)
- [NIST Cryptographic Standards](https://csrc.nist.gov/projects/cryptographic-standards-and-guidelines)
