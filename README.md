**Causal-PHYRE** aspires to be a benchmark for causal physical reasoning. Each of the 2-D physics puzzle has three variables *cause*, *confounder* and *effect*. 

In our examples, the *effect* is manifested by the physical contact of two bodies for more than 3 seconds. The *cause* and *confounder* are pre-defined for each particular task. In the current examples, they can be one of the following :-

| Task ID     | Cause         | Confounder |
| ------------- |:-------------:| -----:|
| 31 | Position | Color |
| 32 | Position | Color |
| 33 | Position | Color |
| 34 | Position | Color |
| 35 | Position | Color |
| 36 | Position | Color |
| 37 | Position | Color |
| 38 | Size | Color |
| 39 | Angle | Color |
| 40 | Angle | Color |
| 41 | Angle | Color |
| 42 | Size| Color |
| 43 | Angle | Color |
| 44 | Angle | Color |
| 45 | Position | Shape |
| 46 | Position | Shape |
| 47 | Position | Shape |
| 48 | Angle | Color |
| 49 | Position | Shape |
| 50 | Angle | Color |
| 51 | Position | Shape |

A model trained on Causal-PHYRE benchmark is expected to learn the correlation between the co-variates, which in the above case include both the original cause and confounder. A model that understands the cause is bound to make decisions only using the cause and ignore the confounder.

### Important Files

- `src/python/phyre/creator/constants.py` - 
	- To introduce a new object category such as triangle
	- To change color of causal objects
- `src/python/phyre/creator/shapes.py` - 
	-  To define the arguments associated with new object category such as triangle
- `src/python/phyre/creator/creator.py` -
	- *over* argument recolors the object depending on the causal structure
- `data/task_scripts/main/task000*` -
	- Task scripts corresponding to each task
	- Every task contains a confounder and cause 


To generate the tasks using the scripts

`python generate_tasks.py data/task_scripts/main/ data/generated_tasks/  --with-eval-stats --save-single-pickle`

To activate the server

`python -m phyre.server`

To view the existing tasks

`http://localhost:30303`


### Installation 

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