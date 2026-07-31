# Summary: 2026-07-30_12-15-41Z_BeyondRephrasing_Book_LevelOrganizationImprovesSyn.md
Saved: 2026-07-30 21:49
Source: 2026-07-30_12-15-41Z_BeyondRephrasing_Book_LevelOrganizationImprovesSyn.md
Model: None

---

## Summary  
The paper investigates whether the organization of synthetic textbook data into coherent book‑level documents can boost language model pre‑training beyond simple rephrasing or local rewriting. It proposes a scalable pipeline that clusters source material, creates hierarchical tables of contents, and assembles sections into full textbooks, producing 686 K books (32 B tokens) across many disciplines. By replacing natural books in a mid‑training mix with this corpus, the authors demonstrate an average performance gain of +1.09 on downstream tasks. The contribution is both the pipeline itself and empirical evidence that book‑level organization matters.

## Key Contributions  
- Finding 1: Book‑level organization yields a consistent +1.02 improvement over a content‑matched Split condition, isolating document packaging as a key factor.  
- Finding 2: A retrieval‑pool‑matched Rephrase condition shows an even larger gain (+1.17) when individual documents are rephrased without clustering or TOC planning, highlighting that structured synthesis adds value beyond simple rewriting.  
- Finding 3: The full pipeline generates 686 K textbooks (≈32 B tokens), providing a large, discipline‑spanning synthetic corpus for mid‑training use.

## Methodology  
The authors built a two‑stage process: first, they retrieve relevant passages from a pre‑training corpus using a topic‑aware pooling strategy; second, they cluster these passages into topical units, generate hierarchical tables of contents, and then stitch the units together into complete books. The pipeline is fully automated and scalable to millions of documents, ensuring that each book contains logically related content while preserving source grounding.

## Results  
The synthetic corpus improves downstream performance on Llama3‑8B by an average +1.09 relative to a RandomConcat baseline (which merely concatenates sections from unrelated books). The Full condition’s gain (+1.02) is attributed specifically to document packaging, while the Split condition’s smaller gain (+0.57) reflects only content matching without organization. These results confirm that book‑level structure matters and can be reliably measured.

## Significance  
Demonstrating that organized synthetic textbooks outperform random concatenation or simple rephrasing provides a practical design principle for mid‑training data generation. It encourages researchers to consider document architecture when augmenting pre‑training corpora, potentially leading to more coherent learning signals and better model performance without massive additional data.

## Related Concepts  
- Synthetic textbook data  
- Book‑level organization  
- Hierarchical tables of contents (TOC)  
- Retrieval pooling  
- Document packaging vs. content matching  
- Rephrasing vs. structured synthesis
