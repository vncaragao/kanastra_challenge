FROM python:3.11

RUN mkdir -p /usr/src/frontend
WORKDIR /usr/src/backend

COPY ./backend/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./backend .

CMD [ "python", "-u", "run.py" ]