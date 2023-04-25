import matplotlib.ticker as ticker
import matplotlib.cm as cm
import matplotlib as mpl
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns

# List of languages in the study
languages=["Basque","Bosnian","Bulgarian","Catalan|Valencian","Croatian","Czech","Danish","Dutch","English","Estonian","Faroese","Finnish","French","Galician","German","Greek","Hungarian","Icelandic","Irish","Italian","Karelian","Latvian","Lithuanian","Luxembourgish","Maltese","Norwegian","Polish","Portuguese","Romani","Romanian|Moldavian|Moldovan","Saami","Serbian","Slovak","Slovene","Spanish","Swedish","Welsh","Yiddish"]

for language in languages:
    # Load the data from each language file
    heat_raw = pd.read_csv(language+'.csv')

    # Pivot the data from the csv into a matrix
    heat_matrix = heat_raw.pivot("Domain", "NLP Task", "Value")

    # Figure creation
    fig = plt.figure()
    fig, ax = plt.subplots(1,1, figsize=(12,12))
    heatplot = ax.imshow(heat_matrix, cmap='BuPu')
    ax.set_xticklabels(heat_matrix.columns)
    ax.set_yticklabels(heat_matrix.index)

    # Plot characteristics
    tick_spacing = 1
    ax.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
    ax.yaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
    ax.set_title("Heatmap of Domains and NLP Tasks")
    ax.set_xlabel('NLP Task')
    ax.set_ylabel('Domain')
    sns.set(font_scale=1.4)
    fig = plt.figure(figsize=(50,40))

    # Plot the data from heat_matrix in the figure
    r = sns.heatmap(heat_matrix, cmap='BuPu',annot=True,square=False,fmt='g')
    r.set_title("Heatmap of Domains and NLP Tasks")

    # Save heatmap to a specific file for each language 
    fig.savefig("Heatmaps_single_files_final/"+language+".svg")