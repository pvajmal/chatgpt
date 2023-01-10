import pandas as pd

class CreateData():
    def datacreater(self,date, name, category, amount, description):
        expensenow = {
            'Date' : [date],
            'Name':[name],
            'Category': [category],
            'Amount': [amount],
            'Description' : [description]
        }
        dataframe = pd.DataFrame.from_dict(expensenow)
        return dataframe
