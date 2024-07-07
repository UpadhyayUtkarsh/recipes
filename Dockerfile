FROM python:3.12
EXPOSE 5000
WORKDIR /app
COPY ./requirements.txt requirements.txt
# RUN pip install --no-cache-dir --upgrade -r requirements.txt
RUN pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org --no-cache-dir --upgrade -r requirements.txt
COPY . .
CMD ["gunicorn", "--bind", "0.0.0.0:80", "app:create_app()"]