FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements file
COPY requirements.txt .
RUN mkdir -p /app/static

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code
COPY . .

# Expose the necessary port
EXPOSE 8000

# Define the command to run your application
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "emoi_backend_project.wsgi:application"]

