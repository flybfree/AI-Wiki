# Summary: 2026-08-05_11-38-33Z_DiagnosingTool_SelectionReasoninginLLMAgentswithCa.md
Saved: 2026-08-05 20:34
Source: 2026-08-05_11-38-33Z_DiagnosingTool_SelectionReasoninginLLMAgentswithCa.md
Model: None

---

## Summary  
The paper tackles the problem of diagnosing why large language model (LLM) agents select the wrong tool, which is often reported only in aggregate terms. By embedding diagnostic “canary” tools into an agent’s Model Context Protocol (MCP), the authors can pinpoint specific reasoning weaknesses that cause a single erroneous choice. A six‑type taxonomy—semantic decoys, parameter traps, capability mirages, prerequisite blindness, temporal decoys, and granularity traps—transforms each failure into a multi‑dimensional profile of tool‑selection error. The study demonstrates that these probes reveal the underlying causes of model‑level mistakes across a broad spectrum of models.

## Key Contributions  
- **Finding 1:** Susceptibility to canary tools drops sharply as models become more capable, with per‑task canary susceptibility rates (CSR) varying roughly 36× from best to worst.  
- **Finding 2:** Capability tier alone does not predict safety; the most susceptible hosted model is mid‑tier, and within a provider the cheaper model can be safer than the pricier one.  
- **Finding 3:** The taxonomy is capability‑stratified: capability mirages reliably trap frontier models, while other types are largely inert on strong models but fire on small open models, allowing discrimination by capability rather than raw weakness.

## Methodology  
The authors introduce “canary tools” that act as diagnostic probes within an agent’s MCP tool set. Each probe is engineered to expose one of the six taxonomy categories, turning a single wrong‑tool outcome into a detailed failure profile. The evaluation involves eight models (six hosted, two 8B open‑weight) across three capability tiers, on 120 tasks under three canary‑density conditions and three seeds (8,640 runs). A subtlety ablation with 2,880 runs isolates the effect of each probe. Task success is judged independently by a provider‑independent judge, confirmed by a second independent judge (Cohen’s κ = 0.75).

## Results  
The per‑task CSR ranges from ~0.9% for Claude Opus 4.8 to >36% for Llama 3.1 8B, confirming the steep drop in susceptibility with capability. The most susceptible hosted model is mid‑tier, and cheaper models can be safer than expensive ones, indicating that tier alone is insufficient. The taxonomy shows that “capability mirages” are the primary failure mode for frontier models, while other types are largely ineffective on strong models but trigger errors on small open models, revealing a capability‑stratified pattern. Softening each probe’s giveaway phrase leaves CSR essentially unchanged, proving the probes measure reasoning rather than simple phrase spotting. Finally, canary susceptibility correlates with task failure (Spearman ρ = –0.34), yet the most robust models remain unaffected by canary pressure.

## Significance  
Understanding why LLMs mis‑select tools is crucial for building reliable agents and for calibrating model capabilities. By isolating specific reasoning flaws through canary probes, practitioners can target interventions rather than treating failures as opaque aggregate metrics. The taxonomy also offers a principled way to compare models across capability tiers, informing resource allocation and safety guarantees.

## Related Concepts  
- Model Context Protocol (MCP) – the framework that allows agents to invoke external tools.  
- Canary tools – diagnostic probes inserted into MCP tool sets.  
- Semantic decoys, parameter traps, capability mirages, prerequisite blindness, temporal decoys, granularity traps – taxonomy categories describing tool‑selection weaknesses.  
- Per‑task canary susceptibility rate (CSR) – a metric quantifying how often a model fails on specific probes.  
- Capability stratification – the observation that certain failure modes are more prevalent in higher‑capability models.
