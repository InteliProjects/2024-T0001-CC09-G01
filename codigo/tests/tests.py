from functions import *
import pytest
import pandas as pd

@pytest.mark.parametrize("purchases_quantities, purchases, expected", 
                        [([5, 15, 4], pd.DataFrame({"Preço": [1, 2, 3]}), 1.96),
                        ([0, 0, 0], pd.DataFrame({"Preço": [1, 2, 3]}), 0),
                        ([1, 1, 1], pd.DataFrame({"Preço": [1, 2, 3]}), 2)
                        ])
def test_calculate_current_price(purchases_quantities, purchases, expected):
    assert calculate_current_price(purchases_quantities, purchases) == expected

@pytest.mark.parametrize("sale_price, du, di, expected", 
                        [(100, 30, 0.11, 98.76530455814981),
                        (30, 120, 0.2, 27.505269175842926),
                        (10, 60, 0.15, 9.67270924218466)
                        ])
def test_calculate_ideal_price(sale_price, du, di, expected):
    assert calculate_ideal_price(sale_price, du, di) == expected


@pytest.mark.parametrize("du, purchase_price, sale_price, di, expected", 
                        [(100, 29.6, 31, 0.11, 112.28044075002049),
                        (30, 119.7, 122, 0.2, 86.68058800971224),
                        (10, 60, 60.5, 0.15, 155.0700122656775)
                        ])
def test_calculate_cdi(du, purchase_price, sale_price, di, expected):
    assert calculate_cdi(du, purchase_price, sale_price, di) == expected