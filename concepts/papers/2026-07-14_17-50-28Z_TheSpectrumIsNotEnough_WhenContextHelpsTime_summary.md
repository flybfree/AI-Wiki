# Summary: 2026-07-14_17-50-28Z_TheSpectrumIsNotEnough_WhenContextHelpsTime_Series.md
Saved: 2026-07-15 00:01
Source: 2026-07-14_17-50-28Z_TheSpectrumIsNotEnough_WhenContextHelpsTime_Series.md
Model: None

---

## Summary  
The paper argues that the conventional spectrum‑based indices used to gauge time‑series predictability are insufficient because they ignore phase information and cannot capture improvements that arise from richer context such as longer look‑back windows, retrieval plug‑ins, or pretrained foundation models. It formalises an impossibility result: a series whose power spectrum is unchanged but whose phase structure is random becomes asymptotically Gaussian, destroying any beyond‑second‑order forecasting value. To quantify this gap the authors introduce a label‑free diagnostic called the *coverage deficit* that isolates the contribution of non‑spectral structure to model performance.

## Key Contributions  
- **Phase‑invariance vs. phase‑dependence**: Spectral indices remain unchanged under phase randomization, whereas retrieval and foundation‑model gains depend on the underlying phase structure, establishing an impossibility result.  
- **Coverage deficit as a diagnostic**: A configuration‑level metric that measures the gain of analog (beyond‑spectrum) versus linear prediction, providing a label‑free way to assess context value without new forecasters.  
- **Empirical validation on surrogate pairs**: Using constructed surrogate pairs that fix spectrum and marginal, retrieval’s value collapses across pairs while every spectral index stays frozen; foundation models split into a surviving second‑order part and a vanishing beyond‑linear margin.

## Methodology  
The authors first build surrogate datasets that share identical power spectra but differ in phase patterns. They compute conventional spectral indices (which are invariant) and evaluate three context‑enhanced forecasters: window‑keyed retrieval, longer linear windows, and a pretrained foundation model. The *coverage deficit* is defined as the difference between the analog beyond‑spectrum gain and the linear prediction baseline. By comparing these scores across all configurations they obtain a label‑free diagnostic that isolates the phase‑dependent component.

## Results  
On seven benchmark series retrieval’s performance swings from +33 % to –35 % while every spectral index remains constant (p < 10⁻⁴⁰). Foundation models retain only their second‑order linear contribution; the beyond‑linear margin collapses. A longer linear window preserves its value, whereas the coverage deficit predicts the sign of the beyond‑spectrum contribution and outperforms the spectral indices in forecasting decisions.

## Significance  
This work provides a principled distinction between what can be learned from pure spectra and what requires additional context, enabling practitioners to make informed deployment choices. By offering a diagnostic that is invariant under phase randomization yet sensitive to non‑spectral structure, it improves interpretability of time‑series forecasts without inventing new models.

## Related Concepts  
- Power spectrum and its invariance under phase randomization  
- Asymptotic Gaussian behavior for random phases  
- Retrieval plug‑ins and longer look‑back windows  
- Foundation models applied to time‑series forecasting  
- Linear prediction as a baseline model  
- Coverage deficit diagnostic  
- Beyond‑second‑order (analog) structure  
- Impossibility result linking spectrum invariance to phase dependence
