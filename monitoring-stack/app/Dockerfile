FROM python:3.9-slim
RUN pip install Flask prometheus-flask-exporter prometheus-client
WORKDIR /workspace
COPY app.py .
EXPOSE 5000
CMD ["python", "app.py"]
