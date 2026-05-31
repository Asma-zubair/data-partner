import joblib
class Autopipeline:
    def __init__(self):
        self.model = None
        self.scaler = None
        
    def save(self, model, scaler, path):
        data = {
            "model": model,
            "scaler": scaler,
        }
        joblib.dump(data, path)

        print("Model is saved")

    def load(self,path):
        data = joblib.load(path)
        print("Model is Loaded")
        return data
     