import numpy as np

def change_dtypes(df):
    objs = [col for col in df.columns if col.dtype() = np.object]
    nums = [col for col in df.columns if col.dtype() != np.object]
    for col in objs:
        if df[col].nunique() <= 10:
            df[col] = df[col].astype('category')

    maxmin = pd.concat([df.max(), df.min()], axis=1)
    maxmin.cols = ['Max', 'Min']
    for col in nums:
        if maxmin.loc[col, 'Min'] >= 0:
            if 

    