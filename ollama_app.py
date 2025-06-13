import requests
import json

def generate_response(prompt):
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": "gemma:2b",
        "prompt": prompt,
        "stream": False
    }
    
    response = requests.post(url, json=payload)
    return response.json()

# Example usage
response = generate_response("Hello, how are you?")
print(response["response"])

# Access different parts of the response
print("\nModel:", response["model"])
print("Response:", response["response"])
print("Created at:", response["created_at"])
print("Done:", response["done"])
print("Done reason:", response["done_reason"])

# Access performance metrics
print("\nPerformance Metrics:")
print("Total duration:", response["total_duration"] / 1e9, "seconds")  # Convert nanoseconds to seconds
print("Load duration:", response["load_duration"] / 1e9, "seconds")
print("Prompt eval count:", response["prompt_eval_count"])
print("Prompt eval duration:", response["prompt_eval_duration"] / 1e9, "seconds")
print("Eval count:", response["eval_count"])
print("Eval duration:", response["eval_duration"] / 1e9, "seconds") 