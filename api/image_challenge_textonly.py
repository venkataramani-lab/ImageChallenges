# -*- coding: utf-8 -*-

import os
import openai
import tiktoken
import pandas as pd


#%%

enc = tiktoken.encoding_for_model("gpt-4")

with open("D:\\Data\\Marc(D)\\k") as k:
    content = k.read()
os.environ["OPENAI_API_KEY"] = content
openai.api_key = os.getenv("OPENAI_API_KEY")


#%%


def promptGPT(text,  model = "gpt-4"):
    completion = openai.ChatCompletion.create(
      model=model,
      messages=[
        {"role": "user", "content": text}
      ])
    ret = completion["choices"][0]["message"]["content"]
    return ret


#%%

path = "" # path to input

data = pd.read_excel(path)

for idx, row in data.iterrows():
    prompt = row["PromptedQuestion"]
    prompt = prompt.replace("n image", "")
    if prompt == " ":
        continue
    print(idx)
    print(prompt)
    try:
        output = promptGPT(prompt)
        print(output)
        data.at[idx, "Output_TextOnly"]  = output
    except Exception as e:
        print(str(e))
        data.at[idx, "Output_TextOnly"]  = str(e)
    print(idx)

data.to_excel("Challenges_output.xlsx")



