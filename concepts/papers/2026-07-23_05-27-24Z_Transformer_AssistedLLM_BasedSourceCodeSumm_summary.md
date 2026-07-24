# Summary: 2026-07-23_05-27-24Z_Transformer_AssistedLLM_BasedSourceCodeSummarisati.md
Saved: 2026-07-24 02:31
Source: 2026-07-23_05-27-24Z_Transformer_AssistedLLM_BasedSourceCodeSummarisati.md
Model: None

---

## Summary  
The paper tackles the problem of generating natural‑language summaries of source code, which are essential for the Secure Software Development Lifecycle (SSDLC) to improve maintainability and reduce vulnerabilities. It proposes “Transformer‑Assisted LLM‑Based Source Code Summarisation,” a method that leverages task‑specific Transformer models as part of prompt engineering to guide Large Language Models (LLMs). By combining the lexical strength of Transformers with the semantic richness of LLMs, the approach yields higher‑quality code summaries. This work demonstrates that such hybrid prompting can boost BLEU scores, offering a practical step toward more secure software development.

## Key Contributions  
- [Finding 1] Combining task‑specific Transformer outputs within LLM prompts improves BLEU‑4 and overall summary quality.  
- [Finding 2] Task‑specific Transformers excel on lexical NLG metrics but lack semantic depth, whereas LLMs capture semantics yet produce low‑scoring abstractive summaries.  
- [Finding 3] Prompt engineering that injects Transformer‑generated snippets into LLM prompts yields higher‑quality code summaries.

## Methodology  
The authors prompt four different LLMs with task‑specific Transformer models as part of the input prompts, thereby creating a hybrid prompting framework. The generated source‑code summaries are evaluated using BLEU‑4 and standard BLEU metrics to measure lexical overlap and overall quality relative to human‑written references.

## Results  
Experimental results show an improvement of 7.8 % in BLEU‑4 scores and a 5 % increase in overall summary quality compared with LLM‑only baselines, indicating that Transformer assistance is effective at enhancing the semantic relevance of code summaries.

## Significance  
By delivering more accurate and semantically coherent summaries, this method supports developers in understanding and maintaining secure codebases, thereby reducing the likelihood of bugs and vulnerabilities introduced during maintenance phases of software development.

## Related Concepts  
Neural Source Code Summarisation (NSCS), Transformer models, Large Language Models (LLMs), Secure Software Development Lifecycle (SSDLC), prompt engineering, abstractive summarisation, BLEU metrics.
