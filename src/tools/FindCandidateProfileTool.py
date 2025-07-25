from crewai import Agent, Task, Crew
from crewai_tools import BaseTool
import os


class find_cv_and_linkedin_path_tool(BaseTool):
    """
    Tool for locating and retrieving both CV and LinkedIn PDF files.

    This tool scans the 'cvs' directory for PDF files and looks for corresponding
    LinkedIn PDF files with the same name in the 'linkedin_pdfs' folder. It returns
    the absolute paths of both files when found, designed to work as part of a CV
    processing pipeline where agents need access to both traditional CV and LinkedIn
    profile information for comprehensive candidate analysis.

    Returns:
        str: Formatted string containing:
             - Absolute path to a CV PDF file
             - Absolute path to corresponding LinkedIn PDF file (if found)
             - Status messages for missing files or folders
             - Error message if no CVs are found

    Usage:
        Used by the supervisor agent and read files task to locate and retrieve
        candidate profile documents (CV and LinkedIn PDFs) before delegating
        CV processing tasks to other agents for structured information extraction.
    """


    name: str = "find_cv_and_linkedin_path_tool"
    description: str = ("Locates and retrieves both CV and LinkedIn PDF files for candidates, "
                        "returning absolute paths for comprehensive profile analysis")

    def _run(self) -> str:
        cvs_folder = os.path.join(os.getcwd(), 'cvs')
        linkedin_folder = os.path.join(os.getcwd(), 'linkedin_pdfs')
        print(60 * "-")
        print("Searching for CV and LinkedIn PDF files...")

        # Find first CV file
        if os.path.exists(cvs_folder):
            for cv in os.listdir(cvs_folder):
                if cv.endswith('.pdf'):
                    cv_path = os.path.abspath(os.path.join(cvs_folder, cv))

                    # Look for corresponding LinkedIn PDF with the same name
                    linkedin_path = os.path.join(linkedin_folder, cv)
                    if os.path.exists(linkedin_path):
                        linkedin_path = os.path.abspath(linkedin_path)
                        print(60* "-")
                        print(f"cv path:{cv_path}\nlinkedin path:{linkedin_path}")
                        return f"cv path:{cv_path}\nlinkedin path:{linkedin_path}"
                    else:
                        print(60 * "-")
                        print(f"cv path:{cv_path}\nNo LinkedIn profile found")
                        return f"cv path:{cv_path}\nNo LinkedIn profile found"
        print(60 * "-")
        print("no CV files found")
        return "No CV files found"
