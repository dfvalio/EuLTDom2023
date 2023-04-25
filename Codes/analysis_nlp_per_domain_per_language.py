#!/usr/bin/env python
# coding: utf-8

import pyarrow as pa
import numpy as np
import pandas as pd
import pyarrow.parquet as pq
import codecs
import re
import json


# Opening and reading file with data
parquet_file = pq.ParquetFile('acl-publication-info.74k.parquet')

data = pd.read_parquet('acl-publication-info.74k.parquet')


# Selecting texts written from 2010 to end of 2022 

list_years=data["year"].to_list()
list_text=data["full_text"]
list_text_from_2010=[]
list_years_from_2010=[]

for i,element in enumerate(list_years):
    if int(element) >= 2010:
        list_text_from_2010.append(list_text[i])
        list_years_from_2010.append(element)


# Languages / Domains / NLP Tasks lists

languages=["Basque","Bosnian","Bulgarian","Catalan|Valencian","Croatian","Czech","Danish","Dutch","English","Estonian","Faroese","Finnish","French","Galician","German","Greek","Hungarian","Icelandic","Irish","Italian","Karelian","Latvian","Lithuanian","Luxembourgish","Maltese","Norwegian","Polish","Portuguese","Romani","Romanian|Moldavian|Moldovan","Saami","Serbian","Slovak","Slovene","Spanish","Swedish","Tornedalian","Welsh","Yiddish"]


domains=["Mathematics|Maths","Computer science|Information science|Computer and information sciences","Physics","Chemistry","Environmental sciences|Environmental science","Biological sciences|Biological science|Biology","Civil engineering","Electrical engineering","Electronic engineering","Information engineering","Mechanical engineering","Chemical engineering","Materials engineering","Medical engineering","Environmental engineering","Environmental biotechnology","Industrial biotechnology","Nano-technology|Nanotechnology|Nano technology|Nanoscience|Nano-science","Agriculture","Forestry","Fisheries","Animal and dairy science|Animal science|Dairy science|Animal and dairy science","Veterenary","Agricultural biotechnology","Psychology","Cognitive sciences","Economics","Business","Finance","Tourism","Sociology|Social Sciences","Political Science","Geography","Archeology","Anthropology","Philology","Linguistics","Religion|religious"]

nlp=["optical character recognition|OCR","speech recognition","speech segmentation","text-to-speech","word segmentation|tokenization","lemmatization","morphological segmentation","part-of-speech tagging|pos tagging","stemming","grammar induction","sentence breaking ","parsing","lexical semantics","distributional semantics","named entity recognition","sentiment analysis","terminology extraction","word-sense disambiguation|word sense disambiguation","entity linking","multiword expressions|MWE","relationship extraction","semantic parsing","semantic role labelling","coreference resolution","discourse analysis","implicit semantic role labelling","recognizing textual entailment","topic segmentation","argument mining","anaphora resolution","temporal processing","automatic summarization","grammatical error correction","machine translation|MT","natural-language understanding|natural language understanding","natural-language generation|natural language generation","book generation","document AI","dialogue management","question answering|QA","text-to-image generation","text-to-scene generation","text-to-video","information retrieval","information extraction","multimodal systems","automated writing assistance","text simplification","author profiling","spam detection","virtual agents|chatbot"]


# Search for each language, each domain, and nlp tasks the number of texts containing at least 2 mentions of the terms

dict_lang_domain_nlp={}
for element in languages:
    dict_lang_domain_nlp[element]={}
    for dom in domains:
        dict_lang_domain_nlp[element][dom]={}
        for task in nlp:
            count=0
            for text in list_text_from_2010:
                if (len(re.findall(element.lower(), text.lower()))>=2):
                    if (len(re.findall(dom.lower(), text.lower()))>=2):
                        if (len(re.findall(task.lower(), text.lower()))>=2):
                            count+=1
            dict_lang_domain_nlp[element][dom][task]=count
    

