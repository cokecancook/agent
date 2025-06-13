import requests
from typing import Dict, List, Optional

class LMStudioClient:
    def __init__(self, base_url: str = "http://localhost:1234/v1"):
        """Initialize the LM Studio client.
        
        Args:
            base_url: The base URL for the LM Studio API. Defaults to localhost:1234
        """
        self.base_url = base_url.rstrip('/')
        
    def generate_response(self, messages: List[Dict[str, str]], temperature: float = 0.7) -> Optional[str]:
        """Generate a response from the model.
        
        Args:
            messages: List of message dictionaries with 'role' and 'content'
            temperature: Controls randomness in the response (0.0 to 1.0)
            
        Returns:
            The generated response text or None if there was an error
        """
        try:
            response = requests.post(
                f"{self.base_url}/chat/completions",
                json={
                    "model": "google/gemma-3-4b",
                    "messages": messages,
                    "temperature": temperature,
                    "stream": False
                }
            )
            response.raise_for_status()
            return response.json()["choices"][0]["message"]["content"]
        except Exception as e:
            print(f"Error generating response: {e}")
            return None 