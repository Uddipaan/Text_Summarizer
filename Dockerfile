# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.6

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

# create root directory for our project in the container
RUN mkdir /text_summarizer

# Set the working directory to /text_summarizer
WORKDIR /text_summarizer

# Copy the current directory contents into the container at /text_summarizer
ADD . /text_summarizer/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# COPY startup script into known file location in container
# COPY start.sh /start.sh

# EXPOSE port 8000 to allow communication to/from server
# EXPOSE 8081

# CMD specifcies the command to execute to start the server running.
# CMD ["/start.sh"]