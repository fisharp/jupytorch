# JuPyTorch :fire:

### JupyterLab based data science workspace using PyTorch with NVIDIA® CUDA® GPU support

This repository contains the Dockerfile and files required for building a Docker image of JupyterLab with "batteries included" for Deep Learning with packages and complements related to PyTorch with NVIDIA® CUDA® support, allowing use of the host's GPU(s) inside the containerized JupyterLab instance

![:fire:](images/jupytorch.svg)

## Introduction

The purpose of this project is to provide an "instant live" out-of-the-box-ready JupyterLab instance for deep learning development (and training) with PyTorch, CUDA and related packages. By simply browsing to localhost at a given port (which defaults to 8888), users can access a pre-configured JupyterLab environment with all the necessary tools and packages installed. 

## Development Status

:warning: **Note: This project is still in early development and is not yet ready for production use.**

We are actively working on this project and welcome any feedback or contributions. Please feel free to open an issue or pull request if you encounter any problems or have suggestions for improvement.

## QuickStart

The easiest way to try this docker image is just by directly pulling and running it from its dockerhub registry in "detached mode" with:

```bash
docker run -d --rm -p 8888:8888 \
    -e JUPYTER_PASSWORD=anyPassphrase \
    fisharp/jupytorch
```

and open your preferred web browser to visit your [localhost at the specified port 8888](http://localhost:8888) 


## Building the Image

To build the Docker image (after cloning this repository) simply run the following command while inside the `docker` directory:

```bash
docker build -t your-registry/jupytorch .
```

> Replace `your-registry` with the name of your Docker registry, if applicable.

## Running the Container

To run the Docker container, use the following command:

```bash
docker run -it --rm -p 8888:8888 -v $(pwd)/subdir/to/your/files:/var/data -e JUPYTER_PASSWORD='YourFailsafePassphrase' -h container_host_name --name custom_container_name your-registry/jupytorch
```

or spread it out in a multi-line command:

```bash
docker run -it --rm \
    -p 8888:8888 \
    -v $(pwd)/subdir/to/your/files:/var/data \
    -e JUPYTER_PASSWORD='YourFailsafePassphrase' \
    -h container_host_name \
    --name custom_container_name \
    your-registry/jupytorch
```

> Replacing again `your-registry` with the name of your own Docker registry, if applicable.

- The `-it` pair starts the container in interactive mode (`-i`) and attaches a pseudo-TTY (`-t`).
- The `--rm` option instruct docker to completely remove the container as soon as the Jupyter server is shutdown due to user action or in the event of a critical error.
- `--name` specifies a custom name for the container
- `-p` maps the container port (default 8888) to the host port (also 8888 in this case)
- The `JUPYTER_PASSWORD` environment variable added with that `-e` parameter, sets the JupyterLab login password to `YourFailsafePassphrase`, which should be replaced with your own password.
- `-v` mounts the local directory `subdir/to/your/files` as a volume inside the container at `/var/data`.
- `-h` sets a custom hostname of the container (internally).

Once the container is up and running, you can access the JupyterLab instance by browsing to http://localhost:8888 in your preferred web browser. You will be prompted for the password you set earlier.


## CUDA with NVIDIA® GPUs

If you have installed the proper drivers for your GPUs and the **NVIDIA container toolkit** (detailed installation instructions [here](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html#installation-guide)), you can also make use of (all of) the power of your GPUs in any Jupyter Notebook or Python file in your containerized Jupyter Lab, just by including the `--gpus all` option (as described [here](https://docs.docker.com/engine/reference/commandline/run/#gpus)) to enable the use of all GPUs in the JupyterLab environment:

```bash
docker run -it --rm \
    -p 8888:8888 \
    #...
    --gpus all
    your-registry/jupytorch
```

---

## Included Packages

This Docker image includes the following packages, among others, the following:

| Component | Package | Repository | Documentation |
| --- | --- | --- | --- |
| PyTorch | `torch` | [pytorch/pytorch](https://github.com/pytorch/pytorch) | [pytorch.org](https://pytorch.org/docs/stable/index.html) |
| Torchvision | `torchvision` | [pytorch/vision](https://github.com/pytorch/vision) | [pytorch.org/docs/stable/torchvision/](https://pytorch.org/vision/stable/index.html) |
| Torchaudio | `torchaudio` | [pytorch/audio](https://github.com/pytorch/audio) | [pytorch.org/audio/stable/index.html](https://pytorch.org/audio/stable/index.html) |
| CUDA | _torch.cuda_ (installed with `torch==2.0.0+cu117`) | [nvidia/nvidia-docker](https://github.com/nvidia/nvidia-docker) | [docs.nvidia.com/cuda/](https://docs.nvidia.com/cuda/) |
| scikit-learn | `scikit-learn` | [scikit-learn/scikit-learn](https://github.com/scikit-learn/scikit-learn) | [scikit-learn.org](https://scikit-learn.org/) |
| Pandas | `pandas` | [pandas-dev/pandas](https://github.com/pandas-dev/pandas) | [pandas.pydata.org](https://pandas.pydata.org/) |
| Matplotlib | `matplotlib` | [matplotlib/matplotlib](https://github.com/matplotlib/matplotlib) | [matplotlib.org](https://matplotlib.org/stable/api/index) |
| NumPy | `numpy` | [numpy/numpy](https://github.com/numpy/numpy) | [numpy.org](https://numpy.org/) |
| SymPy | `sympy` | [sympy/sympy](https://github.com/sympy/sympy) | [docs.sympy.org](https://docs.sympy.org/latest/index.html) |

Also [a few JupyterLab extensions](Docker/packages/server-extensions/requirements.txt) (including code linters, formatters and themes)

## References

- [JupyterLab](https://jupyterlab.readthedocs.io/en/stable/)
- [Jupyter Server](https://jupyter-server.readthedocs.io/en/stable/)
- [Jupyter Docker Stacks](https://github.com/jupyter/docker-stacks): The official Docker images from the JupyterLab team
- [PyTorch Docker image](https://github.com/pytorch/pytorch#docker-image)
- [CUDA @ DockerHub](https://hub.docker.com/r/nvidia/cuda) Base Docker images with CUDA

## Similar Projects

There are some other interesting projects, similar to this one (and for sure in a more mature state) that you may find compelling to browse and try. For instance (just to mention a few that are all worth exploring):

- [Tverous/Pytorch-Notebook](https://github.com/Tverous/pytorch-notebook): Jupyter Notebook with Pytorch
- [stepankuzmin/pytorch-notebook](https://github.com/stepankuzmin/pytorch-notebook) (*Outdated*) Jupyter Notebook Pytorch Stack
- [yhavinga/jupyter-tensorflow-pytorch-gpu](https://github.com/yhavinga/jupyter-tensorflow-pytorch-gpu): (*Outdated*) Jupyter Notebook with TensorFlow, Pytorch and CUDA GPU support


## License

This project is licensed under the [MIT license](LICENSE).