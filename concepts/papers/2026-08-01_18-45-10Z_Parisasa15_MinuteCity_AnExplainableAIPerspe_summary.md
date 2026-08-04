# Summary: 2026-08-01_18-45-10Z_Parisasa15_MinuteCity_AnExplainableAIPerspective.md
Saved: 2026-08-03 23:56
Source: 2026-08-01_18-45-10Z_Parisasa15_MinuteCity_AnExplainableAIPerspective.md
Model: None

---

## Summary  
The paper investigates how the availability of local services within walking or cycling distance influences mobility patterns in Paris, aiming to quantify the link between “15‑minute city” accessibility and observed travel behavior. Using a large dataset of 70 000 segmented trip segments from NetMob 2025, enriched with INSEE sociodemographic data and OpenStreetMap points of interest (POIs), the authors construct indicators of service availability and test their associations with trip duration, mode choice, and short‑trip car use. Gradient‑boosted tree models are interpreted with explainable AI techniques to reveal which variables drive predictions. The study shows that higher POI density reduces private motorized travel while amplifying active mobility, yet this effect is weaker in the outer agglomeration.

## Key Contributions  
- [Finding 1] Higher POI availability is linked to lower car use and more walking/cycling trips for short journeys, especially within the central Paris area.  
- [Finding 2] Gradient‑boosted tree models, interpreted via XAI, consistently identify trip purpose, home‑work distance, local service availability, vehicle ownership, public‑transport subscription, and sociodemographic context as key predictors of travel mode.  
- [Finding 3] Explainable AI demonstrates that feature attributions shift under alternative variable orderings, highlighting the importance of model interpretability for policy relevance.

## Methodology  
The authors assembled mobility trajectories from the NetMob 2025 Data Challenge, paired them with INSEE sociodemographic variables and OSM‑derived POI locations. After stop‑based segmentation and cleaning, they obtained ~70 000 trip segments. Walking‑ and cycling‑based service availability indicators were computed for each segment. Gradient‑boosted decision trees were trained to predict travel mode (car, public transport, active) and trip purpose. Explainable AI tools such as SHAP values were used to interpret model attributions, with the effect of feature orderings examined to ensure robustness.

## Results  
The models reveal that high POI density correlates with lower car ownership impact for short trips, while car‑ownership and licence availability increase predicted car use. When services are sparse, a public‑transport subscription reduces car dependence. Overall predictions align with 15‑minute city assumptions but show substantial spatial and demographic heterogeneity: the central core exhibits strong service‑mobility links, whereas outer zones show weaker effects. XAI analysis confirms that model explanations remain consistent across variable permutations, underscoring interpretability.

## Significance  
These findings validate the 15‑minute city concept as a useful framework for urban planning while exposing its limits in heterogeneous contexts. The integration of explainable AI with accessibility indicators provides actionable insights for policymakers seeking locally relevant hypotheses to reduce car dependence and promote active mobility.

## Related Concepts  
- 15‑minute city  
- Mobility trajectories  
- Points of interest (POI) density  
- Active mobility  
- Gradient‑boosted trees  
- Explainable AI (XAI) / SHAP values  
- Accessibility indicators  
- Urban‑mobility policy
