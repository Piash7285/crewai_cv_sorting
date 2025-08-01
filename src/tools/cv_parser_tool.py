from pathlib import Path

import fitz

from crewai.tools import BaseTool

class CVParserTool(BaseTool):
    name: str = "CVParserTool"
    description: str = ("take the cv file path as input and return the content of the CV data."
                        )

    def _run(self, cv_path: str):
        """
        Parse a CV file and extract all the information. This tool only reads the text in the file and returns raw string

        Args:
            cv_path: Path to the CV file

        Returns:
            string containing extracted CV data
        """
        try:
            file_path = Path(cv_path)
            if not file_path.exists():
                return {"error": f"File not found: {cv_path}"}

            text = self._extract_text_from_pdf(cv_path)

            if not text.strip():
                return {"error": "No text could be extracted from the file"}
            return text

        except Exception as e:
            return {"error": f"Failed to process CV: {str(e)}"}

    def _extract_text_from_pdf(self, pdf_path: str) -> str:
        text = "---BEGIN CV CONTENT---"
        try:
            doc = fitz.open(str(pdf_path))
            for page in doc:
                text += page.get_text()

            text += "---END CV CONTENT---"
            # print("Extracted text from cv",text)
            print("Extracted text from cv")
        except Exception as e:
            print(f"pdfplumber failed for {pdf_path}: {e}")

        return text
