## About

The differences between the two most popular (at the time) options of doing machine learning in the Azure cloud - Azure Machine Learning Service and Azure Machine Learning Studio (classic).

The two tools are evaluated from multiple viewpoints such as ease of use, level of knowledge needed for getting started, the options available for ingesting, analysing, and preparing data, the differences in training and evaluating predictive models, and the particularities of exposing the models as web services, and allowing them to be consumed securely from external applications. 

A video of this talks is available on [YouTube](https://youtu.be/K5W5i6rC5Hk).


## Resources
* First things first, I used the training dataset from Kaggle's Petfinder competition, available [here](https://www.kaggle.com/c/petfinder-adoption-prediction), you will need this in order to be able to run the code.
* A sample configuration file is available in [aml_config](./aml_config), all you need to do is fill in your own subscription/workspace details here.
* Code for _Round 1 - Look and Feel_ is available [here](./Round1), incuding the training script and the Jupyter notebook used for integrating with Machine Learning Service
* Code for _Round 2 - Analysing and Preparing Data_ is [here](./Round2), just a simple notebook with some very light data analysis
* Code for _Round 3 - Training and Evaluating Models_ is [here](./Round3), again just a simple training script and the corresponding Jupyter notebook
* Last but not least, the code for _Round 4 - Deploying and Consuming Models_ is [here](./Round4), where we also have the `score.py` and `conda_dependencies.yml` files needed to build the Docker image. And of course, the `input.json` file used for invoking the scoring web service (this uses the standard structure for Azure ML Studio, this is why the code in `score.py` looks the way it does)
* The Machine Learning Studio experiments are (still) available in the Azure AI Gallery: [Round 1](https://gallery.cortanaintelligence.com/Experiment/Service-versus-Studio-Round-1-Look-and-Feel), [Round 2](https://gallery.cortanaintelligence.com/Experiment/Service-versus-Studio-Round-2-Analysing-and-Preparing-Data), and [Round 3](https://gallery.cortanaintelligence.com/Experiment/Service-versus-Studio-Round-3-Training-and-Evaluating-Models). Since _Round 4_ was all about deploying the experiment as a web service, you can reuse the _Round 3_ experiment.
