FROM python:3.10-slim-bullseye


WORKDIR /src

COPY . . 

# --------------------------------------------------------------------
# requirements
# --------------------------------------------------------------------
RUN pip install --upgrade --user pip
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8501

CMD ["streamlit", "run", "app.py"]