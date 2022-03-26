#FROM jupyter/scipy-notebook
FROM registry.access.redhat.com/ubi8/python-39:latest

USER root

#RUN mkdir data
#RUN mkdir models
#RUN mkdir ./data/transform
#RUN mkdir ./models/experiment
COPY requirements.txt ./requirements.txt
COPY data data/
COPY models models/
COPY images images/
COPY notebooks notebooks/
COPY reports reports/
COPY run.py ./run.py
COPY config config
RUN chmod 777 reports
#COPY data/transform/pipeline.pkl ./data/transform/pipeline.pkl
#COPY models/experiment/xgbc_model.pkl ./models/experiment/xgbc_model.pkl
RUN pip install -r requirements.txt

COPY wsgi.py ./wsgi.py
COPY prediction.py ./prediction.py

#USER 1001
EXPOSE 8080

CMD ["python3", "wsgi.py", "8080"]
