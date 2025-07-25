from crewai import Crew, Process
from src.agents.cv_analysis_agent import cv_processing_agent
from src.agents.linkedin_processing_agent import linkedin_processing_agent
from src.agents.supervisor_agent import supervisor_agent
from src.tasks.processing_cv_into_a_structure import process_cv_into_a_structure
from src.tasks.processing_linkedin_profile_task import process_linkedin_profile_into_a_structure
from src.tasks.judge_cv_with_job_description import judge_cv_against_job_criteria
from src.tasks.read_files_and_delegate_task import read_files_and_delegate_task
from src.utils.llm_call import get_llm


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

# Create a Crew with hierarchical process and supervisor as manager
crew = Crew(
    agents=[supervisor_agent, cv_processing_agent, linkedin_processing_agent],
    tasks=[
        read_files_and_delegate_task,
        process_cv_into_a_structure,
        process_linkedin_profile_into_a_structure,
        judge_cv_against_job_criteria
    ],
    process=Process.hierarchical,
    manager_llm=get_llm(),  # Required for hierarchical process
    verbose=True
)

# Run the crew
print("Starting CV processing workflow...")
result = crew.kickoff(inputs={"criteria": criteria})
print("Crew execution completed!")
print("Result:", result)
