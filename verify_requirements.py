import sys

print("🔍 Verifying Python environment...\n")
print(f"📦 Python path: {sys.executable}")
print(f"🐍 Python version: {sys.version}\n")

# Optional: Import from separate check_airflow script
try:
    import check_airflow
except ImportError:
    print("❌ Failed to import Airflow verification module.")
except Exception as e:
    print(f"⚠️ Error running Airflow check: {e}")

# Helper to print result of each import
def check_import(pkg_name, import_name=None, version_attr="__version__"):
    try:
        module = __import__(import_name or pkg_name)
        version = getattr(module, version_attr, "Version not found")
        print(f"✅ {pkg_name} version: {version}")
    except ImportError:
        print(f"❌ {pkg_name} is NOT installed.")
    except Exception as e:
        print(f"⚠️ Error checking {pkg_name}: {e}")

# Other packages to verify
packages = [
    ("DBT", "dbt"),
    ("Pymongo", "pymongo"),
    ("Finnhub", "finnhub"),
    ("Dotenv", "dotenv", "__file__"),  # Special case: show file path
    ("Snowflake Connector", "snowflake.connector"),
]

for pkg in packages:
    check_import(*pkg)

print("\n✅ All checks complete.")