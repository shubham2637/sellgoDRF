import pandas as pd
from .models import CsvProduct


def csvToModel(csvfile,customer):
    dataframe = pd.read_csv( csvfile )
    # Make a row iterator (this will go row by row)
    iter_data = dataframe.iterrows()
    # print(dataframe)
    products = []
    for i in range( len( dataframe ) ):
        products.append(
            CsvProduct(
                title=dataframe.iloc[i][0], price=dataframe.iloc[i][1],customer=customer
            )
        )
    CsvProduct.objects.bulk_create(products)
    return products