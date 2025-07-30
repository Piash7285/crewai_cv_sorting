from crewai import Agent, Task, Crew
from src.agents.supervisor_agent import supervisor_agent


assign_task = Task(
    name="assign_task",
    description=(
        "You have been assigned the role of HR Workflow Coordinator. Your task is to orchestrate the candidate "
        "evaluation workflow by task delegation to the proper agents. You have cv in the {cv_path} and LinkedIn profile "
        "in the {linkedin_path}. Provide the paths to the CV and LinkedIn profile to the appropriate agents for processing."
    ),
    expected_output=(
        "All relevant agents have been assigned their tasks with the correct CV and LinkedIn profile paths for further"
        " processing."
    ),
    agent=supervisor_agent,
)
