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
AIRFLOW_USERNAME=admin
AIRFLOW_PASSWORD=changeme
AIRFLOW_EMAIL=yourname@example.com
```

4️⃣ Open the repo in VS Code:
	•	Use “Remote-Containers: Open Folder in Container…”
	•	VS Code will build and start the dev container.

5️⃣ Run the Airflow init script:
```bash
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

🌩️ Alternative: GitHub Codespaces

1️⃣ Click “Use this template” → Open in Codespaces
2️⃣ Codespaces prebuilds the dev container and installs dependencies.
3️⃣ Create a .env file in the root folder as above.
4️⃣ Run:
```bash
./init_airflow.sh
```

5️⃣ Access Airflow via the forwarded port.

⸻

📄 Project Contents
	•	Airflow DAGs for stock + news ingestion.
	•	DBT and MongoDB connection scaffolding.
	•	A .devcontainer for preinstalled dependencies.
	•	requirements.txt for Python packages.
	•	.env.example for environment variables.
	•	init_airflow.sh to bootstrap Airflow and admin user.

⸻

🔑 Environment Variables

Create a .env file and configure:

Variable	Example	Description
AIRFLOW_ADMIN_USERNAME	admin	Airflow admin username
AIRFLOW_ADMIN_PASSWORD	mypassword	Airflow admin password
AIRFLOW_ADMIN_EMAIL	admin@example.com	Airflow admin email


⸻

🧰 Utilities

🔷 Initialize Airflow

./init_airflow.sh

Runs:
	•	airflow db init
	•	Creates admin user
	•	Starts webserver & scheduler

🔷 Start Airflow Manually

airflow webserver -p 8080 &
airflow scheduler &


⸻

📚 Learning Objectives
	•	Build and orchestrate ELT pipelines with Airflow and DBT.
	•	Work with APIs, MongoDB, and Snowflake.
	•	Create and transform star and snowflake schemas.
	•	Produce dashboards or ML insights.

⸻

For questions or help, reach out to your instructor or check the course Canvas page.