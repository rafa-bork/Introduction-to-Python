
import pandas as pd
import numpy

# import kagglehub

# Download latest version
# path = kagglehub.dataset_download("vikasukani/forest-firearea-datasets")

fires = pd.read_csv("/workspaces/180669319/misc/forestfires.csv")
fires.dtypes

fires[["month","day"]]

fires[(fires["temp"] > 20 & (fires["temp"] < 25))]

fires[fires["day"].isin(["sat","sun"])]

fires.notna().sum()

fires.loc[fires["month"].isin(["aug","set"]),["FFMC","DMC","DC","ISI"]]

fires.columns.get_indexer(["FFMC","DMC","DC","ISI"])                                            

fires.iloc[0:20]

fires.loc[fires.index[0:20], ["FFMC", "DMC", "DC", "ISI"]]

fires.index[0:20]

fires.loc[fires["temp"]>=30, "temp"] = 30
