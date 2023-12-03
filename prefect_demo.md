# Prefect: A tool for tasks orchestration

## Motivation:
Please see [orchestration](orchestration.md) to know more about the reason of using such tool.

## Installation
If you are using poetry, then execute :
```bash
poetry add prefect
```
If not, you can simply install it buy executing:

```bash
pip install prefect
```
## Build a pipeline using prefect
### Prepare the list of functions, create tasks and create the flow (pipeline or diagram)
First of all, we need to implement our desired python functions to be used in the workflow.
For that, we are going to use the following list of functions, but we are going to add a decorator 
```@task``` just before the definition of each function as described below:



```python
import pandas as pd
from prefect import task, flow

@task
def load_data(path: str) -> pd.DataFrame:
    """This function tries to load the data from different data sources"""
    ...


@task
def fill_missing_values(data: pd.DataFrame) -> pd.DataFrame:
    """This function tries to fill missing values"""
    ...


@task
def encode_categorical_columns(data: pd.DataFrame) -> pd.DataFrame:
    """Task for encoding the categorical columns in the dataset."""
    ...


@task
def create_features(data: pd.DataFrame) -> pd.DataFrame:
    """This function tries to create new features"""
    ...


@flow(log_prints=True, name="prefect-demo-example")
def data_preparation_flow(path: str= 'path-to-data') -> pd.DataFrame:
    print("Hi from Prefect! 🤗")
    data = load_data(path=path)
    data = fill_missing_values(data=data)
    data = encode_categorical_columns(data=data)
    data = create_features(data=data)
    return data
```

**Note**:

`Prefect` automatically manages the orders of execution among tasks so that the workflow is optimized. 

Create a prefect cloud account: https://www.prefect.io/guide/blog/introducing-prefect-cloud-2-0/

### Deployment
### Configure storage and infra structure

```python
from prefect.filesystems import LocalFileSystem
from prefect.infrastructure import Process

my_storage_block = LocalFileSystem(
    basepath="~/prefect_local_storage"
)


# specify where the code will liveand where to pull our code from: it could be s3, GCS, ...
my_storage_block.save(name="demo-prefect-block",
                      overwrite=True)

# specify infra structure block means where we want to our code to run when our deployment executes:
# it could service less infra structure block, cloud job run block
my_process_infra = Process(working_dir="~/work")
my_process_infra.save(
    name="process-infra",
    overwrite=True
)
```
We get the slug name using the following command line:
```bash
prefect block ls
```


#### Build
assume we have a file called ```prefect_testing.py``` having the flow function ```data_preparation_flow``` that we want to run.

First thing is the name of the deployment.

**Entry point**: where the flow file is and what the name of the function is.
*sb*: stands for storage block
*ib*: stands for infra structure block

```bash
prefect deployment build -n name-of-the-deployment -sb local-file-system/demo-prefect-block -ib process/process-infra prefect_testing.py:data_preparation_flow
```
After executing that command, a yaml file ```data_preparation_flow-deployment.yaml``` is created having the initial configuration.
#### Apply
```bash
prefect deployment apply data_preparation_flow-deployment.yaml
```
#### Agent :Work queue

```bash
prefect agent start --work-queue "default"
```




