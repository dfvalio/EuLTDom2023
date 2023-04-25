import pandas as pd
import plotly.graph_objects as go
import numpy as np

# Load the data from the CSV file
df = pd.read_csv('all_langs_combined.csv')

# Get a list of unique languages in the data
languages = df['language'].unique()

# Create an empty list to hold the traces for each language
traces = []

# Loop through each language and create a separate trace for each one
supin=0
for language in languages:
    print(language)
    if language !="Random":
        # Subset the data to only include rows for the current language
        lang_df = df[df['language'] == language]
    
        # Get unique values for the domain and NLP task columns
        domains = lang_df['domain'].unique()
        domains.sort()

        nlp_tasks = lang_df['nlp_tasks'].unique()
        nlp_tasks.sort()

    
        # Create a 2D array to hold the values for the surface plot
        pivoted_df = lang_df.pivot(index='domain', columns='nlp_tasks', values='value')
        values = pivoted_df.values+supin
        
        # Filter out points where z=0
        values = np.where(values == 0, np.nan, values)
    
        # Create a trace for the current language
        #colorscale = 'Viridis_r'
        colorscale = 'plasma_r'
        x, y = np.meshgrid(nlp_tasks, domains)
        trace = go.Scatter3d(x=x.flatten(), y=y.flatten(), z=values.flatten()+supin,
                             mode='markers', marker=dict(color=values.flatten(), colorscale=colorscale,cmin=0,cmax=20),name=language)
        
        # Add the trace to the list of traces
        traces.append(trace)
    
# Create a 3D surface plot for all the languages
fig = go.Figure(data=traces)
    
# Set the plot title and axis labels
fig.update_layout(scene=dict(
                    xaxis=dict(
                        title='Domain',
                        tickmode='linear',
                        dtick=1,
                        ),
                    yaxis=dict(
                        title='NLP Task',
                        tickmode='linear',
                        dtick=1,
                        ),
                    zaxis=dict(
                        title='Value')),
                 margin=dict(l=50, r=50, t=100, b=50))
    
# Show the plot
#fig.show()

fig.update_layout(width=3000, height=3000)

# Save the plot

fig.write_html('3d_all_languages_plasma.html')