import pandas as pd

def save_to_csv(data: list, filename: str):
    """Save paper data to a CSV file."""
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
