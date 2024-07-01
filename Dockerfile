FROM python:3.10.14-alpine3.20

WORKDIR backend/

COPY alembic.ini .
COPY requirements.txt .
COPY src/ src/

RUN \
 apk add --no-cache postgresql-libs && \
 apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
 python3 -m pip install -r requirements.txt --no-cache-dir && \
 apk --purge del .build-deps

CMD [ "python3", "-m", "uvicorn", "src.app:app" ]
