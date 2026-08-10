# Summary: 2026-08-06_22-54-16Z_ShapeYourFeed_AnLLM_basedAgenticSystemforConversat.md
Saved: 2026-08-09 22:26
Source: 2026-08-06_22-54-16Z_ShapeYourFeed_AnLLM_basedAgenticSystemforConversat.md
Model: None

---

## Summary  
The paper introduces **Shape Your Feed (SYF)**, an LLM‑based agentic system that enables real‑time, multimodal co‑curating of content by interpreting explicit user preferences via text prompts, voice commands, and UI interactions. It moves beyond passive ranking to active steering, allowing users to shape their feed dynamically. SYF integrates a perception flow for intent capture, a serving flow for re‑ranking, and a self‑evolution flow that aligns system behavior with human judgments using Direct Preference Optimization (DPO). Offline and online evaluations show significant improvements in relevance and sentiment.

## Key Contributions  
- [Finding 1] The three‑tier architecture (Perception Flow, Serving Flow, Self‑Evolution Flow) provides a systematic pipeline for converting user inputs into actionable re‑ranking decisions.  
- [Finding 2] A persistent Semantic Profile encodes evolving preferences, enabling continuity across interactions and long‑term alignment.  
- [Finding 3] Direct Preference Optimization (DPO) combined with an LLM‑as‑a‑Judge ensemble yields high‑accuracy preference scoring (98.85 % accuracy), outperforming strong few‑shot baselines.

## Methodology  
The authors tackled the gap between user intent and passive recommendation by building an agentic loop where large language models parse multimodal inputs, generate semantic representations, and continuously refine rankings using DPO feedback loops. They trained a model to act as a judge, producing preference signals for offline training and online A/B testing, thereby creating a closed‑loop system that adapts in real time.

## Results  
Offline alignment scoring achieved 98.85 % accuracy versus strong few‑shot baselines. Production A/B experiments on live traffic reported measurable gains: feed relevance increased by roughly 12 %, and user sentiment rose by about 8 %. The system handled thousands of concurrent users with low latency, demonstrating scalability in industrial settings.

## Significance  
This work proves that interactive, user‑steerable recommendation is feasible at scale without sacrificing performance. It offers a blueprint for integrating LLMs into real‑time recommendation pipelines, bridging the theory‑practice gap and enabling personalized, dynamic feeds that align with explicit user intent.

## Related Concepts  
- Agentic recommendation  
- Direct Preference Optimization (DPO)  
- Semantic Profile  
- LLM‑as‑a‑Judge  
- Multimodal intent parsing  
- Active re‑ranking  
- Co‑curating
