FROM python:3.10-slim@sha256:5ddc6ea17ec33701f8d5a6777a7b9953b7786eddeafb28b0d4e84011ebe6976b

WORKDIR /usr/app

COPY . .

RUN pip install -r requirements.txt

CMD [ "python3", "pokemon-stat-calculator.py" ]
