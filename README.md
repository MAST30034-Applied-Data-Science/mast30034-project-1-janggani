# MAST30034 Project 1 README.md
- Name: Jane Vieren Anggani
- Student ID: 1148126


**Research Goal:** My research goal is Effects of Weather on Taxi Consumer Behavior

**Timeline:** The timeline for the research area is January 1 - June 30 2019.

To run the pipeline, please visit the `scripts` directory and run the files in order:
1. `download.py`: This downloads the raw data into the `data/raw` directory.
2. `Preprocess (Taxi).ipynb`: This notebook details all preprocessing steps for taxi and outputs it to the `data/curated` directory.
3. `Preprocess (Weather).ipynb`: This notebook details all preprocessing steps for the weather data and outputs it to the `data/curated` directory.
4. `Preprocess (Both).ipynb`: This notebook details all preprocessing steps for merging both datas and outputs it to the `data/curated` directory.
5. `Visualization.ipynb and Geospatial visualization.ipynb`: This notebook details all visualizations required in the report and is outputed to the `plots` directory
6. `Linear Regression Model.ipynb`: This notebook is used to conduct linear regression on the curated data.
7. `Poisson Regression Model.ipynb`: This notebook is used to conduct poisson regression on the curated data.
