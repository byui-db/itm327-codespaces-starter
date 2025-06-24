import os
import subprocess
import airflow
from airflow.configuration import conf
from airflow.utils.db import create_session
from airflow.models import DagBag

print("\n🔍 Verifying Airflow environment...\n")

# 1. Airflow version
print(f"✅ Airflow version: {airflow.__version__}")

# 2. AIRFLOW_HOME
airflow_home = os.getenv("AIRFLOW_HOME", conf.get("core", "AIRFLOW_HOME", fallback=os.path.expanduser("~/airflow")))
print(f"📁 AIRFLOW_HOME: {airflow_home}")

# 3. DAGs folder check
dags_folder = conf.get("core", "dags_folder", fallback=os.path.join(airflow_home, "dags"))
if os.path.isdir(dags_folder):
    dags = [f for f in os.listdir(dags_folder) if f.endswith(".py")]
    print(f"📄 Found {len(dags)} DAG(s) in folder: {dags_folder}")
    if dags:
        print("🧾 DAG files:", ", ".join(dags))
else:
    print(f"⚠️  DAGS folder not found or invalid: {dags_folder}")

# 4. Airflow DB check via subprocess
print("\n🗄️  Checking Airflow DB status...")
try:
    subprocess.run(["airflow", "db", "check"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print("✅ Airflow DB is ready.")
except subprocess.CalledProcessError:
    print("❌ Airflow DB is not initialized. Run: airflow db migrate")

# 5. List DAGs using CLI
print("\n📡 Listing available DAGs...")
try:
    subprocess.run(["airflow", "dags", "list"], check=True)
except subprocess.CalledProcessError:
    print("⚠️  Could not list DAGs. Scheduler may not be running or DB not initialized.")

# 6. Programmatic DAG parsing
print("\n🧪 Parsing DAGs with DagBag...")
dag_bag = DagBag(dag_folder=dags_folder, include_examples=False)

if dag_bag.import_errors:
    print(f"❌ Found {len(dag_bag.import_errors)} import error(s):")
    for dag, error in dag_bag.import_errors.items():
        print(f"   - {dag}: {error}")
else:
    print(f"✅ All DAGs parsed successfully ({len(dag_bag.dags)} loaded)")

print("\n✅ Airflow environment check complete.")