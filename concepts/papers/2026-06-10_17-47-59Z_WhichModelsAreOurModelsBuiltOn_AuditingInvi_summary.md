# Summary: 2026-06-10_17-47-59Z_WhichModelsAreOurModelsBuiltOn_AuditingInvisibleDe.md
Saved: 2026-06-10 22:00
Source: 2026-06-10_17-47-59Z_WhichModelsAreOurModelsBuiltOn_AuditingInvisibleDe.md
Model: None

---


## Summary  
Modern large‑language model (LLM) training pipelines increasingly embed other models to generate data, filter corpora, judge outputs, and guide development decisions. These hidden dependencies are recursive and scattered across heterogeneous public artifacts, making the full dependency structure difficult for humans to trace. The authors introduce **ModSleuth**, an agentic system that recursively reconstructs these dependency graphs using source‑grounded evidence from publicly available releases. By formalizing both direct and indirect relationships and resolving artifact identities across names, versions, and repositories, ModSleuth produces a comprehensive view of the invisible ecosystem behind contemporary LLMs.

## Key Contributions  
- **Finding 1:** The primary challenge is not extracting information but defining what constitutes a dependency and reconciling references that appear in inconsistent documentation.  
- **Finding 2:** ModSleuth reconstructs over 1,060 source‑verified dependencies across four public LLM releases, constructing large‑scale dependency graphs that capture multi‑hop license obligations and train‑evaluation coupling.  
- **Finding 3:** The formalization distinguishes direct from indirect relationships and represents heterogeneous pipeline roles through operation‑centered relationships, enabling precise artifact identity resolution.

## Methodology  
ModSleuth is an agentic tool that iteratively pulls public artifacts (code, documentation, model checkpoints) and extracts evidence about their usage in LLM pipelines. It employs a formal model that defines **direct** versus **indirect** dependencies and models each pipeline role as an operation‑centered relationship. The system then resolves artifact identities by matching names across different repositories and versions, creating a unified dependency graph. This reconstruction is performed recursively to capture the full chain of upstream artifacts.

## Results  
Applying ModSleuth to four public LLM releases yields 1,060 source‑verified dependencies and generates detailed dependency graphs that expose: (a) multi‑hop license obligations across different components; (b) tight coupling between training data generation and evaluation models; (c) discrepancies where released artifacts differ from those used at training time; and (d) documentation inconsistencies that obscure true relationships. These results demonstrate the depth of hidden dependencies in modern LLM ecosystems.

## Significance  
Understanding these invisible dependencies is crucial for responsible AI development, as they can propagate licensing risks, performance bottlenecks, or quality issues downstream. By making this structure transparent, ModSleuth enables auditors and developers to trace obligations, detect inconsistencies early, and build more reliable LLM pipelines.

## Related Concepts  
- Dependency graph reconstruction  
- Artifact identity resolution across names, versions, repositories  
- Recursive dependency tracing  
- Direct vs. indirect dependencies  
- Operation‑centered relationship modeling  
- Multi‑hop license obligations  
- Train‑evaluation coupling  
- Formalization of heterogeneous pipeline roles
