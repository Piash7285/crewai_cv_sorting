from crewai import Task
from src.agents.criteria_matcher_agent import criteria_matcher_agent
from src.tasks.cv_structuring_task import cv_information_structuring
from src.tasks.linkedin_profile_structuring_task import linkedin_profile_structuring

job_criteria_matching_task = Task(
    name="job_criteria_matching_task",
    description=(
        "You have been given the job description: {criteria}. "
        "Your task is to analyze the candidate's profile against this description and provide a detailed analysis "
        "on whether the candidate meets the job requirements. "
        "You should consider the candidate's qualifications, skills, experience, and any other relevant factors. "
        "Your analysis should be thorough and provide insights into the candidate's suitability for the position. "
        "Make sure to highlight any strengths or weaknesses in the candidate's profile "
        "and provide a clear recommendation based on the analysis.\n\n"
        "Focus your analysis on:\n"
        "1. Skills match percentage against required skills\n"
        "2. Experience level compatibility (required)\n"
        "3. Education requirements (required)\n"
        "4. Overall job fit assessment\n"
        "5. Preferred skills and companies (if applicable)\n\n"
        "DO NOT fabricate or hallucinate any information. "
        "Use the provided candidate profile data to perform the analysis directly. "
        "Ensure your analysis is based on the actual data available in the candidate's profile."
    ),
    expected_output=(
        "A detailed JSON analysis containing:\n"
        "1. skills_match_analysis: detailed breakdown of skill alignment\n"
        "2. experience_analysis: assessment of experience level and relevance\n"
        "3. education_analysis: education background evaluation\n"
        "4. strengths: list of candidate's key strengths\n"
        "5. weaknesses: list of areas of concern\n"
        "6. overall_recommendation: 'hire', 'interview', 'reject'\n"
        "7. confidence_score: number between 0.0 and 1.0"
        "8. detailed_reasoning: explanation of the recommendation\n"
        "9. validation_status: 'passed', 'warning', or 'failed' based on the validation of the candidate's profile against the job criteria\n"
        "10. additional_notes: any other relevant observations or insights that could impact the hiring decision\n"
    ),
    agent=criteria_matcher_agent,
    context=[cv_information_structuring, linkedin_profile_structuring],
)
