ITM 327 Codespaces Starter

This repository provides a ready-to-use development environment for learning and practicing data warehousing and orchestration with Airflow, DBT, and Snowflake.
It is designed to work in either GitHub Codespaces or locally with Docker Desktop & VS Code Remote Development.
🎓 Recommended: Local setup with Docker Desktop & VS Code — no cost and full control.

⸻

🚀 Setup Options

✅ Preferred: Local Setup with Docker & VS Code

1️⃣ Install:
	•	Docker Desktop
	•	Visual Studio Code
	•	VS Code Extension:
        • Remote - Containers extension

2️⃣ Clone this repo:
```bash
git clone https://github.com/your-org/itm327-codespaces-starter.git
cd itm327-codespaces-starter
```

3️⃣ Create a .env file in the root folder:
```bash
cp .env.example .env
```

Before initializing Airflow, open the `.env` file and set your desired admin username, password, and email:

```dotenv
# Airflow admin user settings
AIRFLOW_USERNAME=changeme
AIRFLOW_PASSWORD=changeme
AIRFLOW_FIRSTNAME=Jane
AIRFLOW_LASTNAME=Doe
AIRFLOW_EMAIL=jane.doe@example.com
```

4️⃣ Open the repo in VS Code:
	•	Use “Remote-Containers: Open Folder in Container…”
	•	VS Code will build and start the dev container.

5️⃣ Run the Airflow init script:
```bash
cd ..
chmod +x ./init_airflow.sh
./init_airflow.sh
```

This will:
✅ Initialize the Airflow DB
✅ Create the admin user
✅ Start Airflow webserver & scheduler

6️⃣ Access Airflow:
	•	Open browser at: http://localhost:8080
	•	Login with the credentials from .env

⸻

## 🧪 Test DAGs

To run DAG parsing and import tests:

```bash
cd /workspaces/itm327-codespaces-starter/dags
python test_dbt_dag.py
```

⸻

## ✅ Environment Health Check

To run to reset path:

```bash
cd /workspaces/itm327-codespaces-starter
```

Run this script to verify all dependencies and DAGs are correctly set up:

```bash
python verify_requirements.py
```

⸻