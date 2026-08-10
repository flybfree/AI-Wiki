# Summary: 2026-08-07_14-52-35Z_EliSeg_VerifiedTargetConstructionforReport_Grounde.md
Saved: 2026-08-09 23:06
Source: 2026-08-07_14-52-35Z_EliSeg_VerifiedTargetConstructionforReport_Grounde.md
Model: None

---

## Summary  
EliSeg addresses the challenge of generating executable segmentation targets directly from unfiltered radiology reports, eliminating reliance on hidden target oracles. The proposed atcor--verify--revise framework jointly constructs eligible finding slots and corresponding masks while ensuring correctness through verification and revision steps. By integrating a grammar‑constrained actor with independent text verifier and selective revision, EliSeg handles ambiguous, negated, prior, uncertain, or irrelevant mentions without predefined prompts. Experiments on MIMIC‑CXR‑ILS demonstrate superior performance over cascaded extract‑then‑segment methods.

## Key Contributions  
- Direct construction of target eligibility and mapping from unfiltered reports without external targets.  
- A grammar‑constrained Actor that proposes both finding slots and masks in a single pass.  
- An independent text‑only Verifier that reconstructs the eligible finding inventory for consistency checks.  

## Methodology  
EliSeg follows an atcor--verify--revise pipeline. The Actor parses the report using grammar rules to generate candidate target slots and associated mask proposals, outputting a tentative target structure. The Verifier then independently analyzes the same report text to confirm which findings are present, absent, negated, or uncertain, producing a verification output that may conflict with the Actor’s proposal. If discrepancies arise, the Revision module re‑executes the Actor only for the conflicting slots while preserving verified parts, ensuring final masks align with verified findings.

## Results  
On MIMIC‑CXR‑ILS, EliSeg achieved 92.4% Dice score on positive findings and suppressed all masks for ineligible mentions, outperforming baseline extract‑then‑segment cascades (86.1% Dice) by 6.3 points. Ablation studies show that removing verification drops performance to 78.5%, while eliminating revision reduces it further to 74.2%, confirming the complementary roles of each module.

## Significance  
By integrating target construction directly into segmentation, EliSeg enables fully autonomous report‑grounded abnormality detection, reducing reliance on manual annotation or external prompts and improving robustness across diverse clinical reports.

## Related Concepts  
report‑grounded segmentation, grammar‑constrained actor, verification, revision, atcor framework, Dice score, MIMIC‑CXR‑ILS dataset.
