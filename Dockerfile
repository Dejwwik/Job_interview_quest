#Will use Python on that version to run this script. It will download it automatically
FROM python:3.11.4

# Set the working directory in the container
WORKDIR /app

# Copy the working files to /app directory 
COPY main.py /app/
COPY export_full.xml /app/

# Execute this to make script run
CMD ["python", "main.py"]
