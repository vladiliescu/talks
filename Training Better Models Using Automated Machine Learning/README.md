Here's what you need in order to run this notebook:

* Clone this repository somewhere nice
* Create a [Kaggle](https://www.kaggle.com) account, join the [Titanic competition](https://www.kaggle.com/c/titanic/overview) competition, download its data files to the [data](./data) folder
* Make sure you have an [Azure](https://azure.microsoft.com/en-us/) account, in it create a resource group and a [Machine Learning Service Workspace](https://docs.microsoft.com/en-us/azure/machine-learning/) - you'll need those for running the automated machine learning experiment
* Download `config.json` from your Azure ML Workspace to this folder.
* Install either [Miniconda](https://conda.io/en/latest/miniconda.html) or [Anaconda](https://www.anaconda.com/downloads). The Python 3.7 version 🐍
* Run the following commands inside this directory

```shell
conda env create -f env.yml -n automl_on_titanic
conda activate automl_on_titanic
ipython kernel install --user --name=automl_on_titanic

jupyter notebook
```
* If everything runs fine and at the end you can open the `auto-ml-and-kaggle.ipynb` notebook then you're good to go.
* After you're finished, you can run `conda remove --name automl_on_titanic --all` to remove the environment you had created.