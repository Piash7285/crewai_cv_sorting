from crewai import Task

from src.agents.linkedin_processor_agent import linkedin_processor_agent
from src.tools.linkedin_parser_tool import LinkedInProfileParserTool

linkedin_parser_tool = LinkedInProfileParserTool()

linkedin_information_extraction = Task(
    name="linkedin_information_extraction_task",
    description=(
        "You have been given a path to the linkedin profile file as {linkedin_path} for a candidate. Your task is to parse the pdf file "
        "and extract all the information from the file. You have a specialized tool for this task that can parse the pdf file "
        "and extract all the text from the pdf file. Use this tool to extract the information from the linkedin profile pdf file. The profile is"
        " in PDF format. "
    ),
    expected_output=(
        "Text extracted from the linkedin profile file at {linkedin_path}. the output should be a string containing all the text "
        "extracted from the linkedin profile file for the candidate. Ensure that the text is clean and readable, "
        "removing any unnecessary formatting or artifacts from the PDF extraction process."
    ),
    agent=linkedin_processor_agent,
    tools=[linkedin_parser_tool],
)
