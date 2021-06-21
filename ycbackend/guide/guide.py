import pandas as pd
import random

data = pd.read_csv("./ycbackend/guide/guide_data.csv")


def guide_sentence(label_list):
    temp = data
    result = ""
    for label in label_list:
        temp = temp[temp[label] == 1]
        if len(temp) > 0:
            result = random.choice(list(temp['tweet']))
    return result


