# Summary: 2026-07-22_12-20-58Z_Foundation_model_guidedradiogenomicdiscoverylinkin.md
Saved: 2026-07-24 01:49
Source: 2026-07-22_12-20-58Z_Foundation_model_guidedradiogenomicdiscoverylinkin.md
Model: None

---

## Summary  
This study proposes a foundation‑model‑guided approach to uncover gene–imaging associations that conventional driver‑discovery pipelines miss because they focus only on frequently mutated genes. By applying the Evo~2 language model to all somatic mutations across three TCGA cohorts (cRCC, HCC, BC) and correlating per‑gene severity scores with radiomic features extracted from paired tumor segmentations, the authors generate a genome‑wide list of candidate gene–phenotype links without any task‑specific training. The method uncovers both known drivers and novel genes, including Mendelian ciliopathy and cytoskeletal disease markers, that are invisible to traditional mutation‑frequency based analyses.

## Key Contributions  
- [Finding 1] A framework that pairs an unsupervised genomic language model with routine clinical imaging to discover gene–phenotype associations at genome scale.  
- [Finding 2] Identification of 46 additional genes (beyond curated panels) in cRCC that reach FDR‑significance, many encoding Mendelian ciliopathy and cytoskeletal disease proteins.  
- [Finding 3] Demonstration that the approach can be applied across three TCGA cancer types, showing broad applicability beyond a single organ.

## Methodology  
The authors first built an Evo~2 model to predict a per‑gene “severity score” from raw somatic mutation data in each of the three TCGA cohorts (cRCC = 162 tumors, HCC = 84, BC = 94). The severity scores are computed without any downstream classification task. Next, radiomic features—derived from tumor segmentations that are routinely performed on clinical scans—are extracted for each case and correlated with the per‑gene severity summaries while controlling for total mutation burden to avoid confounding. Statistical significance is assessed via FDR correction across all genes.

## Results  
In cRCC, the sweep recovered 12 known driver genes (e.g., KRAS, CDKN2A) plus 46 novel genes that met FDR <0.05. These novel genes encode proteins involved in ciliopathy pathways and cytoskeletal organization, suggesting functional links to tumor phenotype. Similar analyses in HCC and BC identified additional candidate genes, though the cRCC cohort provided the strongest signal due to higher mutation density. The method required only standard imaging segmentation and no additional annotation.

## Significance  
By leveraging a foundation model as a hypothesis‑free predictor, this work expands the repertoire of cancer‑gene candidates beyond those limited by mutation frequency, potentially revealing biologically relevant genes that could be targeted therapeutically or used for early detection. It also shows how widely available clinical imaging can contribute to radiogenomic discovery, reducing reliance on costly wet‑lab assays.

## Related Concepts  
- Foundation models (e.g., Evo~2)  
- Radiomics  
- TCGA (The Cancer Genome Atlas) cohorts  
- Somatic mutation burden control  
- False discovery rate (FDR) significance  
- Mendelian ciliopathy genes  
- Cytoskeletal disease proteins
