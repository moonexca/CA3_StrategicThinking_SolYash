# Stimulating Ireland's Innovation Ecosystem

Academic analytics project by **Soledad Yash** examining Ireland's innovation ecosystem through public datasets on R&D expenditure, enterprise innovation behaviour, and intellectual property activity.

## Overview

This repository contains a historical academic project developed around public data from Ireland's **Central Statistics Office (CSO)**. The analysis explores how different signals of innovation activity can be prepared, aligned, and interpreted through a data-driven lens.

The project focuses on:

- R&D expenditure patterns
- enterprise distribution across expenditure bands
- innovation and intellectual property signals
- the structural role of ownership and investment concentration
- cautious use of machine learning on a small and fragmented public-data sample

## Research Framing

The notebook does not assume that the three input datasets form a ready-made unified database. Instead, it treats them as partially overlapping views of a broader innovation system and asks how far they can be aligned without introducing artificial structure.

The project is especially relevant to questions such as:

- how innovation investment is distributed across firms
- whether ownership patterns shape the concentration of R&D effort
- how public data can be cleaned and merged conservatively
- what machine learning can reveal in a structurally limited analytical setting

## Methods

The workflow includes:

- dataset-by-dataset inspection
- schema and naming harmonisation
- conservative cleaning and merge logic
- categorical encoding
- statistical imputation rationale and implementation
- engineered indicators for R&D intensity and enterprise structure
- descriptive visualisation
- model comparison using:
  - linear regression
  - decision tree regression
  - random forest regression

The modelling is presented as exploratory rather than definitive, due to the scale and structure of the data.

## Repository Contents

- [Adriana_Soledad_Yash_Ecosystem_of_Innovation_Ireland.ipynb](./Adriana_Soledad_Yash_Ecosystem_of_Innovation_Ireland.ipynb): main notebook
- [CA3_AdrianaSoledadYash_InnovationEcosystem_Report.odt](./CA3_AdrianaSoledadYash_InnovationEcosystem_Report.odt): written report
- [Ireland innovation poster.mp4](./Ireland%20innovation%20poster.mp4): presentation video/poster asset
- `BSA02.20250516T100541.csv`, `BSA22.20250516T200531.csv`, `CIS62.20250516213458.csv`: source datasets
- `df1_imputed.csv`, `df2_imputed.csv`, `df3_imputed.csv`: intermediate imputed outputs

## Environment

The notebook uses Python packages including:

- `pandas`
- `numpy`
- `matplotlib`
- `seaborn`
- `scikit-learn`

See [requirements.txt](./requirements.txt) for a compact environment list.

## Reproducibility Notes

- This repository is published as a **historical academic project**.
- It has been cleaned for portfolio use, but it does not attempt to reconstruct a full production pipeline.
- The notebook preserves the assignment-era workflow and should be read in that context.
- The analytical conclusions should be interpreted with the limitations of small, partially aligned public datasets in mind.

## Academic and IP Statement

This repository contains academic work authored by **Soledad Yash** and is published for portfolio and research-communication purposes.

- The analysis, structuring, and interpretation are presented as the author's academic work.
- Public data sources remain subject to their original usage conditions.
- The academic context is acknowledged for transparency only and does not imply institutional endorsement.

See [ACADEMIC_USE_AND_IP.md](./ACADEMIC_USE_AND_IP.md) for the extended statement.

## AI Use Disclosure

AI-assisted support may have been used in limited surrounding tasks such as drafting, wording refinement, or structural editing support. Final responsibility for validation, interpretation, and publication remains with **Soledad Yash**.

See [AI_USE_DISCLOSURE.md](./AI_USE_DISCLOSURE.md) for a fuller note on limitations, responsible use, and security awareness.

## Portfolio Relevance

This project supports a portfolio narrative around:

- data analytics
- public-sector and economic analysis
- innovation ecosystems
- business and policy interpretation
- cautious machine learning on imperfect datasets

## Author

**Soledad Yash**  
Dublin, Ireland  
[LinkedIn](https://www.linkedin.com/in/soledad-yash)  
[GitHub](https://github.com/asolyash)
