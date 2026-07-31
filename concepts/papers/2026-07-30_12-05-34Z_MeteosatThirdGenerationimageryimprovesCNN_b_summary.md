# Summary: 2026-07-30_12-05-34Z_MeteosatThirdGenerationimageryimprovesCNN_basedSSI.md
Saved: 2026-07-30 21:49
Source: 2026-07-30_12-05-34Z_MeteosatThirdGenerationimageryimprovesCNN_basedSSI.md
Model: None

---

## Summary  
The paper investigates how the higher spatial resolution of Meteosat Third Generation (MTG) imagery can enhance machine‑learning based Surface Solar Irradiance (SSI) retrieval for 10‑minute time steps over northern Europe. By integrating MSG/SEVIRI and MTG/FCI satellite data with solar‑geometry and clear‑sky features, the authors develop a hybrid CNN architecture that outperforms previous SEVIRI‑only models under cloudy conditions while also benchmarking against the physics‑based SARAH‑3 product. The study demonstrates that MTG’s finer resolution improves retrieval accuracy when clouds dominate irradiance variability but does not resolve the inherent clear‑sky limitations of purely data‑driven approaches.

## Key Contributions  
- [Finding 1] A multi‑imager, multi‑resolution CNN architecture using both MSG/SEVIRI and MTG/FCI imagery yields a hybrid SEVIRI‑FCI model that reduces RMSE by 8.2 W m⁻² under overcast conditions compared with the SEVIRI‑only baseline.  
- [Finding 2] The hybrid model’s skill scores reach 35 % under overcast, 21 % under cloudy, and 20 % overall, surpassing SARAH‑3 in these regimes despite higher RMSE than the physics product.  
- [Finding 3] Under partly cloudy or clear skies, the hybrid model shows no statistically significant improvement over SEVIRI alone, indicating that higher resolution alone cannot eliminate clear‑sky errors.

## Methodology  
The authors constructed a convolutional neural network trained on 10‑minute SSI measurements from eight Estonian meteorological stations. The dataset combines MSG/SEVIRI and MTG/FCI images with solar‑position, cloud‑cover, and clear‑sky irradiance features. Model performance is assessed via site‑based cross‑validation across multiple training seeds to mitigate overfitting. Results are compared against ground truth pyranometer data and the SARAH‑3 satellite product.

## Results  
The SEVIRI‑FCI hybrid model achieves lower RMSE (8.2 W m⁻² under overcast, 5.7 W m⁻² under cloudy) than the SEVIRI‑only version, translating to a 35 % skill score improvement relative to SARAH‑3 in cloudy regimes. However, RMSE differences vanish for partly cloudy and clear conditions, where both models perform similarly to each other but still lag behind SARAH‑3’s accuracy. Overall, the hybrid model demonstrates robust gains when clouds dominate irradiance variability.

## Significance  
Accurate SSI retrieval is critical for photovoltaic system monitoring and forecasting; errors directly affect energy production estimates. This work shows that leveraging MTG’s higher resolution can meaningfully boost machine‑learning performance under cloudy skies, offering a practical upgrade to existing CNN pipelines without replacing physics‑based products entirely.

## Related Concepts  
- Surface Solar Irradiance (SSI) retrieval  
- Convolutional Neural Networks (CNN) for remote sensing  
- Meteosat Third Generation (MTG) and Second Generation (MSG) satellite constellations  
- SEVIRI and FCI imaging sensors  
- SARAH‑3 physics‑based satellite product  
- Clear‑sky vs. cloudy irradiance regimes
