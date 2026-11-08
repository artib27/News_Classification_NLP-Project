# News position classification

I used article text to predict the left, center, and right labels in an AllSides-based news dataset. The project includes exploratory analysis and a TF-IDF and LSI model followed by a feed-forward neural network. In the recorded run, the best test accuracy was **43%**.

## Data

Download the [News Dataset for News Bias Analysis on Kaggle](https://www.kaggle.com/datasets/articoder/news-dataset-for-news-bias-analysis). Put the JSON-lines file at `data/news_article_dataset.json`. It should contain one JSON object per line. The dataset is not included in this repository.

## Files

- `notebooks/01_Webscrape_code.ipynb` — collection code. Its final cell needs intermediate pickle files that are not included here.
- `notebooks/02_Basic_EDA.ipynb` — reshaping, cleaning, and exploratory plots.
- `notebooks/03_NLP_Classification_Model.ipynb` — feature extraction, training, and evaluation.
- `utils.py` and `model_LSI_NN.py` — preprocessing and network code.
- `report/REPORT.md` — short report with results and limitations.

## Run

Use Python 3.10 or later. From the repository root:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
jupyter lab
```

Run the EDA notebook before the model notebook. Both notebooks locate the repository root and read the downloaded data; EDA files are written to `outputs/`. The model notebook downloads NLTK resources on first use and trains five validation folds plus two final models, so it may take time. The scraping notebook is not needed to run the analysis from the Kaggle data.

## Results and interpretation

Basic text cleanup reached **0.43 accuracy** and **0.43 macro F1** on the later test set. Extended normalization reached **0.40 accuracy** and **0.39 macro F1**. These are recorded notebook results, not a fresh rerun. The labels come from the dataset and do not establish an independent measure of political bias. See the [report](report/REPORT.md) for details.
