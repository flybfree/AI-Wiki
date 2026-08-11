# Summary: 2026-08-10_17-39-05Z_Space_CreatingversusDeadPossession_AnOff_BallPosse.md
Saved: 2026-08-11 00:03
Source: 2026-08-10_17-39-05Z_Space_CreatingversusDeadPossession_AnOff_BallPosse.md
Model: None

---

## Summary  
Seongjin Choi’s paper tackles the paradox that football statistics treat ball possession as a simple binary metric, ignoring whether that possession actually creates space or is merely dead circulation. The research proposes an event‑based “junk‑possession” flag that evaluates each possession sequence on its threat potential while correcting for lead‑protecting cycles in tied or losing states. A complementary Space‑Creation Index (SCI) uses broadcast video to measure net pitch‑control change, distinguishing space‑creating actions from sterile ball movement. By layering these two metrics, the authors reveal a richer picture of possession quality that event‑only on‑ball models cannot capture.

## Key Contributions  
- [Finding 1] The junk‑possession flag shows a strong negative correlation with points (r = –0.37) and xG difference (r = –0.51), indicating that low‑value possessions depress team performance.  
- [Finding 2] This association persists even after controlling for on‑ball VAEP and field tilt, proving the flag adds predictive information beyond existing on‑ball value models.  
- [Finding 3] The Space‑Creation Index identifies that 74 % of flagged windows are spatially dead, only 19 % represent weak progression, and just 6 % truly create space, including two cases where the ball exited solely via penalties.

## Methodology  
The authors build a junk‑possession index by reconstructing live scorelines to strip out lead‑protecting circulation and assigning each possession a peak threat value from an expected‑threat grid. Positions that fall below a low‑threshold are flagged as “junk.” For the World Cup sample, they then project broadcast footage onto pitch coordinates to compute the Space‑Creation Index (SCI), which quantifies net change in ball control over the window. The two layers are applied jointly: the junk flag signals low on‑ball value, while SCI determines whether that value was earned through space creation or dead circulation.

## Results  
Across 31 of 35 flagged windows from nine World Cup matches, the junk flag correlates with a –0.37 coefficient for points and a –0.51 coefficient for xG difference after controlling for on‑ball VAEP (p < 0.0001). The SCI reveals that only 6 % of flagged windows are space‑creating; the remaining 94 % are either dead or weak progressions, confirming that many possessions are “junk” in both value and spatial impact. The model’s explanatory power is demonstrated by a same‑match regression where the junk flag improves fit beyond VAEP alone.

## Significance  
Possession statistics dominate media narratives yet mislead audiences because they conflate dead circulation with space creation. Choi’s two‑layer index clarifies that not all ball movement translates into tactical advantage, offering leagues and broadcasters a more accurate metric for evaluating on‑field decisions and informing coaching strategies.

## Related Concepts  
- Off‑ball possession value  
- Expected threat (ET) grid  
- VAEP (Value Added Expected Points)  
- xG (expected goals) difference  
- Pitch‑control change (Space‑Creation Index)  
- Event‑based analytics in football
