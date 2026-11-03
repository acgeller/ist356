def clean_currency(value:str) -> float:
    return float(value.replace(',', '').replace('$',''))


if __name__ == "__main__":
    assert clean_currency