# Summary: 2026-08-04_19-18-41Z_MindtheCap_Output_BudgetRegimesChangetheMeasuredMu.md
Saved: 2026-08-05 20:22
Source: 2026-08-04_19-18-41Z_MindtheCap_Output_BudgetRegimesChangetheMeasuredMu.md
Model: None

---

## Summary  
The paper investigates whether the observed multilingual reasoning gap between native and translation models is an artifact of a fixed output‑token cap rather than genuine linguistic ability. By treating the cap as an independent experimental variable, the authors show that the measured gap can swing by up to 57 points across different budgets, and that length normalization can even reverse which prompting strategy scores higher when the cap binds tightly. Experiments freeze three Qwen model peaks and a near‑zero value at 1024 tokens, then evaluate them on 540 k independently hard‑capped decodes to confirm that any residual difference reflects strategy performance rather than an unaddressed reasoning deficit. The study also demonstrates that announcing different budgets (e.g., 128 vs. 2048) changes Thai native accuracy by about 5 points, indicating the cap is a distinct driver of results.

## Key Contributions  
- [Finding 1] Output‑budget regimes cause a hidden variable that can shift the measured multilingual reasoning gap by up to 57 points and allow normalization to reverse strategy rankings at tight caps.  
- [Finding 2] A frozen test at the 1024‑token budget fails to reject the null because native accuracy is already saturated; any remaining difference is a strategy‑performance gap, not an unmet reasoning requirement.  
- [Finding 3] Changing the announced budget (e.g., 128 vs. 2048 tokens) alters Thai native accuracy by ~5.1 points, showing that the cap itself—not just the enforced limit—drives observed differences.

## Methodology  
The authors employ four prompting strategies on the MGSM benchmark using Qwen3‑8B and Llama‑3.1‑8B‑Instruct. They freeze three Qwen model peaks and a near‑zero value at 1024 tokens, then run 540 k independent decodes with hard caps. Holm‑corrected tests are applied to assess significance, and additional analyses include cross‑fitted Thai vocabulary extensions, varying announced budgets, and computing correct‑emission timing identities across runs.

## Results  
The measured gap varies by up to 57 points when the cap is relaxed, while normalization moves it by as much as 38.9 points where the cap binds. At tight caps (e.g., 128 tokens), length normalization can flip which strategy leads. The frozen test at B* = 1024 does not reject the null because native accuracy saturates there; above saturation, residual differences are attributed to strategy performance. A Thai vocabulary extension closes 0.0 points of the gap at the frozen budget but improves by 4.9 points where 19 % of traces still truncate. Announcing a smaller budget (128) instead of 2048 reduces Thai native accuracy by about 5.1 points, confirming that the cap is an independent variable.

## Significance  
Treating output caps as experimental variables rather than fixed constraints prevents misleading conclusions about multilingual reasoning ability. Reporting accuracy across budgets and normalizing for token length enables fair comparisons between models and strategies. This work also highlights practical adaptation levers—such as vocabulary extensions—that can mitigate budget‑induced gaps, informing future model deployment.

## Related Concepts  
- Output‑cap (token budget)  
- Multilingual reasoning gap  
- Prompting strategy performance  
- Length normalization  
- Holm correction for multiple testing  
- Frozen benchmark evaluation
