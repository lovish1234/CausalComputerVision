# Installation 

The recommended way to install and compile Causal-PHYRE from source is by using a [Conda](https://docs.conda.io/en/latest/) package manager.

 ```(bash)
git clone https://github.com/facebookresearch/phyre.git
cd phyre
conda env create -f env.yml
source activate phyre
pip install -e src/python
```

  To check that the installation was successful, run `python -m phyre.server` and open http://localhost:30303. That should start a local demo server.

```