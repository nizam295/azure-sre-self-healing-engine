# Azure Cloud Observability & Closed-Loop Self-Healing SRE Engine

A production-tier, cost-optimized, and fully automated Site Reliability Engineering (SRE) ecosystem deployed on Azure. This project demonstrates advanced Infrastructure-as-Code (IaC), multi-container system orchestration, real-time PromQL performance monitoring, and an event-driven closed-loop auto-remediation engine that resolves application runtime deadlocks with zero human intervention.

## 🏗️ Architecture & Data Workflow Blueprint

[ Target Server Node: Standard_D2s_v5 ] ──(Exposes Telemetry)──► [ Prometheus Server Container ]
▲                                                               │
│ (Automated Native Restart)                                    ▼
[ Python Webhook Handler (Port 5001) ] ◄───(Alerting Webhook)─── [ Grafana Dashboard (Port 3000) ]


1. **Infrastructure Tier:** Provisioned via **Terraform** using a General Purpose `Standard_D2s_v5` Linux instance inside **Azure (West US 2)**, protected by atomic firewall configurations (**Network Security Groups**).
2. **Observability Stack:** Orchestrated via **Docker Compose**, running a custom metrics-producing **Python Flask app** (Port 5000), a **Prometheus Time-Series Database** (Port 9090) scraping endpoints every 5 seconds, and a **Grafana Visualization UI** (Port 3000).
3. **Automated Remediation Loop:** Grafana Alertmanager monitors telemetry spikes. When thresholds are breached, it fires an HTTP Webhook payload down to an unbuffered host-level **Python Remediation Engine** (Port 5001) which automatically executes container restarts, reducing Mean Time to Resolution (MTTR) to **under 10 seconds**.

---

## 🛠️ Tech Stack & Tools Used
*   **Cloud Platform:** Microsoft Azure (Compute, Networking, Security)
*   **Infrastructure-as-Code:** Terraform (~> 3.0 AzureRM Provider)
*   **Containerization & Orchestration:** Docker, Docker Compose
*   **Monitoring & Telemetry:** Prometheus (TSDB), PromQL
*   **Data Visualization Engine:** Grafana Core Analytics
*   **Automation Languages:** Python 3.9 (Flask, Custom HTTP Servers), Bash Shell Scripting

---

## 📂 Project Repository Structure
```text
azure-sre-self-healing-engine/
├── terraform/
│   └── main.tf                 # Complete Azure Cloud Network & VM infrastructure blueprint
├── monitoring-stack/
│   ├── docker-compose.yml      # Multi-container multi-tier microservice manifest
│   ├── prometheus.yml          # Prometheus scrape settings and application targets
│   └── app/
│       ├── Dockerfile          # Multi-stage custom local container build script
│       └── app.py              # Custom Flask web application with integrated metrics endpoints
└── sre-automation/
    └── auto_heal.py            # Unbuffered Python self-healing automated event receiver
```

---

## 🚀 Deployment & Operational Execution Steps

### 1. Provision Infrastructure
Authenticate your session and execute the modular infrastructure deployment steps:
```bash
cd terraform
terraform init
terraform apply -auto-approve
```

### 2. Boot Up the Containerized Applications
Connect to your remote virtual machine via SSH and trigger the localized multi-container build engines:
```bash
cd ~/monitoring-stack
docker-compose up -d --build
```

### 3. Launch the Automated Self-Healer Daemon
Initialize the unbuffered Python receiver in the background to handle asynchronous automated webhooks:
```bash
cd ~/sre-automation
nohup python3 -u auto_heal.py > auto_heal.log 2>&1 &
```

---

## 📊 Telemetry Visualizations & Validation Proof

### 1. Live Production Traffic Slopes
*Raw system metrics processed through Prometheus and rendered inside Grafana panels utilizing PromQL expressions tracking `flask_http_request_total`.*

*(Insert Your Dashboard Here: e.g., `![Grafana Dashboard]`)*

### 2. Closed-Loop Auto-Remediation Logs
*Proof of automated self-healing. When traffic metrics breached normal limits, Grafana fired an active alert, triggering our Python webhook handler to successfully restart the target app node without human intervention.*

*(Insert Your Terminal Log Here: e.g., `![SRE Logs])*

