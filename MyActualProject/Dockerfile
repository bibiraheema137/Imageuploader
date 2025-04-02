# Use the official Python image from Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install the required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container
COPY . /app/

# Expose port 8000 (Django default port)
EXPOSE 8000

# Command to run the application when the container starts
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
