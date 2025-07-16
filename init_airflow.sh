#!/bin/bash

# Initialize Airflow DB
set -e

# Load environment variables
if [ -f .env ]; then
    export $(grep -v '^#' .env | xargs)
fi

echo "📄 Checking for custom Airflow user credentials…"

if [[ "$AIRFLOW_USERNAME" != "changeme" && "$AIRFLOW_PASSWORD" != "changeme" ]]; then
    echo "🔑 Creating Airflow user with credentials from .env…"

    airflow users create \
        --username "$AIRFLOW_USERNAME" \
        --password "$AIRFLOW_PASSWORD" \
        --firstname "${AIRFLOW_FIRSTNAME:-User}" \
        --lastname "${AIRFLOW_LASTNAME:-User}" \
        --role Admin \
        --email "${AIRFLOW_EMAIL:-user@example.com}"

    echo "✅ Custom Airflow user created: $AIRFLOW_USERNAME"
else
    echo "⚠️ No custom credentials detected in .env. Using default admin/admin."
fi

echo "Airflow admin user created. You can log in at http://localhost:8080"

# Start the webserver & scheduler (optional here)
echo "🚀 Starting Airflow webserver & scheduler..."
airflow webserver -p 8080 &
airflow scheduler &