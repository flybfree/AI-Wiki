# Summary: 2026-08-06_11-15-41Z_AppDeltaWorld_Transition_GroundedDeltaCodeWorldMod.md
Saved: 2026-08-06 20:39
Source: 2026-08-06_11-15-41Z_AppDeltaWorld_Transition_GroundedDeltaCodeWorldMod.md
Model: None

---

## Summary  
AppDeltaWorld introduces a transition‑grounded delta code world model for mobile GUI agents, aiming to predict the next screen as a reachable code update rather than an unconstrained visual description. By retrieving app‑specific Level‑1 HTML references under action‑transition constraints and generating executable Level‑2 HTML conditioned on current state, predicted text, and retrieved structure, the system inserts generated assets into image slots before browser rendering to produce high‑fidelity simulated environments. The approach enables privacy‑preserving training with synthetic data and achieves state‑of‑the‑art performance on mobile interaction benchmarks without requiring real app interactions.

## Key Contributions  
- [Finding 1] AppDeltaWorld is the first transition‑grounded delta code world model that predicts GUI updates as reachable code rather than unconstrained image or text.  
- [Finding 2] It retrieves Level‑1 HTML references under action‑transition constraints and generates executable Level‑2 HTML conditioned on current screen, predicted next‑screen text, and retrieved structure.  
- [Finding 3] The framework supports filtered closed‑loop SFT data construction with public supervision, enabling state‑of‑the‑art performance on AndroidLens while providing consistent gains on MobileGym and MobileWorld.

## Methodology  
The authors treat the mobile GUI as a code world where each screen is represented by HTML. For any action, AppDeltaWorld first looks up Level‑1 references that are reachable under the transition constraint, then constructs a Level‑2 executable HTML model conditioned on the current screen state, the action, and the predicted next‑screen text. Generated visual assets are placed into image slots within this HTML before it is rendered in a browser simulation, producing a stable, high‑fidelity environment that can be used for training and test‑time reinforcement learning.

## Results  
AppDeltaWorld attains the highest fidelity on CMGUIBench‑500 under Code2World evaluation, showing clear improvements in structural layout and UI element reconstruction compared to image‑only and code‑only baselines. When combined with filtered closed‑loop SFT data constructed from public supervision, AppDeltaAgent reaches state‑of‑the‑art performance on AndroidLens and yields consistent gains on MobileGym and MobileWorld. Test‑time reinforcement learning further adapts policies without additional real‑app interaction.

## Significance  
By simulating GUI updates as code rather than images, AppDeltaWorld sidesteps privacy issues associated with collecting real user trajectories while reducing the cost of scaling up simulation environments. It stabilizes world‑model generation, expands modality coverage to executable HTML, and provides a robust training pipeline that enables long‑horizon mobile interaction policies without compromising user data.

## Related Concepts  
Delta code world model, transition‑grounded learning, Level‑1/Level‑2 HTML references, executable HTML generation, image slots, browser rendering simulation, supervised fine‑tuning (SFT), Code2World evaluation, AndroidLens benchmark, MobileGym, MobileWorld.
