import googletrans
from googletrans import Translator
translator=Translator()
import pandas as pd
df=pd.read_excel(r'C:\Users\Frank Shin\Desktop\exctrans\source.xlsx')
df_rus=df.copy()
df_rus.rename(columns=lambda x: translator.translate(x,'ru').text, inplace=True)
translations={}
for column in df.columns:
    elements_per_col=df[column].unique()
    for element in elements_per_col:
        if isinstance(element, str):
            ## put every unique element to dic (element, translate_element)
            translations[element]=translator.translate(element,'ru').text
        else:
            translations[element]=element
##print(translations)
df_rus.replace(translations, inplace = True)
df_rus.to_excel(r'C:\Users\Frank Shin\Desktop\exctrans\source_rus.xlsx', index = False)
