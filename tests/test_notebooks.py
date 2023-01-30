# https://github.com/matthewfeickert/Statistics-Notes/blob/main/tests/test_notebooks.py
import papermill as pm
import pytest

@pytest.fixture()
def common_kwargs(tmpdir):
    outputnb = tmpdir.join("output.ipynb")
    return {
        "output_path": str(outputnb),
    }

def test_probability(common_kwargs):
    pm.execute_notebook("book/probability.ipynb", **common_kwargs)