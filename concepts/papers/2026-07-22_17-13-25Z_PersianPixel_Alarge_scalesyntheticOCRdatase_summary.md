# Summary: 2026-07-22_17-13-25Z_PersianPixel_Alarge_scalesyntheticOCRdatasetforPer.md
Saved: 2026-07-23 00:02
Source: 2026-07-22_17-13-25Z_PersianPixel_Alarge_scalesyntheticOCRdatasetforPer.md
Model: None

---

## Summary  
The paper introduces Persian Pixel, a large‑scale synthetic OCR dataset for the Persian language to address data scarcity and script complexity. It generates 343 000 high‑fidelity image‑text pairs from a seven‑million‑word corpus using SynthOCR‑Gen and realistic degradation models. The dataset enables training of modern OCR models such as TrOCR and Donut, offering an open, scalable alternative to manual annotation for Persian OCR.  

## Key Contributions  
- Generates 343 000 high‑quality synthetic image‑text pairs covering sentence, paragraph, and full‑page layouts.  
- Models all typographic features of the Perso‑Arabic script (cursive connectivity, glyph variants, diacritics) across Naskh and Nastaliq typefaces.  
- Augments data with more than twenty‑five stochastic degradation models to simulate real document artifacts such as ink bleed, paper aging, blur, illumination variation, scanner imperfections, compression artifacts, and noise.  

## Methodology  
The authors first curated a seven‑million‑word Persian corpus, then fed it into SynthOCR‑Gen, which renders text according to authentic typographic rules including contextual joining and glyph placement. The synthetic images are subsequently processed through twenty‑five stochastic degradation pipelines that emulate ink bleed, paper aging, blur, illumination variation, scanner imperfections, compression artifacts and various noise processes, thereby bridging the gap between synthetic and real‑world data.  

## Results  
Experimental evaluation shows that models trained on Persian Pixel achieve state‑of‑the‑art performance on benchmark OCR tasks, outperforming prior datasets by up to 4.2 % in word error rate reduction. The entire pipeline is fully automated, enabling the generation of millions of samples within minutes and providing a reproducible, cost‑effective resource for research.  

## Significance  
By supplying a massive, open, and realistic dataset, Persian Pixel removes the bottleneck of manual annotation for low‑resource Persian OCR research. It accelerates the development of end‑to‑end document understanding systems and supports historical manuscript digitization where authentic script rendering is critical.  

## Related Concepts  
- Optical Character Recognition (OCR)  
- Synthetic data generation  
- Transformer‑based OCR models (TrOCR, Donut)  
- Perso‑Arabic script typography  
- Data augmentation for low‑resource languages
