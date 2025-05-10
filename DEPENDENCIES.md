# Project Dependencies

The Blockchain Research Assistant relies on the following Python packages:

## Core Dependencies

- **streamlit**: Web application framework for the user interface
  - Version: >=1.32.0
  - Purpose: Provides the interactive web interface

- **openai**: Official OpenAI API client
  - Version: >=1.12.0
  - Purpose: Interacts with OpenAI's GPT models for research analysis and elaboration

- **requests**: HTTP library
  - Version: >=2.31.0
  - Purpose: Makes API calls to the Firecrawl service

- **python-dotenv** (optional): Environment variable management
  - Version: >=1.0.0
  - Purpose: Helps manage environment variables for API keys

## Installation

These dependencies are installed via pip:

```bash
pip install streamlit openai requests python-dotenv
```

Or by using the packager tool in the Replit environment.

## Python Version

The application is designed to work with Python 3.8 or newer.

## External API Dependencies

The application also depends on these external services:

- **OpenAI API**: Provides the AI models for research analysis
  - Authentication: API key
  - Documentation: https://platform.openai.com/docs/

- **Firecrawl API**: Provides web crawling for blockchain research
  - Authentication: API key
  - Documentation: https://firecrawl.dev/docs/