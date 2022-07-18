FROM tensorflow/tensorflow:2.8.0-gpu
RUN rm /etc/apt/sources.list.d/cuda.list
RUN rm /etc/apt/sources.list.d/nvidia-ml.list
RUN apt-get update && apt-get install git -y
RUN cd / && git clone https://github.com/ml-for-good/automl.git
RUN pip install -r /automl/lib/requirements.txt