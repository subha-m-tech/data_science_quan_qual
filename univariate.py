class Univariate:
    def quanQual(dataset):
        quan = []
        qual = []
        for column_name in dataset.columns:
            print (column_name)
            if dataset[column_name].dtype == 'O':
                qual.append(column_name)
            else:
                quan.append(column_name)
        return quan, qual
            
        
        