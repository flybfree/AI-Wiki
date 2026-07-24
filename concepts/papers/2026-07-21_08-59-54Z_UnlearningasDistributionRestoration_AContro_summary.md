# Summary: 2026-07-21_08-59-54Z_UnlearningasDistributionRestoration_AControlledCou.md
Saved: 2026-07-24 00:38
Source: 2026-07-21_08-59-54Z_UnlearningasDistributionRestoration_AControlledCou.md
Model: None

---

## Summary  
The paper proposes unlearning as a problem of restoring model outputs to match a reference distribution rather than merely improving probe scores, and it introduces a controlled counterfactual testbed to evaluate oracle‑free certification criteria. By treating the retained knowledge as a fault that must be erased, the authors develop an oracle‑free selective screen and demonstrate its limits through extensive experiments across 45 model seeds spanning five architecture families.  

## Key Contributions  
- [Finding 1] The controlled testbed reveals that common unlearning metrics can favor models that retain held‑out facts by up to –2.82 nats, indicating a failure of the retained/round‑trip certificate in most cells.  
- [Finding 2] Oracle‑free screens and certificate‑style criteria are evaluated on 45 model‑seed cells; only 15 cells pass damage‑relative recalibration while others fall within retraining noise, showing that such methods are not universally valid.  
- [Finding 3] A fixed‑magnitude logit‑suppression attack defeats the full forward battery in 12/45 cells, proving that forward‑only certification is unsound and that unlearning must be assessed as a selective test rather than a guarantee.  

## Methodology  
The authors construct a matched retraining reference where a small set of facts is deliberately retained. They then inject these facts into freshly trained models across diverse seeds to create “retain” instances. The study measures how well oracle‑free criteria (e.g., fixed retain thresholds, damage‑relative recalibration) reject the injected model while accepting the reference. A sealed challenge suite provides a controlled environment where only the retained set is known, allowing a selective screen that must be both necessary and sufficient.  

## Results  
Experimental results show that 41 out of 45 inject‑retain models fail the fixed retain threshold, and their round‑trip certification succeeds in only 31/45 cells. The reference model fully certifies in just 1/45. Oracle‑free screens reject the injected model in all 45 cells but partially detect entity‑routing suppression (35/45). Damage‑relative recalibration certifies a subset of 15 cells; where it abstains, its predictions lie within retraining noise (±0.8 nats) on optimized axes, while the probe criterion is 5.17 nats away. A logit‑suppression attack defeats the full forward battery in 12/45 cells.  

## Significance  
By reframing unlearning as restoration and exposing the fragility of oracle‑free certification, the paper provides a more honest evaluation framework that aligns with how models are actually produced. It also establishes an identifiability theorem that limits which facts can be forgotten without an oracle, highlighting TOFU (Train‑Offline‑Future‑Update) as the boundary case.  

## Related Concepts  
- Unlearning / Forgetting  
- Oracle‑free certification  
- Retention / round‑trip certificate  
- Damage‑relative recalibration  
- Logit suppression attack  
- Identifiability theorem
