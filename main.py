import matplotlib as mpl
import matplotlib.pyplot as plt

import pandas as pd

import numpy as np


if __name__ == '__main__':
    plt.style.use('classic')


    # Read the CSV file
    df = pd.read_csv("C:\\Working\\Data\\100_Batches_IndPenSim_V3.csv")

    # View the first 5 rows
    print(df.head())

    # List Columns
    print(df.columns)

    #list only column
    print(df.columns[4])

    data = df['Acid flow rate(Fa:L/h)'].tolist()

    # print(data)
    # print(len(data))

    x = range(0,len(data))

    #plt.plot(x, data)
    plt.plot(x[0:10000], data[0:10000])

    plt.show()



