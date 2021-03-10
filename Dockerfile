# Use an official Python runtime as a parent image
FROM python:3.7

ENV TZ=Asia/Jakarta
ENV DB_HOST=mariadb
ENV DB_PORT=3306
ENV DB_USER=root
ENV DB_PASS=naikgaji
ENV DB_NAME=fastapi

ENV CACHE_HOST=127.0.0.1
ENV CACHE_PORT=6379
ENV CACHE_DB=0

ENV GATEWAY_URL="http://api-gateway:23120/"
ENV MONGO_URL='mongodb://qqplaysMonggoh:L3nOvo_57@localhost:27017/'
# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip
RUN pip install redis sqlalchemy pymysql pandas fastapi uvicorn python-dotenv pymongo sockets requests

# Copy the current directory contents into the container at /app
COPY . .

EXPOSE 3001

# Run app.py when the container launches
CMD ["python","-u","__main__.py"]