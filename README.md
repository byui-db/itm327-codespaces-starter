# 🚀 ITM 327 Codespaces + Docker Starter

This repo provides a full development environment for Apache Airflow and DBT — ideal for building ETL pipelines with support for stock + news ingestion, MongoDB, and more.

---

## 🧰 What's Included

- **Apache Airflow**: Fully configured for local or remote development.
- **DBT**: Analytics engineering ready out of the box.
- **MongoDB integration**: Via `pymongo`.
- **Finnhub client support**: For financial/market data.
- **Docker-based dev container**: Easy to spin up locally.
- **Airflow DAG examples**: With basic DAG testing setup.

---

## 💻 Preferred Setup: Local Development with Docker

> ✅ Free, fast, and doesn't require GitHub Codespaces credits.

### Requirements

- [Docker Desktop](https://www.docker.com/products/docker-desktop)
- [Visual Studio Code](https://code.visualstudio.com/)
- [Remote - Containers Extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)

### Steps

1. **Clone the Repository**

```bash
git clone https://github.com/byui-db/itm327-codespaces-starter.git
cd itm327-codespaces-starter
```

2. **Open in VS Code**

Open the folder in VS Code.

3. **Reopen in Container**

When prompted, click **“Reopen in Container”**, or open the command palette (shortcut Windows: Ctrl + Shift + P, Mac: Cmd + Shift + P) and run:

```
Remote-Containers: Reopen in Container
```

This builds the environment using the `.devcontainer` folder.

4. **Start Airflow**

Once inside the container:

```bash
# Initialize DB (only once)
airflow db init

# Start scheduler
airflow scheduler

# Start web server
airflow webserver --port 8080
```

Then open `http://localhost:8080` (or the forwarded port in VS Code).  
Default credentials:

```
Username: airflow
Password: airflow
```

---

## 🧪 Test DAGs

To run DAG parsing and import tests:

```bash
cd /workspaces/itm327-codespaces-starter/dags
python test_dbt_dag.py
```

---

## ✅ Environment Health Check

To run to reset path:

```bash
cd /workspaces/itm327-codespaces-starter
```

Run this script to verify all dependencies and DAGs are correctly set up:

```bash
python verify_requirements.py
```

---

## 🛰️ Optional: GitHub Codespaces Setup

> ⚠️ Codespaces may incur cost depending on usage. Consider local dev if you're on a budget.

1. Click **“Use this template”** on GitHub.
2. Choose **“Open in Codespaces”**.
3. Let the dev container initialize.
4. Use the pre-installed environment as described above.
