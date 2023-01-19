import os
import papermill as pm
import pytest

notebooks = []
for file in os.listdir("book"):
    if file.endswith('.ipynb') and file not in ["notebooks.ipynb", "hypothesisTesting.ipynb"]:
        notebooks.append(os.path.join("book", file))
for file in os.listdir("book/interactive-nbs"):
    if file.endswith('.ipynb'):
        notebooks.append(os.path.join("book/interactive-nbs", file))

@pytest.fixture()
def common_kwargs(tmpdir):
    outputnb = tmpdir.join("output.ipynb")
    return {
        "output_path": str(outputnb),
    }

@pytest.mark.parametrize("notebook", notebooks)
def test_notebook(notebook, common_kwargs):
    pm.execute_notebook(notebook, **common_kwargs)