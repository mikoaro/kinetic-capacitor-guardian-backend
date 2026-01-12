# Use Python 3.14-slim (Targeting Jan 2026 context)
FROM python:3.14-slim

# Set working directory to /code to avoid cluttering root
WORKDIR /code

# Install dependencies first (Caching layer)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into /code/app
COPY ./app ./app

# Expose the port Cloud Run expects
EXPOSE 8080

# Command to run the application
# Note the syntax: app.main:app (Module app > File main > Instance app)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]