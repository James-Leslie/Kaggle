## Titanic Data Column Descriptions
Values column should contain any information about the column which needs to be dealt with

| Field | Type | Description | Values | Use as input |
| ----- | ---- | ----------- | ------ | ------------ |
| PassengerID | int | Unique Identifier | 891 rows | No |
| Survived | int | Did the passenger survive? | 1/ 0 | **Target** |
| Pclass | int | Class of passenger | 1, 2 or 3 only | **Yes** |
| Name | str | Name of passenger | - | No |
| Sex | str | Gender of passenger | Male/ Female only | **Yes** |
| Age | float | Age of passenger | min: 0.42, max: 80.0, 117 Null values | **Yes** |
| SibSp | int | # of siblings / spouses aboard | min: 0, max: 8, 0 Null values | **Yes** |
| Parch | int | # of parents / children aboard | min: 0, max: 6, 0 Null values | **Yes** |
| Ticket | str | Ticket number | - | No |
| Fare | float | Passenger fare | min: 0.0 (15 values), max: 512.33, 0 Null values | **Yes** |
| Cabin | str | Cabin number | - | No |
| Embarked | str | Port of Embarkation | ? | *Maybe?* |
