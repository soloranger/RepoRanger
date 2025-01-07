FROM python:3.10-alpine AS builder

WORKDIR /opt/app

COPY Pipfile Pipfile.lock .

RUN pip install pipenv && PIPENV_VENV_IN_PROJECT=1 pipenv install

FROM python:3.10-alpine AS starter

RUN addgroup -g 1000 app && \
  adduser -u 1000 -h /opt/app -g app -s /bin/sh -G app -DH app

RUN mkdir /opt/app && chown app:app /opt/app

USER 1000

WORKDIR /opt/app

COPY --chown=app:app --from=builder /opt/app/.venv .venv

COPY --chown=app:app . .

EXPOSE 8000

ENV REPORANGER_API_ENV=production
ENV REPORANGER_API_DEBUG=0
ENV REPORANGER_API_TESTING=0
 #ENV REPORANGER_API_SECRET_KEY=secretkey 
ENV REPORANGER_API_DATABASE_URI=None 
ENV REPORANGER_API_TIMEZONE=Asia/Tehran


ENV PATH="/opt/app/.venv/bin:$PATH"

CMD ["gunicorn"]
