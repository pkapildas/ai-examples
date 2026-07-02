# Use a slim Python runtime environment for high efficiency
FROM python:3.11-slim

# Set container engine system environment variable rules 
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Establish isolated internal application footprint
WORKDIR /app

# Install native OS dependencies required by pdfplumber processing frameworks
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Optimize layer caching steps by copying requirements independently first
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Sync application source code frameworks
COPY src/ ./src/
COPY app.py .

# Streamlit uses network socket port 8501 by default
EXPOSE 8501

# Command layout instructions matching cloud hosting configurations
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
