import pandas as pd


def csvToModel(csvfile):
    your_dataframe = pd.read_csv(csvfile)
    # Make a row iterator (this will go row by row)
    iter_data = your_dataframe.iterrows()
    print(your_dataframe)
