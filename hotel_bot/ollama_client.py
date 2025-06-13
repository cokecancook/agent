import requests
from typing import Dict, List, Optional

class OllamaClient:
    def __init__(self, base_url: str = "http://localhost:11434"):
        """Initialize the Ollama client.
        
        Args:
            base_url: The base URL for the Ollama API. Defaults to localhost:11434
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
            # Convert messages to a single prompt string
            prompt = "\n".join([f"{msg['role']}: {msg['content']}" for msg in messages])
            
            response = requests.post(
                f"{self.base_url}/api/generate",
                json={
                    "model": "gemma",
                    "prompt": prompt,
                    "stream": False,
                    "temperature": temperature
                }
            )
            response.raise_for_status()
            return response.json()["response"]
        except Exception as e:
            print(f"Error generating response: {e}")
            return None 