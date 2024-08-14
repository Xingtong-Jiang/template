import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

### DEFINE
def main():
    df = pd.read_csv('output/data_merged.csv')
    plot_data(df)
    df = clean_data(df)
    df.to_csv('output/data_cleaned.csv', index = False)

def plot_data(df):
    plt.hist(df['chips_sold'], weights = 100 * np.ones(len(df['chips_sold'])) / len(df['chips_sold']))
    
    # Set labels and title
    plt.xlabel('Chips Sold')
    plt.ylabel('Percentage')
    plt.title('Histogram of Chips Sold (Percentage)')
    
    plt.savefig('output/chips_sold.pdf')

def clean_data(df):
    df['chips_sold'][df['chips_sold'] == -999999] = np.nan
    return(df)
    
### EXECUTE
main()
