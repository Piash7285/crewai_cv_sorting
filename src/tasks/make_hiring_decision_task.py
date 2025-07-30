from crewai import Agent, Task, Crew
from src.agents.acceptance_decision_agent import acceptance_decision_agent
from src.tasks.cross_check_cv_and_linkedin_task import cross_check_cv_and_linkedin_task
from src.tasks.job_criteria_matching_task import job_criteria_matching_task

make_acceptance_decision = Task(
    name="make_acceptance_decision_task",
    description=(
        "Your task is to process the reports from Cross Checker Agent and Job Criteria Matcher, to decide "
        "whether to accept the cv for interview or not. "
        "You will receive the following inputs:\n"
        "- Cross Checker Report: A JSON report containing the results of the cross-checking between the CV and LinkedIn profile.\n"
        "- Job Criteria Matching Report: A JSON report containing the results of the job criteria matching analysis.\n\n"
        "ANALYSIS REQUIREMENTS:\n"
        "1. Review the Cross Checker Report to assess the credibility and consistency of the candidate's profile.\n"
        "2. Examine the Job Criteria Matching Report to evaluate the candidate's fit with the job requirements.\n"
        "3. Consider any red flags or warning signs from the cross-checking process.\n"
        "4. Evaluate the overall risk vs. benefit of hiring this candidate.\n"
        "5. Factor in the confidence scores from both analysis processes.\n"
        "6. Make a data-driven hiring recommendation with clear justification.\n\n"
    ),
    expected_output=(
        "A comprehensive hiring decision report in JSON format containing:\n\n"
        "{\n"
        '  "cv_acceptance": "ACCEPTED|REJECTED",\n'
        '  "confidence_score": "0.0-1.0",\n'
        '  "decision_summary": "Executive summary of the hiring decision",\n'
        '  "risk_assessment": {\n'
        '    "overall_risk_level": "low|medium|high",\n'
        '    "specific_risks": ["List of identified risks"],\n'
        '    "mitigation_strategies": ["Suggested risk mitigation approaches"]\n'
        '  },\n'
        '  "decision_reasoning": {\n"Your overall opinion and thought process for your decision.",\n'
        '}\n\n'
        "The output will be structured in a way that hiring managers can easily interpret and use for decision-making. "
        "Ensure that the analysis is thorough, actionable, and provides clear insights into the candidate's suitability for the position."
    ),
    agent=acceptance_decision_agent,
    context=[job_criteria_matching_task, cross_check_cv_and_linkedin_task],
)
