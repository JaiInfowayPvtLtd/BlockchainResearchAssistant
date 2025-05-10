# Contributing to Blockchain Research Assistant

Thank you for considering contributing to the Blockchain Research Assistant! This document provides guidelines and instructions for contributing to this project.

## Code of Conduct

By participating in this project, you agree to abide by our Code of Conduct. Please be respectful and considerate of others.

## How Can I Contribute?

### Reporting Bugs

If you encounter a bug, please create an issue with the following information:

- A clear, descriptive title
- Steps to reproduce the issue
- Expected behavior
- Actual behavior
- Screenshots (if applicable)
- Environment information (OS, browser, Python version)

### Suggesting Features

We welcome feature suggestions! To suggest a feature:

- Create an issue with a clear, descriptive title
- Provide a detailed description of the proposed feature
- Explain why this feature would be valuable to users
- Include any relevant examples or mockups

### Pull Requests

We welcome pull requests for bug fixes, features, or documentation improvements. To submit a pull request:

1. Fork the repository
2. Create a new branch from `main`
3. Make your changes
4. Write or update tests if necessary
5. Update documentation if necessary
6. Submit a pull request to the `main` branch

## Development Setup

1. Clone your fork of the repository
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up your API keys as environment variables:
   ```bash
   export OPENAI_API_KEY="your_openai_api_key"
   export FIRECRAWL_API_KEY="your_firecrawl_api_key"
   ```
4. Start the application:
   ```bash
   streamlit run app.py
   ```

## Code Style

Please follow these style guidelines:

- Use consistent indentation (4 spaces)
- Follow PEP 8 style guidelines
- Write clear, descriptive comments
- Use descriptive variable and function names
- Add docstrings to functions and classes

## Testing

- Write tests for new features
- Ensure all tests pass before submitting a pull request
- Run the tests with:
  ```bash
  pytest
  ```

## Documentation

- Update documentation for any changed functionality
- Document new features thoroughly
- Keep the README.md up to date

## Git Workflow

1. Create an issue describing the change you want to make
2. Fork the repository and create a branch from `main`
3. Make your changes with clear, descriptive commit messages
4. Push your branch to your fork
5. Submit a pull request to the `main` branch

## Review Process

- All pull requests will be reviewed by a maintainer
- Feedback may be provided for requested changes
- Once approved, the pull request will be merged

## License

By contributing to this project, you agree that your contributions will be licensed under the project's [MIT License](LICENSE).

Thank you for your interest in improving the Blockchain Research Assistant!