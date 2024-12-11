# dummy_gnn/
# │
# ├── app/
# │   ├── __init__.py
# │   ├── main.py  # The FastAPI app script
# │
# ├── requirements.txt  # Dependencies
# ├── Dockerfile         # Dockerfile for containerization

# Use the official Python 3.11 image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY app/ ./app/

# Expose the port FastAPI will run on
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
