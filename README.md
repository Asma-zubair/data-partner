# data-partner
# SafeLearn

SafeLearn is a Python package for validating machine learning data before training or prediction.

## Features

- Required column validation
- Data type validation
- Automatic type conversion
- Null value checking
- Range validation
- Allowed values validation
- Feature order validation
- Schema saving and loading

## Installation

```bash
pip install safelearn
```

## Example

```python
from safelearn import DataValidator

validator = DataValidator()

validator.set_required_columns([
    "age",
    "bp"
])

validator.set_column_types({
    "age": int,
    "bp": int
})

validator.validate({
    "age": 25,
    "bp": 120
})
```

## Author

Asma Zubair
