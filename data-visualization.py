import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

def load_data(file):
    return pd.read_csv(file)

def plot_data(df):
    st.write("### Data Visualization")

    # Exclude Fault Code, Fault Message, and Fault Solution columns
    columns_to_exclude = ['Fault Code', 'Fault Message', 'Fault Solution']
    columns_to_plot = [col for col in df.columns if col not in columns_to_exclude and col != 'Timestamp']

    for column in columns_to_plot:
        fig, ax = plt.subplots()
        ax.plot(df['Timestamp'], df[column])
        ax.set_title(column)
        ax.set_xlabel('Timestamp')
        ax.set_ylabel(column)

        # Set major ticks locator for y-axis to integers
        ax.yaxis.set_major_locator(MaxNLocator(integer=True))
        
        # Optionally set x-axis to display fewer ticks
        ax.xaxis.set_major_locator(MaxNLocator(nbins=10, prune='both'))

        st.pyplot(fig)

def main():
    st.title("CSV Data Visualization Tool")

    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    if uploaded_file is not None:
        data = load_data(uploaded_file)
        st.write("### Data Preview")
        st.write(data.head())
        plot_data(data)

if __name__ == "__main__":
    main()
