import json
import os

from crewai import Crew, Process
from src.utils.FindCandidateProfile import get_candidate
from src.utils.move_cv import move

from src.agents.supervisor_agent import supervisor_agent
from src.agents.cv_processor_agent import CV_processor_agent
from src.agents.linkedin_processor_agent import linkedin_processor_agent
from src.agents.criteria_matcher_agent import criteria_matcher_agent
from src.agents.cross_checker_agent import cross_checker_agent
from src.agents.acceptance_decision_agent import acceptance_decision_agent
from src.agents.checking_process_manager_agent import checking_process_manager_agent

from src.tasks.delegate_checking_tasks import oversee_checker_agents_task
from src.tasks.make_hiring_decision_task import make_acceptance_decision
from src.tasks.cross_check_cv_and_linkedin_task import cross_check_cv_and_linkedin_task
from src.tasks.job_criteria_matching_task import job_criteria_matching_task
from src.tasks.linkedin_information_extract_task import linkedin_information_extraction
from src.tasks.linkedin_profile_structuring_task import linkedin_profile_structuring
from src.tasks.cv_information_extract_task import cv_information_extraction
from src.tasks.cv_structuring_task import cv_information_structuring
from src.tasks.delegate_task import assign_task




criteria = {
  "position": "Machine Learning Engineer",
  "required_skills": ["Python", "TensorFlow", "Machine Learning", "Data Science", "PyTorch", "Scikit-learn"],
  "preferred_skills": ["Deep Learning"],
  "min_experience_years": 0,
  "max_experience_years": 10,
  "required_degree": "Bachelor",
  "preferred_companies": [],
  "minimum_skill_match_percentage": 40,
  "minimum_validation_score": 0.7
}

profiles= get_candidate()

crew = Crew(
    agents=[CV_processor_agent,
            linkedin_processor_agent,
            checking_process_manager_agent,
            criteria_matcher_agent,
            cross_checker_agent,
            acceptance_decision_agent],
    manager_agent=supervisor_agent,
    tasks=[
        assign_task,
        cv_information_extraction,
        cv_information_structuring,
        linkedin_information_extraction,
        linkedin_profile_structuring,
        oversee_checker_agents_task,
        job_criteria_matching_task,
        cross_check_cv_and_linkedin_task,
        make_acceptance_decision

    ],
    process=Process.hierarchical,
    # verbose=True
    verbose=False
)
results=[]
accepted_path = os.path.abspath(os.path.join(os.getcwd(), "accepted"))
rejected_path = os.path.abspath(os.path.join(os.getcwd(), "rejected"))
for profile in profiles:
    # Run the crew
    print("Starting CV processing workflow...")
    result = crew.kickoff(inputs={"criteria": criteria,"cv_path": profile["cv_path"], "linkedin_path": profile["linkedin_path"]})
    results.append(result)
    result_dict = result.json_dict
    if result_dict["cv_acceptance"] == "Accepted":
        move(profile["cv_path"], accepted_path)
    else:
        move(profile["cv_path"], rejected_path)

print("Crew execution completed!")
print("Results:", results)

for result in results:
    result_dict = result.json_dict
    print(result_dict)
    print("Final Decision:", result_dict["cv_acceptance"])
