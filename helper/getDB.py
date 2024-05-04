# getDB
import pandas as pd


def getDB(filename: str, kls: str) -> pd.DataFrame:
    df = pd.read_csv(filename)
    df['Kelas'] = df['Kelas']+"    "
    df['Kelas'] = df['Kelas'].replace(r'\s+', ' ', regex=True).str.upper().str.strip()
    df = df.loc[df['Kelas'] == kls]
    df['Nama'] = df['Nama'].str.title()
    df = df.sort_values(by=['Nama'])
    df.rename(columns={"Email (Harus Aktif Untuk E-Ticket)": "email"},
              inplace=True)
    df.reset_index(drop=True, inplace=True)
    return df