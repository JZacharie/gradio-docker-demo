FROM python:3.9

ARG GRADIO_SERVER_PORT=7860
ENV GRADIO_SERVER_PORT=${GRADIO_SERVER_PORT}

WORKDIR /workspace
ADD requirements.txt /workspace/
RUN pip install -r /workspace/requirements.txt

EXPOSE 7860
ADD main.py /workspace/

CMD ["python3", "/workspace/main.py"]