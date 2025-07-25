from crewai import Agent, Task, Crew
from src.agents.supervisor_agent import supervisor_agent
from src.tools.FindCandidateProfileTool import find_cv_and_linkedin_path_tool




read_files_and_delegate_task = Task(
    description=(
        "As the HR manager supervisor, execute the following workflow:\n"
        "1. Use find_cv_and_linkedin_path_tool to locate CV and LinkedIn PDF files\n"
        "2. Extract the absolute file paths from the tool output\n"
        "3. Parse the CV Path and LinkedIn PDF Path from the tool results\n"
        "4. Store the file paths for delegation to processing agents\n"
        "5. Prepare delegation instructions with specific file paths\n\n"
        "The tool will return results in format:\n"
        "CV Path: /absolute/path/to/cv.pdf\n"
        "LinkedIn PDF Path: /absolute/path/to/linkedin.pdf\n\n"
        "Extract these paths and prepare them for task delegation."
    ),
    expected_output=(
        "A comprehensive delegation report containing:\n"
        "1. CV file path extracted from find_cv_and_linkedin_path_tool\n"
        "2. LinkedIn PDF file path (if available)\n"
        "3. Delegation instructions for CV processing agent with specific cv_file_path\n"
        "4. Delegation instructions for LinkedIn processing agent with specific linkedin_file_path\n"
        "5. Workflow coordination status\n\n"
        "Format the output to clearly specify:\n"
        "- CV_FILE_PATH: [extracted path]\n"
        "- LINKEDIN_FILE_PATH: [extracted path or 'Not available']\n"
        "- DELEGATION_STATUS: Ready for processing\n\n"
        "This output will be used by subsequent tasks to access the correct file paths."
    ),
    tools=[find_cv_and_linkedin_path_tool],
    agent=supervisor_agent,
)
