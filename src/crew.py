from crewai import Crew, Process
from src.tasks import tasks
from src.agents import agents

crew = Crew(
  agents=[
    cv_extractor, cv_structurer, job_matcher,
    linkedin_extractor, linkedin_structurer,
    cross_checker, final_decider
  ],
  tasks=[
    cv_extract_task, cv_structuring_task, job_matching_task,
    linkedin_extract_task, linkedin_structuring_task,
    cross_check_task, final_decision_task
  ],
  process=Process.sequential
)
