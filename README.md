docker build -t fastapi-image  .
docker run -d --name fastapi-container -p 8000:8000 fastapi-image
