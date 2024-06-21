FROM python:3.8

# Set the working directory in the container
WORKDIR /flask_app

# Copy everything including the dependencies file to the working directory
COPY . /flask_app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# expose to port 5000
EXPOSE 5000

# run the Flask app
CMD ["python", "docker_app.py"]