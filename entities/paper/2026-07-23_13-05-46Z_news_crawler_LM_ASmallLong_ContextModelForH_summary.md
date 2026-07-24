# Summary: 2026-07-23_13-05-46Z_news_crawler_LM_ASmallLong_ContextModelForHigh_Qua.md
Saved: 2026-07-24 02:44
Source: 2026-07-23_13-05-46Z_news_crawler_LM_ASmallLong_ContextModelForHigh_Qua.md
Model: None

---

## Summary  
The paper introduces **news-crawler‑LM**, a compact long‑context language model designed to replace costly, rule‑heavy crawlers with a flexible yet efficient alternative for extracting structured information from HTML news pages. By fine‑tuning the model on a curated set of human‑validated extractions from the Fundus library, it can convert raw HTML into plaintext and JSON representations that include headline, author, publication date, and article body. The approach reduces the need for site‑specific handcrafted rules while keeping computational overhead low enough for practical deployment. Experiments demonstrate clear performance gains over strong baselines in both HTML‑to‑Markdown and HTML‑to‑JSON extraction tasks.

## Key Contributions  
- **Introduces news-crawler‑LM**, a small long‑context language model fine‑tuned on high‑quality, human‑validated extractions from the Fundus library.  
- **Achieves +4.8 BLEU and +6.1 METEOR** improvements over strong baselines for HTML‑to‑Markdown extraction, and **+2.2 BLEU and +4.1 METEOR** gains for HTML‑to‑JSON extraction.  
- **Shows only modest advantage** (small BLEU uplift) compared to rule‑based parsing libraries on the plaintext task, highlighting that the model’s strength lies in structured output rather than generic parsing.

## Methodology  
The authors adopt a fine‑tuning strategy: they train a lightweight LLM on the Fundus news‑crawling dataset, which consists of raw HTML pages paired with manually verified JSON and Markdown outputs. The training objective is to map the entire HTML document into the desired structured formats while minimizing token usage. Evaluation involves comparing the model’s performance against several strong baselines, including rule‑based parsers (e.g., BeautifulSoup, lxml) and other large language models that are typically too expensive for real‑time crawling.

## Results  
In the **HTML‑to‑Markdown** task, news-crawler‑LM outperforms all baselines by **+4.8 BLEU** and **+6.1 METEOR**, indicating substantial quality gains in generating readable markdown representations of articles. For the **HTML‑to‑JSON** task, the model improves BLEU by **+2.2** and METEOR by **+4.1**, delivering clean JSON structures with correct metadata fields. When compared to rule‑based parsers on a plaintext conversion benchmark (unseen publishers), the LLM’s advantage is modest, suggesting that for simple text extraction rules may still be preferable. Overall, the model consistently exceeds expectations while remaining computationally feasible.

## Significance  
This work provides a practical, low‑cost alternative to deploying massive language models for news aggregation, thereby lowering barriers to entry for automated content harvesting across diverse publishers. By delivering high‑quality structured outputs with modest performance improvements over handcrafted rules, it can be integrated into real‑time pipelines without prohibitive latency or expense.

## Related Concepts  
- Long‑context language models (LLMs)  
- HTML parsing and extraction  
- Rule‑based parsers vs. learned models  
- BLEU and METEOR evaluation metrics for text quality  
- Fine‑tuning on limited, human‑validated datasets  
- Structured output generation (JSON/Markdown)
