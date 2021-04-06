import pandas as pd;
import plotly.express as px;

df = pd.read_csv("data.csv");
line_graph = px.scatter(df, x = "Population", y = "Per capita",size = "Percentage", color = "Country", size_max = 1000, title = "Graph");

line_graph.show();