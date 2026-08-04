# Summary: 2026-08-03_05-36-49Z_MNC_Scope_BoundSemanticDeclassificationforPrivateL.md
Saved: 2026-08-03 23:37
Source: 2026-08-03_05-36-49Z_MNC_Scope_BoundSemanticDeclassificationforPrivateL.md
Model: None

---

## Summary  
The paper proposes MNC, a scope‑bound semantic declassification protocol for private LLM‑agent communication that restricts what agents disclose based on task requirements and enforces strict usage constraints. It introduces typed semantic‑declassification with explicit recipient, purpose, forwarding, lifetime, logging, and memory scopes, enforced by a reference monitor and a history‑aware extension. The work demonstrates that conventional defenses can preserve utility while exposing extra inference signal, showing MNC blocks unauthorized actions beyond text‑only declassifiers. Controlled experiments on MAGPIE show mediated disclosures propagate through subsequent planning, tool use, coordination, and memory retrieval.

## Key Contributions  
- **MNC defines a typed semantic‑declassification protocol with explicit scope constraints** (recipient, purpose, forwarding, lifetime, logging, memory).  
- **A reference monitor enforces these scopes across subsequent operations while a history‑aware extension tracks cumulative inference risk**.  
- **Experiments show conventional defenses expose substantial additional inference signal, whereas MNC preserves authorized delivery and blocks unauthorized forwarding, logging, storage, retrieval**.

## Methodology  
The authors approached the problem by analyzing how LLM agents communicate internally via messages, tool arguments, logs, and persistent memory. They designed a protocol that selects a minimal disclosure from an application‑authored candidate family based on task sufficiency, then binds it to explicit constraints. A reference monitor continuously checks subsequent actions for scope violations; a history‑aware extension accumulates inference risk over repeated disclosures. Controlled experiments compare MNC against text‑only semantic declassifiers and conventional privacy prompts.

## Results  
Under identical receipt text, MNC preserves authorized delivery while blocking unauthorized forwarding, logging, durable storage, and retrieval after expiration that a text‑only semantic declassifier permits. Two‑backbone MAGPIE executions demonstrate that mediated disclosures propagate through subsequent planning, tool use, coordination, and memory retrieval. Conventional defenses preserve protocol‑level utility but expose extra inference signal.

## Significance  
This matters because private LLM‑agent systems require precise communication boundaries; MNC provides a practical boundary that limits exposure beyond surface text while maintaining functionality, thereby reducing the risk of unintended data leakage or downstream misuse.

## Related Concepts  
Scope‑bound semantic declassification, typed protocols, reference monitor, history‑aware extension, MAGPIE (Multi‑Agent Generative Programming Interface), privacy prompts, redaction methods, source‑level access controls, inference risk accumulation.
