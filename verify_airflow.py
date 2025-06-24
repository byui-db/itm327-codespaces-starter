import os
import subprocess
import importlib.util

print("🔍 Verifying Airflow environment...\n")

# 1. Airflow Installed
try:
    import verify_airflow
    print(f"✅ Airflow version: {verify_airflow.__version__}")
except ImportError:
    print("❌ Airflow is not installed.")
    exit(1)

# 2. AIRFLOW_HOME
airflow_home = os.environ.get("AIRFLOW_HOME", os.path.expanduser("~/airflow"))
print(f"📁 AIRFLOW_HOME: {airflow_home}")

# 3. DAGs directory check
dags_folder = os.path.join(airflow_home, "dags")
if not os.path.exists(dags_folder):
    print(f"⚠️  DAGs folder not found at: {dags_folder}")
else:
    dags = [f for f in os.listdir(dags_folder) if f.endswith(".py")]
    print(f"📄 Found {len(dags)} DAG(s): {dags}")

# 4. Airflow DB check
print("🗄️  Checking Airflow DB status...")
try:
    subprocess.run(["airflow", "db", "check"], check=True)
    print("✅ Airflow DB is ready.")
except subprocess.CalledProcessError:
    print("❌ Airflow DB is not initialized. Run: airflow db migrate")

# 5. List DAGs if possible
print("\n📡 Listing available DAGs...")
try:
    subprocess.run(["airflow", "dags", "list"], check=True)
except subprocess.CalledProcessError:
    print("⚠️  Could not list DAGs. Scheduler may not be running or DB not initialized.")