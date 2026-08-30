# Summary: 2026-08-27_17-59-11Z_WikiSkill_CompilingAgentExperienceintoPersistentKn.md
Saved: 2026-08-28 09:36
Source: 2026-08-27_17-59-11Z_WikiSkill_CompilingAgentExperienceintoPersistentKn.md
Model: None

---

## Summary  
The paper introduces WikiSkill, a framework that turns an agent’s accumulated experience into a persistent knowledge base (wiki) to enable skill evolution. By separating raw execution logs, learned knowledge, and executable skills, WikiSkill continuously consolidates these components so that later skill updates can build on prior ones. The approach aims to make skill development systematic, reusable, and transferable across model iterations and architectures. Experiments show that WikiSkill consistently improves performance over state‑of‑the‑art methods and no‑skill baselines.  

## Key Contributions  
- [Finding 1] WikiSkill creates a persistent knowledge base (wiki) that aggregates raw execution experience and accumulated knowledge into executable skills, enabling continuous skill evolution.  
- [Finding 2] The framework consistently outperforms existing state‑of‑the‑art skill‑evolution methods across diverse benchmarks and model families.  
- [Finding 3] Persistent accumulation in the wiki is essential; ablation studies demonstrate that without it, skill updates degrade or fail to improve.  

## Methodology  
WikiSkill adopts a three‑layer pipeline: first, raw execution logs from an agent are stored as experience entries; second, these logs are processed by a knowledge extraction module that identifies patterns and generates new skills; third, the generated skills are compiled into the wiki where they become persistent resources. The system iteratively updates both the skill set and the wiki, allowing later iterations to reference earlier knowledge. This co‑evolutionary loop is orchestrated through a lightweight scheduler that balances exploration (trying new skills) with exploitation (using stored ones).  

## Results  
Across benchmark suites such as MMLU, GSM8K, and ARC, WikiSkill achieved higher accuracy and F1 scores than the best prior skill‑evolution baselines. In many cases, models equipped with WikiSkill outperformed larger models without any evolved skills, while smaller models with WikiSkill sometimes surpassed significantly bigger models lacking skills. Transfer experiments confirmed that skills learned by one model family could be applied to another, and cross‑model skill reuse yielded up to 12 % absolute gains. Ablation results showed a sharp drop in performance when the wiki was disabled, confirming its critical role.  

## Significance  
WikiSkill demonstrates that systematic accumulation of agent experience can transform incremental improvements into robust, reusable capabilities. By providing a persistent knowledge base, it bridges the gap between short‑term learning and long‑term skill evolution, offering a scalable solution for continual improvement in large language models. This work advances the field toward more adaptive AI agents that learn from their own history rather than starting each task anew.  

## Related Concepts  
- Skill evolution  
- Persistent knowledge base (wiki)  
- Knowledge distillation  
- Continual learning  
- Model adaptation
