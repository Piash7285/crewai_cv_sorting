from crewai import Agent, Task, Crew
from pydantic import BaseModel
from typing import List, Optional
from src.agents.cv_analysis_agent import cv_processing_agent
from src.tools.cv_processing_tool import CVProcessingTool
from src.tasks.read_files_and_delegate_task import read_files_and_delegate_task

cv_processing_tool = CVProcessingTool()

class Education(BaseModel):
    degree: str
    institution: str
    year: str

class Experience(BaseModel):
    job_title: str
    company: str
    duration: str
    responsibilities: str

class Certification(BaseModel):
    name: str
    year: str

class dataModel(BaseModel):
    name: str
    email: str
    phone: str
    address: str
    education: List[Education]
    experience: List[Experience]
    skills: List[str]
    certifications: List[Certification]

process_cv_into_a_structure = Task(
    description=(
        "Extract and process CV information from the PDF file path provided by the supervisor agent. "
        "Use the CV file path from the context to extract the following information:\n"
        "1. Personal details: name, email, phone, address\n"
        "2. Education background: degree, institution, graduation year\n"
        "3. Work experience: job titles, companies, duration, key responsibilities\n"
        "4. Skills: technical and soft skills\n"
        "5. Certifications: certification names and years obtained\n\n"
        "Convert all extracted information into the structured dataModel format "
        "ensuring all fields are properly populated and formatted. "
        "Use the cv_file_path parameter from the supervisor's delegation."
    ),
    expected_output=(
        "A structured dataModel object containing all extracted CV information "
        "in the following format:\n"
        "- name: Full candidate name\n"
        "- email: Email address\n"
        "- phone: Phone number\n"
        "- address: Complete address\n"
        "- education: List of Education objects with degree, institution, year\n"
        "- experience: List of Experience objects with job_title, company, duration, responsibilities\n"
        "- skills: List of skills as strings\n"
        "- certifications: List of Certification objects with name and year\n\n"
        "The output must be a valid dataModel instance that can be serialized to JSON "
        "if any information is missing, it should be marked as 'Not available'. "
        "and used for further analysis and hiring decisions."
    ),
    tools=[cv_processing_tool],
    agent=cv_processing_agent,
    context=[read_files_and_delegate_task],
    output_pydantic=dataModel,
)
