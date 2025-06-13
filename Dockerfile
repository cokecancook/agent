# Use the official Ollama image as base
FROM ollama/ollama:latest

# Create a volume for Ollama data
VOLUME /root/.ollama

# Expose the Ollama API port
EXPOSE 11434

# Create a startup script
RUN echo '#!/bin/bash\nollama serve & sleep 5 && ollama pull gemma:latest && tail -f /dev/null' > /start.sh && \
    chmod +x /start.sh

# Use the startup script as the entrypoint
ENTRYPOINT ["/start.sh"] 