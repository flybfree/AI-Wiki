# Summary: 2026-08-05_07-48-35Z_WhenDoCorrectiveFeaturesHelp_AnAgentforCorrectiveF.md
Saved: 2026-08-06 21:40
Source: 2026-08-05_07-48-35Z_WhenDoCorrectiveFeaturesHelp_AnAgentforCorrectiveF.md
Model: None

---

**## Summary**  
The paper tackles the problem of repairing frozen pretrained forecasters that fail in systematic, costly ways. It introduces CRAFTER—a source‑agnostic corrective feature discovery agent—that mines interpretable features from a model’s residual and applies them as lightweight post‑hoc corrections. By combining a compositional search over raw input channels with a large language model that proposes feature combinations, binary flags, or short executable code, the method enables rapid, budget‑aware correction without retraining the backbone. The validation gate selects only the most promising candidates, ensuring that improvements are attributable to the discovered features alone.

**## Key Contributions**  
- [Finding 1] Corrective feature discovery can substantially improve the performance of frozen forecasters by targeting their residual error rather than fine‑tuning the entire model.  
- [Finding 2] CRAFTER consistently outperforms all dedicated feature‑engineering systems across six public datasets and six frozen backbones, roughly doubling the gain achieved by the corrector alone.  
- [Finding 3] The source‑agnostic pipeline allows prior feature‑engineering tools to be evaluated under identical conditions, providing a clear attribution of forecast improvements to the discovered features.

**## Methodology**  
CRAFTER keeps the backbone frozen and focuses on its residual output. Two generators produce candidate corrective features: (1) a compositional search that enumerates all possible subsets of raw input channels, and (2) an LLM that generates named feature combinations, binary flags, or short executable snippets. A single validation gate evaluates each candidate regardless of origin, accepting only those that reduce validation error below a threshold. The selected corrector then applies the accepted features to the forecast; if none are beneficial, it leaves the prediction unchanged. This pipeline is fully source‑agnostic and works with any LLM backend.

**## Results**  
Across six public datasets and six frozen backbones, CRAFTER surpasses every dedicated feature‑engineering system at each feature budget. The corrector’s contribution alone doubles the improvement over baseline fine‑tuning, while the full pipeline reduces the error of the weakest backbones by up to 27 %. These gains are robust across different LLM backends and persist even when applied on top of fine‑tuned models.

**## Significance**  
The work addresses a major pain point in AI forecasting: repairing black‑box forecasters is often prohibitively expensive. By providing an automated, interpretable corrective feature discovery mechanism, CRAFTER enables cost‑effective maintenance and clear attribution of performance gains to specific features rather than model updates.

**## Related Concepts**  
frozen pretrained forecaster, residual mining, corrective feature discovery, compositional search over input channels, large language model (LLM) feature generation, validation gate, source‑agnostic pipeline, attribute attribution, feature budget.
