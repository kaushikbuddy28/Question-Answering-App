# Testing Instructions

This folder contains scripts to verify the API functionality.

## Prerequisites
- The API server must be running locally on port 5000.
  ```bash
  uvicorn app.main:app --host 0.0.0.0 --port 5000
  ```

## 1. Python Test
Run the Python test script to check basic connectivity and response structure.
```bash
python test_api.py
```

## 2. Curl Test (Windows)
Run the batch file to send a request using `curl` and the sample payload.
```bash
test_curl.bat
```

## 3. Manual Curl
You can also run curl manually:
```bash
curl -X POST "http://localhost:5000/ask" -H "Content-Type: application/json" -d "{\"context\": \"My name is Alice.\", \"question\": \"Who am I?\"}"
```
