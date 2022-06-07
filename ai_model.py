import pickle


def save_model(model):
    with open("models/model.pickle", "wb") as f:
        pickle.dump(model, f)


def load_model():
    with open("models/model.pickle", "rb") as f:
        return pickle.load(f)