import subprocess

print("🔍 Verifying dbt project...\n")

# 1. Run dbt debug
print("🔧 Running: dbt debug")
try:
    subprocess.run([
        "dbt",
        "debug",
        "--project-dir", "dbt",
        "--profiles-dir", "dbt_config"
    ], check=True)
except subprocess.CalledProcessError:
    print("❌ dbt debug failed.")
    exit(1)

# 2. Run dbt run
print("\n🏗️ Running: dbt run")
try:
    subprocess.run([
        "dbt",
        "run",
        "--project-dir", "dbt",
        "--profiles-dir", "dbt_config"
    ], check=True)
except subprocess.CalledProcessError:
    print("❌ dbt run failed.")
    exit(1)

print("\n✅ dbt debug + run completed successfully.")