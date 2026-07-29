# Summary: 2026-07-28_09-37-11Z_Anti_BackdoorCoresetSelectionviaCumulativeEntropy.md
Saved: 2026-07-28 22:38
Source: 2026-07-28_09-37-11Z_Anti_BackdoorCoresetSelectionviaCumulativeEntropy.md
Model: None

---

## Summary  
This paper tackles the problem of constructing a training‑time coreset that can be used to train a backdoor‑free model by selecting only benign samples from a mixed dataset. The authors propose using cumulative entropy as a selection criterion, which captures how informative each sample is for learning while reflecting its learning dynamics during training. By unlearning the chosen samples at the end of each epoch, they maintain a clean separation between poisonous and benign data, enabling an effective anti‑backdoor defense with minimal degradation in natural performance.

## Key Contributions  
- [Finding 1] The authors formulate anti‑backdoor coreset selection as an optimization problem that balances informativeness and the need to exclude poisoned examples.  
- [Finding 2] They introduce cumulative entropy, a metric that tracks learning dynamics and favors samples with high predictive uncertainty that are associated with benign functionality.  
- [Finding 3] The method unlearns each selected sample at epoch end, preserving separability between benign and backdoor‑poisoned data throughout training.

## Methodology  
The methodology proceeds in three stages: first, the cumulative entropy of a sample is computed as the sum of its contribution to the overall uncertainty over time; second, coresets are built by greedily adding the most informative benign samples while excluding those with low entropy or high poisoning likelihood; third, after each training epoch, the selected samples are removed from future consideration and “unlearned,” ensuring that subsequent epochs do not re‑expose the model to poisonous information. This iterative unlearning prevents the model from inadvertently retaining backdoor behavior.

## Results  
Experimental results on several benchmark datasets demonstrate that the cumulative entropy–based coreset yields a backdoor‑free model with accuracy within 0.2 % of the natural baseline, while prior defense methods suffer larger drops (up to 3 %). The approach consistently outperforms random or entropy‑only coresets and is robust across varying poisoning ratios up to 15 %. Ablation studies confirm that unlearning each epoch is crucial for maintaining separation.

## Significance  
This work provides a principled, training‑time solution to anti‑backdoor attacks that does not compromise natural performance, offering a practical tool for secure model training in environments where data poisoning is possible. By integrating cumulative entropy with iterative unlearning, the method bridges theory and real‑world deployment, making backdoor defenses more reliable and less intrusive.

## Related Concepts  
- Coreset selection  
- Cumulative entropy as an informativeness metric  
- Anti‑backdoor defense  
- Unlearning in training  
- Backdoor poisoning detection
