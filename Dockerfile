FROM python:3.7
RUN apt-get update
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN dpkg -i google-chrome-stable_current_amd64.deb; apt-get -fy install
COPY requirements.txt requirements.txt
RUN pip install -r ./requirements.txt
ENV APP_HOME /app
ENV PORT 5000
WORKDIR ${APP_HOME}
COPY . .
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]