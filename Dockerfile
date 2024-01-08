FROM python:latest
COPY . /task1
WORKDIR /task1
RUN pip install -r requirements.txt 
EXPOSE 8080
ENTRYPOINT [ "python" ] 
CMD [ "demo.py" ] 