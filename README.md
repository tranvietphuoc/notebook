# Notebooks
### Aming to practice `Python` and `Rust`
* Here I use `docker` to associate with `jupyter`.
* The `Dockerfile`'s built from [here](https://github.com/tvph/images/tree/master/jupyter).
* You must clone all files into your local machine:
```
git clone https://github.com/tranvietphuoc/images.git
```
* Then run:
```
cd ./images/jupyter/ && docker image build -t <Image-Name> .
```
* After building completed, then run:
```
docker run -it --rm -p 8888:8888 -e JUPYTER_ENABLE_LAB=yes -v $(pwd):/home/phuoc/work <Image-Name>:latest
```
* Notice that `<Image-Name>` must be change. And use `-v $(pwd):/home/phuoc/work` to associate the image with local folder.
* Base on [Jupyter Docker Stacks](https://jupyter-docker-stacks.readthedocs.io/en/latest/)...
* Or you can use `docker pull phuoctv/jupyter:latest` to pull the image. Then run the command above.
* If unable to use `docker run...` then change the `<Image-Name>:latest` to image id of the command `docker images`
