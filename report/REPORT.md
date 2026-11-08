# News position classification

## Question and data

I tested how well article text predicts the **left**, **center**, or **right** position in an [AllSides-based news dataset](https://www.kaggle.com/datasets/articoder/news-dataset-for-news-bias-analysis). The local JSON-lines file holds 8,478 roundup records. Each record can contain up to three article versions. The modeling notebook reshapes those fields into **24,523 article rows**, with a title, text, topic, date, source, and position label for each row. The articles span **July 2012 to February 2025** and cover **126 topics** and **414 extracted source names**. There are **7,706 center**, **8,436 left**, and **8,381 right** articles. Politics and elections are the two most common topics, so topic coverage is less even than the position labels. These are labels supplied by the dataset; I did not independently assess the political position of each article.

## Preparation and model

I joined the title, article text, and topic into one input field. The basic cleaning step lowercases text and collapses extra spaces. For the second run, extended cleaning also removes punctuation and stop words and lemmatizes words. I applied each version consistently to the training and test text.

I sorted articles by date and reserved the newest **4,905 articles (20%)** for the final test. The older **19,618 articles (80%)** formed the training and validation set. Within that older set, I used five stratified folds for validation. For each fold, I fitted TF-IDF and truncated SVD on the fold's training text, then transformed its validation text. The SVD step reduced the text matrix to **768 latent semantic features**. A feed-forward neural network with hidden layers of 128, 64, and 32 units predicted the three labels. The network uses ReLU hidden activations and 0.5 dropout after its first two layers. Training used batches of 16, cross-entropy loss, Adam, and 30 epochs per fold or final run.

## Results

Five-fold validation accuracy was **0.3593, 0.3652, 0.3565, 0.3581, and 0.3663**, for a mean of **0.3611**. The final test results below come from the saved notebook output. Precision is the share of predictions for a class that were correct; recall is the share of articles in that class that the model found. F1 combines the two.

### Basic cleaning

| Class | Precision | Recall | F1 | Support |
| --- | ---: | ---: | ---: | ---: |
| Center | 0.41 | 0.34 | 0.37 | 1,566 |
| Left | 0.42 | 0.48 | 0.45 | 1,671 |
| Right | 0.46 | 0.46 | 0.46 | 1,668 |
| **Macro average** | **0.43** | **0.43** | **0.43** | **4,905** |
| **Weighted average** | **0.43** | **0.43** | **0.43** | **4,905** |

**Accuracy: 0.43** across 4,905 test articles.

### Extended cleaning

| Class | Precision | Recall | F1 | Support |
| --- | ---: | ---: | ---: | ---: |
| Center | 0.38 | 0.25 | 0.30 | 1,566 |
| Left | 0.39 | 0.48 | 0.43 | 1,671 |
| Right | 0.42 | 0.45 | 0.43 | 1,668 |
| **Macro average** | **0.39** | **0.39** | **0.39** | **4,905** |
| **Weighted average** | **0.40** | **0.40** | **0.39** | **4,905** |

**Accuracy: 0.40** across 4,905 test articles.

Basic cleaning gave the stronger result in this run. Center was the hardest class to recover: its recall fell from **0.34** to **0.25** with extended cleaning. The notebook also plots one-versus-rest ROC curves and shows sample predictions, but it does not print AUC values, so I do not report AUC scores here.

## Interpretation and limits

The test scores are modest, so this is an exploratory classifier rather than a reliable bias detector. The five validation folds are stratified samples of the older period, while the final test consists of later articles; their accuracies should be compared with that difference in mind. The input includes topic words, and articles from the same sources may appear across periods. I cannot separate those cues from political framing with this experiment alone. The numbers above are from the saved notebook run; I did not rerun the full training pipeline while editing this report.
