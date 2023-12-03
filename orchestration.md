# Tasks orchestration

One of the most important workflow that needs orchestration is the data preparation for the ML model.
The importance of using a tool for tasks orchestration is very important to save time and to handle 
errors while executing a series of tasks in a row.

Example:

Assume that we need to prepare the data from different data sources to feed an ML model. 
For that, we will need to implement few python functions that did the job.

```python
import pandas as pd


def load_data(path: str) -> pd.DataFrame:
    """This function tries to load the data from different data sources"""
    ...


def fill_missing_values(data: pd.DataFrame) -> pd.DataFrame:
    """This function tries to fill missing values"""
    ...


def encode_categorical_columns(data: pd.DataFrame) -> pd.DataFrame:
    """Task for encoding the categorical columns in the dataset."""
    ...


def create_features(data: pd.DataFrame) -> pd.DataFrame:
    """This function tries to create new features"""
    ...
```

If we are not using a tool for tasks orchestration, the normal way is to execute the following code:
```python

data = load_data(path="path-to-data")
data = fill_missing_values(data=data)
data = encode_categorical_columns(data=data)
data = create_features(data=data) 

```
If the code is working fine from the first shot, then nothing to add here. 
But if we have an error is ```encode_categorical_columns``` we are going to lose the output of the previous functions.
Rather than that, we can execute ```encode_categorical_columns``` and ```create_features``` at the same time.
Both of them are waiting for the above functions to be executed, and they are independent while executing them.
By using an orchestration, we could save time of executing the first two functions when we have errors in the third 
or the fourth one. We can automatically optimize the workflow by adding only several lines of code? 
That is when orchestration libraries come in handy.

In the current case, the pipeline of the workflow is:

```
load_data --> fill_missing_values   --> encode_categorical_columns
                                    --> create_features
```