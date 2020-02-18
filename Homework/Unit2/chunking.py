import pandas as pd
import numpy as np

def get_data(file_path, chunksize):

    file_type = file_path.split('.')[-1]
    if file_type in ['csv', 'txt']:
        data = pd.read_csv(file_path, chunksize=chunksize)
    elif file_type in ['xlsx']:
        data = pd.read_excel(file_path, chunksize=chunksize)
    return data


def probe_df(file_path, chunksize=1000):
    """
    parameters
    ------------
    file_path: str; required
        Location of file to read in.
    chunksize: int; required, default value is 1000
        Size of the chunk to use when streaming in the file.
    
    return
    ------------
    a dictionary encoded in the following way: 
        - each key is the name of a column within your dataset
        - the value for each key is another dictionary with the following key/value pairs:
        - `null values`: number of null values for that column
        - `dtype`: data type for that column
        - `avg_val`: average value for that column ( if numeric, otherwise don't include )
    """
    data = get_data(file_path, chunksize)
    sums = pd.Series(dtype=np.number)
    nrows = 0
    nulls = 0
    dtypes = pd.Series(dtype='object')
    columns = []
    for chunk in data:
        nulls += chunk.isnull().sum()
        if sums.empty:
            # 'Initializing the sums Series'
            sums = chunk.sum(numeric_only=True)
        else:
            sums += chunk.sum(numeric_only=True)
        nrows += chunk.shape[0] - chunk[sums.index].isnull().sum()
        
        if dtypes.empty:
            dtypes = chunk.dtypes
            columns = chunk.columns

    means = sums / nrows
    data_dict = {}
    for col in columns:
        data_dict[col] = {}
        
        data_dict[col]['null values'] = nulls[col]
        data_dict[col]['dtype'] = dtypes[col].name
        if col in means.index:
            data_dict[col]['avg_val'] = means[col] 
        # {data[col]].isnull().sum(),
        #                     data[col].dtype,
        #                     data[col].mean()
    

    return data_dict


def chunk_writer(chunk, file_path, first_chunk, index=False):
    """
    """
    file_type = file_path.split('.')[-1]
    if file_type in ['csv', 'txt']:
        if first_chunk:
            chunk.to_csv(file_path, index=False)
        else:
            chunk.to_csv(file_path, index=False, header=False, mode='a')
    elif file_type in ['xlsx']:
        if first_chunk:
            chunk.to_excel(file_path, index=False)
        else:
            writer = pd.ExcelWriter(file_path, engine='openpyxl', mode='a')
            chunk.to_excel(writer, index=False, header=False)


def write_df(file_path_read, file_path_write, chunksize=1000, missing_vals=None):
    """
    parameters
    ------------
    file_path_read: str, required 
        location of file to read in.
    file_path_write: str, required 
        location of the file to write the new file out to
    chunksize: int, required, default value is 1000.
        Size of the chunk to use when streaming in the file.
    missing_vals: dict, optional
        accepts a dictionary as an argument with key/value pairs that list the column in the dataset(key) as well as the value to fill 
        missing values with for that column(value).  The values in this dictionary will be used to fill missing values in the file at 
        the location in file_path_read
    """
    data = get_data(file_path_read, chunksize)

    first_chunk = True
    for chunk in data:
        if missing_vals:
            chunk = chunk.fillna(missing_vals)
        chunk_writer(chunk, file_path_write, first_chunk, index=False)
        first_chunk = False
        

if __name__ == '__main__':
    d = probe_df('data/titanic.csv', chunksize=100)
    nas = {'Age': 0, 'Cabin': 'Nope', 'Embarked':'Nope'}
    write_df('data/titanic.csv', 'data/titanic2.csv', chunksize=100, missing_vals=nas)
    write_df('data/titanic.csv', 'data/titanic2.txt', chunksize=100, missing_vals=nas)
    write_df('data/titanic.csv', 'data/titanic2.xlsx', chunksize=100, missing_vals=nas)