# Stimulating Ireland's Innovation Ecosystem

Innovation is often described in broad and triumphant language. Nations speak of ecosystems, strategy, talent, competitiveness, resilience. But once the slogans are set aside, the harder question remains: where is innovation actually concentrated, who carries it, and what kind of structure does it leave behind? This project begins there, in the space between public language and measurable pattern.

This repository contains an academic analytics project by **Soledad Yash** built around public data from Ireland's **Central Statistics Office (CSO)**. It examines research and development expenditure, enterprise behaviour, and intellectual property activity in order to read Ireland's innovation ecosystem with greater precision and less mythology.

## What this project does

The notebook does not assume that the available datasets form a clean, unified picture. They do not. Instead, it treats them as partial views of the same landscape and asks how far they can be aligned without forcing false coherence.

The workflow includes:

- dataset-by-dataset inspection
- schema and naming harmonisation
- conservative cleaning and merge logic
- categorical encoding
- statistical imputation with explicit rationale
- engineered indicators for R&D intensity and enterprise structure
- descriptive visualisation
- exploratory modelling

The models are not presented as instruments of certainty. They are used to test whether the structure of the sample carries enough internal consistency to support cautious interpretation.

## Main analytical components

- public-sector data integration
- exploratory analytics
- imputation strategy
- feature engineering
- structural interpretation of ownership and expenditure patterns
- model comparison using:
  - linear regression
  - decision tree regression
  - random forest regression

## Repository contents

- [Adriana_Soledad_Yash_Ecosystem_of_Innovation_Ireland.ipynb](./Adriana_Soledad_Yash_Ecosystem_of_Innovation_Ireland.ipynb): main notebook
- [CA3_AdrianaSoledadYash_InnovationEcosystem_Report.odt](./CA3_AdrianaSoledadYash_InnovationEcosystem_Report.odt): written report
- [Ireland innovation poster.mp4](./Ireland%20innovation%20poster.mp4): presentation asset
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

## Why it matters

This project sits close to questions that matter to me:

- how institutions describe themselves
- how investment is concentrated or dispersed
- how public data can be read without pretending it says more than it does
- how analytics can sharpen interpretation in policy and strategic contexts

## Reproducibility notes

- This repository is published as a **historical academic project**.
- It has been cleaned for portfolio use, but it does not attempt to reconstruct a production pipeline.
- The notebook preserves the assignment-era workflow and its limitations.

## Academic and IP statement

This repository contains academic work authored by **Soledad Yash** and is published for portfolio and research communication.

- The analysis, structuring, and interpretation are presented as the author's academic work.
- Public data sources remain subject to their original usage conditions.
- The academic context is acknowledged for transparency only and does not imply institutional endorsement.

See [ACADEMIC_USE_AND_IP.md](./ACADEMIC_USE_AND_IP.md) for the extended statement.

## AI use disclosure

AI-assisted support may have been used in limited surrounding tasks such as drafting, wording refinement, or structural editing support. Final responsibility for validation, interpretation, and publication remains with **Soledad Yash**.

See [AI_USE_DISCLOSURE.md](./AI_USE_DISCLOSURE.md) for a fuller note on limitations, responsible use, and security awareness.

## Author

**Soledad Yash**  
Dublin, Ireland  
[LinkedIn](https://www.linkedin.com/in/soledad-yash)  
[GitHub](https://github.com/moonexca)
