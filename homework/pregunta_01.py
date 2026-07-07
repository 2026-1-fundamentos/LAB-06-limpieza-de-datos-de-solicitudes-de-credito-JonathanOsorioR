"""
Escriba el codigo que ejecute la accion solicitada en la pregunta.
"""
import pandas as pd
import os
def pregunta_01():
    """
    Realice la limpieza del archivo "files/input/solicitudes_de_credito.csv".
    El archivo tiene problemas como registros duplicados y datos faltantes.
    Tenga en cuenta todas las verificaciones discutidas en clase para
    realizar la limpieza de los datos.

    El archivo limpio debe escribirse en "files/output/solicitudes_de_credito.csv"

    """
    """
Escriba el codigo que ejecute la accion solicitada en la pregunta.
"""

    df = pd.read_csv("files/input/solicitudes_de_credito.csv", sep=";")
    df = df.iloc[:, 1:]

    df.dropna(inplace = True)

    barrio_original = df["barrio"].copy()

    col_texto = ["sexo", "tipo_de_emprendimiento", "idea_negocio", "línea_credito"]
    for col in col_texto:
        df[col] = (
            df[col]
            .astype(str)
            .str.lower()
            .str.replace(r"[-_.]", " ", regex=True)
            .str.replace(r"[!\"#$%&'()*+,/:;<=>?@[\\\]^`{|}~]", "", regex=True)
            .str.replace(r"\s+", " ", regex=True)
            .str.strip()
        )

    df["monto_del_credito"] = (
        df["monto_del_credito"]
        .astype(str)
        .str.replace(r"\.\d+", "", regex=True)
        .str.replace(r"[^0-9]", "", regex=True)
    )

    def normalizar_fecha(fecha):
        partes = str(fecha).split("/")
        if len(partes) != 3:
            return fecha
        if len(partes[0]) == 4:
            return f"{partes[2]}/{partes[1]}/{partes[0]}"
        return fecha

    df["fecha_de_beneficio"] = df["fecha_de_beneficio"].apply(normalizar_fecha)

    df["estrato"] = pd.to_numeric(df["estrato"], errors="coerce").astype("Int64")
    df["comuna_ciudadano"] = pd.to_numeric(df["comuna_ciudadano"], errors="coerce").astype("Int64")
    df["barrio"] = (
        barrio_original.loc[df.index]
        .astype(str)
        .str.lower()
        .str.replace(r"[-_]", " ", regex=True)
        .str.replace(r"[!\"#$%&'()*+,/:;<=>?@[\\\]^`{|}~]", "", regex=True)
        .str.replace(r"\s+", " ", regex=True)
    )

    df = df.drop_duplicates()




    if not os.path.exists("files/output"):
        os.makedirs("files/output")

    df.to_csv("files/output/solicitudes_de_credito.csv", index=False, sep=";")
    return df
print(pregunta_01())

print(pregunta_01().sexo.value_counts().to_list())