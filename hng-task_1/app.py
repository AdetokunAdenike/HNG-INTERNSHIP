from fastapi import FastAPI, Query, HTTPException, Request
from fastapi.responses import JSONResponse, RedirectResponse
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
import httpx
import math

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Custom exception handler for validation errors
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    # Extract the invalid input from the query parameters
    query_params = request.url.query
    invalid_number = query_params.split("=")[1] if "=" in query_params else ""
    return JSONResponse(
        status_code=400,
        content={"number": invalid_number, "error": True},
    )

# Redirect root URL to /api/classify-number
@app.get("/")
async def redirect_to_api():
    return RedirectResponse(url="/api/classify-number")

# Helper functions
def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, math.isqrt(abs(n)) + 1):  # Use math.isqrt for better performance
        if n % i == 0:
            return False
    return True

def is_perfect(n: int) -> bool:
    if n < 2:
        return False
    divisors = [i for i in range(1, abs(n)) if n % i == 0]
    return sum(divisors) == abs(n)

def is_armstrong(n: int) -> bool:
    digits = [int(d) for d in str(abs(n))]
    length = len(digits)
    return sum(d ** length for d in digits) == abs(n)

def digit_sum(n: int) -> int:
    return sum(int(d) for d in str(abs(n)))

# Cache for fun facts
fun_fact_cache = {}

async def get_fun_fact(n: int) -> str:
    if n in fun_fact_cache:
        return fun_fact_cache[n]
    
    url = f"http://numbersapi.com/{n}/math"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
    fun_fact = response.text if response.status_code == 200 else "No fun fact available."
    fun_fact_cache[n] = fun_fact  # Cache the result
    return fun_fact

# API Endpoint
@app.get("/api/classify-number")
async def classify_number(number: int = Query(..., description="The number to classify")):
    properties = []
    if is_armstrong(number):
        properties.append("armstrong")
    if number % 2 == 0:
        properties.append("even")
    else:
        properties.append("odd")

    fun_fact = await get_fun_fact(number)  # Await the async function

    response = {
        "number": number,
        "is_prime": is_prime(number),
        "is_perfect": is_perfect(number),
        "properties": properties,
        "digit_sum": digit_sum(number),
        "fun_fact": fun_fact,
    }
    return response