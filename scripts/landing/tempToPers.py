from datetime import datetime as dt
import shutil
import glob
import os

def tempToPers():
  # Moving from temporal to persistent and adding the timestamp
  cFiles = glob.glob("../data/landing/temporal/crimes/*.csv")
  for file in cFiles:
    month = os.path.basename(file).split("-")[0:2]
    month = "-".join(month)
    shutil.copy2(file, "../data/landing/persistent/crimes/crimes" + month + "-t-" + dt.now().strftime("%Y-%m-%d-%H_%M_%S") + ".csv")
    os.remove(file)


  # Moving from temporal to persistent and adding the timestamp
  cFiles = glob.glob("../data/landing/temporal/prices/*.csv")
  for file in cFiles:
    fileBase = os.path.basename(file).split(".")[0]
    shutil.copy2(file, "../data/landing/persistent/prices/" + fileBase + "-t-" + dt.now().strftime("%Y-%m-%d-%H_%M_%S") + ".csv")
    os.remove(file)