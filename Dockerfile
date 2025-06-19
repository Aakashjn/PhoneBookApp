# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
# If you have external libraries, list them in a requirements.txt file
# RUN pip install --no-cache-dir -r requirements.txt
# For this simple app, we just need Flask
RUN pip install Flask

# Expose port 5000 (Flask's default)
EXPOSE 5000

# Run app.py when the container launches
CMD ["python", "app.py"]