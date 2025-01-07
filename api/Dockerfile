 FROM python:3.10-alpine
 WORKDIR /opt/app
 COPY Pipfile Pipfile.lock .
 RUN pip install pipenv && PIPENV_VENV_IN_PROJECT=1 pipenv install
 COPY . .
 EXPOSE 8000
 ENV REPORANGER_API_ENV=production
 ENV REPORANGER_API_DEBUG=0
 ENV REPORANGER_API_TESTING=0
 #ENV REPORANGER_API_SECRET_KEY=secretkey 
 ENV REPORANGER_API_DATABASE_URI=None 
 ENV REPORANGER_API_TIMEZONE=Asia/Tehran
 RUN addgroup app && adduser -h /dev/null -g app -s /bin/sh -G app -DH app
 USER 1000

 CMD ["pipenv", "shell"]
 CMD ["pipenv","run","gunicorn"]
