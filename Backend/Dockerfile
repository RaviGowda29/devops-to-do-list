#for base python image 
FROM python:3.10-slim

#working directory
WORKDIR /app

#copy req.txt file
COPY req.txt .

#Install requirments
RUN pip install --no-cache-dir -r req.txt

#to copy application code
COPY app/ /app

#command to run app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
