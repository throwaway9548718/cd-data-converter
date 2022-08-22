FROM python:3.8

COPY . /Setup
WORKDIR /Setup
RUN make clean
RUN make setup

ADD https://www.w3schools.com/xml/cd_catalog.xml /Demo/cd_catalog.xml
WORKDIR /Demo

RUN echo "source /Setup/venv/bin/activate" >> ~/.bashrc
ENTRYPOINT ["bash"]