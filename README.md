# Background_Removal

You can directly use the notebook or this Docker container. 
Note that the resizing has been done due to RAM restrictions, if you have a RAM size of more than 8 GB you can remove the resize part.

This Docker container provides background removal based on Carvekit toolkit.

Usage
To use this container, you'll need to have Docker installed on your system. Then, follow these steps:

To build the docker image:
sudo docker build -t <image_name> .

To create a container from the image:
(This will run the docker container in port 9091, you can use any other free port)
sudo docker run -v /home:/home --name <container_name> -p 9091:7860 -it -d <image_name>

Get the list of containers:
sudo docker ps

To start the container:
sudo docker exec -it <container_name> /bin/bash

After starting the container, background_removal will start automatically in the background.
You can acces it from the following url:
http://<ip_address>:9091/

Once you start the container you reach inside the directory app
Then run the command:
python3 background_removal_gradio.py

This will produce a shreable link by which you can use gradio on any device.
