# Summary: 2026-07-30_14-45-18Z_FromTextualRequirementstoMicroserviceArchitectures.md
Saved: 2026-07-30 21:55
Source: 2026-07-30_14-45-18Z_FromTextualRequirementstoMicroserviceArchitectures.md
Model: None

---

## Summary  
The paper investigates whether a Large Language Model (LLM) can synthesize complete microservice architectures from natural‑language requirements alone, bridging the gap between textual specifications and system design. It evaluates an LLM’s ability to produce service definitions and inter‑service interactions for two small test systems—Bookstore and PetClinic—using both zero‑shot (ZS) and few‑shot (FS) prompting strategies with OpenAI o3. The study combines quantitative metrics such as precision, recall, and F1‑score for service identification and communication recovery with a blinded expert assessment of correctness, completeness, modularity, and plausibility. Results show that while the LLM can generate architectures from textual input, its performance depends heavily on prompting style and system context.

## Key Contributions  
- [Finding 1] The LLM can produce microservice‑level designs directly from textual requirements without prior code or reference architecture.  
- [Finding 2] Few‑shot prompting markedly improves service identification agreement (F1 = 0.97) compared to zero‑shot (F1 = 0.61), reducing unsupported dependencies.  
- [Finding 3] Human experts perceive FS‑generated architectures as more modular, coherent, and plausible than ZS outputs.

## Methodology  
The authors conducted a mixed‑method study employing OpenAI o3 under two prompting conditions: zero‑shot (providing only the requirement text) and few‑shot (supplying a short example of a reference architecture). Two independent systems—Bookstore and PetClinic—were each evaluated under both ZS and FS prompts, yielding four execution pairs. Quantitative evaluation used precision, recall, and F1‑score to measure how well generated services matched the reference set and whether inter‑service communication was correctly recovered. Complementary qualitative assessment involved a blind expert review of each architecture on criteria such as correctness, completeness, modularity, and plausibility, followed by open feedback synthesis.

## Results  
Quantitatively, FS prompting achieved higher agreement: service identification F1 = 0.97 (ZS = 0.61) and communication recovery F1 = 0.82 (ZS = 0.65). Expert evaluation confirmed that FS architectures were rated significantly better on modularity (mean score 4.3 vs 3.1) and plausibility (4.0 vs 2.7), while ZS outputs often contained redundant or unsupported service links. The differences were system‑specific; the Bookstore task showed modest gains, whereas PetClinic exhibited larger improvements.

## Significance  
These findings demonstrate that LLMs can act as a bridge between textual requirements and microservice design, but their utility is contingent on prompt engineering and domain context. The study highlights the value of few‑shot prompting in guiding LLM outputs toward more coherent architectures, offering a practical pathway for early‑stage system modernization where only natural language specifications are available.

## Related Concepts  
microservice architecture, textual requirements, Large Language Models (LLMs), prompt engineering, decomposition, service identification, inter‑service interaction, evaluation metrics (precision/recall/F1), expert assessment.
