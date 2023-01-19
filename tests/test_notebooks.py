import papermill as pm
import pytest


@pytest.fixture()
def common_kwargs(tmpdir):
    outputnb = tmpdir.join("output.ipynb")
    return {
        "output_path": str(outputnb),
    }

def test_errors(common_kwargs):
    pm.execute_notebook("book/errors.ipynb", **common_kwargs)