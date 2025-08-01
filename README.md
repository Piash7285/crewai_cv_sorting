# CV Processing System

An AI-powered CV processing system that automatically evaluates candidate CVs and LinkedIn profiles against job criteria using CrewAI agents. The system integrates with Odoo for HR management and uses Docker for easy deployment.

## Features

- **Automated CV Processing**: Extract and structure information from PDF CVs
- **LinkedIn Profile Analysis**: Process LinkedIn profiles in PDF format
- **AI-Powered Evaluation**: Multi-agent system for comprehensive candidate assessment
- **Job Criteria Matching**: Compare candidates against specific job requirements
- **Cross-Validation**: Verify consistency between CV and LinkedIn data
- **Odoo Integration**: Automatically upload accepted candidates to Odoo HR system
- **Docker Support**: Easy deployment with Docker Compose

## Architecture

The system uses a hierarchical multi-agent approach with the following agents:
- **Supervisor Agent**: Orchestrates the entire workflow
- **CV Processor Agent**: Extracts and structures CV data
- **LinkedIn Processor Agent**: Processes LinkedIn profile information
- **Criteria Matcher Agent**: Evaluates candidates against job criteria
- **Cross Checker Agent**: Validates consistency between CV and LinkedIn data
- **Acceptance Decision Agent**: Makes final hiring recommendations

## Getting Started
### Prerequisites
- Python 3.10+
- pip (Python package manager)
- Docker and Docker Compose
- Odoo instance (optional, for HR integration)
- Google Gemini API key


## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Piash7285/crewai_cv_sorting.git
   cd crewai_cv_sorting
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   Create a `.env` file in the root directory:
   ```env
   # Google/Gemini API Configuration
   GOOGLE_API_KEY=your_gemini_api_key_here
   
   # Odoo Connection Settings
   ODOO_URL=http://localhost:8069
   ODOO_DB=your_database_name
   ODOO_USERNAME=your_odoo_username
   ODOO_PASSWORD=your_odoo_password
   ```

## Docker Compose Setup

### Starting Odoo with Docker Compose

The project includes a Docker Compose configuration for running Odoo locally:

1. **Navigate to the Docker Compose directory**
   ```bash
   cd docker_compose_file
   ```

2. **Start Odoo and PostgreSQL**
   ```bash
   docker-compose up -d
   ```

3. **Access Odoo**
   - URL: http://localhost:8069
   - Create a new database when prompted
   - Install the HR module for recruitment features

4. **Stop the services**
   ```bash
   docker-compose down
   ```

### Docker Compose Configuration

The `docker-compose.yml` file includes:
- **Odoo**: HR management system on port 8069
- **PostgreSQL**: Database backend for Odoo
- **Persistent volumes**: Data persistence across container restarts

## Usage

### Preparing Files

1. **Add CV files**: Place PDF CVs in the `cvs/` folder
2. **Add LinkedIn profiles**: Place corresponding LinkedIn PDFs in the `linkedin_pdfs/` folder
3. **Ensure matching names**: CV and LinkedIn files should have identical filenames

### Running the System

1. **Start the processing**
   ```bash
   python main.py
   ```

2. **Review results**
   - Accepted candidates are moved to `accepted/` folder
   - Rejected candidates are moved to `rejected/` folder
   - Results are automatically uploaded to Odoo (if configured)

### Job Criteria Configuration

Edit the criteria in `main.py`:
```python
criteria = {
    "position": "Machine Learning Engineer",
    "required_skills": ["Python", "TensorFlow", "Machine Learning"],
    "preferred_skills": ["Deep Learning"],
    "min_experience_years": 0,
    "max_experience_years": 10,
    "required_degree": "Bachelor",
    "minimum_skill_match_percentage": 40,
    "minimum_validation_score": 0.7
}
```

## Odoo Integration

The system automatically integrates with Odoo for HR management:

### Features
- **Position Management**: Fetch available job positions from Odoo
- **Candidate Upload**: Automatically create applicant records for accepted candidates
- **CV Attachment**: Attach original CV files to applicant records
- **Metadata Tracking**: Include evaluation scores and reasoning

### CV Manager Functions

The `cv_manager.py` module provides three core functions:

1. **check_positions()**: Returns all available job positions
2. **add_cvs(cv_path, position)**: Adds a CV to a specific position
3. **show_uploads()**: Displays all uploaded CVs and their positions

### Usage Example
```python
from cv_manager import check_positions, add_cvs, show_uploads

# Check available positions
positions = check_positions()
print(positions)

# Add a CV to a position
success = add_cvs("path/to/cv.pdf", "Software Engineer")

# Show all uploads
uploads = show_uploads()
```

## File Structure

```
cv_processing_2/
├── main.py                     # Main application entry point
├── cv_manager.py              # Odoo integration module
├── requirements.txt           # Python dependencies
├── pyproject.toml            # UV configuration
├── docker_compose_file/      # Docker Compose setup
│   └── docker-compose.yml
├── cvs/                      # Input CV files
├── linkedin_pdfs/           # Input LinkedIn profiles
├── accepted/                # Accepted candidates
├── rejected/               # Rejected candidates
├── config/                 # Configuration files
├── src/
│   ├── agents/            # CrewAI agent definitions
│   ├── tasks/             # Task definitions
│   ├── tools/             # Custom tools
│   └── utils/             # Utility functions
```

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `GOOGLE_API_KEY` | Google Gemini API key | Required |
| `ODOO_URL` | Odoo instance URL | http://localhost:8069 |
| `ODOO_DB` | Odoo database name | test |
| `ODOO_USERNAME` | Odoo username | Required |
| `ODOO_PASSWORD` | Odoo password | Required |

## Troubleshooting

### Common Issues

1. **API Key Errors**: Ensure your Google Gemini API key is correctly set in `.env`
2. **Odoo Connection Issues**: Verify Odoo is running and credentials are correct
3. **File Processing Errors**: Ensure PDF files are not corrupted and properly formatted
4. **Docker Issues**: Check if ports 8069 (Odoo) and 5432 (PostgreSQL) are available

### Logs and Debugging

- Set `verbose=True` in `main.py` for detailed agent logs
- Check Docker logs: `docker-compose logs -f`
- Review Odoo logs in the web interface
