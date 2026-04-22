# Use Python 3.9 base image
FROM python:3.9-slim

# Set working directory inside container
WORKDIR /app

# Copy requirements first (for caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files
COPY . .

# Expose port 8080
EXPOSE 8080

# Set environment variables
ENV FLASK_APP=api.app
ENV FLASK_DEBUG=0

# Command to run the application
CMD ["flask", "run", "--host=0.0.0.0", "--port=8080"]