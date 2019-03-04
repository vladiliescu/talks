## About

> A tale as old as time: boy meets girl, girl asks boy to train a predictive model, boy succeeds. But when she discovers that he cannot operationalize said model, he is forced to go through a perilous journey into the strange and unfamiliar world of Azure Machine Learning deployment options. He learns to face his fears and evaluate the advantages and disadvantages of Azure Machine Learning Studio and Azure Machine Learning services, all the while hoping to redeem himself in the process.
 
> Will he succeed? Will he manage to find an option that allows him to deploy a trained model as a web service, scale it, and consume it easily? Let’s find out!

These are the resources used for my [Boy meets Girl](https://vladiliescu.net/talks/boy-meets-girl/) talk.

* [BmG.ipynb](BmG.ipynb) - the [Jupyter](http://jupyter.org) notebook used to train and serialize the model
* [iris.data.csv](./data/iris.data.csv) - the Iris data set, downloaded from [here](https://archive.ics.uci.edu/ml/datasets/iris)
* The [Azure ML Studio](https://studio.azureml.net) experiment used to load the pickled model is available on the [Azure AI Gallery](https://gallery.azure.ai/Experiment/Custom-Python-model-integration-using-the-Iris-dataset)
* [conda_dependencies.yml](conda_dependencies.yml) - the [Conda](http://conda.io) configuration file needed to create the Docker image in ML Service
* [score.py](score.py) - the interface for our model running on the Docker image
* [input.json](input.json) - input sample using the standard structure for Azure ML Studio; can also be used to invoke the web service deployed using Azure ML Service (this is why the code in [score.py](score.py) looks the way it does 🤓)
* During the talk I've demo-ed the code using [Visual Studio Code](https://code.visualstudio.com), with the [Azure Machine Learning](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.vscode-ai) and [REST Client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client) extensions