def lerExcel(nomeArquivo):
    import pandas as pd

    data_frame = pd.read_excel(f"assets/{nomeArquivo}.xlsx")
    return data_frame