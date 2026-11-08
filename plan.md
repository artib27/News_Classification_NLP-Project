# Plan for the news classification project

This is a plan only. It does not authorize changes to the notebooks, report, README, dataset, or code.

## 1. Review and preserve the project

- Inventory the current files and notebook cells before editing.
- Keep all existing notebook Markdown cells and code comments. Revise wording in place where needed; do not delete those cells or comments as a cleanup shortcut.
- Record the current limitations: earlier work cleared saved notebook outputs and shortened some Markdown. The original PDF and exact earlier notebook text are unavailable in this workspace, and work must proceed without a backup.

## 2. Clean the folder structure

- Use a simple layout for notebooks, helper scripts, report, and local data. Update paths and imports whenever a file moves.
- Remove contributor names, email addresses, and logos from presentation material, including filenames and notebook content. Keep source attribution and citations needed to explain the dataset.
- Keep generated files and the local dataset out of the GitHub repository. Link to the Kaggle source instead: https://www.kaggle.com/datasets/articoder/news-dataset-for-news-bias-analysis.

## 3. Edit the notebooks carefully

- Read every Markdown cell and code comment. Replace repetitive or generic explanations with concise statements tied to the actual code, figures, and results.
- Preserve the purpose of each Markdown cell and comment. Keep useful technical explanations and observations.
- Correct stale dataset paths and unsupported numerical claims. Clearly identify any result that comes from an earlier run and has not been rerun.

## 4. Finish the report and README

- Write a short Markdown report in one consistent first-person voice. Cover the aim, dataset, method, key results, and limitations. Check each figure against available evidence.
- Prepare a GitHub README with the project layout, setup, run order, Kaggle download link, expected local dataset path, results, and known limits. State that the dataset is not included in the repository.

## 5. Verify before publishing

- Validate notebook JSON and Python syntax, file paths, and links.
- Compare Markdown-cell and comment counts before and after editing to confirm they were preserved.
- Search public-facing files for remaining names, emails, logos, stale paths, and unsupported claims.
- Inspect the staged Git file list to confirm the dataset is absent. Do not upload or publish it as part of this work.
