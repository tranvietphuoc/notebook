## Notebooks
#### Aming to practice `Python` and `Rust`
* Here I use `docker` to associate with `jupyter`
* The `Dockerfile`'s build from [here](https://github.com/tranvietphuoc/images/tree/master/jupyter)
* You must clone all files into specific local folder name `jupyter`
* Then run `cd jupyter && docker build -t <Image-Name> .`
* After building completed, then run `docker run --network="bridge" -it --rm -p 8888:8888 -e JUPYTER_ENABLE_LAB=yes -v $(pwd):/home/phuoc/work <Image-Name>:latest`
* Notice that `<Image-Name>` must be change
