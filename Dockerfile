# Pull the python base image for container
FROM python:3.9

# Set a working dir
WORKDIR /code

# Copy the requirements to run app
COPY ./requirements.txt /code/requirements.txt

# Install requirements
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy the scripts
COPY ./src/claim_service /code/claim_service

# Provide a entrypoint command for docker container to startup
CMD ["uvicorn", "claim_service.app:app", "--host", "0.0.0.0", "--port", "8000"]
