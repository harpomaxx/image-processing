FROM tensorflow/tensorflow:latest

WORKDIR /convnet

# Install dependencies
RUN /bin/bash -c 'pip install Pillow'

RUN /bin/bash -c 'pip install --user numpy scipy matplotlib ipython jupyter pandas sympy nose'

COPY . .

# Execute image sorting script
RUN /bin/bash -c 'python /convnet/sortImages.py'

ENTRYPOINT [ "python", "/convnet/convnet.py"]