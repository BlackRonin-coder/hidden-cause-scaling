# Research Progress Note — 3 November 2026

**Hidden Causes: residual-guided inquiry, observational controls and falsification**

**Status:** Exploratory research update. The wider mathematical investigation is unpublished and has **not** been independently validated, peer reviewed or demonstrated to discover dark matter or establish a new law of gravity.

## Purpose

The public project originally introduced a discipline for investigating unobserved causes through their measurable consequences, always testing ordinary explanations, observational uncertainties and alternative models. Since that overview, a separate **private scientific validation programme** has added observational controls and attempted to make the claims more vulnerable to meaningful falsification.

This note summarises the scientifically relevant *boundaries and methodology*, without presenting unpublished equations or internal source code as proven discoveries.

## Observational reference work

A private, standard-library scientific test suite has been run on **publicly available galaxy rotation curves**. Its principal reference dataset is [SPARC](https://astroweb.cwru.edu/SPARC/) (Lelli, McGaugh & Schombert, 2016), containing 175 galaxies. A documented quality-selection configuration retains 104 galaxy profiles for a set of strictly defined comparisons.

The analysis compares **existing**, not newly invented, descriptions: a fixed visible-matter calculation, the empirical radial-acceleration relation and an NFW-shaped halo model. It includes withheld-radius checks, galaxy-grouped validation, alternative dataset cuts, numerical stability checks, and deliberately fabricated null and injected-signal controls.

An external kinematic control draws on a separate, source-pinned public compilation of **THINGS, LITTLE THINGS and WALLABY** rotation curves. Strict quality filters and checks for identifiable overlaps with SPARC limit the analysed subset. Those observational shapes are not substitutes for a baryonic decomposition or an independent test of a new gravitational field equation.

## What the tests have already challenged

| Scientific issue | Why it matters | Current treatment |
|---|---|---|
| Apparent model improvement | A flexible model can fit fluctuations even when no hidden component generated them | Known-noise and known-injected-signal controls |
| Distance and inclination errors | Galaxy-wide uncertainties move many points together | Initial correlated-error covariance tests; **not** a complete experimental error model |
| Halo parameter identifiability | A good fit at a search-grid boundary may reflect an unconstrained parameter | Explicit search-range sensitivity and boundary warnings |
| Selection effects | Galaxy-quality cuts can change conclusions | Multiple reported selection variants; exploratory, not preregistered |
| Data reuse | Historical calibration and reanalysis of the same survey are not independent confirmation | Explicit distinction between within-survey and external-survey evidence |
| Theory completeness | A proposed gravitational correction must follow from a specified action and its field equations | Covariant reference-model checks kept distinct from the unfinished original theory |
| Cross-observable consistency | Rotation curves and lensing are physically different measurements | Standard reference forward-model calculations; **no independent lensing observations admitted** |

One particularly important result of the work is a **negative constraint on overinterpretation**: the numerical ranking between models is sensitive to assumptions about covariance and halo parameter search bounds. Therefore, the current calculations should **not** be advertised as evidence that one new physical theory has won.

## Reproducibility and review

The private development package has **66 local regression tests** and distinct Python/Go reference implementations that agree on selected benchmark quantities. These checks support code reproducibility and scientific error detection, but they are **not** an independent astrophysicist's reproduction, a calibrated discovery significance, or a peer-reviewed result.

A technical manuscript and independent review protocol have been prepared privately. A qualified physicist would still need a fully specified original gravitational action, correctly derived field equations, one preregistered prediction, realistic error models, genuinely independent observations and independent expert reproduction.

The public repository remains a **deliberately limited conceptual release** with a synthetic educational example. The private working paper and analysis code are not being released here; readers cannot use this public overview alone to audit the full private calculations.

## Where criticism would be most useful

The greatest value would come from challenges to model identifiability, covariance and observational systematics, the completeness of any proposed gravity action, fair model-comparison protocols, and realistic independent data tests.

An informative negative result is an improvement. The aim is not to construct a hypothesis that cannot be falsified; it is to specify one clearly enough that serious attempts to falsify it can be decisive.

## Selected public sources

- [Lelli, McGaugh & Schombert (2016), SPARC — *Astronomical Journal* 152, 157](https://doi.org/10.3847/0004-6256/152/6/157)
- [McGaugh, Lelli & Schombert (2016), The radial acceleration relation — *Physical Review Letters* 117, 201101](https://doi.org/10.1103/PhysRevLett.117.201101)
- [SPARC source data and documentation](https://astroweb.cwru.edu/SPARC/)
- [EPS Research — public cross-survey galaxy rotation-curve compilation](https://github.com/eps-research/rag-corpus-series)
- [THINGS high-resolution galaxy rotation-curve research, de Blok et al. (2008)](https://doi.org/10.1088/0004-6256/136/6/2648)

**Scientific status:** No new dark-matter detection, gravity law, quantum-gravity result or independent peer-review acceptance is claimed.

[← Return to the research project](../README.md) · [Scientific boundaries](SCIENTIFIC_BOUNDARIES.md)
