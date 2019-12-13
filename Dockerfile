FROM python:3.7

WORKDIR /usr/src/todo-list

#being able to use cache (speed up docker build)
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PYTHONPATH "${PYTHONPATH}:/usr/src/todo-list"
CMD ["python", "./entry.py"]
