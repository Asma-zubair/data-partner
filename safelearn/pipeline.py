import joblib


class Autopipeline:
    def save(self, model, scaler, path):
        data = {
            "model": model,
            "scaler": scaler,
        }
        joblib.dump(data, path)

    def load(self, path):
        return joblib.load(path)

        