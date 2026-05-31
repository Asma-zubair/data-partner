from safelearn import Autopipeline
from safelearn import DataValidator
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
model=LinearRegression()
scaler=StandardScaler()
pipe=Autopipeline()

validator=DataValidator()
sample_data={"age": "None",
              "bp": 120}


validator.set_required_columns(["age",
                                "bp"])

validator.set_column_types({"age": str, 
                            "bp": int})

validator.validate(sample_data)
validator.save_schema("schema.json")
validator.load_schema("schema.json")

print(validator.required_columns)

print(validator.column_types)

validator.set_column_ranges({
    "age": (0, 120),
    "bp": (50, 250)
})

sample_data = {
    "age": 500,
    "bp": 120
}

validator.validate(sample_data)


pipe.save(model=model,
          scaler=scaler, 
          path="model.pkl")

data=pipe.load(path="model.pkl")

print(data)