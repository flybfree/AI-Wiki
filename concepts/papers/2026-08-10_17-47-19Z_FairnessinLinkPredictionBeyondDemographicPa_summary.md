# Summary: 2026-08-10_17-47-19Z_FairnessinLinkPredictionBeyondDemographicParity_AR.md
Saved: 2026-08-11 00:04
Source: 2026-08-10_17-47-19Z_FairnessinLinkPredictionBeyondDemographicParity_AR.md
Model: None

---

## Summary  
The paper revisits the common fairness metric demographic parity in ranked link prediction and demonstrates that it can mask subgroup‑specific ranking disparities caused by exposure bias. By reproducing this limitation, the authors introduce a rank‑aware Normalized Discounted KL‑divergence (NDKL) that explicitly captures where links appear in the ordering. They also evaluate a post‑processing method called MORAL that mitigates these hidden biases while preserving prediction utility across multiple experimental configurations.

## Key Contributions  
- [Finding 1] Demographic parity ($Δ_{DP}$) can indicate overall parity even when subgroup‑pair links are systematically ranked lower, revealing its failure to detect exposure bias.  
- [Finding 2] The rank‑aware Normalized Discounted KL‑divergence (NDKL) successfully uncovers such ranking disparities by incorporating position information into the fairness objective.  
- [Finding 3] MORAL post‑processing reduces exposure‑induced biases with only a modest loss in utility, outperforming $Δ_{DP}$ and comparable metrics across diverse datasets.

## Methodology  
The authors first reproduce Mattos et al.’s claim by generating synthetic homophily scenarios where sensitive attributes influence link visibility. They then implement NDKL to compute fairness scores that weight the discounted KL divergence according to each link’s rank, ensuring that lower‑ranked links from under‑represented groups are penalized more heavily. MORAL is applied as a post‑processing step that re‑ranks pairs based on a fairness‑aware attention function. Experiments compare NDKL, MORAL, and the original $Δ_{DP}$ metric across synthetic data, categorical sensitive attributes, and real‑world datasets, also evaluating utility (e.g., MAP@k) and an Attention‑Weighted Rank Fairness (AWRF) measure.

## Results  
Experimental results confirm that $Δ_{DP}$ yields a single aggregate score while NDKL produces subgroup‑specific rankings that expose the bias. MORAL consistently reduces disparity scores by up to 23 % compared with baseline models, and its MAP@k loss is under 5 % relative to the original model. AWRF also shows comparable fairness improvements, indicating that attention‑weighted approaches are robust. All findings hold across synthetic homophily settings, categorical sensitive attributes, and three benchmark datasets.

## Significance  
These results demonstrate that exposure bias can evade traditional parity metrics in ranked recommendation systems, highlighting the need for position‑aware fairness measures. MORAL’s minimal utility penalty shows that post‑processing can effectively correct hidden biases without compromising performance. The study underscores the importance of reproducibility and open implementation (GitHub link) to enable broader validation.

## Related Concepts  
demographic parity, exposure bias, rank‑aware KL divergence, NDKL, MORAL post‑processing, attention‑weighted rank fairness (AWRF), homophily, synthetic experiments, categorical sensitive attributes.
