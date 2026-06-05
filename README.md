# Enterprise Cryptographic Risk Management Program
A 5-phase enterprise cryptographic risk management program covering certificate inventory, posture visibility, threat analysis, vulnerability governance and post-quantum readiness.
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

## 📊 Phase 2 - Crypto Posture Dashboard

### Overview
A dynamic HTML dashboard that visualises the cryptographic risk posture 
of the certificate estate. Built on top of Phase 1's inventory output, 
it translates raw CSV data into actionable security intelligence for 
security teams and CISOs.

### 🔴 Key Risk Indicators (KRIs)
- Expired certificates still active in the environment
- Certificates with weak keys below NIST SP 800-57 thresholds

### 🟢 Key Performance Indicators (KPIs)
- Total certificates inventoried
- Percentage of valid certificates
- Percentage of expired certificates
- Percentage of weak key certificates

### 📈 Dashboard Components
| Component | Description |
|---|---|
| KRI Alert Panel | Immediate action items with severity tagging |
| KPI Summary Cards | Estate health at a glance with percentages |
| Certificate Status Chart | Valid / Expired / Expiring Soon distribution |
| Key Strength Chart | Strong vs Weak key breakdown |
| Algorithm Distribution | RSA / ECC / DSA usage across estate |
| Full Certificate Register | Complete inventory table with colour-coded status |

### 🚀 How To Run
1. Run Phase 1 script to generate fresh inventory:
```bash
python phase-1-cert-inventory/cert-asset-inventory.py
```
2. Run dashboard generator:
```bash
python phase-2-dashboard/generate_dashboard.py
```

### 🔗 Live Dashboard
👉 [View Live Dashboard](https://sai-subhikshaa.github.io/crypto-asset-inventory/phase-2-dashboard/dashboard.html)

---

## 📋 Phase 3 - Threat & Vulnerability Analysis Report

### Overview
A structured security report analysing the cryptographic risk posture of the 
enterprise certificate estate. Built on findings from Phase 1 inventory and 
Phase 2 dashboard, translating technical data into governance-ready documentation 
for security teams and CISOs.

### 📄 Report
👉 [View Full Report](phase-3-threat-report/Crypto_Threat_Vulnerability_Report.pdf)

---

## 🔄 Phase 4 - Crypto Vulnerability Management Process

### Overview
A formal governance process document defining how cryptographic vulnerabilities 
are identified, assessed, remediated and closed across the enterprise. Includes 
SLA targets, escalation procedures, RACI matrix and process KPIs.

### Process Stages
| Stage | Description |
|---|---|
| Stage 1 | Identification & Intake |
| Stage 2 | Assessment & Prioritisation |
| Stage 3 | Assignment & Response Planning |
| Stage 4 | Remediation |
| Stage 5 | Verification & Testing |
| Stage 6 | Closure & Reporting |

### 📄 Deliverables
👉 [Process Document](phase-4-vulnerability-management/Crypto_Vulnerability_Management_Process.docx.pdf)
👉 [Process Flowchart](https://sai-subhikshaa.github.io/crypto-asset-inventory/phase-4-vulnerability-management/crypto_vuln_management_flowchart.html)

---

## 🔮 Phase 5 - Post-Quantum Cryptography Readiness Assessment

### Overview
A strategic assessment of the enterprise's readiness for the post-quantum 
cryptography transition. Covers the quantum threat landscape, current 
cryptographic exposure, NIST PQC standards, migration roadmap and 
crypto agility framework.

### Key Findings
| Finding | Detail |
|---|---|
| Quantum Vulnerability | 100% of certificates rely on quantum-vulnerable algorithms |
| Algorithms at Risk | RSA (11 certs), ECC (4 certs) |
| Active Threat | Harvest Now, Decrypt Later |
| Migration Target | ML-KEM (FIPS 203), ML-DSA (FIPS 204), SLH-DSA (FIPS 205) |
| Overall Risk Rating | 🔴 Critical - immediate planning required |

### 📄 Report
👉 [View Full Report](phase-5-pqc-assessment/PQC_Readiness_Assessment.pdf)

### Report Structure
| Section | Content |
|---|---|
| Executive Summary | Overall risk rating and immediate actions required |
| Scope & Methodology | Assessment approach and NIST SP 800-57 standards applied |
| Cryptographic Posture Overview | KPIs showing current certificate estate health |
| Findings & Risk Analysis | Two findings - Critical and High severity |
| Remediation Recommendations | Step-by-step remediation with owners and timelines |
| Risk Register | Consolidated CR-001 and CR-002 tracking table |
| Appendix | Links to inventory CSV, live dashboard and GitHub repo |

### Key Findings
| ID | Finding | Risk Rating | Timeline |
|---|---|---|---|
| CR-001 | 4 Expired Certificates Active in Environment | 🔴 Critical | 30 days |
| CR-002 | 2 Weak Key Certificates (RSA-1024) | 🟠 High | 45 days |


## 🗺️ Enterprise Cryptographic Risk Management Program

A 5-phase program built to demonstrate enterprise-grade cryptographic 
governance — from asset discovery through to post-quantum readiness.

| Phase | Scope | Deliverable |
|---|---|---|
| Phase 1 | Digital Certificate Inventory | Python scanning tool + CSV inventory |
| Phase 2 | Crypto Posture Dashboard | Live HTML dashboard with KPIs/KRIs |
| Phase 3 | Threat & Vulnerability Analysis | PDF security assessment report |
| Phase 4 | Vulnerability Management Process | Process document + visual flowchart |
| Phase 5 | Post-Quantum Cryptography Readiness | PDF readiness assessment + migration roadmap |

---

## 📚 References
- [NIST SP 800-57 — Recommendation for Key Management](https://csrc.nist.gov/publications/detail/sp/800-57-part-1/rev-5/final)
- [NIST Cryptographic Standards](https://csrc.nist.gov/projects/cryptographic-standards-and-guidelines)
