from sys import path

import pandas as pd
import json
class DataValidator:

    def __init__(self):
        self.required_columns=[]
        self.column_types={}
        self.column_ranges={}
        self.allowed_values={}
        self.feature_order=[]
        self.allow_null=False

    def set_required_columns(self, columns):
        self.required_columns = columns
    

    def set_column_types(self,column_types):
        self.column_types = column_types


    def set_column_ranges(self,column_ranges):
        self.column_ranges=column_ranges

    def set_allowed_values(self,allowed_values):
        self.allowed_values= allowed_values
    
    def set_feature_order(self,columns):
        self.feature_order= columns

    def save_schema(self,path):
        schema={
            "required_columns":self.required_columns,
            "column_types":{
                key: value.__name__ for key,value in self.column_types.items()
            },
            "column_ranges": self.column_ranges,
            "allowed_values": self.allowed_values,
            "feature_order": self.feature_order
        }
        with open(path,"w") as file:
            json.dump(schema,file,indent=4)
        print("Schema is saved")


    def load_schema(self,path):
        with open(path,"r") as file:
            schema=json.load(file)
        self.required_columns=schema["required_columns"]
        self.feature_order = schema.get("feature_order",[])
        self.column_ranges=schema.get("column_ranges",{})
        self.allowed_values=schema.get("allowed_values",{})

        type_mapping={
            "int":int,
            "float": float,
            "str":str,
            "bool":bool
        }

        self.column_types={
            key :type_mapping[value]
            for key,value in schema["column_types"].items()
        }
        print("Schema is loaded")

    def validate(self,data):
        if not isinstance(data,(dict ,pd.DataFrame)):
            raise ValueError("Data should be a dictionary")
        
        if isinstance(data,pd.DataFrame):
            data=data.to_dict(orient="records")[0]
        
        for  column in self.required_columns:
            if column not in data:
                raise ValueError(f"Missing required column: {column}")
            
        if self.feature_order:
            data_columns=list(data.keys())
            if data_columns != self.feature_order:
                    raise ValueError(f"Expected column order {self.feature_order}, got {data_columns}")
            
        for column,expected_type in self.column_types.items():
            if column in data:

                if data[column] is None or data[column]=="":
                    raise ValueError(f"Column '{column}' cannot be null")
                
                if not isinstance(data[column],expected_type):
                    try:
                        data[column]=expected_type(data[column])
                    except: 
                       raise ValueError(f"Column '{column}' should be of type {expected_type.__name__}")
                if column in  self.column_ranges:
                    if not isinstance(data[column], (int, float)):
                       raise ValueError(  f"Range validation can only be applied to numeric columns. '{column}' is {type(data[column]).__name__}")
            
                    min_value,max_value= self.column_ranges[column]
                    if not (min_value <= data[column] <= max_value):
                           raise ValueError(f"Column '{column}' should be between {min_value} and {max_value}")
                if column in self.allowed_values:
                    if data[column] not in self.allowed_values[column]:
                        raise ValueError(f"Column '{column}' must be one of {self.allowed_values[column]}")
       
        print("Data is valid")
