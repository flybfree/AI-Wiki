# Summary: 2026-07-20_18-13-49Z_EnablingMultilingualPrivacyPolicyAudits_Large_Scal.md
Saved: 2026-07-24 00:24
Source: 2026-07-20_18-13-49Z_EnablingMultilingualPrivacyPolicyAudits_Large_Scal.md
Model: None

---

## Summary  
The paper investigates whether large language models (LLMs) can perform multilingual privacy‑policy audits without requiring language‑specific adaptation, focusing on the Spanish mobile ecosystem within the European Union. It creates a cross‑lingual dataset from 24 EU languages using expert‑annotated OPP‑115 and MAPP corpora, evaluates translation fidelity, and trains an LLM classifier to detect personal‑data‑collection categories. The study then audits 2,611 Android apps in the Spanish Google Play Store, linking policy text with privacy labels and runtime network traffic. Findings show that multilingual LLMs achieve high accuracy while exposing systematic language barriers between declared policies and observed data practices.

## Key Contributions  
- [Finding 1] The LLM classifier attains stable cross‑lingual performance, delivering macro‑F1 scores of 0.91–0.94 across all EU languages.  
- [Finding 2] Public‑sector apps predominantly provide privacy policies in Spanish, whereas popular commercial apps use English, creating a multilingual transparency gap.  
- [Finding 3] Automated audits reveal systematic discrepancies between declared policy categories and actual runtime data collection.

## Methodology  
The authors assembled an evaluation corpus by translating expert‑annotated OPP‑115 and MAPP datasets into all 24 EU languages, measuring translation fidelity with automated metrics and legal‑expert review. They trained a multilingual LLM classifier to identify personal‑data‑collection categories, then applied it to the Play Store audit dataset, correlating policy text with privacy labels and network traffic logs.

## Results  
Macro‑F1 scores range from 0.91 to 0.94, indicating high classification accuracy. The audit demonstrates that Spanish policies dominate public apps but are not mirrored by English‑only commercial apps; observed data collection often exceeds declared scope, especially for sensitive categories such as location and contacts.

## Significance  
This work shows that English‑centric audits can mask privacy issues in multilingual environments, urging developers of policy‑analysis tools to adopt language‑agnostic approaches. It underscores the necessity for systematic cross‑lingual evaluation of AI systems used in privacy compliance within EU digital services.

## Related Concepts  
Large Language Models (LLMs), privacy‑policy auditing, multilingual NLP, European Union Digital Services Regulation, translation fidelity, runtime network traffic analysis, public vs. commercial app policies.
