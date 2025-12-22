FROM python:3.10-alpine

# Set working directory
WORKDIR /app

# Copy the requirements file into the image
# COPY requirements.txt /app/requirements.txt

COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port FastAPI runs on
EXPOSE 8000

# RUN the FastAPI application with Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
