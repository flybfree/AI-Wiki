# Summary: 2026-07-29_08-59-43Z_Filesystem_BasedMemoryforLLMAgents_Organization_Ev.md
Saved: 2026-07-29 20:30
Source: 2026-07-29_08-59-43Z_Filesystem_BasedMemoryforLLMAgents_Organization_Ev.md
Model: None

---

## Summary  
The paper investigates filesystem‑based memory for LLM agents, exploring how organizing memory as a directory tree affects retrieval cost, answer quality, and store health over time. It formalizes three roles—management agent, search agent, execution agent—and systematically varies memory organization, stream scale, tool harnesses, and management/search strengths across long conversations and embodied tasks.

## Key Contributions  
- Finding 1: Organized memory roughly halves retrieval cost when material is large.  
- Finding 2: Organization erodes for all but the strongest management agent; no agent converts organization into better answers.  
- Finding 3: The tool set reshapes the store as strongly as swapping the model, indicating that storage architecture is a design lever.

## Methodology  
The authors formalize filesystem memory as a three‑agent system: the management agent organizes incoming content into a directory tree of markdown files; the search agent retrieves and cites sources; the execution agent supplies tasks distilled into skills. They vary memory shape (hierarchy vs verbatim dump), stream scale, tool harness (sandboxed shell, function‑like tools), and the strengths of management and search agents across long‑conversation benchmarks and embodied tasks.

## Results  
Experiments show that organized stores reduce retrieval cost by about 50 % for large material. However, answer quality does not improve with organization; even the strongest management agents underperform. Store health degrades as memory grows unless managed well. Changing tool harness alone reshapes the store similarly to changing the model, indicating architecture sensitivity.

## Significance  
This work treats the filesystem default as a design space rather than an assumption, providing empirical evidence on trade‑offs between organization, cost, and answer quality. It guides future agent memory design by highlighting that organizational choices are learnable and impactful.

## Related Concepts  
- Memory‑as‑filesystem  
- Retrieval economy  
- Agent orchestration  
- Tool harnesses  
- Store health
