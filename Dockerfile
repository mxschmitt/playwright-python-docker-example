FROM mcr.microsoft.com/playwright:v1.25.0-focal

# Installing pip3
RUN apt-get update && apt-get install -y \
    software-properties-common
RUN add-apt-repository universe
RUN apt-get update && apt-get install -y \
    python3-pip
# RUN apt install xvfb -y

# Set user as root because of playwright
USER root

# Setting working directory
WORKDIR /automation

# Copying project into dockerfile
COPY test_requirements.txt ./
COPY conftest.py ./
COPY tests ./

# Installing dependencies for the project
RUN pip3 install -r test_requirements.txt

# Installing browsers with deps
RUN playwright install --with-deps

# Running pytest tests
CMD ["pytest"]
# CMD [ "xvfb-run", "--auto-servernum", "--server-num=1", "pytest"]