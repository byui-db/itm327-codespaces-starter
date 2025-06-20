import sys

# Core packages
import airflow
import pymongo
import finnhub
import dotenv
import snowflake.connector

# Check for dbt-core
try:
    import dbt
    print(f"DBT core (CLI) is available")
except ImportError:
    print("❌ dbt-core is NOT installed or not accessible")

print("\n✅ All other imports successful!\n")
print(f"Python version: {sys.version}")
print(f"Airflow version: {airflow.__version__}")
print(f"Finnhub client: {finnhub.Client}")
print(f"Mongo version: {pymongo.version}")
print(f"Dotenv loaded from: {dotenv.__file__}")
print(f"Snowflake connector version: {snowflake.connector.__version__}")