from preswald import text, plotly, connect, get_df, table, query
import pandas as pd
import plotly.express as px

# 1. Welcome message
text("# Welcome to Preswald!")
text("## Cereal Data Dashboard")
text("This dashboard includes two visualizations: a bar chart for cereals with calories > 100 and a pie chart showing the distribution of total calories grouped by rating bins.")

# 2. Connect and load the cereal dataset
connect()
df = get_df('cereal_csv')

# 3. Filter the dataset using a SQL-like query for cereals with calories > 100
sql = "SELECT * FROM cereal_csv WHERE calories > 100"
filtered_df = query(sql, "cereal_csv")

# 4. Limit the data to only include 'name' and 'calories'
df_subset = filtered_df[['name', 'calories']]

text("### Bar Chart: Cereals with Calories > 100")
bar_fig = px.bar(
    df_subset,
    x='name',
    y='calories',
    title="Cereals with Calories > 100",
    labels={'name': 'Cereal Name', 'calories': 'Calories'}
)

# Increase the chart width and force x-axis tick labels for every bar.
bar_fig.update_layout(width=1000)
bar_fig.update_xaxes(
    tickangle=-45,
    tickmode='array',
    tickvals=df_subset['name'],
    ticktext=df_subset['name']
)

plotly(bar_fig)

# 4. Chart 2: Pie Chart (Distribution of Total Calories by Rating Bins)
# Create a rating_bin column by grouping ratings into 10-point bins.
df['rating_bin'] = (df['rating'] // 10) * 10

# Group by rating_bin and sum the calories.
calories_by_rating = df.groupby('rating_bin', as_index=False)['calories'].sum()

text("### Pie Chart: Distribution of Total Calories by Rating Bins")
pie_fig = px.pie(
    calories_by_rating,
    names='rating_bin',
    values='calories',
    title="Total Calories Contribution by Rating Bins",
    labels={'rating_bin': 'Rating Bin', 'calories': 'Total Calories'},
    color_discrete_sequence=px.colors.qualitative.Pastel
)
plotly(pie_fig)
