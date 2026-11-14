# Dataset Report

This template is created according to Gebru, Timnit, et al. "Datasheets for datasets." Communications of the ACM 64.12 (2021): 86-92. You can visit the paper here or read it on ODTUClass:

Datasheets for Datasets

| Date Updated: | 14/11/2026 |
|---|---|
| Last Updated by: | Aliye Yeşim Yaman |
| Team Name: | ELIZA |
| Team Members: | Aliye Yeşim Yaman, Yaren Gürsoy, Kaan Kocatürk, Gözde Nur Özdemir |
| Dataset Name: | ELIZA retrieval corpus v1: in-scope provisions of the EU AI Act (Regulation (EU) 2024/1689), consolidated text of 27/07/2026 (`data/chunks.jsonl`) |

- Motivation
- Composition
- Collection Process
- Uses
- Distribution
- Maintenance

## Motivation

The following questions are primarily intended to encourage dataset creators to clearly articulate their reasons for creating the dataset and to promote transparency about funding interests. The latter may be particularly relevant for datasets created for research purposes.

| # | Question | Answer |
|---|---|---|
| 1 | For what purpose was the dataset created? Was there a specific task in mind? Was there a specific gap that needed to be filled? | It is the retrieval set of ELIZA: the chunks that the retriever searches and that answers cite when EdTech developers ask about the EU AI Act. The task is retrieval-augmented question answering with a provision reference and the version date. The gap: the official text is one long document, and answers must point to the exact provision and the consolidated source version used by ELIZA (27/07/2026, which includes Regulation (EU) 2026/1744). |
| 2 | Who created the dataset (for example, which team, research group) and on behalf of which entity (for example, company, institution, organization)? | Team ELIZA, as the term project of METU DI502. The text itself is written by the EU legislator and published by the Publications Office of the EU on EUR-Lex; the team selected, split and annotated it. |
| 3 | Who funded the creation of the dataset? If there is an associated grant, please provide the name of the grantor and the grant name and number. | No funding; it is a course project. |
| 4 | Any other comments? | - |

## Composition

Dataset creators should read through these questions prior to any data collection and then provide answers once data collection is complete. Most of the questions here are intended to provide dataset consumers with the information they need to make informed decisions about using the dataset for their chosen tasks. Some of the questions are designed to elicit information about compliance with the EU's General Data Protection Regulation (GDPR) or comparable regulations in other jurisdictions.

