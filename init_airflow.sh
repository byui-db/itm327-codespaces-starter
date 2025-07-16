#!/bin/bash

# Initialize Airflow DB
echo "🔧 Initializing Airflow database..."
airflow db init

# Load environment variables
set -e

# load env vars
if [ -f ".env" ]; then
  export $(grep -v '^#' .env | xargs)
fi

echo "Initializing Airflow DB..."
airflow db init

echo "Creating admin user..."
airflow users create \
  --username "${AIRFLOW_USERNAME:-admin}" \
  --firstname Admin \
  --lastname User \
  --role Admin \
  --email "${AIRFLOW_EMAIL:-admin@example.com}" \
  --password "${AIRFLOW_PASSWORD:-changeme}"

echo "Airflow admin user created. You can log in at http://localhost:8080"

# Start the webserver & scheduler (optional here)
echo "🚀 Starting Airflow webserver & scheduler..."
airflow webserver -p 8080 &
airflow scheduler &