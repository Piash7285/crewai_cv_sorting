from crewai import Agent, Task, Crew
from src.agents.checking_process_manager_agent import checking_process_manager_agent
from src.tasks.cv_structuring_task import cv_information_structuring
from src.tasks.linkedin_profile_structuring_task import linkedin_profile_structuring


oversee_checker_agents_task = Task(
    name="oversee_checker_agents_task",
    description=(
        "You have been assigned the role of the manager of the checking team. Your task is to ensure that all relevant agents "
        "have gotten their appropriate data and working efficiently on their tasks. You will oversee the "
        "cross_checker_agent and criteria_matcher_agent to ensure they have the necessary information to perform their tasks. "
        "After they have finished their tasks, the acceptance_checker_agent will process the reports and provide a final decision. "
        "Your goal is to ensure your subordinates are working effectively and that all tasks are completed within timelines.\n\n"

    ),
    expected_output=(
        "All relevant agents have been assigned their tasks and are working efficiently. "
    ),
    agent=checking_process_manager_agent,
    context=[cv_information_structuring,linkedin_profile_structuring],
)
