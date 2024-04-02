# billbot

*billbot* is a Python-based tool for managing house bills. It provides functionalities for indexing documents, querying them using natural language, and retrieving relevant information, leveraging [llama-index](https://github.com/run-llama/llama_index) and [OpenAI APIs](https://platform.openai.com/docs/overview).

## Features
- Document indexing: automatically indexes documents, such as bills and invoices, stored in a specified directory.
- Document parsing: parses various document formats, including PDF, to extract relevant information.
- Querying: enables users to query the indexed documents using natural language queries.
- Response synthesis: synthesizes responses to queries based on the indexed documents.

## Installation
1. Clone the repository

```bash
git clone https://github.com/yourusername/billbot.git
```

2. Go to project directory

```bash
cd billbot
```

3. Create a virtual environment and activate it:

```bash
# create a virtual environment
python -m venv venv

# activate the virtual environment
source venv/bin/activate  # for Linux/macOS
# or
.\venv\Scripts\activate    # for Windows
```

4. Install dependencies:

```bash
pip install -r requirements.txt
```

5. Create a ```data``` directory in the project root and place your input PDF files (e.g., bills, invoices) inside it.

6. Create a ```.env``` file in the project root and add your LlamaCloud and OpenAI API keys:

## Usage

1. Configure the settings in utils.py according to your preferences.

2. Run the main.py script with the desired query:

```bash
python main.py "Your query here"
```

## Contributing
Contributions are welcome! Please feel free to open issues for feature requests, bug fixes, or general feedback. Pull requests are also appreciated.

## License
This project is licensed under the MIT License.

## Acknowledgements
This project utilizes the following libraries:

- [llama-index](https://github.com/run-llama/llama_index): for document indexing and querying.
- [OpenAI](https://platform.openai.com/docs/overview): for natural language processing capabilities.
