import streamlit as st
import pdfplumber
from langchain_community.llms import Ollama

# Main Streamlit App
def main():
    st.title("Cover Letter Generator")

    # User Inputs
    job_title = st.text_input("Enter the Job Title:")
    company_name = st.text_input("Enter the Company Name:")
    addressed_to = st.text_input("To Whom Should the Cover Letter be Addressed:")
    job_description = st.text_area("Paste the Job Description Here:")
    uploaded_pdf = st.file_uploader("Upload your Resume PDF", type="pdf")

    # On form submission
    if st.button("Generate Cover Letter"):

        if uploaded_pdf is None:
            st.error("Please upload a PDF file.")
            return

        # Initialize the LLM
        llm = Ollama(
            model="llama2",
            base_url="http://localhost:11434"  # Adjust this URL based on your setup
        )

        # Extract resume text from PDF
        with open("uploaded_resume.pdf", "wb") as f:
            f.write(uploaded_pdf.read())
        
        with pdfplumber.open("uploaded_resume.pdf") as pdf:
            resume_text = ""
            for page in pdf.pages:
                resume_text += page.extract_text()

        # Create a prompt for generating the cover letter
        prompt = (f"Using the following job details provided by the user through Streamlit:\n\n"
                  f"Job Title: {job_title}\n"
                  f"Company Name: {company_name}\n"
                  f"Addressed To: {addressed_to}\n\n"
                  f"Resume Content:\n{resume_text}\n\n"
                  f"Job Description:\n{job_description}\n\n"
                  f"Please generate a personalized and professional cover letter that aligns the applicant's "
                  f"qualifications and experiences with the job description, highlighting strengths and relevant experiences.")

        # Generate the cover letter using the LLM
        try:
            response = llm.predict(prompt)
            cover_letter = response.strip()

            # Ensure the cover letter is not empty
            if not cover_letter:
                cover_letter = "Generated content is too short. Please try again."

            st.write(f"Generated Cover Letter:\n\n{cover_letter}")

        except Exception as e:
            st.error(f"Error: {e}")

if __name__ == "__main__":
    main()
