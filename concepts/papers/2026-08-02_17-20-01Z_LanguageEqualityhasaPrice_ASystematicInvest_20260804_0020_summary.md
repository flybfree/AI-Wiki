# Summary: 2026-08-02_17-20-01Z_LanguageEqualityhasaPrice_ASystematicInvestigation.md
Saved: 2026-08-04 00:20
Source: 2026-08-02_17-20-01Z_LanguageEqualityhasaPrice_ASystematicInvestigation.md
Model: None

---

## Summary  
This paper systematically investigates how large language models (LLMs) perform as language agents in goal‑directed, multi‑turn dialogue games across 30 languages—24 official EU languages plus six others. The authors evaluate nine open‑weight and commercial LLMs using a reference‑free, programmatic scoring system that can be localized for new languages. Their key finding is that no open‑weight model meets the performance threshold in any of the EU languages, while commercial systems consistently outperform them. Moreover, linguistic parity is achievable with commercial models even when public web text is extremely limited.

## Semantic links
- [[concepts/papers/2026-07-23_21-59-56Z_QwenAgentWorld_LanguageWorldModelsforGeneralAgents_summary.md|Summary: Qwen-AgentWorld: Language World Models for General Agents]] — 5 title terms overlap; 29 backlinks; 9 summary/topic terms overlap
- [[concepts/ai-foundations/ai-ml-foundations-lesson-11-large-language-models-the-modern-ai-interface.md|AI/ML Foundations Lesson 11 - Large Language Models: The Modern AI Interface]] — 4 title terms overlap; 54 backlinks; 5 summary/topic terms overlap
- [[concepts/llm-models/2026-07-10_OpenSourceModelsStateOfTheArt.md|Open-Source Models State of the Art — 2026-07-10]] — 4 title terms overlap; 12 backlinks; 4 summary/topic terms overlap

## Key Contributions  
- [Finding 1] No open‑weight LLM reaches acceptable performance in any of the EU‑24 official languages; commercial systems outrank all open‑weight models.  
- [Finding 2] Linguistic parity is attainable with commercial LLMs even when public web text is scarce, though not solely from crawls.  
- [Finding 3] A model’s home region lifts its score without closing the gap; Chinese models still fall behind US commercial systems.

## Methodology  
The authors construct a self‑play dialogue game that is language‑agnostic: each turn generates a response based on a fixed prompt and a word list, and the entire interaction is scored programmatically. To test 30 languages they localize only the prompt text and the word‑list file, leaving the underlying model unchanged. Nine open‑weight models (e.g., LLaMA, Mistral) and nine commercial models (e.g., GPT‑4, Claude) are run in parallel across all languages, producing a single aggregate score per language.

## Results  
In every official EU language both commercial systems outscore every open‑weight model. The two weakest commercial averages fall below 40 points across the EU‑24. Commercial models remain superior even in languages that have roughly four orders of magnitude less public web text, indicating that performance is not limited by crawl coverage alone. When pooling all results, non‑English languages cost about 31 % more to run than English and score 10 % lower on average.

## Significance  
The study demonstrates that achieving true linguistic parity among LLMs requires commercial resources; open‑weight models cannot match the performance of leading commercial systems in any EU language. It also reveals a persistent cost disparity, where non‑English usage incurs higher compute expenses and slightly lower quality, highlighting challenges for multilingual AI deployment.

## Related Concepts  
- Large Language Model (LLM) evaluation  
- Multi‑turn dialogue games  
- Reference‑free scoring  
- Linguistic parity  
- Home region advantage  
- Web crawl coverage vs. model quality
