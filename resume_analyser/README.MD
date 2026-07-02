# Build the container image
docker build -t resume-analyser:latest .

# Run the isolated application
docker run -p 8501:8501 --env-file .env resume-analyser:latest
