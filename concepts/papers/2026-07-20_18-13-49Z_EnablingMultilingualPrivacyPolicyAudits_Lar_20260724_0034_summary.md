# Summary: 2026-07-20_18-13-49Z_EnablingMultilingualPrivacyPolicyAudits_Large_Scal.md
Saved: 2026-07-24 00:34
Source: 2026-07-20_18-13-49Z_EnablingMultilingualPrivacyPolicyAudits_Large_Scal.md
Model: None

---

## Summary  
The paper investigates whether large language models can perform privacy‑policy audits in any EU language without requiring separate, language‑specific adaptations, thereby extending English‑centric auditing to multilingual ecosystems. By training an LLM on translated versions of expert‑annotated datasets across all 24 official languages, the authors demonstrate stable cross‑lingual performance and apply it to a large‑scale audit of 2 611 Android apps from the Spanish Google Play Store. The study reveals systematic gaps between declared privacy policies and actual data practices, especially in public‑sector applications that only publish policies in Spanish. This work shows how English‑only audits can mask transparency issues in linguistically diverse environments.

## Key Contributions  
- [Finding 1] An LLM classifier for personal‑data collection categories achieves macro‑F1 scores of 0.91–0.94 across the full set of 24 EU languages, indicating robust cross‑lingual transfer.  
- [Finding 2] Public‑sector apps predominantly provide privacy policies in Spanish, while popular commercial apps use English; observed practices often diverge from the declared language, exposing a systematic discrepancy.  
- [Finding 3] Multilingual audits uncover hidden transparency gaps that would be invisible to English‑only analyses, highlighting the need for language‑aware evaluation.

## Methodology  
The authors assembled an evaluation corpus by translating expert‑annotated datasets OPP‑115 and MAPP into all 24 EU languages. Translation fidelity was assessed with automated metrics (BLEU, METEOR) and confirmed by legal experts. A multilingual LLM classifier was trained to identify categories of personal data collection from policy texts; its performance was evaluated on the translated corpus. The classifier was then deployed on a large‑scale audit of 2 611 Android apps from the Spanish Google Play Store, where each app’s privacy label and runtime network traffic were recorded alongside the multilingual policy analysis.

## Results  
The cross‑lingual classifier delivered macro‑F1 scores between 0.91 and 0.94 on held‑out test sets across all languages, confirming stable translation‑aware performance. The audit of 2 611 apps showed that public‑sector applications almost exclusively publish policies in Spanish, yet their actual data collection practices varied widely and were not fully aligned with the declared policy. In contrast, many commercial apps provide English policies but also exhibit similar discrepancies. These findings demonstrate that English‑only audits systematically overlook language barriers, obscuring transparency gaps.

## Significance  
This research demonstrates a scalable, language‑agnostic method for evaluating privacy transparency across EU digital services, countering the bias of English‑centric tools and informing policy, app design, and audit frameworks to ensure equitable protection of user data in multilingual contexts. It underscores that without addressing linguistic diversity, automated audits risk missing critical privacy violations.

## Related Concepts  
- Large language models (LLMs)  
- Cross‑lingual transfer learning  
- Privacy policy audit  
- Translation fidelity metrics  
- Personal data classification  
- EU Digital Services Act compliance  
- Multilingual UI and user experience  
- Runtime network traffic analysis
