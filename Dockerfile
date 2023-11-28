# OPTIMIZED SOLUTION

# tensorflow base-images are optimized: lighter than python-buster + pip install tensorflow
FROM tensorflow/tensorflow:2.10.0

WORKDIR /prod

# We strip the requirements from useless packages for user
COPY requirements_prod.txt requirements.txt
RUN pip install -r requirements.txt

COPY taxifare taxifare
COPY setup.py setup.py
RUN pip install .

COPY Makefile Makefile
RUN make reset_local_files

CMD uvicorn taxifare.api.fast:app --host 0.0.0.0 --port $PORT
