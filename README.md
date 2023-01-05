# From POC to Production

## Introduction

This repository stores my first work on building a ML model and deploying into a production environment.

The goal consists on building a model that predict a stackoverflow tag based on an input text. The model is divided in 3 parts:
  
  - *Preprocessing* : Package with useful functions used by the model for both training and prediction. We herited the Sequence Class from **`Keras`**.
  - *Train* : Train the deep learning model.
  - *Predict* Load the trained model then predict the input text.

After building the model, we create a **`flask`** application so that we can send the input text via a HTTP request.

Then we want to dockerize our application so that it can be deployed on any machine. 

## Getting started

First you need to clone the repository:
```bash
git clone https://github.com/GabrielTruong/poc2prod_capstone.git
```

Then you need to create a python conda environment: 

```bash
conda create -n ENVNAME --file environment.yml
```

Deploy the app locally without docker:
```bash
python predict/predict/app.py
```

The application will run at the following adress: http://127.0.0.1:5000/

## Use the app
**1. Using the form**

Use the link http://127.0.0.1:5000/ and use the form to predict the input text.

**2. Using a curl request**

You can use a HTTP request by sending the input text via the parameter string `text` as shown below:
```curl
curl http://127.0.0.1:5000/predict?text=<INPUT TEXT>
```

## Useful command

### Running tests
**1. Test on predict**
```bash
python -m unittest predict.tests.test_predict
```

**2. Test on train**
```bash
python -m unittest train.tests.test_model_train
```

**3. Test on preprocessing**
```bash
python -m unittest preprocessing.tests.test_utils
```

**Problem with module error**

add python files to python path
```bash
export PYTHONPATH=$PYTHONPATH:/home/dev/python-files

export PYTHONPATH=$PYTHONPATH:/home/lapbeer/Documents/epf/5A/poc2prod/poc2prod_capstone
```

**Train model**
```
python train/train/run.py "train/data/training-data/stackoverflow_posts.csv" train/conf/train-conf.yml "train/data/artefacts/train/"
```

**CHECK SETUPTOOLS**

RESTE à FAIRE:
- Revoir les path pour l'artefact
- Revoir le fichier predict car bancal
- Faire fonctionner l'app flask avec curl et UI
- Dockeriser l'app
- Airflow