# Same search but with specific cases where terms can have multiple meaning. In these cases, we also search for the mention of the adjective related to the noun (at least one mention for the text to be considered) 

    dict_lang_domain_nlp[element]["Literature"]={}
    for task in nlp:
        count=0
        for text in list_text_from_2010:
            if (len(re.findall(element.lower(), text.lower()))>=2):
                if (len(re.findall("literature", text.lower()))>=2):
                    if(len(re.findall("literary", text.lower()))>=1):
                        if (len(re.findall(task.lower(), text.lower()))>=2):
                            count=count+1
            dict_lang_domain_nlp[element]["Literature"][task]=count

    dict_lang_domain_nlp[element]["Government"]={}
    for task in nlp:
        count=0
        for text in list_text_from_2010:
            if (len(re.findall(element.lower(), text.lower()))>=2):
                if (len(re.findall("government", text.lower()))>=2):
                    if(len(re.findall("governmental", text.lower()))>=1):
                        if (len(re.findall(task.lower(), text.lower()))>=2):
                            count=count+1
            dict_lang_domain_nlp[element]["Government"][task]=count
            
    dict_lang_domain_nlp[element]["Law"]={}
    for task in nlp:
        count=0
        for text in list_text_from_2010:
            if (len(re.findall(element.lower(), text.lower()))>=2):
                if (len(re.findall("law", text.lower()))>=2):
                    if(len(re.findall("legal", text.lower()))>=1):
                        if (len(re.findall(task.lower(), text.lower()))>=2):
                            count=count+1
            dict_lang_domain_nlp[element]["Law"][task]=count            
            
    dict_lang_domain_nlp[element]["Education"]={}
    for task in nlp:
        count=0
        for text in list_text_from_2010:
            if (len(re.findall(element.lower(), text.lower()))>=2):
                if (len(re.findall("education", text.lower()))>=2):
                    if(len(re.findall("educational", text.lower()))>=1):
                        if (len(re.findall(task.lower(), text.lower()))>=2):
                            count=count+1
            dict_lang_domain_nlp[element]["Education"][task]=count
        
    dict_lang_domain_nlp[element]["History"]={}
    for task in nlp:
        count=0
        for text in list_text_from_2010:
            if (len(re.findall(element.lower(), text.lower()))>=2):
                if (len(re.findall("history", text.lower()))>=2):
                    if(len(re.findall("historical", text.lower()))>=1):
                        if (len(re.findall(task.lower(), text.lower()))>=2):
                            count=count+1
            dict_lang_domain_nlp[element]["History"][task]=count

    dict_lang_domain_nlp[element]["Philosophy"]={}
    for task in nlp:
        count=0
        for text in list_text_from_2010:
            if (len(re.findall(element.lower(), text.lower()))>=2):
                if (len(re.findall("philosophy", text.lower()))>=2):
                    if(len(re.findall("philosophical", text.lower()))>=1):
                        if (len(re.findall(task.lower(), text.lower()))>=2):
                            count=count+1
            dict_lang_domain_nlp[element]["Philosophy"][task]=count

    dict_lang_domain_nlp[element]["Ethics"]={}
    for task in nlp:
        count=0
        for text in list_text_from_2010:
            if (len(re.findall(element.lower(), text.lower()))>=2):
                if (len(re.findall("ethics", text.lower()))>=2):
                    if(len(re.findall("ethical", text.lower()))>=1):
                        if (len(re.findall(task.lower(), text.lower()))>=2):
                            count=count+1
            dict_lang_domain_nlp[element]["Ethics"][task]=count

# Specific search regarding the domain "Arts" for the disambiguation with mentions concerning state-of-the-art and variants

    dict_lang_domain_nlp[element]["Arts"]={}
    for task in nlp:
        count=0
        for text in list_text_from_2010:
            if (len(re.findall(element.lower(), text.lower()))>=2):
                match_art=re.findall("\sart\s|\sarts\s", text.lower(), flags=0)
                match_sota=re.findall("state of the arts", text.lower(),flags=0)
                match_sota1=re.findall("state of the art", text.lower(),flags=0)
                total=len(match_art)-len(match_sota)-len(match_sota1)
                if total >=2:
                    if (len(re.findall(task.lower(), text.lower()))>=2):
                        count=count+1
            dict_lang_domain_nlp[element]["Arts"][task]=count


# Creation of results file in json format


result = json.dumps(dict_lang_domain_nlp, indent = 3)

file = codecs.open("count_nlp_per_domain_per_language.json", "w", "UTF-8")
file.write(result)
