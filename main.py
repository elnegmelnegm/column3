import streamlit as st
import plotly.express as px
import pandas as pd

# Your data
data = {
    'Column': ["Zorbax Extend C18", "Capcell C18 ACR", "SepaxGP-C18", "Zorbax Eclipse XDB C18", "Monitor C18",
               "Genesis C18"],
    'Prin1': [-2.148996991, -1.610939802, -1.462305548, -2.030175195, -1.312132388, -1.602679708],
    'Prin2': [0.626657136, 1.077198945, 0.860370528, 0.381349879, 0.088940351, -0.362529862],
    'Prin3': [1.204634825, 0.82007068, 0.337134626, 0.813631363, 0.312310888, 0.724997885]
}

df = pd.DataFrame(data)

# Streamlit app
st.title("3D Scatter Plot with Plotly and Streamlit")
st.write("Hover over points to see labels.")

# 3D Scatter Plot with a darker gray background
fig = px.scatter_3d(df, x='Prin1', y='Prin2', z='Prin3', text='Column', color='Column')

fig.update_traces(marker=dict(size=12))

fig.update_layout(scene=dict(
                    xaxis_title='Principal Component 1',
                    yaxis_title='Principal Component 2',
                    zaxis_title='Principal Component 3'),
                    scene_bgcolor='rgba(50, 50, 50, 0.8)')  # Darker gray background

st.plotly_chart(fig)
