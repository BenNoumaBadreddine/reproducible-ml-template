import pytest
import sys


@pytest.fixture
def capture_stdout(monkeypatch):
    buffer = {"stdout": "", "write_calls": 0}

    def fake_write(s):
        buffer["stdout"] += s
        buffer["write_calls"] += 1

    monkeypatch.setattr(sys.stdout, "write", fake_write)
    return buffer


# if we fix the scope of the fixture decorator to be session, that means that the result of this
# function will be cached during the execution of all tests.
@pytest.fixture(scope="session")
def db_conn():
    # from src.src.databases_util.configs.database_configs import MLFLOW_DB_CONFIG
    # from dbconnections.databases_connection import get_db_connection
    # MLFLOW_DB_CONNECTION = get_db_connection(MLFLOW_DB_CONFIG)

    db = ...
    url = ...
    with db.connect(
        url
    ) as conn:  # connection will be torn down after all tests finish
        yield conn
