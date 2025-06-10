from datasets import load_dataset
import pandas as pd
import re

def load_medquad():
    dataset=load_dataset("Laurent1/MedQuad-MedicalQnADataset_128tokens_max")
    df= pd.DataFrame(dataset['train'])
    # print(df['text'][0])
    # df=df[['question','answer']].dropna()
    df = df[['text']].dropna()
    df.drop_duplicates(subset=['text'],inplace=True)

    # pattern = re.compile(r"### Instruction:\s*(.*?)\s*### Response:\s*(.*)", re.DOTALL)
    pattern = re.compile(r"### Instruction:\s*(.*?)\s*### Response:\s*(.*)", re.DOTALL)

    instructions = []
    responses = []
    for text in df['text']:
        match = pattern.search(text)
        if match:
            instructions.append(match.group(1).strip())
            responses.append(match.group(2).strip())
        else:
            instructions.append(None)
            responses.append(None)

    df['Instruction'] = instructions
    df['Response'] = responses
    df.drop('text',axis=1, inplace=True)

    return df

df=load_medquad()
# print(df.describe(include='all'))

