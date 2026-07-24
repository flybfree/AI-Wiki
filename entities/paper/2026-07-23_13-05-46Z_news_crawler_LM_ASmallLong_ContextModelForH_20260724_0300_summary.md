# Summary: 2026-07-23_13-05-46Z_news_crawler_LM_ASmallLong_ContextModelForHigh_Qua.md
Saved: 2026-07-24 03:00
Source: 2026-07-23_13-05-46Z_news_crawler_LM_ASmallLong_ContextModelForHigh_Qua.md
Model: None

---

## Summary  
The authors propose **news-crawler‑LM**, a compact long‑context language model designed to extract structured information from noisy HTML pages into plaintext and JSON formats. By fine‑tuning the model on high‑quality, human‑validated extractions from the Fundus news‑crawling library, they aim to replace costly rule‑based parsers while preserving good performance. The model converts raw HTML into markdown summaries and machine‑readable JSON records containing headline, author, date, and body text. Experiments show that it improves both extraction tasks over strong baselines, but its advantage over existing rule‑based tools is modest on plaintext conversion.

## Key Contributions  
- Finding 1: A small long‑context language model (news-crawler‑LM) can reliably convert HTML into structured JSON with human‑validated quality.  
- Finding 2: The model achieves substantial gains in extraction metrics, gaining +4.8 BLEU and +6.1 METEOR on HTML‑to‑Markdown and +2.2 BLEU and +4.1 METEOR on HTML‑to‑JSON compared to strong baselines.  
- Finding 3: Although the model is competitive with rule‑based parsers, its performance advantage over them remains limited, especially for unseen publishers.

## Methodology  
The authors leveraged a fine‑tuning approach: first they collected a large dataset of manually extracted articles from Fundus, each annotated in both markdown and JSON. These examples were used to train a lightweight transformer that takes raw HTML as input and outputs the desired structured representations. The model was evaluated on three tasks—HTML‑to‑plaintext, HTML‑to‑markdown, and HTML‑to‑JSON—using standard evaluation metrics (BLEU, METEOR). To compare with rule‑based systems, they also measured performance against established parsers such as BeautifulSoup and lxml.

## Results  
In the HTML‑to‑Markdown task, news-crawler‑LM outperformed baselines by +4.8 BLEU and +6.1 METEOR, indicating higher fidelity of extracted content. For HTML‑to‑JSON, improvements were +2.2 BLEU and +4.1 METEOR, reflecting better structured output. On the plaintext conversion task, the model’s gain over rule‑based parsers was only modest, confirming that its strength lies in JSON generation rather than simple text extraction.

## Significance  
This work demonstrates that even a small language model can replace costly handcrafted crawlers for news data pipelines, offering flexibility across publishers without extensive configuration. By providing both human‑readable markdown and machine‑readable JSON, it bridges the gap between usability and automation in information extraction tasks.

## Related Concepts  
- Long‑context language models (e.g., T5, BART)  
- Fine‑tuning on domain‑specific datasets  
- Rule‑based web parsing libraries (BeautifulSoup, lxml)  
- Extraction metrics: BLEU, METEOR
