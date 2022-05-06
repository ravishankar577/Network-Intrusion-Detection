import pandas as pd
import numpy as np
import pickle

try:
    model = pickle.load(open("balanced_random_forest_model_final.pkl", "rb"))
    file = open("enc.obj",'rb')
    enc_loaded = pickle.load(file)
    file.close()
    inputs = pd.read_csv("predict.csv") #provide path of csv file with input values here
    inputs_encoded = enc_loaded.transform(inputs)
    prediction = model.predict(inputs_encoded.iloc[:,:])
    if prediction[0] == 1:
        output = "Attack"
    elif prediction[0] == 0:
        output = "Normal Connection"
    print(output)
except:
    output = "An error occured"
    print(output)

