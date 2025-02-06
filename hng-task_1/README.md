# Number Classification API

This API classifies a number and returns its mathematical properties along with a fun fact.

## Endpoint
`GET /api/classify-number?number=<number>`

## Example
Request:
```
GET /api/classify-number?number=371
```

Response:
```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
```

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/HNG-INTERNSHIP.git
   cd HNG-INTERNSHIP/hng-task_1
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the server:
   ```bash
   uvicorn app:app --reload
   ```

4. Access the API at:
   ```
   http://127.0.0.1:8000/api/classify-number?number=<your-number>
   ```

## Deployment
[API Live on Vercel]()

## Technologies Used
- Python
- FastAPI
- Uvicorn
- Vercel (for deployment)

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.