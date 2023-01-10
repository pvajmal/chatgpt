import pandas as pd

class CreateData():
    def datacreater(self,name, category, amount):
        expensenow = {
            'Name':[name],
            'Category': [category],
            'Amount': [amount],
        
        }
        dataframe = pd.DataFrame.from_dict(expensenow)
        return dataframe
