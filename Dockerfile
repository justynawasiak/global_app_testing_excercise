# Dockerfile

# Base image
FROM python:3.6

# Copy test project files to the image folder
COPY ./pytest_project /var/pytest_project

# For debugging purposes
#RUN ls -la /var/pytest_project 

# Make the folder as a working directory
WORKDIR /var/pytest_project
ENV PYTHONPATH /var/pytest_project

# Install the test project libraries
RUN pip install -r requirements.txt