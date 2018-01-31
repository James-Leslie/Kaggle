## Titanic Data Column Descriptions
Values column should contain any information about the column which needs to be dealt with

| Field | Type | Description | Values | Use as input |
| ----- | ---- | ----------- | ------ | ------------ |
| PassengerID | int | Unique Identifier | - | No |
| Survived | int | Did the passenger survive? | 1/ 0 | **Target** |
| Pclass | int | Class of passenger | ? | **Yes** |
| Name | str | Name of passenger | - | No |
| Sex | str | Gender of passenger | Male/ Female | **Yes** |
| Age | float | Age of passenger | ? | **Yes** |
| SibSp | int | # of siblings / spouses aboard | ? | **Yes** |
| Parch | int | # of parents / children aboard | ? | **Yes** |
| ticket | str | Ticket number | - | No |
| fare | float | Passenger fare | ? | **Yes** |
| cabin | str | Cabin number | ? | No |
| embarked | str | Port of Embarkation | ? | *Maybe?* |
