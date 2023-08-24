xhost + 127.0.0.1

docker run -d -it --rm --name quantus \
--mount type=bind,source=/Users/davidspector/Home/Stanford/Project_Data,target=/Local\ Data quantus \

docker exec quantus python3 main.py

docker stop quantus