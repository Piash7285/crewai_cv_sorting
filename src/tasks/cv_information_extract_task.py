from crewai import Agent, Task, Crew
from src.agents.cv_processor_agent import CV_processor_agent
from src.tools.cv_parser_tool import CVParserTool

cv_parser_tool = CVParserTool()

cv_information_extraction = Task(
    name="cv_information_extraction_task",
    description=(
        "You have been given a path to the CV file as {cv_path} for a candidate. Your task is to parse the CV file "
        "and extract all the information from the CV. You have a specialized tool for this task that can parse the CV "
        "and extract all the text from the CV file. Use this tool to extract the information from the CV file. The cv is"
        " in PDF format. "
    ),
    expected_output=(
        "Text extracted from the CV file at {cv_path}. the output should be a string containing all the text "
        "extracted from the CV file for the candidate. Ensure that the text is clean and readable, "
        "removing any unnecessary formatting or artifacts from the PDF extraction process."
    ),
    agent=CV_processor_agent,
    tools=[cv_parser_tool],
)
