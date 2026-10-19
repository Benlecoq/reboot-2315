from fastapi import FastAPI
import pickle

# FastAPI instance
app = FastAPI()

# Root endpoint
@app.get("/")
def root():
    return {'greeting':"hello"}

# Root endpoint
@app.get("/predict")
def predict(x1, x2, x3, x4):

    # load model
    with open('models/model.pkl', 'rb') as file:
        best_model = pickle.load(file)

    prediction = best_model.predict([[float(x1), float(x2), float(x3), float(x4)]])

    return {'prediction': float(prediction)}
