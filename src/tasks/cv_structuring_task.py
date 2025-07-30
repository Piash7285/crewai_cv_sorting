from crewai import Agent, Task, Crew
from src.agents.cv_processor_agent import CV_processor_agent
from src.tasks.cv_information_extract_task import cv_information_extraction



cv_information_structuring = Task(
    name="cv_information_structuring_task",
    description=(
        "Your task is to structure candidate CV data using ONLY the content provided between the "
        "`---BEGIN CV CONTENT---` and `---END CV CONTENT---` markers.\n\n"
        "Do NOT generate, infer, or fabricate any data.\n"
        "Do NOT repeat skills or content unnecessarily.\n"
        "If any required information is not present, explicitly write 'Not Available'.\n\n"
        "Extract the following fields:\n"
        "- Personal Details: name, email, phone, address\n"
        "- Education: degree, institution, graduation year\n"
        "- Work Experience: job title, company, duration, key responsibilities\n"
        "- Skills: only the actual skills listed\n"
        "- Certifications: certification name and year\n\n"
        "Strictly extract only what is visible between the content markers."
    ),
    expected_output=(
        "A Python dictionary structured as follows:\n\n"
        "```\n"
        "{\n"
        "  'name': str,\n"
        "  'email': str,\n"
        "  'phone': str,\n"
        "  'address': str,\n"
        "  'education': [\n"
        "    {'degree': str, 'institution': str, 'graduation_year': str}\n"
        "  ],\n"
        "  'experience': [\n"
        "    {'job_title': str, 'company': str, 'duration': str, 'responsibilities': str}\n"
        "  ],\n"
        "  'skills': [str],\n"
        "  'certifications': [\n"
        "    {'name': str, 'year': str}\n"
        "  ]\n"
        "}\n"
        "```\n\n"
        "Only use the data from the CV content block. Do not generate or infer missing details."
        "If any information is not present, explicitly note 'Not Available'.\n"
        "Ensure all data types match the expected schema.\n"
        "Remove any duplicate entries.\n"
    ),
    agent=CV_processor_agent,
    context=[cv_information_extraction]
)
