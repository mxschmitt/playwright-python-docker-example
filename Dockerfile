FROM mcr.microsoft.com/playwright/python:v1.25.0-focal

# Setting working directory
WORKDIR /automation

# Copying project into dockerfile
COPY test_requirements.txt ./
COPY conftest.py ./
COPY tests ./

# Installing dependencies for the project
RUN pip install -r test_requirements.txt

# Running pytest tests
CMD [ "xvfb-run", "--auto-servernum", "pytest"]