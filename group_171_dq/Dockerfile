FROM python:3.9

# Set the working directory within the container
WORKDIR /app

# Copy the gx logic into the container at /app

COPY * /app

RUN pip install --upgrade pip
RUN pip install great-expectations
RUN pip install pandas
RUN pip install great-expectations-experimental


ENTRYPOINT ["python3"]
