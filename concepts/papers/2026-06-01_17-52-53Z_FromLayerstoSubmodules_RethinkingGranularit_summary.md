# Summary: 2026-06-01_17-52-53Z_FromLayerstoSubmodules_RethinkingGranularityinRepl.md
Saved: 2026-06-01 23:00
Source: 2026-06-01_17-52-53Z_FromLayerstoSubmodules_RethinkingGranularityinRepl.md
Model: None

---


## Summary  
The paper critiques the prevailing replacement‑based compression paradigm for Large Language Models, which restricts granularity to whole layers and contiguous submodule selections. It argues that pretrained transformers exhibit redundancy across non‑contiguous attention and feed‑forward submodules, suggesting a more flexible approach. The authors propose SubFit, a method that compresses LLMs at the submodule level by fitting lightweight residual bypasses for each submodule independently. Experiments on ten models across five sparsity levels demonstrate that SubFit outperforms existing baselines in perplexity‑accuracy trade‑offs while delivering measurable inference speedups and KV‑cache savings.

## Key Contributions  
- [Finding 1] Redundancy in pretrained transformers is not confined to contiguous depth ranges or evenly distributed between attention and feed‑forward outputs.  
- [Finding 2] Full‑layer granularity and contiguous selection are overly restrictive constraints for replacement‑based compression.  
- [Finding 3] Submodule‑level fitting yields better perplexity‑accuracy trade‑offs, especially under aggressive sparsities.

## Methodology  
SubFit operates post‑training on calibration data without any fine‑tuning. It treats each attention and feed‑forward submodule as an independent residual component that can be replaced by a lightweight fitted bypass. The selection of submodules is non‑contiguous, allowing the algorithm to target regions with higher redundancy. Compression proceeds by iteratively fitting these residuals until a desired sparsity level (12.5 %–37.5 %) is reached.

## Results  
Across ten LLMs (five base, five instruction‑tuned) and four replacement baselines, SubFit achieved the best aggregate perplexity‑accuracy trade‑off at each sparsity level. At 25 % sparsity it retained 84.6 % of dense downstream accuracy with only a 2.42× perplexity degradation, compared to 81.6 % and 4.34× for the strongest baselines. The method also delivered inference speedup and significant KV‑cache memory savings.

## Significance  
By relaxing granularity constraints, SubFit enables more efficient compression that preserves model behavior while reducing size and latency—critical for deploying LLMs on resource‑constrained devices. Its submodule‑level approach opens a path to compressing heterogeneous parts of the architecture without sacrificing performance.

## Related Concepts  
- Replacement‑based compression  
- Sparsity levels (12.5 %–37.5 %)  
- Perplexity‑accuracy trade‑off  
- KV‑cache savings  
- Post‑training calibration data  
- Residual bypass fitting

[[2026-06-01_17-52-53Z_FromLayerstoSubmodules_RethinkingGranularityinRepl.md]]