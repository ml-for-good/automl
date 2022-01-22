FROM tensorflow:2.8.0
RUN pip install Flask tflite-model-maker
CMD python main.py