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

**CHECK SETUPTOOLS**
