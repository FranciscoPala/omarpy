def num_describe(data_in):
    """returns a better vesion of describe

    Args:
        data_in (pd.DataFrame): input pandas DataFrame

    Returns:
        pd.DataFrame: output dataframe
    """
    # get extra percentiles
    data_out = data_in.describe([.01,.02,.98,.99]).T
    data_out = data_out.drop(columns='count')
    data_out.insert(0,'skewness', data_in.skew())
    data_out.insert(0,'kurtosis', data_in.kurtosis())
    data_out.insert(0,'sparsity', (data_in==0).sum()/len(data_in))
    data_out.insert(0,'nulls', (data_in.isna()).sum()/len(data_in))
    return data_out