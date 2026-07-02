---
title: Theoria: Rewrite-Acceptability Verification over Informal Reasoning States
url: http://arxiv.org/abs/2607.01223v1
type: paper-summary
date: 2026-07-01
source_paper: 2026-07-01_17-56-42Z_Theoria_Rewrite_AcceptabilityVerificationoverInfor.md
generated_at: 2026-07-01 23:00
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Theoria, a verification framework that rewrites AI answers into typed state transitions each backed by explicit justification such as citations or computations. It demonstrates high precision on expert problem sets while producing auditable proof traces. Certified solutions achieve comparable performance to holistic LLM judges but with better traceability.

## Key Takeaways
- Theoria certifies 105 out of 185 Gold problems at 91.4% strict precision, providing human readable audit trails where each transition can be challenged.
- Holistic judges match coverage but show lower precision on different problem sets, highlighting complementary strengths.
- Structured judges detect hidden premises and fabricated citations more effectively than holistic methods across adversarial poisoned proofs.

## Context
AI systems often rely on informal reasoning or opaque scores to evaluate answers, leading to trust issues. Formal verification offers certainty but limited applicability, while LLM judges cover broader problems yet lack auditability. Theoria bridges this gap by combining formal structure with traceable justifications.

## Implications
Practitioners can adopt Theoria to generate verifiable AI responses that are both accurate and auditable. This approach could improve trust in automated systems across domains such as education, healthcare, and scientific research where correctness is critical. Its integration could streamline compliance checks and reduce liability risks.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.01223v1)
