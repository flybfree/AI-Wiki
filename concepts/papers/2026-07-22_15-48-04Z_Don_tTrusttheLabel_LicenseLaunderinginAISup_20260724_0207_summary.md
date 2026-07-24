# Summary: 2026-07-22_15-48-04Z_Don_tTrusttheLabel_LicenseLaunderinginAISupplyChai.md
Saved: 2026-07-24 02:07
Source: 2026-07-22_15-48-04Z_Don_tTrusttheLabel_LicenseLaunderinginAISupplyChai.md
Model: None

---

## Summary  
The paper investigates how AI artifacts propagate through a multi‑platform supply chain, tracking dataset→model→application chains to detect license laundering—where licenses are stripped or replaced. It quantifies two forms of laundering across 232,270 chains and finds that most downstream artifacts lack declared licenses or suffer from license substitution. The study reveals stark survival rates for different license categories, highlighting the fragility of legal obligations in AI ecosystems.

## Key Contributions  
- [Finding 1] 62.3% of chains pass through at least one artifact with no declared license, concentrated in a small set of foundational datasets.  
- [Finding 2] Every obligation‑bearing license category survives below 7 % end‑to‑end, except the Permissive category which reaches 95.1%.  
- [Finding 3] The research provides actionable recommendations for practitioners, model publishers, rights holders, and platform owners.

## Methodology  
The authors constructed a comprehensive dataset of 232,270 dataset→model→application chains by scraping Hugging Face datasets, model repositories, and GitHub applications. They traced each chain to capture the license metadata at every transfer point, then applied statistical analysis to compute survival rates and identify laundering events.

## Results  
Across all chains, 62.3% contained unlabeled artifacts; only 7 % or less of any non‑permissive license survived end‑to‑end, while the permissive category survived at 95.1%. The data also show that foundational datasets drive most licensing loss.

## Significance  
These findings demonstrate that legal compliance is fragile in AI supply chains, with licenses often lost or replaced as artifacts move downstream. They underscore the need for robust provenance tracking and standardized license enforcement mechanisms across platforms.

## Related Concepts  
License laundering, AI supply chain, dataset licensing, model licensing, GitHub/Hugging Face ecosystems, provenance tracking, permissionless datasets.
