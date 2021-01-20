FROM python
COPY . app/
WORKDIR /app
RUN pip install -r requirements.txt
RUN pip install .
ENV PYTHONPATH /app