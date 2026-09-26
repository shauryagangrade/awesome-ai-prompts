---
prompt: Reusable PR Review
repo: UCIP (Urban Climate Intelligence Platform)
link: https://github.com/AnayDhawan/ucip
commit: cdc7387
---

# UCIP: Removing an invalid data indicator

**Task:** Review a large feature removal that cascaded across pipeline, API, and frontend after discovering the source data was invalid.

**Agent:** Claude (Code)

**Stack:** Python (data pipeline), TypeScript (API + frontend), geospatial data

**Before:** UCIP ranks Mumbai ward heat vulnerability. The elderly share indicator contributed 13.6% to the score and drove cooling-centre placement rules. But the data came from WorldPop's age-sex raster, which applies district-level age structure uniformly. Across 541 cells it took exactly two values, revealing which revenue district each cell belonged to, not actual age distribution. No ward-level 60+ data exists in public Census tables.

**What the prompt made the agent do:**

1. Verified data quality: confirmed why WorldPop was invalid.
2. Mapped the cascade: 83 files changed, API contract breaks, 225 test lines deleted.
3. Checked edge cases: zero-population cells were staying out only because elderly share was undefined there.
4. Validated recomputation: top five wards reranked; 13 changed position.
5. Found a secondary insight: dropping child_pct (not elderly_pct) resolves disagreement between PCA and equal-weight methods.

**After:**

- Indicator and all dependencies removed.
- All scores recomputed with seven remaining indicators.
- Migration 0008 prepared (field removal normally requires v2; UCIP documents why it's done inside v1).
- Ablation study added to compare weighting methods.

**Would you use it again?** Yes. Data quality decisions create cascade risk; the prompt's tracing prevented missing API breaks, test gaps, or downstream consumers.
