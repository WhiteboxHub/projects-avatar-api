# Use the official Python image from Docker Hub
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application files into the container
COPY . /app

# Expose port 8000 for the FastAPI app
EXPOSE 8000

# Set the environment variable for Python path
ENV PYTHONPATH=/app

# Command to run the FastAPI app using Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
