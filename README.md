# Cover Letter Generator

This application is a simple, interactive web tool built with Streamlit, which helps users generate personalized cover letters. The application uses a language model (LLM) to create cover letters based on user input, including job title, company name, resume PDF, and job description.

## Features

- **Input Fields**: Users can input the job title, company name, and the person to whom the cover letter should be addressed.
- **Resume Upload**: Users can upload their resume in PDF format.
- **Job Description**: Users can paste the job description, which will be used to tailor the cover letter.
- **Cover Letter Generation**: The application generates a cover letter that aligns the user's qualifications and experiences with the job description.

## Prerequisites

Ensure you have the following installed on your system:

- Python 3.8+
- Pip (Python package installer)

## Installation

1. **Clone the repository** (or download the code):
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install the required Python packages**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Start the Streamlit application**:
   ```bash
   streamlit run app.py
   ```
    replace app with the code name
## Usage

1. **Open the Web Interface**: After starting the application, open the provided URL (usually `http://localhost:8501`) in your web browser.

2. **Fill in the Input Fields**:
   - Enter the job title.
   - Enter the company name.
   - Enter the name of the person the cover letter is addressed to.
   - Paste the job description.
   - Upload your resume in PDF format.

3. **Generate the Cover Letter**: Click the "Generate Cover Letter" button to produce a personalized cover letter.

4. **Review the Generated Cover Letter**: The generated cover letter will be displayed on the page.

## Requirements

The application requires the following Python packages, which are listed in the `requirements.txt` file:

```plaintext
streamlit
pdfplumber
langchain
```

Note: Make sure to adjust the `Ollama` LLM's `base_url` according to your local setup in the code. The current configuration expects an LLM server running at `http://localhost:11434`.

## Troubleshooting

- If the cover letter generation fails, ensure that the LLM server is running and accessible at the configured URL.
- Check that the uploaded resume PDF is not corrupted and contains text that can be extracted.

## Acknowledgments

- [Streamlit](https://streamlit.io/) for the easy-to-use web app framework.
- [PDFPlumber](https://github.com/jsvine/pdfplumber) for the PDF extraction capabilities.
- [LangChain](https://github.com/hwchase17/langchain) for the seamless integration with language models.
