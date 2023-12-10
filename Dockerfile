FROM python:3.10

WORKDIR /app

# Copy the requirements.txt file into our working directory /app
COPY requirements.txt /app/

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app.py file into our working directory /app
COPY ./app.py /app/app.py

# Copy only the models/ and test_datasets/ directories
COPY models/ /app/models/
COPY test_datasets/ /app/test_datasets/

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]
