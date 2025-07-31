# CrewAI CV Sorting

## Overview
CrewAI CV Sorting is an AI-powered automation tool for recruiters and HR professionals. It intelligently sorts, analyzes, and matches CVs and LinkedIn profiles against job criteria using autonomous agents and advanced parsing tools.

## Features
- Automated CV & LinkedIn PDF parsing
- Job criteria matching with customizable templates
- Multi-agent architecture for modular workflows
- Cross-verification of CV and LinkedIn data
- Scalable, extensible, and easy to configure

## Getting Started
### Prerequisites
- Python 3.10+
- pip (Python package manager)

### Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/Piash7285/crewai_cv_sorting.git
   cd crewai_cv_sorting
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

### Usage
1. Place your CV PDFs in the `cvs/` folder and LinkedIn PDFs in the `linkedin_pdfs/` folder.
2. Configure job criteria in `config/job_criteria.json` or use templates in `config/job_criteria_templates.txt`.
3. Run the main script:
   ```sh
   python main.py
   ```
4. Review results and logs for candidate matches and decisions.

## Project Structure
- `src/` - Core logic, agents, tasks, tools, and utilities
- `config/` - Job criteria templates and configuration files
- `cvs/` & `linkedin_pdfs/` - Candidate documents

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
MIT

## Author
Piash7285
