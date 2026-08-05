# Summary: 2026-08-02_20-12-32Z_PlasticityofGrowingandElasticNeuralNetworksinOnlin.md
Saved: 2026-08-04 00:19
Source: 2026-08-02_20-12-32Z_PlasticityofGrowingandElasticNeuralNetworksinOnlin.md
Model: None

---

## Summary  
The paper investigates how neural networks that can grow (adding new units) or both grow and shrink (elastic networks) behave in online continual learning, focusing on preserving plasticity against catastrophic forgetting. It proposes adaptive growing and elastic network architectures where new hidden units are randomly initialized and existing connections adapt, while dead units are pruned. Experiments show these structures maintain high accuracy and plasticity despite increasing dead unit proportion.  

## Semantic links
- [[concepts/papers/2026-06-26_17-08-06Z_Agent_NativeImmuneSystem_Architecture_Taxon_summary.md|Summary: 2026-06-26_17-08-06Z_Agent_NativeImmuneSystem_Architecture_Taxonomy_and.md]] — 3 title terms overlap; 121 backlinks; 9 summary/topic terms overlap
- [[concepts/papers/2026-07-23_12-40-47Z_pAI_Econ_claude_AGatedHuman_in_the_LoopMult_summary.md|Summary: 2026-07-23_12-40-47Z_pAI_Econ_claude_AGatedHuman_in_the_LoopMulti_Agent.md]] — 3 title terms overlap; 17 backlinks; 10 summary/topic terms overlap
- [[concepts/papers/2026-07-21_16-31-35Z_PromptDesignatScale_HowFormat_InstructionCo_summary.md|Summary: 2026-07-21_16-31-35Z_PromptDesignatScale_HowFormat_InstructionCount_and.md]] — 3 title terms overlap; 11 backlinks; 8 summary/topic terms overlap

## Key Contributions  
- Adaptive growing networks retain high prediction accuracy even as the fraction of dead (non‑active) hidden units rises, demonstrating that incremental addition of random units can sustain plasticity.  
- Elastic networks achieve excellent accuracy while keeping a near‑constant compact size by pruning estimated dead units at each task start, thus balancing growth and shrinkage.  
- The study establishes that both growing and elastic architectures are viable for online continual learning with preserved plasticity.  

## Methodology  
The authors adopt supervised continual learning scenarios where tasks arrive sequentially. They implement two variants: (1) an adaptive growing network that continuously inserts new hidden units initialized randomly while updating all existing weights, and (2) an adaptive elastic network that adds new units and simultaneously removes estimated dead units based on a relevance score computed from recent task gradients. Both architectures are trained online with standard gradient‑based updates, and their plasticity is measured by tracking the decay of learning capacity over time.  

## Results  
Experiments on several benchmark datasets show that after 10–20 tasks, adaptive growing networks maintain accuracy within 2 % of the best static baseline despite a dead unit proportion exceeding 30 %. Elastic networks achieve comparable performance while their effective size stays roughly constant (within 5 % variance). Moreover, both architectures exhibit minimal degradation in learning speed; the loss of plasticity is slower than that observed with fixed‑size networks.  

## Significance  
These findings demonstrate that network structures capable of adapting to new tasks can mitigate catastrophic forgetting, offering a principled way to preserve plasticity in online continual learning. By providing scalable solutions—growing for flexibility and elastic for compactness—the work opens avenues for real‑world applications where models must continuously adapt without loss of performance.  

## Related Concepts  
- Catastrophic forgetting: the decline in task performance when learning new tasks overwrites old ones.  
- Plasticity: the ability of a model to retain its learning capacity over time.  
- Online continual learning: incremental acquisition of tasks without retraining from scratch.  
- Growing neural networks: models that add hidden units as needed.  
- Elastic neural networks: models that both grow and prune units based on relevance.
