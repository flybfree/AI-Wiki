# Summary: 2026-08-10_01-40-25Z_MindtheHook_Source_LevelAuditingofPrivacyDefensesi.md
Saved: 2026-08-10 23:35
Source: 2026-08-10_01-40-25Z_MindtheHook_Source_LevelAuditingofPrivacyDefensesi.md
Model: None

---

## Summary  
The paper introduces an active‑path audit methodology for source‑level auditing privacy defenses in retrieval‑augmented generation (RAG), which maps each metric to the specific pipeline hook it observes and validates generated‑text effects using exact‑match canaries. It demonstrates that DP‑style defenses only modify retrieval scores while leaving generation hooks as placeholder stubs, thereby affecting membership‑inference behavior but not named‑entity leakage measured by NEL_strict. In contrast, the end‑to‑end LPRAG path validates with canaries and recovers most canaries under No‑Defense while none are recovered under LPRAG.  

## Key Contributions  
- Active‑path audit framework maps privacy metrics to specific pipeline hooks across retrieval, retrieved content, and generation.  
- DP defenses only alter retrieval scores; their generation hooks are TODO‑flagged stubs that return unchanged responses, explaining observed membership‑inference impact but no NEL_strict leakage.  
- LPRAG end‑to‑end path validates with canaries, recovering 53/150 canaries under No‑Defense and 0/150 under LPRAG.  

## Methodology  
The authors inventory source‑level hooks in the retrieval pipeline (score adjustment), the content retrieval step (retrieved text selection), and the generation step (text synthesis). Each metric is mapped to the leakage channel it directly observes, and generated‑text effects are validated using exact‑match canaries that check whether the output matches a pre‑defined reference.  

## Results  
Benchmark reimplementations show DP defenses modify only retrieval scores; their generation hooks remain stubs, so they influence membership‑inference attacks but do not affect NEL_strict named‑entity leakage. The LPRAG end‑to‑end path validates 53 out of 150 canaries under No‑Defense and none under LPRAG, confirming that the defense’s full pipeline is active only when intended.  

## Significance  
These findings provide a methodology and case study illustrating that many privacy defenses in RAG are not end‑to‑end; they may create hidden vulnerabilities or limited protection scopes. Active‑path auditing reveals which hooks actually contribute to privacy guarantees, enabling more accurate risk assessment rather than relying on black‑box scores alone.  

## Related Concepts  
Retrieval‑augmented generation (RAG), privacy defenses (DP, No‑Defense), membership inference attacks, named‑entity leakage (NEL_strict), canary validation, pipeline hooks, active‑path audit.
