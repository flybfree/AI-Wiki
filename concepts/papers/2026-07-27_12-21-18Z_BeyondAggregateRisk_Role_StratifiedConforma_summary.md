# Summary: 2026-07-27_12-21-18Z_BeyondAggregateRisk_Role_StratifiedConformalRiskCo.md
Saved: 2026-07-27 21:36
Source: 2026-07-27_12-21-18Z_BeyondAggregateRisk_Role_StratifiedConformalRiskCo.md
Model: None

---

## Summary  
The paper tackles the problem that existing conformal risk‑control methods treat all arguments in a tool call uniformly, thereby masking high‑risk failures hidden among benign inputs. It introduces **role‑stratified per‑field conformal risk control**, a calibration layer that assigns separate thresholds and risk budgets to each semantic argument role based on its prevalence. By guaranteeing calibrated risk for rare roles directly rather than pooling them into an aggregate budget, the method prevents catastrophic errors from being concealed by safe arguments.

## Key Contributions  
- **Role‑stratified per‑field conformal risk control** provides calibrated guarantees for each semantic argument role in LLM tool calls.  
- Empirical evaluation shows that this approach achieves the most consistent compliance with individual role budgets across diverse language models, attacks, and gradual drift compared to aggregate‑only certification.  
- Formal per‑role certificates are derived under exchangeability or recalibration assumptions, while rare roles are handled via pooled certification.

## Methodology  
The authors wrap any existing per‑field detector with a calibration layer that sets thresholds proportional to the role prevalence \(p_r\). For each role they apply finite‑sample conformal bounds to obtain direct risk guarantees; when a role is too infrequent for sufficient sampling, a pooled certification aggregates its risk. This yields separate aggregate‑only budgets of \(\alpha p_r\) and precise per‑role budgets that are calibrated to the actual prevalence.

## Results  
Across **AgentDojo** and **InjecAgent** with six language models, the utility gap aligns with the predicted “price of coarseness” for coarse risk control. The method maintains compliance under model transfer, detector noise, gradual drift, unseen tool suites, and adaptive attacks. Formal per‑role guarantees hold under exchangeability or recalibration; empirical compliance is observed even when the data distribution shifts frozenly.

## Significance  
Certifying structured tool calls at the semantic‑role level rather than as a whole action prevents high‑risk failures from being obscured by benign arguments, thereby improving safety and reliability in LLM agents that rely on tool invocations. This shift toward role‑aware risk control is essential for trustworthy deployment of large language models.

## Related Concepts  
- Conformal risk control  
- Calibration layers  
- Per‑field detection  
- Role prevalence \(p_r\)  
- Finite‑sample guarantees  
- Exchangeability assumption  
- Calibrated risk budgets
