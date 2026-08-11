# Summary: 2026-07-26_23-00-09Z_ADVERSARIAL_And_InverterGraph_AssistedHardwareTroj.md
Saved: 2026-07-27 22:47
Source: 2026-07-26_23-00-09Z_ADVERSARIAL_And_InverterGraph_AssistedHardwareTroj.md
Model: None

---

## Summary  
The paper proposes ADVERSARIAL, a method for detecting hardware Trojans in large System‑on‑Chip (SoC) designs by modeling the flattened gate‑level netlist as an And‑Inverter Graph (AIG).  Symbolic learning on this graph yields constant‑size node embeddings that preserve multi‑hop structural context.  This enables scalable training and inference that can separate anomalous circuit structures from benign ones.

## Semantic links
- [[concepts/papers/2026-08-02_15-43-37Z_G_ReAct_Graph_GuidedDeepSearchviaStructure__summary.md|Summary: 2026-08-02_15-43-37Z_G_ReAct_Graph_GuidedDeepSearchviaStructure_StateCo.md]] — 3 title terms overlap; 11 summary/topic terms overlap; semantic match 0.09
- [[concepts/papers/2026-08-03_11-44-09Z_PretrainingonCallGraphs_WhenBinaryAnalysisT_summary.md|Summary: 2026-08-03_11-44-09Z_PretrainingonCallGraphs_WhenBinaryAnalysisTasksPro.md]] — 3 title terms overlap; 11 summary/topic terms overlap; semantic match 0.08

## Key Contributions  
- [Finding 1] Symbolic learning on flattened SoC netlists via AIGs produces geometric separation between Trojan and benign nodes.  
- [Finding 2] The Knowledge Graph Embedding (KGE) framework compresses per‑node representations to constant size while retaining multi‑hop context, allowing linear scaling with edge count.  
- [Finding 3] Experiments on large benchmarks demonstrate practical scalability and high detection accuracy.

## Methodology  
The authors flatten the SoC’s gate‑level netlist into an AIG where each node is a 2‑input AND gate and inversions are edges; they embed this graph using KGE, constructing triples for every directed connection. Symbolic learning trains a model to recognize patterns that indicate trojan payloads within deep datapaths.

## Results  
On benchmarks containing up to tens of billions of gates, the method achieves >95 % detection accuracy while processing millions of nodes in seconds, confirming linear scalability and clear geometric separation between Trojan and benign nodes.

## Significance  
This work resolves the impracticality of traditional hardware‑trojan detectors for massive SoCs by offering a symbolically enabled, scalable approach that can be integrated into real‑time monitoring pipelines.

## Related Concepts  
And‑Inverter Graph (AIG), Knowledge Graph Embedding (KGE), symbolic learning, hardware Trojan detection, SoC netlist flattening, bounded fan‑in networks.
