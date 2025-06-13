#!/bin/bash

# Start Ollama in the background
ollama serve &

# Wait for Ollama to start
sleep 5

# Pull the model
ollama pull gemma:2b

# Keep the container running
tail -f /dev/null 