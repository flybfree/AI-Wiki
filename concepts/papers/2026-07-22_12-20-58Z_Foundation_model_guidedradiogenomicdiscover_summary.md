# Summary: 2026-07-22_12-20-58Z_Foundation_model_guidedradiogenomicdiscoverylinkin.md
Saved: 2026-07-24 01:49
Source: 2026-07-22_12-20-58Z_Foundation_model_guidedradiogenomicdiscoverylinkin.md
Model: None

---

## Summary  
The paper proposes a foundation‑model‑guided approach to discover gene–phenotype associations between cancer genomes and routine clinical scans without task‑specific training. By leveraging the Evo~2 language model, it predicts per‑gene severity scores from somatic mutations across TCGA cohorts and then correlates these scores with radiomic features extracted from tumor segmentations. The method uncovers both known drivers and novel genes linked to imaging phenotypes that conventional driver discovery misses. This work demonstrates a hypothesis‑free, genome‑wide discovery pipeline that integrates genomics and radiomics.

## Key Contributions  
- [Finding 1] Identification of 46 additional genes with FDR‑significant gene–imaging associations in TCGA clear‑cell renal cell carcinoma beyond curated cancer‑gene panels.  
- [Finding 2] Detection of Mendelian ciliopathy and cytoskeletal disease genes among the novel associations, highlighting rare genetic pathways.  
- [Finding 3] Demonstration that a foundation model can predict per‑gene severity scores from mutation data alone, enabling hypothesis‑free genome‑wide discovery.

## Methodology  
The authors paired Evo~2‑based genome analysis with routine clinical imaging. For each somatic mutation across three TCGA cohorts (cRCC, HCC, BC; n=340), the model generated a per‑gene severity score without task‑specific training. These scores were aggregated per gene and normalized to control for total mutation burden. Radiomic features extracted from paired tumor segmentations were then correlated with these severity summaries using statistical models that accounted for confounding variables.

## Results  
In TCGA cRCC (n=162), the sweep recovered 46 genes at FDR‑significance, including previously unrecognized drivers and disease‑associated genes. The novel gene set comprised Mendelian ciliopathy genes such as TMEM67 and cytoskeletal genes like KIF20A, suggesting links to imaging phenotypes not captured by mutation frequency alone.

## Significance  
This approach expands the catalog of cancer‑imaging associations beyond conventional driver discovery, offering a scalable hypothesis‑free tool that can be applied across tumor types. By integrating foundation models with radiomics, it bridges gaps in functional gene understanding and may guide personalized therapeutic strategies.

## Related Concepts  
Foundation models, Evo~2, radiomics, TCGA, somatic mutation analysis, per‑gene severity scoring, false discovery rate (FDR), radiogenomics, genomics‑imaging integration.
