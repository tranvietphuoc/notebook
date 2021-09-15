## Notebooks
#### Aming to practice `Python` and `Rust`
* Here I use `docker` to associate with `jupyter`.
* The `Dockerfile`'s built from [here](https://github.com/tranvietphuoc/images/tree/master/jupyter).
* You must clone all files into your local machine:
```
git clone https://github.com/tranvietphuoc/images.git
```
* Then run:
```
cd ./images/jupyter/ && docker build -t <Image-Name> .
```
* After building completed, then run:
```
docker run -it --rm -p 8888:8888 -e JUPYTER_ENABLE_LAB=yes -v $(pwd):/home/phuoc/work <Image-Name>:latest
```
* Notice that `<Image-Name>` must be change. And use `-v $(pwd):/home/phuoc/work` to associate the image with local folder.
