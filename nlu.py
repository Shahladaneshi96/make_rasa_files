import pandas as pd
import numpy as np
from collections import defaultdict
from pandas.core.api import notnull


path='.csv'

path_train= path

intent_list=['greeting','search','phone_question','out_of_scope','reset','change','sort','decrease_price','increase_price']

df = pd.read_csv(path_train)

grouped = df.groupby('label')['text'].apply(list)

dict_intent_example = grouped.to_dict()

intent_json_file = open("/content/nlu.yml", "a")

header1 = 'version: "3.1"'+'\n'+'nlu:'+'\n'

intent_json_file.write(header1)

for intent in dict_intent_example.keys():
  header2 = '\n'+'- intent: '+ str(intent)+'\n'+'  examples: |'+'\n'
  intent_json_file.write(header2)
  for example in dict_intent_example[intent]:
    intent_json_file.write('    - '+str(example)+'\n')

intent_json_file.close()