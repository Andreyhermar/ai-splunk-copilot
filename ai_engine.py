import requests

OLLAMA_URL = "http://localhost:11434/api/generate"


def analyze_log(log_text):
    prompt = f"""
You are a Senior Splunk Support Engineer and Site Reliability Engineer.

Analyze the following log.

Provide:

1. Root Cause
2. Impacted Component
3. Severity (P1, P2, or P3)
4. Recommended Troubleshooting Steps
5. Confidence Level

Log:

{log_text}
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        },
        timeout=120
    )

    response.raise_for_status()

    return response.json()["response"]