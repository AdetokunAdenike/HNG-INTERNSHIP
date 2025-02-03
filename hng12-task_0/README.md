# HNG Stage 0 - Public API

## Introduction
This is a simple public API developed for the **HNG12 Stage 0 Backend Task**. The API returns basic information in JSON format, including:

- **Your registered email address** (used to register on the HNG12 Slack workspace).
- **The current datetime** as an ISO 8601 formatted timestamp (UTC).
- **The GitHub URL** of the project's codebase.

The API is designed to be **fast**, **lightweight**, and **publicly accessible**.

## Features
- Returns a structured JSON response.
- Dynamically generates the current datetime.
- Implements CORS handling.
- Hosted on a publicly accessible endpoint.

## Technologies Used
- **Python**
- **Flask**
- **Flask-CORS**
- **Vercel** (for deployment)

## API Specification
### Endpoint: `GET /`
This endpoint returns the required JSON response.

#### Example Response (200 OK):
```json
{
  "email": "your-email@example.com",
  "current_datetime": "2025-01-30T09:30:00Z",
  "github_url": "https://github.com/yourusername/your-repo"
}
```

## Getting Started
### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/HNG12-INTERNSHIP.git
cd HNG12-INTERNSHIP
```

### 2. Create a Virtual Environment (Recommended)
```bash
python3 -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the API Locally
```bash
python app.py
```
This will start the server on **http://127.0.0.1:5000/**.

### 5. Test the API Locally
Use a tool like **Postman** or **cURL**:
```bash
curl http://127.0.0.1:5000/
```

## Deployment
The API is deployed to **Vercel** for public access.

### Deploying to Vercel
1. Install the Vercel CLI (if not already installed):
   ```bash
   npm install -g vercel
   ```
2. Run the deployment command:
   ```bash
   vercel --prod
   ```
3. The API will be live at the generated Vercel URL.

## Link to the Live API
[API Live on Vercel](https://hng-12-internship-gamma.vercel.app)

## Contribution
Feel free to fork the repository, open issues, or submit pull requests. Contributions are always welcome!

## License
This project is licensed under the **MIT License**.

## Useful Links
- [Python Developers](https://hng.tech/hire/python-developers)
- [HNG Internship](https://hng.tech)

