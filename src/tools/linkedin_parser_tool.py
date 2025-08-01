from pathlib import Path
import fitz
from crewai.tools import BaseTool


class LinkedInProfileParserTool(BaseTool):
    name: str = "LinkedInProfileParserTool"
    description: str = ("Extract and process LinkedIn profile information from PDF files. "
                        "Takes the LinkedIn PDF file path as input and returns the content.")

    def _run(self, linkedin_file_path: str):
        """
        Parse a LinkedIn PDF file and extract profile information. This tool only reads the text in the file and returns raw string

        Args:
            linkedin_file_path: Path to the LinkedIn PDF file

        Returns:
            string containing extracted LinkedIn profile data
        """
        try:
            file_path = Path(linkedin_file_path)
            if not file_path.exists():
                return {"error": f"LinkedIn file not found: {linkedin_file_path}"}

            text = self._extract_text_from_pdf(linkedin_file_path)

            if not text.strip():
                return {"error": "No text could be extracted from the LinkedIn file"}
            return text

        except Exception as e:
            return {"error": f"Failed to process LinkedIn profile: {str(e)}"}

    def _extract_text_from_pdf(self, pdf_path: str) -> str:
        """Extract text from LinkedIn PDF using PyMuPDF."""
        text = "---BEGIN PROFILE CONTENT---"
        try:
            doc = fitz.open(str(pdf_path))
            for page in doc:
                text += page.get_text()
            doc.close()
            text += "---END PROFILE CONTENT---"
            # print("Extracted LinkedIn profile text successfully.", text)
            print("Extracted LinkedIn profile text successfully.")
        except Exception as e:
            print(f"LinkedIn PDF extraction failed for {pdf_path}: {e}")
        return text
