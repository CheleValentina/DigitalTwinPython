import pickle

from config import settings


def save_model(model):
    with open(settings.MODEL_FILENAME, "wb") as f:
        pickle.dump(model, f)


def load_model():
    with open(settings.MODEL_FILENAME, "rb") as f:
        return pickle.load(f)
