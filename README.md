# SGMGPSO-FULL: Stability-Guided Multi-Guide Particle Swarm Optimization

A research project exploring and benchmarking multiple variants of Multi-Objective Particle Swarm Optimization (MOPSO) algorithms. This work builds incrementally from basic PSO formulations toward a fully enhanced optimizer — **SGMGPSO-FULL** — that consistently outperforms its predecessors across standard benchmark suites.

---

## What This Project Is About

Multi-objective optimization is a challenging problem in computational intelligence. Real-world engineering problems often involve conflicting objectives — you can't improve one without hurting another. Particle Swarm Optimization (PSO) is a population-based metaheuristic that mimics social behavior to search for good solutions, but applying it effectively to multi-objective problems requires careful design choices.

This project implements **six PSO-based algorithms**, each adding new ideas on top of the previous one. The goal was to understand how each enhancement — stability-guided parameter sampling, multi-guide velocity updates, archive management strategies, and adaptive mechanisms — contributes to overall performance. Every algorithm is evaluated on **14 well-known benchmark functions** (5 from the ZDT family and 9 from the WFG family) over **30 independent runs** each, using standard performance metrics.

---

## Algorithm Variants

| # | Algorithm | Key Idea |
|---|-----------|----------|
| 1 | **SGPSO** | Stability-guided inertia and acceleration sampling from the PSO stability region |
| 2 | **MGPSO** | Multi-guide approach with neighborhood (ring topology) and archive-based global guides |
| 3 | **SGMGPSO** | Combines stability-guided sampling with the multi-guide framework |
| 4 | **SGMGPSO-PP-PD** | Adds vectorized PP-PD (position-position, position-direction) stability sampling |
| 5 | **SGMGPSO-TVSR** | Introduces time-varying stability region with EMA-smoothed convergence signals |
| 6 | **SGMGPSO-FULL** | The complete variant — integrates all enhancements with adaptive tournament guide selection and crowding-distance-aware archive management |

Each variant builds on the one before it, so the progression tells a clear story of how incremental improvements affect optimization quality.

---

## Performance Metrics

Two standard indicators are used to evaluate the quality of the obtained Pareto fronts:

- **IGD (Inverted Generational Distance)** — Measures how close the obtained front is to the true Pareto front. *Lower is better.*
- **HV (Hypervolume)** — Measures the volume of objective space dominated by the obtained front. *Higher is better.*

---

## Key Results

After running all six algorithms on 14 benchmarks (30 trials each), the average rank across all functions tells the story:

### IGD Ranking (lower rank = better convergence)

| Algorithm | Average Rank |
|-----------|:------------:|
| **SGMGPSO-FULL** | **2.29** |
| SGMGPSO-TVSR | 2.93 |
| SGPSO | 3.57 |
| SGMGPSO | 3.86 |
| SGMGPSO-PD | 4.07 |
| MGPSO | 4.29 |

### HV Ranking (lower rank = better coverage)

| Algorithm | Average Rank |
|-----------|:------------:|
| **SGMGPSO-FULL** | **1.86** |
| SGMGPSO-TVSR | 2.71 |
| SGPSO | 2.93 |
| SGMGPSO | 3.79 |
| MGPSO | 4.00 |
| SGMGPSO-PD | 4.64 |

SGMGPSO-FULL ranks first in both metrics, and its low standard deviation (1.33 for IGD, 1.10 for HV) shows it performs consistently well — not just on a few easy problems but across the board.

---

## Project Structure

