from safelearn import Autopipeline
from safelearn import DataValidator
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
model=LinearRegression()
scaler=StandardScaler()
pipe=Autopipeline()
validator=DataValidator()
sample_data={"model": model, "scaler": scaler}
validator.validate(sample_data)
pipe.save(model=model,
          scaler=scaler, 
          path="model.pkl")

data=pipe.load(path="model.pkl")
print(data)