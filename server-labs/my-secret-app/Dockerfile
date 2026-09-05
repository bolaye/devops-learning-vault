# 1. Start with a base image that already has Python installed
FROM python:3.14-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy all files from your local folder into the container's working directory
COPY . .

# 4. Tell the container what command to run when it starts
CMD ["python", "-m", "http.server", "8000"]