| # | Question | Answer |
|---|---|---|
| 1 | What do the instances that comprise the dataset represent (for example, documents, photos, people, and countries)? Are there multiple types of instances (for example, movies, users, and ratings; people and interactions between them; nodes and edges)? Please provide a description. | Each instance is a chunk of legal text: one Article paragraph (or point) or one Annex point of the AI Act. There are two kinds: `article` and `annex`. |
| 2 | How many instances are there in total (of each type, if appropriate)? | 105 chunks from 103 provisions: 101 from Articles and 4 from Annex III, point 3. Two provisions (Article 4a(1) and Article 13(3)) are longer than 1,500 characters and are split into two chunks each. By priority: 69 core, 28 supporting, 2 boundary, 6 if-time. Length: 7 to 224 words (median 42), 6,155 words in total. |
| 3 | Does the dataset contain all possible instances or is it a sample (not necessarily random) of instances from a larger set? If the dataset is a sample, then what is the larger set? Is the sample representative of the larger set (for example, geographic coverage)? If so, please describe how this representativeness was validated/verified. If it is not representative of the larger set, please describe why not (for example, to cover a more diverse range of instances, because instances were withheld or unavailable | It is a deliberate selection, not a random sample. The larger set is the whole consolidated text: 119 Articles and 12 Annexes, 1,377 units, of which 174 belong to the in-scope Articles and Annex points. The 103 provisions come from the provision list (D3, [`data/provision-list.csv`](../../data/provision-list.csv)): the education use cases, high-risk classification, requirements, provider obligations, application dates, and the scope and definitions they rely on. It is not representative of the whole Act on purpose: the project only answers education-related questions (Scope Definition). |
| 4 | What data does each instance consist of? "Raw" data (for example, unprocessed text or images) or features? In either case, please provide a description. | The text of the provision (`text`), extracted from the HTML of the consolidated text with its wording unchanged, plus metadata: `chunk_id`, `ref` (as cited in answers), `parent`, `kind`, `number`, `title`, `chapter`, `priority`, `area`, `amended_by`, `version_date`, `celex`, `language`, `source`, `heading`, `intro` (the lead-in sentence of the paragraph, for 41 chunks), `embed_text` (heading, lead-in and text, the input of the embedding model), `order`, `units`, `prev_id`, `next_id` and `words`. `data/chunks.csv` holds the same 105 chunks without `heading`, `intro`, `embed_text` and `order`, and adds `part` (`1/2`, `2/2` for the parts of a split provision). The fields are described in [`docs/eval/preprocessing.md`](../../docs/eval/preprocessing.md). |
| 5 | Is there a label or target associated with each instance? If so, please provide a description. | No. The targets are in the Q&A set: each question names its gold chunks in `gold_ids` (see the [Q&A Data Report](03-qa-data-report.md)). `priority` and `area` are scope tags, not labels. |
| 6 | Is any information missing from individual instances? If so, please provide a description, explaining why this information is missing (for example, because it was unavailable). This does not include intentionally removed information, but might include, for example, redacted text. | No required identifier or version date is missing: every chunk has an ID and a version date (0 missing, 0 duplicates). Some metadata fields are empty on purpose where they do not apply: `amended_by` where the 2026 amendment did not change the provision, and `intro` where the paragraph has no lead-in sentence. Article 10(5) is deleted in this version (▼M1), so it is not in the corpus. |
| 7 | Are relationships between individual instances made explicit (for example, users' movie ratings, and social network links)? If so, please describe how these relationships are made explicit. | Yes: `parent` gives the paragraph a chunk belongs to (for example, the points of one paragraph, or the two parts `#1` and `#2` of a split provision, share a parent), `prev_id` and `next_id` give the chunks before and after it in the same Article, and `order` the position in the law. Cross-references inside the legal text (for example, "referred to in Article 6(2)") are left as text and are not linked. |
| 8 | Are there recommended data splits (for example, training, development/validation, testing)? If so, please describe these splits, explaining the rationale behind them. | No. The corpus is not split; the val/test split is on the questions (Q&A set), and both splits search the same 105 chunks. |
| 9 | Are there any errors, sources of noise, or redundancies in the dataset? If so, please provide a description. | In the check of 20 random chunks against the stored PDF after normalisation (seed 42, KAN-94), 19 matched; Article 113, first paragraph (ART113-1), has an extra space before the final full stop, caused by an italic tag in the HTML. No word, number or reference differs; no chunk was corrected by hand. Removing the space in the parsing code is planned for the next re-index (KAN-93). The consolidated text is a documentation tool with no legal effect; only the Official Journal texts are authentic. |
| 10 | Is the dataset self-contained, or does it link to or otherwise rely on external resources (for example, websites, tweets, and other datasets)? If it links to or relies on external resources, a) are there guarantees that they will exist, and remain constant, over time; b) are there official archival versions of the complete dataset (that is, including the external resources as they existed at the time the dataset was created); c) are there any restrictions (for example, licenses, fees) associated with any of the external resources that might apply to a dataset consumer? Please provide descriptions of all external resources and any restrictions associated with them, as well as links or other access points, as appropriate. | It is built from the consolidated text on EUR-Lex (CELEX [02024R1689-20260727](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:02024R1689-20260727)): a) EUR-Lex keeps every consolidated version under its own CELEX number; on 04/11/2026 this was still the latest version (KAN-157). b) The HTML (parsing input) and PDF (fallback) are stored in `data/` with their SHA-256 hashes in [`data/manifest.csv`](../../data/manifest.csv). c) The consolidated texts on EUR-Lex are licensed under CC BY 4.0 (© European Union): reuse is allowed if the source is acknowledged and changes are indicated; the Commission's reuse policy is based on Decision 2011/833/EU. |
| 11 | Does the dataset contain data that might be considered confidential (for example, data that is protected by legal privilege or by doctor-patient confidentiality, data that includes the content of individuals' non-public communications)? If so, please provide a description. | No. It is published legislation. |
| 12 | Does the dataset contain data that, if viewed directly, might be offensive, insulting, threatening, or might otherwise cause anxiety? If so, please describe why. | No. |

If the dataset does not relate to people, you may skip the remaining questions in this section.

The dataset does not relate to people, so these questions are skipped.

## Collection Process

As with the questions in the previous section, dataset creators should read through these questions prior to any data collection to flag potential issues and then provide answers once the collection is complete. In addition to the goals outlined earlier, the following questions are designed to elicit information that may help researchers and practitioners to create alternative datasets with similar characteristics. Again, questions that apply only to datasets that relate to people are grouped at the end of the section.

| # | Question | Answer |
|---|---|---|
| 1 | How was the data associated with each instance acquired? Was the data directly observable (for example,raw text, movie ratings),reported by subjects (for example, survey responses), or indirectly inferred/derived from other data (for example, part-of-speech tags, model-based guesses for age or language)? If the data was reported by subjects or indirectly inferred/derived from other data, was the data validated/verified? If so, please describe how. | Directly observable raw text, downloaded from EUR-Lex. The metadata is derived from the structure of the text (Article and paragraph numbers, ▼M1 markers) and from the provision list. Checks: the file hashes match the manifest; every chunk has an ID and a version date; 20 random chunks were compared word for word with the stored PDF (19 of 20 match after normalisation, see Composition 9). |
| 2 | What mechanisms or procedures were used to collect the data (for example, hardware apparatuses or sensors, manual human curation, software programs, and software APIs)? How were these mechanisms or procedures validated? | Manual download of the PDF and HTML from EUR-Lex, then a parsing and chunking script ([`src/chunking.ipynb`](../../src/chunking.ipynb)); the provisions were selected by hand in the provision list (D3). Validated with the checks in Collection 1 and in [`docs/eval/preprocessing.md`](../../docs/eval/preprocessing.md). |
| 3 | If the dataset is a sample from a larger set, what was the sampling strategy (for example, deterministic, probabilistic with specific sampling probabilities)? | Deterministic: every provision in the provision list, chosen by the scope and the D2 questions (see Composition 3). |
| 4 | Who was involved in the data collection process (for example, students, crowd workers, contractors) and how were they compensated (for example, how much were crowd workers paid)? | The four team members (students); no payment. |
| 5 | Over what timeframe was the data collected? Does this timeframe match the creation timeframe of the data associated with the instances (for example, recent crawl of old news articles)? If not, please describe the timeframe in which the data associated with the instances was created. | The PDF was stored on 26/10/2026 and the HTML on 05/11/2026; the chunks were built in November 2026 (Sprint 2). The text is the consolidated version of 27/07/2026; the Regulation is from 2024, amended by Regulation (EU) 2026/1744 of 8 July 2026. |
| 6 | Were any ethical review processes conducted (for example, by an institutional review board)? If so, please describe these review processes, including the outcomes, as well as a link or other access point to any supporting documentation. | No; the data is public legislation and contains no personal data. |

If the dataset does not relate to people, you may skip the remaining questions in this section.

The dataset does not relate to people, so these questions are skipped.

## Preprocessing/ Cleaning/ Labeling

Dataset creators should read through these questions prior to any preprocessing, cleaning, or labeling and then provide answers once these tasks are complete. The questions in this section are intended to provide dataset consumers with the information they need to determine whether the "raw" data has been processed in ways that are compatible with their chosen tasks. For example, text that has been converted into a "bag of words" is not suitable for tasks involving word order.

| Question | Answer |
|---|---|
| Was any preprocessing/cleaning/labeling of the data done (for example, discretization or bucketing, tokenization, part-of-speech tagging, SIFT feature extraction,removal of instances, processing of missing values)? If so, please provide a description. If not, you may skip the remaining questions in this section. | Yes. The HTML was parsed into Articles, paragraphs and Annex points; out-of-scope units were left out; one chunk was made per provision, provisions longer than 1,500 characters were split at point boundaries (D7); the metadata was added. Word order and wording are unchanged. Full report: [`docs/eval/preprocessing.md`](../../docs/eval/preprocessing.md) (KAN-95). |
| Was the "raw" data saved in addition to the preprocessed/cleaned/labeled data (for example, to support unanticipated future uses)? If so, please provide a link or other access point to the "raw" data. | Yes: [`data/CELEX_02024R1689-20260727_EN.html`](../../data/CELEX_02024R1689-20260727_EN.html) and [`data/CELEX_02024R1689-20260727_EN.pdf`](../../data/CELEX_02024R1689-20260727_EN.pdf). |
| Is the software that was used to preprocess/clean/label the data available? If so, please provide a link or other access point. | Yes: [`src/chunking.ipynb`](../../src/chunking.ipynb). |
| Any other comments? | - |

## Uses

The following questions are intended to encourage dataset creators to reflect on the tasks for which the dataset should and should not be used. By explicitly highlighting these tasks, dataset creators can help dataset consumers to make informed decisions, thereby avoiding potential risks or harms.

| Question | Answer |
|---|---|
| Has the dataset been used for any tasks already? If so, please provide a description. | Yes: in the baseline experiment E1 ([E1 card](../12-experiment-cards/E1-baseline.md)) with hybrid retrieval (bge-m3 and BM25) on the 30 `val` questions: Recall@8 0.59 and Recall@5 0.43 on the 27 questions with `gold_ids` (W&B run `v7g5hhxh`); the retrieved chunks were given to Llama-3.1-8B-Instruct to answer the questions. |
| Is there a repository that links to any or all papers or systems that use the dataset? If so, please provide a link or other access point. | The team repository: [ELIZA-DI502/ELIZA_DI502_ORGANIZATION](https://github.com/ELIZA-DI502/ELIZA_DI502_ORGANIZATION). |
| What (other) tasks could the dataset be used for? | Testing other retrieval or chunking methods on the same provisions, and citation checks (does an answer cite a provision that exists in the corpus). |
| Is there anything about the composition of the dataset or the way it was collected and preprocessed/cleaned/labeled that might impact future uses? For example, is there anything that a dataset consumer might need to know to avoid uses that could result in unfair treatment of individuals or groups (for example, stereotyping, quality of service issues) or other risks or harms (for example, legal risks, financial harms)? If so, please provide a description. Is there anything a dataset consumer could do to mitigate these risks or harms? | It covers only the 103 listed provisions, in English, in the version of 27/07/2026. A question outside these provisions cannot be answered from it, and a later amendment can make a chunk out of date (risk R-02). To reduce this: check EUR-Lex for a newer consolidated version before use, and cite the version date with every answer. |
| Are there tasks for which the dataset should not be used? If so, please provide a description. | It should not be used as legal advice or as the authentic text of the law (only the Official Journal is authentic), or for questions on parts of the AI Act outside the provision list. |
| Any other comments? | - |

## Distribution

Dataset creators should provide answers to these questions before distributing the dataset either internally within the entity on behalf of which the dataset was created or externally to third parties.

| Question | Answer |
|---|---|
| Will the dataset be distributed to third parties outside of the entity (for example, a company, institution, or organization) on behalf of which the dataset was created? If so, please provide a description. | It is in the public team repository, so anyone can see it. |
| How will the dataset be distributed (for example, tarball on the website, API, GitHub)? Does the dataset have a digital object identifier (DOI)? | On GitHub, in [`data/`](../../data/). No DOI. |
| When will the dataset be distributed? | The chunk files have been in the team repository since 06/11/2026; this dataset report is prepared for the Sprint 2 submission on 14/11/2026. |
| Will the dataset be distributed under a copyright or other intellectual property (IP) license, and/or under applicable terms of use (ToU)? If so, please describe this license and/ or ToU, and provide a link or other access point to, or otherwise reproduce, any relevant licensing terms or ToU, as well as any fees associated with these restrictions. | The repository has no licence file. The text comes from EUR-Lex and is reused under CC BY 4.0 (see the next question). |
| Have any third parties imposed IP-based or other restrictions on the data associated with the instances? If so, please describe these restrictions, and provide a link or other access point to, or otherwise reproduce, any relevant licensing terms, as well as any fees associated with these restrictions. | EUR-Lex licenses its consolidated texts under the [Creative Commons Attribution 4.0 International licence](https://creativecommons.org/licenses/by/4.0/) (© European Union, https://eur-lex.europa.eu): the source must be acknowledged and changes indicated; the Commission's reuse policy is based on Decision 2011/833/EU ([EUR-Lex legal notice](https://eur-lex.europa.eu/content/legal-notice/legal-notice.html)). Changes made by ELIZA: provisions selected, split into chunks and given metadata; the wording is unchanged. No fees. |
| Do any export controls or other regulatory restrictions apply to the dataset or individual instances? If so, please describe these restrictions, and provide a link or other access point to, or otherwise reproduce, any supporting documentation. | No. |
| Any other comments? | - |

## Maintenance

As with the previous questions, dataset creators should provide answers to these questions before distributing the dataset. The questions in this section are intended to encourage dataset creators to plan for dataset maintenance and communicate this plan to dataset consumers.

| Question | Answer |
|---|---|
| Who will be supporting/hosting/maintaining the dataset? | Team ELIZA, on GitHub, until the end of the course (30/12/2026). |
| How can the owner/curator/manager of the dataset be contacted (for example, email address)? | Through the team members listed above, in the METU DI502 course. |
| Is there an erratum? If so, please provide a link or other access point. | No separate erratum. The known issue (the extra space in ART113-1) is recorded in [`docs/eval/preprocessing.md`](../../docs/eval/preprocessing.md). |
| Will the dataset be updated (for example, to correct labeling errors, add new instances, or delete instances)? If so, please describe how often, by whom, and how updates will be communicated to dataset consumers (for example, mailing list, GitHub). | EUR-Lex is checked for a newer consolidated version at the start of each sprint (Sprint 2: KAN-157; Sprint 3: KAN-187). A change of version needs Product Owner approval and an ADR; the chunks are then rebuilt and re-indexed. A provision within the scope is added when an evaluation question needs it (as Article 6(4) and Article 49(2) were on 05/11/2026). Changes are recorded in the Git history and in this report. |
| If the dataset relates to people, are there applicable limits on the retention of the data associated with the instances (for example, were the individuals in question told that their data would be retained for a fixed period and then deleted)? If so, please describe these limits and explain how they will be enforced. | Not applicable. |
| Will older versions of the dataset continue to be supported/hosted/maintained? If so, please describe how. If not, please describe how its obsolescence will be communicated to dataset consumers. | Older versions stay in the Git history; the version submitted for each sprint is tagged (for example, `sprint-1`). |
| If others want to extend/augment/build on/contribute to the dataset, is there a mechanism for them to do so? If so, please provide a description. Will these contributions be validated/verified? If so, please describe how. If not, why not? Is there a process for communicating/distributing these contributions to dataset consumers? If so, please provide a description. | Within the team, through changes to the repository; a change of version follows the update process above. No outside contributions are planned during the course. |
| Any other comments? | - |
