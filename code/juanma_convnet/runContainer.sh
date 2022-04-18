sudo docker stop coffetf
sudo docker rm coffetf
sudo docker run -v "$PWD/graphs:/convnet/graphs" -it --name coffetf coffetf

