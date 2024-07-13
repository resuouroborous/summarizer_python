import click
import requests
import sys

# Generate your own Ollama API key
OLLAMA_API_URL = "http://localhost:11434/api/generate"


def summarize_text(text):
    prompt = f"Please provide a concise summary of the following text:\n\n{text}\n\nSummary:"
    
    payload = {
        "model": "qwen2:0.5b",
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(OLLAMA_API_URL, json=payload)
        response.raise_for_status()
        summary = response.json()["response"]
        return summary.strip()
    except requests.RequestException as e:
        print(f"Error: Failed to connect to Ollama API. Make sure it's running and accessible. {e}", file=sys.stderr)
        sys.exit(1)

@click.command()
@click.option('-t', '--text', help='Text to summarize')
@click.option('-f', '--file', type=click.File('r'), help='Text file to summarize')
def main(text, file):
    if text and file:
        print("Error: Please provide either text or a file, not both.", file=sys.stderr)
        sys.exit(1)
    
    if not text and not file:
        print("Error: Please provide either text or a file to summarize.", file=sys.stderr)
        sys.exit(1)
    
    if file:
        content = file.read()
        filename = file.name
        summary = summarize_text(content)
        print(f"Summary of {filename}:")
    else:
        summary = summarize_text(text)
        print("Summary:")
    
    print(summary)

if __name__ == '__main__':
    main()