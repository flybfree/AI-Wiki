---

title: A Horn extension of DL-Lite with NL data complexity
url: http://arxiv.org/abs/2605.13367v1
type: paper-summary
date: 2026-06-11
source_paper: 2026-05-13_11-26-32Z_AHornextensionofDL_LitewithNLdatacomplexity.md
generated_at: "2026-06-11 10:39"
model: nvidia/nemotron-3-nano-4b

---


## Summary
The paper introduces ELbotpreceq, a Horn description logic that extends DL-Lite to support natural language reasoning and can be rewritten into nested two‑way regular path queries of GQL. It resolves the AC0 vs PTime dichotomy by providing an ontology language that enables practical OMQA solutions beyond first‑order constraints.

## Key Takeaways
- The stratification mechanism controls how conjunctions interact with recursion within ELI, yielding a logic that can express reachability axioms while preserving Horn properties.
- This extension adds restricted conjunction and reachability to the core DL-Lite, allowing reasoning in NL without increasing complexity beyond AC0.
- An NL upper bound is established by rewriting into nested two‑way regular path queries, a fragment of GQL, showing compatibility with graph query languages.

## Context
This work tackles the limitation that most description logics beyond DL-Lite are PTime hard for data complexity, restricting OMQA to first‑order queries. By offering an AC0‑level logic that aligns with NL‑complete graph query standards, it bridges formal semantics and modern database query capabilities.

## Implications
Practitioners can adopt ELbotpreceq to model richer ontologies while maintaining performance comparable to DL-Lite. This enables OMQA to handle natural language queries on graph data, expanding the scope of ontology‑mediated reasoning beyond first‑order limits.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2605.13367v1)
