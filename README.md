# Description
Spam Filter is a microservice made specifically for the E-petitions Project made in Go. Due to special needs (NLP + AI), we decided to stop on Python and implement a Web Socket type connection with the frontend.

## Contents
- [Conventions](#conventions)
- [Run Project](#run-project)
- [Usages](#usages)
- [Data](#data)
- [Contributors and Contributions](#contributors-and-contributions)
  
## Conventions
Spam Filter is developed to use the Web Sockets, thus to try it, just connect to Postman and initialize the web-socket route

## Run Project
- Navigate to `app.py`
- Run the file
- Open Postman and choose web-socket connection
- Type in: `ws://localhost:8567`
- Push 'Connect' and good to go.

## Usages

> ALERT: A lot of bad words here (sorry<3)

There are two main functionalities that can be found in `src`. First one is censoring (finding the uncesored words) and
second one is grammar correction.

```python
from src.censore.censore_main import check_censoring

seq = "I don't know why but I am filling shitty today"
print(check_censoring(seq))
```
```
['shitty']
```
The `check_censoring` func is available in three languages in total (RO, ENG, RU).
```python
from src.censore.censore_main import check_censoring

seq = "M-am săturat de toți idioții ăștea de politicieni"
print(check_censoring(seq))
```
```
['idioții']
```
Now, let's talk about grammar correction functionality. It basically imports the `language_tool_python` library and then just returns the necessary content. To put it simply:
```python
from src.grammar_correction.grammar_correction_main import print_all_necessary

seq = "M-am sturat de toti idiotii ăștia"
print(print_all_necessary(seq))
```
```
[
    {'offset': 4, 'errorLength': 6, 'suggestions': ['Seurat', 'Stuart', 'saturat', 'strat', 'stucat', 'stufat', 'suturat', 'săturat', 'turat', 'usturat', 'ștucat', 'șturț', 's turat', 'st urat'
        ]
    },
    {'offset': 14, 'errorLength': 4, 'suggestions': ['toți', 'Titi', 'boți', 'coti', 'coți', 'foți', 'goți', 'hoți', 'loti', 'moți', 'oți', 'poți', 'roti', 'roți', 'soți', 'tați', 'toci', 'togi', 'toi', 'toni', 'tonți', 'topi', 'tot', 'tota', 'tote', 'totei', 'toto', 'totă', 'toși', 'toții', 'țoi', 'țoii', 'țoli', 'țopi', 'tot i', 'TOTP'
        ]
    },
    {'offset': 19, 'errorLength': 7, 'suggestions': ['idioții', 'idiotei', 'idiotip', 'idioți', 'idioția', 'idioție', 'idioției', 'idioțio', 'idiot ii'
        ]
    }
]
```
As seen, it corrects not only grammar mistakes, but diacritics too. 
As a return statement, it returns the location of the error and the suggestions.

Now about the main function that does all this together:
```python
from filtering import filter_spam

seq = "Счастье в мелочах, бля"
print(filter_spam(seq))
```

```
['бля'] / [{'offset': 19, 'errorLength': 3, 'suggestions': ['для', 'оля']}]
```
Where first return is the uncensored word and the second return is the json with the error and suggestions.

## Data
We have searched a lot to obtain this data. In conclusion, we got three `.txt` datasets with three different languages (romanian `md_ro.txt`, english `eng.txt` and russian `rus.txt`). Here is the snippet for the english file:
```
titfuck
titi
tits
titt
tittie5
tittiefucker
titties
titty
tittyfuck
tittyfucker
tittywank
titwank
```

# Contributors and Contributions
![Contributors](https://img.shields.io/github/contributors/grumpycatyo-collab/spam_filter_epetitions)

All contributions, bug reports, bug fixes, documentation improvements, enhancements, and ideas are welcome.