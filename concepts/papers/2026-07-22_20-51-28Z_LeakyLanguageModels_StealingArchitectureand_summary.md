# Summary: 2026-07-22_20-51-28Z_LeakyLanguageModels_StealingArchitectureandInferen.md
Saved: 2026-07-24 02:13
Source: 2026-07-22_20-51-28Z_LeakyLanguageModels_StealingArchitectureandInferen.md
Model: None

---

## Summary  
This paper introduces LeakyLMs, a novel attack that extracts sensitive information from production language models using only per‑token generation timing data. The attacks reveal deployment‑level optimizations such as speculative decoding and the draft context window, as well as key architectural parameters like the number of transformer layers, hidden dimension size, and attention heads. By modeling how latency scales with model configuration and hardware, LeakyLMs performs a search over the architecture space that often yields near‑correct guesses within the top ten possibilities. The work demonstrates that even remote API interactions can leak proprietary details without exposing model weights or code.

## Semantic links
- [[concepts/papers/2026-06-15_17-59-28Z_Context_AwareRLforAgenticandMultimodalLLMs_summary.md|Summary: 2026-06-15_17-59-28Z_Context_AwareRLforAgenticandMultimodalLLMs.md]] — 4 title terms overlap; 8 summary/topic terms overlap; semantic match 0.12
- [[concepts/ai-foundations/ai-ml-foundations-lesson-11-large-language-models-the-modern-ai-interface.md|AI/ML Foundations Lesson 11 - Large Language Models: The Modern AI Interface]] — 3 title terms overlap; 5 backlinks; 4 summary/topic terms overlap
- [[concepts/papers/2026-07-31_10-14-28Z_SmallIsEnough_Per_UserStyleRewritingofAI_Ed_20260803_0817_summary.md|Summary: 2026-07-31_10-14-28Z_SmallIsEnough_Per_UserStyleRewritingofAI_EditedTex.md]] — 4 title terms overlap; 4 summary/topic terms overlap; semantic match 0.08

## Key Contributions  
- [Finding 1] LeakyLMs proves that inference optimizations such as speculative decoding and draft context lengths are detectable solely from token‑generation latency, providing a covert way to infer deployment strategies.  
- [Finding 2] The attack recovers core architectural properties of the model, including layer count, hidden dimension, and attention heads, with high accuracy using a timing‑based search algorithm.  
- [Finding 3] Experimental results show that for Llama models, the correct architecture is guessed correctly more than 90 % of the time within the top ten candidates.

## Methodology  
The authors first collect fine‑grained latency measurements across a range of model sizes and NVIDIA GPU configurations while generating tokens through standard APIs. These measurements are fitted into a regression model that maps timing patterns to specific architectural parameters and hardware settings. Leveraging this model, they perform an exhaustive search over plausible architecture spaces, comparing predicted timings with the observed data to identify the most likely configuration. The entire pipeline is automated, allowing rapid inference of both deployment strategies and structural details.

## Results  
Experiments on Google Gemini Flash 2.5 reveal that speculative decoding is present and the draft context window is approximately 128 K tokens. When applied to Llama‑based models, the timing model predicts architectural configurations with a success rate exceeding 90 % for the correct answer among the top ten guesses. The latency scaling analysis confirms a strong correlation between hidden dimension size and per‑token latency, supporting the inference of hidden dimensions from timing alone.

## Significance  
LeakyLMs highlights a previously overlooked attack vector that can expose proprietary model architectures and deployment choices without compromising security or performance. By showing that token‑generation timing is rich enough to encode sensitive information, the work underscores the need for robust timing‑based defenses in AI services and informs future research on secure inference pipelines.

## Related Concepts  
- Speculative decoding (inference optimization)  
- Draft context window  
- Token‑generation latency measurement  
- Architecture recovery via regression modeling  
- Attack surface of remote APIs
