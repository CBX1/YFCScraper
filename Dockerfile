FROM python:3.7

RUN apt-get update

#download and install chrome
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN dpkg -i google-chrome-stable_current_amd64.deb; apt-get -fy install

#install python dependencies
COPY requirements.txt requirements.txt
RUN pip install -r ./requirements.txt

#some envs
ENV APP_HOME /app
ENV PORT 5000

#set workspace
WORKDIR ${APP_HOME}

#copy local files
COPY . .

CMD exec gunicorn --bind :${PORT} --workers 1 --threads 8 app:app