import os
import papermill as pm
import pytest

exclude = ["notebooks.ipynb", "hypothesisTesting.ipynb"]

notebooks = []
for file in os.listdir("book"):
    if file.endswith('.ipynb') and file not in exclude:
        notebooks.append(os.path.join("book", file))

@pytest.fixture()
def common_kwargs(tmpdir):
    outputnb = tmpdir.join("output.ipynb")
    return {
        "output_path": str(outputnb),
    }

@pytest.mark.parametrize("notebook", notebooks)
def test_notebook(notebook, common_kwargs):
    pm.execute_notebook(notebook, **common_kwargs)