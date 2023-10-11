# EuLTDom2023
European Language Technology Domains 2023

The EuLTDom2023 project reports on the current state-of-the-art of the usage of LT in different domains. The main purpose of this deliverable is to map the usage of NLP in various domains, to report findings regarding the fields that make regular use of these technologies, and to list domains that infrequently use LT or do not use it at all. For this aim, we analysed scientific papers published between 2010 and 2022 in the ACL Anthology, thus corresponding to scientific work done by the LT community. By applying a dictionary-based approach based on precise lists of terms related to languages, domains, and NLP tasks, we were able to present an overview of each of these dimensions, and to provide language-specific results mapping the usage of NLP tasks by the different domains. With the overall analysis, it is possible to identify the language, domains, and LT that have been the focus of the NLP research in the past years, and the language-specific results allow the clear identification of potential future developments to improve language equality at the level usage of LT. 

We provide here:
  1) The complete list of Domains and NLP tasks that were used in the dictionary-based approach
  2) The csv files corresponding to the language-specific results of the LT in each domain, index 1 refers to general NLP tasks, while index 2 refers to Higher-level NLP applications
  3) The csv files corresponding to the language-specific results of the LT in each domain with all NLP tasks (i.e.: concatenation of 2) files)
  4) .svg figures presented in the report other than heatmaps
  5) .pdf figures of complete heatmaps (i.e.: with all NLP tasks in the same graph for each language)
  6) Three 3-dimensional graphes (html) containing the overview of all languages, domains, and NLP tasks. Each graph correspond to one colour-scale (heat, viridis, and plasma). The x and y axis correspond to domains and tasks respectively. The z-axis corresponds to the number of ACL papers mentioning the specific domain/task/language. By clicking each point, detailed information is displayed. The graph can be rotated and zoomed in for a more detailed analysis of specific areas.

Moreover, we provide the following python scripts:
- overall_analysis.py - code for counting in the data the number of articles mentioning at least twice each language, domain, and NLP task. Each dimension is analysed separatly
- analysis_nlp_per_domain_per_language.py - code for counting the number of articles that mention each NLP and each domain for every language in our pre-defined list
- heatmap_generator_for_all_languages.py - code used for generating heatmaps for all languages of our study
- 3d_graph_generator.py - code used for the 3D graph generation

For further information, please consult the ELE-2 report available at: 
https://european-language-equality.eu/wp-content/uploads/2023/04/ELE2_Project_Report_EuLTDom2023.pdf
