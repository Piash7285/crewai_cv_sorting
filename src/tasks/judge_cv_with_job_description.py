from crewai import Agent, Task, Crew
from src.agents.cv_analysis_agent import cv_processing_agent
from src.tasks.processing_cv_into_a_structure import process_cv_into_a_structure



judge_cv_against_job_criteria=Task(
    description=(
        "You have the structured CV data and the job description. "
        "now you need to analyze the CV against the job requirements "
        "and provide a detailed analysis on if the candidate is a good fit for the job. "
        "You should consider the candidate's qualifications, skills, experience, and any other relevant factors. "
        "Your analysis should be thorough and provide insights into the candidate's suitability for the position. "
        "Make sure to highlight any strengths or weaknesses in the candidate's profile "
        "and provide a clear recommendation based on the analysis."
    ),
    expected_output=(
        "A structured JSON object containing "
        "detailed analysis of the candidate's fit for the job, "
        "including strengths, weaknesses, and a clear recommendation. "
        "The output should also include any relevant insights or observations "
        "that can help in making a hiring decision. "
        "Also, include a confidence score for the recommendation "
        "(0.0 to 1.0, where 1.0 is very confident and 0.0 is not confident at all). "
    ),
    tools=[],
    context=[process_cv_into_a_structure],
    agent=cv_processing_agent,


)
