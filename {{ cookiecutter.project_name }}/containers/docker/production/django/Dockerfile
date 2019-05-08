# Pull base image
FROM python:3.6

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /code

# Set work directory
WORKDIR /code

# Copy the project
COPY ./{{ cookiecutter.project_slug }}/ /code/

# Install the package requirements
RUN pip install --upgrade pip && pip install -r requirements.txt

# expose the port 8000
EXPOSE 8000

# define the default command to run when starting the container
CMD ["gunicorn", "--chdir ", "/code/{{ cookiecutter.project_slug }}", "--bind", ":8000", "{{ cookiecutter.project_slug }}.wsgi:application"]
