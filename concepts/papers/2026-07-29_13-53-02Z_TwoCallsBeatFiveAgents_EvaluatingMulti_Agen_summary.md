# Summary: 2026-07-29_13-53-02Z_TwoCallsBeatFiveAgents_EvaluatingMulti_AgentPipeli.md
Saved: 2026-07-29 20:34
Source: 2026-07-29_13-53-02Z_TwoCallsBeatFiveAgents_EvaluatingMulti_AgentPipeli.md
Model: None

---

## Summary  
This paper evaluates a structured multi‑agent pipeline called Parishad, which splits tasks among five roles, on the local 7 B Qwen2.5‑Instruct model using two benchmark suites: GSM8K and HumanEval. The authors compare the pipeline with direct prompting and a two‑call self‑refinement strategy to understand how communication format and implementation affect performance. Their key finding is that multi‑agent setups can degrade accuracy on local models, while simpler approaches often match or exceed them. The work demonstrates that architectural complexity alone does not guarantee better results when deployed locally.

## Key Contributions  
- [Finding 1] The multi‑agent system drops GSM8K accuracy from 75 % to 45 % when using JSON data format due to error accumulation, but plaintext restores it to 82 %.  
- [Finding 2] A two‑call self‑refinement strategy (V1) achieves 86.2 % on GSM8K with a token usage reduction of 7.4× compared with the full multi‑agent pipeline.  
- [Finding 3] Task‑aware gated redesign (V2) preserves HumanEval accuracy at 95.1 %, whereas direct prompting already reaches 96.3 % and V1 actually harms performance.

## Methodology  
The authors deployed Parishad, a five‑role multi‑agent pipeline, on the Qwen2.5‑7B‑Instruct model using both GSM8K (500 questions) and HumanEval (164 problems). They measured two metrics: accuracy and token usage. The evaluation compared three configurations: direct prompting, the full multi‑agent pipeline in JSON format, plaintext version of the pipeline, V1 self‑refinement, and V2 task‑aware gated redesign.

## Results  
On GSM8K, the JSON‑format pipeline yields 45 % accuracy; switching to plaintext improves it to 82 %. The two‑call V1 reaches 86.2 % while using roughly 7.4× fewer tokens than the full multi‑agent setup. For HumanEval, direct prompting scores 96.3 %, V1 drops performance to 66.5 %, and V2 maintains 95.1 %. Token usage is consistently lower for V1 across both tasks.

## Significance  
The results show that communication format and implementation details are more influential than the complexity of a multi‑agent architecture when using local language models. Simpler, task‑aware approaches can match or surpass the performance of complex pipelines, suggesting that resource‑constrained deployments may benefit from streamlined designs rather than elaborate role division.

## Related Concepts  
Multi‑agent LLM pipeline, self‑refinement, task‑aware gating, token usage efficiency, error accumulation in JSON format, local language model deployment, benchmark suites (GSM8K, HumanEval).
