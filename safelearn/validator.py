import pandas as pd
import json
class DataValidator:

    def __init__(self):
        self.required_columns=[]
        self.column_types={}
        self.allow_null=False

    def set_required_columns(self, columns):
        self.required_columns = columns
    

    def set_column_types(self,column_types):
        self.column_types = column_types

    def save_schema(self,path):
        schema={
            "required_columns":self.required_columns,
            "column_types":{
                k
            }

        }

    def validate(self,data):
        if not isinstance(data,(dict ,pd.DataFrame)):
            raise ValueError("Data should be a dictionary")
        
        if isinstance(data,pd.DataFrame):
            data=data.to_dict(orient="records")[0]
        
        for  column in self.required_columns:
            if column not in data:
                raise ValueError(f"Missing required column: {column}")
            
        for column,expected_type in self.column_types.items():
            if column in data:

                if data[column] is None or data[column]=="":
                    raise ValueError(f"Column '{column}' cannot be null")
                
                if not isinstance(data[column],expected_type):
                    try:
                        data[column]=expected_type(data[column])
                    except:
                       raise ValueError(f"Column '{column}' should be of type {expected_type.__name__}")
            
        print("Data is valid")