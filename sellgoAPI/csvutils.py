import pandas as pd
from .models import CsvProduct


def csvToModel(csvfile,customer):
    dataframe = pd.read_csv( csvfile )
    # Make a row iterator (this will go row by row)
    iter_data = dataframe.iterrows()
    # print(dataframe)
    #products = []
    count =0
    for i in range( len( dataframe ) ):

        try:
            product = CsvProduct(title=str(dataframe.iloc[i][0]), price=dataframe.iloc[i][1],customer=customer)
            product.save()
            count+=1
        except Exception as e:
            print(str(e))
    return count
