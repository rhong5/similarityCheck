FROM python
MAINTAINER raymondhong 'raym.hong@gmail.com'
WORKDIR /Fetch_Rewards
COPY  /flask_docker .
RUN pip install -r requirements.txt
ENTRYPOINT python webapp.py
