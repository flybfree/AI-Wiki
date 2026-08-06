# Summary: 2026-08-04_10-04-16Z_CAMP_ACycle_AwareMulti_ScalePatchMixerforTimeSerie.md
Saved: 2026-08-06 00:05
Source: 2026-08-04_10-04-16Z_CAMP_ACycle_AwareMulti_ScalePatchMixerforTimeSerie.md
Model: None

---

## Summary  
The paper introduces CAMP, a Cycle‑Aware Multi‑Scale Patch Mixer designed to improve long‑term time‑series forecasting when periodic behavior varies across datasets and when patches near the forecast boundary require different levels of contextual refinement. By removing cycles through an Adaptive Cycle Learning module that discovers dominant frequencies per input window without pre‑defined cycle lengths, CAMP preserves the residual dynamics within a multi‑resolution framework. The Horizon‑Guided Patch Mixer adds position‑dependent processing, giving earlier patches broader temporal context while keeping recent patches close to the output. This combination enables a single model to handle multiple scales and cycles simultaneously.

## Key Contributions  
- Adaptive Cycle Learning identifies dominant frequencies separately for each input window without requiring a pre‑defined cycle length.  
- Horizon‑Guided Patch Mixer provides position‑dependent refinement, allowing earlier patches to incorporate broader temporal context while preserving information close to the forecast boundary.  
- Temporal multi‑resolution modeling captures complementary dynamics at different scales within one forecasting framework.

## Methodology  
CAMP tackles the challenges of varying cycles and patch positions by first applying Adaptive Cycle Learning to decompose each window into its cyclic component, which is then removed without a fixed period assumption. The remaining residual is fed through a Horizon‑Guided Patch Mixer that processes patches according to their distance from the forecast horizon: distant patches receive richer context, while recent patches are treated as high‑resolution signals. Finally, the de‑cycled residual is represented in temporally aligned multi‑scale layers, enabling complementary temporal dynamics at various resolutions to be processed together.

## Results  
Across seven long‑term forecasting benchmarks, CAMP achieves the best average MSE on six datasets and the best or tied‑best MAE on six. In addition, it obtains the highest MSE win count across sixteen settings on four PEMS traffic benchmarks. These results demonstrate that CAMP outperforms existing cycle‑aware and patch‑mixing methods in both accuracy and robustness.

## Significance  
CAMP’s significance lies in its ability to handle datasets where periodic patterns shift over time and where the temporal position of patches matters. By integrating adaptive cycle detection with horizon‑guided patch processing, it offers a flexible, single‑model solution that can capture multi‑scale dynamics without sacrificing performance. This advances the state of the art for long‑term forecasting in domains such as traffic prediction.

## Related Concepts  
Cycle‑aware forecasting, Multi‑Scale Patch Mixer, Adaptive Cycle Learning, Horizon‑Guided refinement, Temporal multi‑resolution modeling, residual modeling, time‑series decomposition.
