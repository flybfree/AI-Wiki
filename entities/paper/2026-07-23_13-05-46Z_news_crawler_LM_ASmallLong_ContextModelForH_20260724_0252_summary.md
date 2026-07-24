# Summary: 2026-07-23_13-05-46Z_news_crawler_LM_ASmallLong_ContextModelForHigh_Qua.md
Saved: 2026-07-24 02:52
Source: 2026-07-23_13-05-46Z_news_crawler_LM_ASmallLong_ContextModelForHigh_Qua.md
Model: None

---

## Summary  
The paper proposes **news-crawler‑LM**, a compact long‑context language model that automatically extracts structured information from raw HTML news pages into plaintext and JSON without requiring handcrafted parsing rules. By fine‑tuning on human‑validated extractions from the Fundus library, the authors demonstrate that their model can generate high‑quality Markdown and JSON outputs while remaining lightweight enough for practical deployment. The work bridges the gap between rule‑based crawlers, which are brittle to new publishers, and large language models, which are computationally expensive, by offering a small yet effective alternative.  

## Key Contributions  
- [Finding 1] news-crawler‑LM achieves +4.8 BLEU and +6.1 METEOR gains over strong baselines in the HTML‑to‑Markdown extraction task compared to rule‑based parsers.  
- [Finding 2] it improves HTML‑to‑JSON performance by +2.2 BLEU and +4.1 METEOR, producing structured JSON fields such as headline, author, publication date, and article body.  
- [Finding 3] despite modest gains on plaintext extraction, the model remains competitive with rule‑based libraries on unseen publishers, highlighting its limited need for site‑specific configuration.  

## Methodology  
The authors construct a dataset of high‑quality extractions from the Fundus news‑crawling library, where each HTML page is paired with human‑validated plaintext and JSON representations. They then fine‑tune a small transformer‑based language model on this dataset, training it to map raw HTML tokens directly to the target plaintext or JSON schema. The model is evaluated on three downstream tasks: converting HTML into Markdown, converting HTML into JSON, and extracting plaintext only.  

## Results  
Experimental results show that news-crawler‑LM outperforms both strong rule‑based parsers and larger language models in relative terms, delivering the BLEU and METEOR improvements listed above. On unseen publishers, its plaintext extraction is comparable to existing rule‑based tools, indicating limited degradation when new sites are introduced. The model’s inference time is measured as under 200 ms per page on a single GPU, confirming its practicality for real‑time crawling pipelines.  

## Significance  
By delivering a lightweight yet high‑performing extraction pipeline, news-crawler‑LM enables automated news aggregation services to process diverse publishers without costly manual rule engineering or massive compute resources. This reduces the operational burden of scaling crawlers and improves data quality, which is crucial for downstream analytics and knowledge‑graph construction. The open release of models and artifacts fosters reproducibility and encourages community adoption.  

## Related Concepts  
- Long‑context language modeling  
- HTML parsing with LLMs  
- Rule‑based web crawling  
- BLEU and METEOR evaluation metrics  
- Fine‑tuning on structured datasets
