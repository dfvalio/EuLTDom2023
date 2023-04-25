#!/usr/bin/env python
# coding: utf-8

import pyarrow as pa
import numpy as np
import pandas as pd
import pyarrow.parquet as pq
import codecs
import re
import json


# Opening and reading data file
parquet_file = pq.ParquetFile('acl-publication-info.74k.parquet')

data = pd.read_parquet('acl-publication-info.74k.parquet')

# Selcting texts from 2010 to end of 2022

list_years=data["year"].to_list()
list_text=data["full_text"]
list_text_from_2010=[]
list_years_from_2010=[]

for i,element in enumerate(list_years):
    if int(element) >= 2010:
        list_text_from_2010.append(list_text[i])
        list_years_from_2010.append(element)


# Lists of languages, domains, and NLP tasks

languages=["Basque","Bosnian","Bulgarian","Catalan|Valencian","Croatian","Czech","Danish","Dutch","English","Estonian","Faroese","Finnish","French","Galician","German","Greek","Hungarian","Icelandic","Irish","Italian","Karelian","Latvian","Lithuanian","Luxembourgish","Maltese","Norwegian","Polish","Portuguese","Romani","Romanian|Moldavian|Moldovan","Saami","Serbian","Slovak","Slovene","Spanish","Swedish","Tornedalian","Welsh","Yiddish"]

domains=["Mathematics|Maths","Computer science|Information science|Computer and information sciences","Physics","Chemistry","Environmental sciences|Environmental science","Biological sciences|Biological science|Biology","Civil engineering","Electrical engineering","Electronic engineering","Information engineering","Mechanical engineering","Chemical engineering","Materials engineering","Medical engineering","Environmental engineering","Environmental biotechnology","Industrial biotechnology","Nano-technology|Nanotechnology|Nano technology|Nanoscience|Nano-science","Agriculture","Forestry","Fisheries","Animal and dairy science|Animal science|Dairy science|Animal and dairy science","Veterenary","Agricultural biotechnology","Psychology","Cognitive sciences","Economics","Business","Finance","Tourism","Sociology|Social Sciences","Political Science","Geography","Archeology","Anthropology","Philology","Linguistics","Religion|religious"]

nlp=["optical character recognition|OCR","speech recognition","speech segmentation","text-to-speech","word segmentation|tokenization","lemmatization","morphological segmentation","part-of-speech tagging|pos tagging","stemming","grammar induction","sentence breaking ","parsing","lexical semantics","distributional semantics","named entity recognition","sentiment analysis","terminology extraction","word-sense disambiguation|word sense disambiguation","entity linking","multiword expressions|MWE","relationship extraction","semantic parsing","semantic role labelling","coreference resolution","discourse analysis","implicit semantic role labelling","recognizing textual entailment","topic segmentation","argument mining","anaphora resolution","temporal processing","automatic summarization","grammatical error correction","machine translation|MT","natural-language understanding|natural language understanding","natural-language generation|natural language generation","book generation","document AI","dialogue management","question answering|QA","text-to-image generation","text-to-scene generation","text-to-video","information retrieval","information extraction","multimodal systems","automated writing assistance","text simplification","author profiling","spam detection","virtual agents|chatbot"]


# Count the number of articles with 2 or more mentions of each language

dict_lang={}
for element in languages:
    count=0
    for text in list_text_from_2010:
        if (len(re.findall(element.lower(), text.lower()))>=2):
            count+=1
    dict_lang[element]=count

# Count the number of articles with 2 or more mentions of each domain 
    
dict_dom={}
for element in domains:
    count=0
    for text in list_text_from_2010:
        if (len(re.findall(element.lower(), text.lower()))>=2):
            count+=1
    dict_dom[element]=count

# Count the number of articles with 2 or more mentions of each domain and at least 1 mention of the adjective associated to the domain
   
dict_dom["Literature"]={}
count=0
for text in list_text_from_2010:
    if (len(re.findall("literature", text.lower()))>=2):
        if(len(re.findall("literary", text.lower()))>=1):
            count+=1
dict_dom["Literature"]=count

dict_dom["Government"]={}
count=0
for text in list_text_from_2010:
    if (len(re.findall("government", text.lower()))>=2):
        if(len(re.findall("governmental", text.lower()))>=1):
            count+=1
dict_dom["Government"]=count

dict_dom["Law"]={}
count=0
for text in list_text_from_2010:
    if (len(re.findall("law", text.lower()))>=2):
        if(len(re.findall("legal", text.lower()))>=1):
            count+=1
dict_dom["Law"]=count

dict_dom["Education"]={}
count=0
for text in list_text_from_2010:
    if (len(re.findall("education", text.lower()))>=2):
        if(len(re.findall("educational", text.lower()))>=1):
            count+=1
dict_dom["Education"]=count
          
dict_dom["History"]={}
count=0
for text in list_text_from_2010:
    if (len(re.findall("history", text.lower()))>=2):
        if(len(re.findall("history", text.lower()))>=1):
            count+=1
dict_dom["History"]=count

dict_dom["Phylosophy"]={}
count=0
for text in list_text_from_2010:
    if (len(re.findall("philosophy", text.lower()))>=2):
        if(len(re.findall("philosophical", text.lower()))>=1):
            count+=1
dict_dom["Philosophy"]=count

dict_dom["Ethics"]={}
count=0
for text in list_text_from_2010:
    if (len(re.findall("ethics", text.lower()))>=2):
        if(len(re.findall("ethical", text.lower()))>=1):
            count+=1
dict_dom["Ethics"]=count

# Specific counting regarding the domain "Arts" for disambiguation with terms such as "state-of-the-art"

dict_dom["Arts"]={}
count=0
for text in list_text_from_2010:
    if (len(re.findall(element.lower(), text.lower()))>=2):
        match_art=re.findall("\sart\s|\sarts\s", text.lower(), flags=0)
        match_sota=re.findall("state of the arts", text.lower(),flags=0)
        match_sota1=re.findall("state of the art", text.lower(),flags=0)
        total=len(match_art)-len(match_sota)-len(match_sota1)
        if total >=2:
            count=count+1
dict_dom["Arts"]=count

# Count the number of articles with 2 or more mentions of each NLP task

dict_nlp_task={}
for element in nlp:
    count=0
    for text in list_text_from_2010:
        if (len(re.findall(element.lower(), text.lower()))>=2):
            count+=1
    dict_nlp_task[element]=count
    

# Result files for each dimension of the study: languages, domains, and NLP tasks

file_lang = codecs.open("count_articles_per_lang.tsv", "w", "UTF-8")
file_lang.write("languague\tnumber of articles\n")

for key in dict_lang:
    file_lang.write(key + "\t" + str(dict_lang[key]) + "\n")
file_lang.close()    

file_dom = codecs.open("count_articles_per_domain.tsv", "w", "UTF-8")
file_dom.write("domain\tnumber of articles\n")

for key in dict_dom:
    file_dom.write(key + "\t" + str(dict_dom[key]) + "\n")
    
file_nlp = codecs.open("count_articles_per_nlp.tsv", "w", "UTF-8")
file_nlp.write("NLP task\tnumber of articles\n")

for key in dict_nlp_task:
    file_nlp.write(key + "\t" + str(dict_nlp_task[key]) + "\n")

