from crewai import Task
from pydantic import BaseModel
from typing import List, Optional
from src.agents.linkedin_processing_agent import linkedin_processing_agent
from src.tools.linkedin_processing_tool import LinkedInProcessingTool
from src.tasks.read_files_and_delegate_task import read_files_and_delegate_task

linkedin_processing_tool = LinkedInProcessingTool()


class ProfileSummary(BaseModel):
    name: str
    current_position: str
    industry: str
    location: str
    professional_headline: str


class CareerAnalysis(BaseModel):
    total_experience_years: str
    career_progression: str
    job_stability: str
    industry_consistency: str


class SkillsVerification(BaseModel):
    technical_skills: List[str]
    leadership_skills: List[str]
    industry_specific: List[str]
    skill_endorsements_available: bool


class EducationVerification(BaseModel):
    degrees: List[str]
    institutions: List[str]
    graduation_years: List[str]


class LinkedInDataModel(BaseModel):
    profile_summary: ProfileSummary
    career_analysis: CareerAnalysis
    skills_verification: SkillsVerification
    education_verification: EducationVerification
    experience_timeline: List[str]
    professional_credibility: str
    profile_completeness: str


process_linkedin_profile_into_a_structure = Task(
    description=(
        "Process LinkedIn profile PDF and extract comprehensive professional information. "
        "Analyze the LinkedIn profile data to provide:\n"
        "1. Professional summary and career trajectory analysis\n"
        "2. Skills validation and categorization\n"
        "3. Experience timeline verification\n"
        "4. Education background analysis\n"
        "5. Professional network and endorsement insights (if available)\n"
        "6. Career growth pattern assessment\n"
        "7. Industry expertise identification\n\n"
        "Use the LinkedIn file path provided by the supervisor agent to process the correct profile."
    ),
    expected_output=(
        "A structured LinkedInDataModel object containing comprehensive LinkedIn analysis "
        "in JSON format with the following structure:\n"
        "- profile_summary: name, current_position, industry, location, professional_headline\n"
        "- career_analysis: total_experience_years, career_progression, job_stability, industry_consistency\n"
        "- skills_verification: technical_skills, leadership_skills, industry_specific, skill_endorsements_available\n"
        "- education_verification: degrees, institutions, graduation_years\n"
        "- experience_timeline: chronological work history\n"
        "- professional_credibility: assessment (high/medium/low)\n"
        "- profile_completeness: score out of 100\n\n"
        "If any information is missing, mark as 'Not available'."
    ),
    tools=[linkedin_processing_tool],
    agent=linkedin_processing_agent,
    context=[read_files_and_delegate_task],
    output_pydantic=LinkedInDataModel,
)
