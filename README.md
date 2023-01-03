# poc2prod

This repository stores my first work on conducting a ML project to production.

## Tests

To run tests: 

**Test on predict**
```bash
python -m unittest predict.tests.test_predict
```

**Test on train**
```bash
python -m unittest train.tests.test_model_train
```

**Test on preprocessing**
```bash
python -m unittest preprocessing.tests.test_utils
```

**Problem with module error**
add python files to python path
```bash
export PYTHONPATH=$PYTHONPATH:/home/dev/python-files
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