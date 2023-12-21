# Gemini-File
Pdf Query chat-bot using Gemini Pro model and Llama Index

Gemini-File is a Streamlit web application that allows users to upload PDF files, index their contents using the Gemini search engine from the Llama-Index library, and query the documents.

## Preview

https://github.com/AjayK47/Gemini-File/assets/88961945/33ac787d-ea55-4571-af70-f3a46c2c60d1

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Uploading a PDF](#uploading-a-pdf)
  - [Querying Documents](#querying-documents)
- [Customisation](#Customisation)
- [Contributing](#contributing)
- [Future improvements](#Future-improvements)

## Features

- Upload PDF files for indexing.
- Perform text queries on the indexed documents.
- Powered by the Gemini Pro model and Hugging Face embeddings.

## Getting Started
### Prerequisites

!! Strongly Recommend running this code while connected to GPU !!

Before you begin, ensure you have the following installed:

- Python (>=3.6)
- [Streamlit](https://streamlit.io/)
- [Llama-Index](https://github.com/example/llama-index) library
- Google API key (set as an environment variable)

You can get this Google gemini APi key from [Google AI Developer Website](https://ai.google.dev/) , you can easily signup and get one  for free.

### Google API Key Configuration

The Google API key is set as an environment variable. Ensure it is correctly configured before running the app.


### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/AjayK47/Gemini-File.git
   ``` 
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
    ```
## Usage
### Uploading a PDF
1. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```
2. Access the app in your web browser.
3. Use the "Upload your PDF" button to upload a PDF file.

### Querying Documents
1. It takes some time to index your file to database or storage depending on size of your file.

2. Click on the search or submit button to perform the query., it will produce a Response.

## Customisation

### Using Other Embedding Models

You can customize the embedding model used for document indexing. Edit the 'app.py' file and modify the 'HuggingFaceEmbedding' instantiation:

```bash
# Example using a different Hugging Face model
embed_model_custom = HuggingFaceEmbedding(model_name="your/own-model-name")
```
you can find best text embedding model for you with help of 
[MTEB Leaderboard](https://huggingface.co/spaces/mteb/leaderboard)

![image](https://github.com/AjayK47/Gemini-File/assets/88961945/7de6ee4a-2a36-4ce5-81b3-06f81151eb68)

## Contributing

Contributions are encouraged! Fork the repository, create a feature branch, make changes, push to the branch, and open a pull request

## Future improvements

- **Use Open Source Embedding Models:** Explore integrating open-source embedding models instead of relying on proprietary models like Gemini API.

- **Improved UI/UX:** Enhance the user interface and experience for better usability.

- **Scalability:** Optimize the application for large document collections and improve search speed.

- **Dockerization:** Provide a Docker container for easy deployment.

## Authors

- [Ajay K](https://www.github.com/AjayK47)















