FROM python:3.10-slim-bullseye


WORKDIR /src

COPY . . 

# --------------------------------------------------------------------
# requirements
# --------------------------------------------------------------------
RUN pip install --upgrade --user pip
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]