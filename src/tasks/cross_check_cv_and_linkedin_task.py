from crewai import Task
from src.agents.cross_checker_agent import cross_checker_agent
from src.tasks.cv_structuring_task import cv_information_structuring
from src.tasks.linkedin_profile_structuring_task import linkedin_profile_structuring

cross_check_cv_and_linkedin_task = Task(
    name="cross_check_cv_and_linkedin_task",
    description=(
        "Your task is to analyze the structured CV and LinkedIn profile data provided in the context.\n"
        "You will compare the two profiles to ensure consistency and alignment in skills, experience, and education.\n\n"
        "It doesn't have to be a perfect match, but they should not contradict each other. "
        "If there are significant discrepancies, flag them as potential issues.\n\n"
        "Do NOT generate, infer, or fabricate any data. "
        "Prepare a report that describes your opinion on the candidate's transparency and consistency.\n\n"
        "The report should include:\n"
        "1. skills_match_analysis: a detailed breakdown of how the skills from both profiles align\n"
        "2. experience_analysis: an assessment of the experience level and relevance from both profiles\n"
        "3. education_analysis: an evaluation of the education background from both profiles\n"
        "4. consistency_check: a summary of any inconsistencies found between the CV and LinkedIn profile\n"
        "5. confidence_score: a number between 0.0 and 1.0 indicating your confidence in the consistency of the profiles\n"
        "6. opinion: your overall opinion on the candidate's transparency and consistency based on the analysis\n"
    ),
    expected_output=(
        "A comprehensive JSON report containing:\n"
        "1. skills_match_analysis: detailed breakdown of skill alignment\n"
        "2. experience_analysis: assessment of experience level and relevance\n"
        "3. education_analysis: education background evaluation\n"
        "4. consistency_check: summary of inconsistencies found between the CV and LinkedIn profile\n"
        "5. confidence_score: number between 0.0 and 1.0 indicating confidence in the consistency of the profiles\n"
        "6. opinion: overall opinion on the candidate's transparency and consistency based on the analysis"
    ),
    agent=cross_checker_agent,
    context=[cv_information_structuring, linkedin_profile_structuring],
)
