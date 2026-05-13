class DataValidator:
    def validate(self,data):
        if not isinstance(data,dict):
            raise ValueError("Data should be a dictionary")
        print("Data is valid")