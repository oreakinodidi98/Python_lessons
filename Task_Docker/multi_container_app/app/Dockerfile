# Use the official Python image from the Docker Hub
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy everything including the dependencies file to the working directory
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# expose to port 5000, available to the world outside this container
EXPOSE 5000

# Run the command to start the Flask app
CMD ["python", "app.py"]