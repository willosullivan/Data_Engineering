import pandas as pd
import numpy as np
import pytest
from numpy import nan
from customer_pipeline import extract, load


# get data
@pytest.fixture(scope='session', autouse=True)
def df():
    # Will be executed before the first test
    df, tbl = extract()
    yield df
    # Will be executed after the last test
    load(df, tbl)
#

# check if column exists
def test_col_exists(df):
    name="CustomerKey"
    assert name in df.columns

# check for nulls
def test_null_check(df):
    assert df['CustomerKey'].notnull().all()

# check values are unique
def test_unique_check(df):
    assert pd.Series(df['CustomerKey']).is_unique

# check data type
def test_productkey_dtype_int(df):
    assert (df['CustomerKey'].dtype == int or df['CustomerKey'].dtype == np.int64)

# check data type
def test_productname_dtype_srt(df):
    assert (df['Customer'].dtype == str or  df['Customer'].dtype == 'O')


# check values in a list
def test_range_val_str(df):
    assert set(df['Country-Region'].unique()) == {'[Not Applicable]', 'Australia', 'Canada', 'France', 'Germany', 'United Kingdon', 'United States'}