```
SGMGPSO_FULL/
│
├── sgpso-model.ipynb              # Model 1: Stability-Guided PSO
├── mgpso-model.ipynb              # Model 2: Multi-Guide PSO
├── sgmgpso-model.ipynb            # Model 3: Combined SG + MG approach
├── sgmgpso-pp-pd-model.ipynb      # Model 4: With PP-PD stability sampling
├── sgmgpso-tvsr-model.ipynb       # Model 5: With time-varying shift ratio
├── finale-model(sgmgpso-full).ipynb  # Model 6: Full enhanced variant
│
├── ranks-test.ipynb               # Rank comparison
│
├── results/                       # All experimental results
│   ├── SGPSO/
│   │   ├── summary.csv            # Aggregated metrics across benchmarks
│   │   ├── zdt1/metrics.csv       # Per-run metrics for each function
│   │   ├── zdt2/
│   │   └── ...
│   ├── MGPSO/
│   ├── SGMGPSO/
│   ├── SGMGPSO_PP_PD/
│   ├── SGMGPSO_TVSR/
│   └── SGMGPSO_FULL/
│
├── rank_comparison_IGD_Mean.csv    # IGD rank table across all algorithms
├── rank_comparison_HV_Mean.csv     # HV rank table across all algorithms
├── IGD_Mean_win_loss_rank_table.csv  # Pairwise win/loss analysis (IGD)
├── HV_Mean_win_loss_rank_table.csv   # Pairwise win/loss analysis (HV)
└── algorithm_results_summary.json    # Consolidated results in JSON format
```

---

## Benchmark Functions

### ZDT Test Suite (2-objective)
| Function | Variables | Characteristics |
|----------|:---------:|-----------------|
| ZDT1 | 30 | Convex Pareto front |
| ZDT2 | 30 | Non-convex Pareto front |
| ZDT3 | 30 | Disconnected Pareto front |
| ZDT4 | 10 | Multimodal (many local fronts) |
| ZDT6 | 10 | Non-uniform density |

### WFG Test Suite (3-objective)
| Function | Variables | Objectives | Characteristics |
|----------|:---------:|:----------:|-----------------|
| WFG1–WFG9 | 24 | 3 | Mixed separability, modality, bias, and geometry |

---

## How to Run

### Prerequisites

```bash
pip install pymoo numpy pandas matplotlib
```

### Running a Model

Each notebook is self-contained. Open any model notebook (e.g., `finale-model(sgmgpso-full).ipynb`) in Jupyter and run all cells. It will:

1. Define the algorithm
2. Run 30 independent trials on all 14 benchmarks
3. Compute IGD and HV for each trial
4. Save per-function metrics to `results/{ALGO_NAME}/{function}/metrics.csv`
5. Save a summary to `results/{ALGO_NAME}/summary.csv`
6. Generate Pareto front comparison plots

### Running the Rank Comparison

After all models have been executed, open `ranks-test-local.ipynb` and run it. This will:

- Load all `summary.csv` files from the `results/` directory
- Compute per-function ranks for each algorithm
- Generate win/loss/net/rank tables
- Export the comparison tables as CSV files

---

## Dependencies

| Package | Purpose |
|---------|---------|
| `pymoo` | Multi-objective optimization framework, benchmark problems, performance indicators |
| `numpy` | Numerical computation |
| `pandas` | Data handling and CSV I/O |
| `matplotlib` | Pareto front visualization |

---

## Experimental Setup

| Parameter | Value |
|-----------|-------|
| Population size | 150 particles |
| Independent runs | 30 per benchmark |
| Generations (ZDT) | 300 (500 for ZDT4) |
| Generations (WFG) | 400 |
| Archive size | 300 |
| Mutation | Polynomial (η = 20) |
| Neighborhood | Ring topology (radius = 3) |
| HV reference point (ZDT) | [2.5, 2.5] |
| HV reference point (WFG) | [3.0, 5.0, 7.0] |

---

## Notes

- The `ranks-test.ipynb` file does the analysis using the local `results/` directory structure.
- Each model notebook includes publication-quality Pareto front plots (2D for ZDT, 3D for WFG) comparing the obtained solutions against the true Pareto front.
- All results in the `results/` folder are from actual experimental runs and can be reproduced by re-executing the model notebooks.
