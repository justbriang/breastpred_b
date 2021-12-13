import joblib

def loadModel():
    return joblib.load('static/model/PredModel')

def makepred(model,val):
   return model.predict(val)