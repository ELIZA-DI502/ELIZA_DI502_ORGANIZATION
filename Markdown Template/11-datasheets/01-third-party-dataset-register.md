# Third-party Dataset Register

This register is where you will keep track of all third party datasets if they are to be used as-is.

When naming the dataset please include a full name and a link to the main page.

Specify what purpose each dataset will satisfy, who accessed this dataset, and when.

Finally mention the associated experiment and the result, whether the dataset passed quality checks, or performed well in conjunction with existing models.

| Dataset Name | Purpose | Accesser | Date of Access | License | Experiment and Results |
|---|---|---|---|---|---|
| [EUR-Lex: Regulation (EU) 2024/1689 (Artificial Intelligence Act), consolidated text of 27/07/2026, English (CELEX 02024R1689-20260727)](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:02024R1689-20260727) | The single source of the retrieval corpus; processed into 105 chunks, see the [Dataset Report](02-dataset-report.md) | Yeşim (PDF), Gözde (HTML) | 26/10/2026 (PDF), 05/11/2026 (HTML) | CC BY 4.0 for the EUR-Lex consolidated text (© European Union); acknowledge the source and indicate changes | Hashes match `data/manifest.csv`; 19 of 20 sampled chunks matched the stored PDF after normalisation; ART113-1 differed only by a space before the final full stop (KAN-94); used in E1: Recall@8 0.59 on `val` |
