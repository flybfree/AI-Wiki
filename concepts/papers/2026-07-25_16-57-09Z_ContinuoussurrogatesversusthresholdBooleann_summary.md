# Summary: 2026-07-25_16-57-09Z_ContinuoussurrogatesversusthresholdBooleannetworks.md
Saved: 2026-07-27 23:42
Source: 2026-07-25_16-57-09Z_ContinuoussurrogatesversusthresholdBooleannetworks.md
Model: None

---

## Summary  
This paper evaluates two families of models—continuous surrogate models (Random Forest regression and a Multi‑Layer Perceptron) and a threshold Boolean network (TBN)—on the same Arabidopsis thaliana induced systemic resistance gene expression dataset. The authors compare both the raw continuous measurements and their sign‑binarized representation to assess predictive accuracy, dynamical fidelity, and interpretability. By using rolling‑origin one‑step prediction, recursive multi‑step rollout, and interpretability analysis, they reveal that numerical performance and qualitative dynamics are not aligned. Their contribution is a comparative framework showing when each model type excels.

## Key Contributions  
- Continuous surrogates (RF, MLP) achieve the lowest average one‑step MAE (1.910) and RMSE (2.836), outperforming the TBN in numerical prediction on continuous data.  
- The threshold Boolean network reproduces the exact binary trajectory with 100 % rollout fidelity, while RF suffers larger cumulative deviation (binary accuracy = 0.708).  
- Performance metrics (MAE, RMSE, binary accuracy, Hamming distance) demonstrate a trade‑off: continuous models excel numerically but lose dynamical faithfulness, whereas TBN captures global qualitative dynamics at the cost of slightly higher numerical error.

## Methodology  
The study uses eight defense‑related Arabidopsis genes measured over nine time points. Two continuous predictors—Random Forest regression and an MLP—are trained on both raw expression values and their sign‑binarized versions. A threshold Boolean network is constructed to model the same binary data. Evaluation proceeds via rolling‑origin one‑step prediction, recursive multi‑step rollout, and interpretability analysis (e.g., pathway relevance). The authors compare average one‑step numerical accuracy, trajectory binary accuracy, and Hamming distance.

## Results  
In the continuous domain, Random Forest yields MAE = 1.910 and RMSE = 2.836, whereas MLP performs worse (MAE = 2.089, RMSE = 3.106). In the binary domain, TBN achieves the highest accuracy (0.550) with Hamming distance = 3.600; RF scores 0.500/4.000 and MLP 0.495/4.040. Rolling‑origin prediction shows TBN reproducing the observed trajectory exactly, MLP attaining binary accuracy ≈ 0.986, while RF’s trajectory accuracy drops to 0.708.

## Significance  
The findings underscore that local numerical precision and global dynamical fidelity are distinct metrics; continuous surrogate models provide superior short‑term prediction but may misrepresent underlying regulation over time, whereas threshold Boolean networks preserve the exact gene‑state dynamics at the expense of slightly higher error. This encourages researchers to select or combine model types based on whether interpretability of regulatory logic is more valuable than precise numerical forecasts.

## Related Concepts  
gene regulatory network modeling, induced systemic resistance (ISR), continuous surrogate models, threshold Boolean networks, Random Forest regression, Multi‑Layer Perceptron, rolling‑origin prediction, multi‑step rollout, MAE/RMSE, binary accuracy, Hamming distance, interpretability analysis.
