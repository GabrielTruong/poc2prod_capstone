from flask import Flask, request
from run import TextPredictionModel


app = Flask(__name__)
 
@app.route("/predict", methods=['GET'])
def get_prediction():

    model = TextPredictionModel.from_artefacts("/train/data/artefacts/test")

    text = request.args.get('text')

    predictions = model.predict(text,top_k=1)
 
    return predictions
 
if __name__ == '__main__':
    app.run()