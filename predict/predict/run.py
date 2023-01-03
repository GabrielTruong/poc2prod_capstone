import json
import argparse
import os
import time
from collections import OrderedDict

import tensorflow as tf
from tensorflow.keras.models import load_model
from numpy import argsort

from preprocessing.preprocessing.embeddings import embed

import logging

logger = logging.getLogger(__name__)


class TextPredictionModel:
    def __init__(self, model, params, labels_to_index):
        self.model = model
        self.params = params
        self.labels_to_index = labels_to_index
        self.labels_index_inv = {ind: lab for lab, ind in self.labels_to_index.items()}

    @classmethod
    def from_artefacts(cls, artefacts_path: str):
        """
            from training artefacts, returns a TextPredictionModel object
            :param artefacts_path: path to training artefacts
        """

        # load model
        print("path",artefacts_path)
        model = load_model(f"train/data/artefacts/{artefacts_path}/model.h5")

        # load params
        param_file = open(f"train/data/artefacts/{artefacts_path}/params.json")
        params = json.load(param_file)
        #params = json.loads(f"train/data/artefacts/{artefacts_path}/params.json")

        # load labels_to_index
        index_file = open(f"train/data/artefacts/{artefacts_path}/labels_index.json")
        labels_to_index = json.load(index_file)
        #labels_to_index = json.loads(f"train/data/artefacts/{artefacts_path}/labels_index.json")

        return cls(model, params, labels_to_index)

    def predict(self, text_list, top_k=1):
        """
            predict top_k tags for a list of texts
            :param text_list: list of text (questions from stackoverflow)
            :param top_k: number of top tags to predict
        """
        tic = time.time()


        logger.info(f"Predicting text_list=`{text_list}`")

        # embed text_list
        embeddings = embed(text_list)
        print(embeddings.shape)

        # predict tags indexes from embeddings
        tag_pred = self.model.predict(embeddings)
        print("tag pred: ",tag_pred)
        # from tags indexes compute top_k tags for each text
        tags_indexes = argsort(tag_pred)
        print("tags index here: ",tags_indexes)
        print("labels_index: ",self.labels_to_index)
            
        predictions = [self.labels_to_index[str(index[-top_k])] for index in tags_indexes]
        print(predictions)

        logger.info("Prediction done in {:2f}s".format(time.time() - tic))

        return predictions


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("artefacts_path", help="path to trained model artefacts")
    parser.add_argument("text", type=str, default=None, help="text to predict")
    args = parser.parse_args()

    logging.basicConfig(format="%(name)s - %(levelname)s - %(message)s", level=logging.INFO)

    model = TextPredictionModel.from_artefacts(args.artefacts_path)

    if args.text is None:
        while True:
            txt = input("Type the text you would like to tag: ")
            predictions = model.predict([txt])
            print(predictions)
    else:
        print(f'Predictions for `{args.text}`')
        print(model.predict([args.text]))
