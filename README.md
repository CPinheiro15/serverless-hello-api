# Serverless Hello API

A simple serverless API built using **AWS Lambda** and **API Gateway**.  
It returns a JSON response with a greeting and timestamp, and logs all requests to **CloudWatch**.

## 🚀 Live Demo
[Serverless Hello API](https://0gmu83cl9k.execute-api.eu-west-2.amazonaws.com)

## 🛠 Tools Used
- **AWS Lambda** (Python)
- **API Gateway**
- **CloudWatch Logs**

## 📌 Key Features
- Serverless design — no servers to manage
- Auto-scalable and cost-efficient
- Integrated logging with CloudWatch
- Returns dynamic timestamp for each request

## 💡 Usage
Send a GET request to the API Gateway endpoint and receive a JSON response:

```json
{
  "message": "Hello from AWS Lambda!",
  "timestamp": "2025-09-17 23:57:22.822195"
}
