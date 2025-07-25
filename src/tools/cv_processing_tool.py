from pathlib import Path

import fitz

from crewai_tools import BaseTool


class CVProcessingTool(BaseTool):
    name: str = "CvProcessingTool"
    description: str = ("take the cv file path as input and return the content of the CV data."
                        )

    def _run(self, cv_file_path: str):
        """
        Parse a CV file and extract structured information.

        Args:
            cv_file_path: Path to the CV file

        Returns:
            string containing extracted CV data
        """
        try:
            file_path = Path(cv_file_path)
            if not file_path.exists():
                return {"error": f"File not found: {cv_file_path}"}

            text = self._extract_text_from_pdf(cv_file_path)

            if not text.strip():
                return {"error": "No text could be extracted from the file"}
            return text

        except Exception as e:
            return {"error": f"Failed to process CV: {str(e)}"}

    def _extract_text_from_pdf(self, pdf_path: str) -> str:
        """Extract text from PDF using both PyPDF2 and pdfplumber for better results."""
        text = ""

        # Try with pdfplumber first (better for complex layouts)
        try:
            doc = fitz.open(str(pdf_path))
            for page in doc:
                text += page.get_text()

            # print("Extracted text using pdfplumber",text)
        except Exception as e:
            print(f"pdfplumber failed for {pdf_path}: {e}")

        return text
