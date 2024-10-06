# Text Summarizer CLI

A command-line interface tool that summarizes text from files or direct input using the Ollama API with the Qwen2 0.5B model.

## Features

- Summarize text from a file
- Summarize text provided directly in the command line
- Uses Ollama API with Qwen2 0.5B model for efficient summarization

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.6+
- Ollama installed and running on your machine
- Qwen2 0.5B model available in Ollama

## Installation

1. Clone this repository: git clone [https://github.com/resuouroborous/python_assignment.git](https://github.com/resuouroborous/summarizer_python.git)

2. Install the required Python packages:
   pip install click requests

3. Install Ollama if you haven't already:
- For macOS or Linux:
  ```
  curl https://ollama.ai/install.sh | sh
  ```
- For Windows, download the installer from [ollama.ai/download](https://ollama.ai/download)

4. Pull the Qwen2 0.5B model:
   ollama pull qwen2:0.5b

## Usage

1. Start the Ollama service:
   ollama serve

2. Run the summarizer:

- To summarize a text file:
  ```
  python summarizer.py -f path/to/your/file.txt
  ```

- To summarize text directly:
  ```
  python summarizer.py -t "Your long text goes here..."
  ```

## Examples

1. Summarize a file named 'article.txt':
   python summarizer.py -f article.txt

2. Summarize a given text:
   python summarizer.py -t "The quick brown fox jumped over the lazy dog."

## Contributing

Contributions to this project are welcome. Please feel free to submit a Pull Request.

## License

This project is not licensed under any as it's an assignment but if you want you could license it under the MIT License, etc...

## Acknowledgments

- [Ollama](https://ollama.ai/) for providing the API and model
- [Click](https://click.palletsprojects.com/) for the command-line interface
- [Qwen2 0.5B model](https://github.com/QwenLM/Qwen) for text summarization
