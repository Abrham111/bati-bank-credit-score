import pandas as pd

def extract_transaction_features(df, datetime_column):
  """
  Extracts transaction features (hour, day, month, year) from a datetime column in a DataFrame.

  Parameters:
    df (pd.DataFrame): The DataFrame containing the datetime column.
    datetime_column (str): The name of the column containing the datetime values.

  Returns:
    pd.DataFrame: The original DataFrame with new columns for transaction hour, day, month, and year.
  """
  # Ensure the datetime column is in datetime format
  df[datetime_column] = pd.to_datetime(df[datetime_column])

  # Extract features
  df['Transaction Hour'] = df[datetime_column].dt.hour
  df['Transaction Day'] = df[datetime_column].dt.day
  df['Transaction Month'] = df[datetime_column].dt.month
  df['Transaction Year'] = df[datetime_column].dt.year

  return df
