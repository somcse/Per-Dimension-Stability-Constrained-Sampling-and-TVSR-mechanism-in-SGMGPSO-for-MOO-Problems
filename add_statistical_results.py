import json
import os

JSON_PATH = os.path.join(os.path.dirname(__file__), "algorithm_results_summary.json")

WILCOXON_HV = [
    {"comparison": "SGMGPSO-PD-TVSR vs SGPSO",        "median_p_value": 4.6011e-04, "significant": True},
    {"comparison": "SGMGPSO-PD-TVSR vs MGPSO",        "median_p_value": 1.6391e-07, "significant": True},
    {"comparison": "SGMGPSO-PD-TVSR vs SGMGPSO",      "median_p_value": 2.6077e-08, "significant": True},
    {"comparison": "SGMGPSO-PD-TVSR vs SGMGPSO_PD",   "median_p_value": 1.8626e-09, "significant": True},
    {"comparison": "SGMGPSO-PD-TVSR vs SGMGPSO_TVSR", "median_p_value": 3.2391e-06, "significant": True},
]

WILCOXON_IGD = [
    {"comparison": "SGMGPSO-PD-TVSR vs SGPSO",        "median_p_value": 1.5537e-04, "significant": True},
    {"comparison": "SGMGPSO-PD-TVSR vs MGPSO",        "median_p_value": 4.5635e-07, "significant": True},
    {"comparison": "SGMGPSO-PD-TVSR vs SGMGPSO",      "median_p_value": 1.5985e-04, "significant": True},
    {"comparison": "SGMGPSO-PD-TVSR vs SGMGPSO_PD",   "median_p_value": 1.3318e-06, "significant": True},
    {"comparison": "SGMGPSO-PD-TVSR vs SGMGPSO_TVSR", "median_p_value": 3.9535e-06, "significant": True},
]

FRIEDMAN = {
    "HV":  {"chi2": 17.5510, "p_value": 3.5651e-03, "null_rejected": True,
            "note": "Algorithms perform significantly differently."},
    "IGD": {"chi2": 10.3265, "p_value": 6.6494e-02, "null_rejected": False,
            "note": "Null hypothesis not rejected at α=0.05."},
}

FUNCTIONS = [
    "WFG1","WFG2","WFG3","WFG4","WFG5","WFG6","WFG7","WFG8","WFG9",
    "ZDT1","ZDT2","ZDT3","ZDT4","ZDT6",
]

IGD_RANKS_RAW = {
    "WFG1": [1.00,  5.00,  2.00,  4.00,  3.00,  6.00],
    "WFG2": [2.00,  4.00,  5.00,  6.00,  1.00,  3.00],
    "WFG3": [5.00,  3.00,  1.00,  2.00,  4.00,  6.00],
    "WFG4": [2.00,  4.00,  1.00,  3.00,  5.00,  6.00],
    "WFG5": [3.00,  5.00,  2.00,  6.00,  4.00,  1.00],
    "WFG6": [6.00,  5.00,  1.00,  3.00,  4.00,  2.00],
    "WFG7": [6.00,  3.00,  2.00,  5.00,  4.00,  1.00],
    "WFG8": [2.00,  4.00,  1.00,  5.00,  3.00,  6.00],
    "WFG9": [5.00,  1.00,  2.00,  3.00,  4.00,  6.00],
    "ZDT1": [4.00,  5.00,  2.00,  6.00,  3.00,  1.00],
    "ZDT2": [6.00,  5.00,  3.00,  4.00,  1.00,  2.00],
    "ZDT3": [4.00,  5.00,  2.00,  6.00,  3.00,  1.00],
    "ZDT4": [5.00,  1.00,  3.00,  2.00,  4.00,  6.00],
    "ZDT6": [3.00,  1.00,  4.00,  5.00,  2.00,  6.00],
}
IGD_AVG = {"MGPSO": 3.86, "SGMGPSO": 3.64, "SGMGPSO-PD-TVSR": 2.21,
           "SGMGPSO_PD": 4.29, "SGMGPSO_TVSR": 3.21, "SGPSO": 3.79}

HV_RANKS_RAW = {
    "WFG1": [2.00,  5.00,  1.00,  4.00,  3.00,  6.00],
    "WFG2": [3.00,  4.00,  5.00,  6.00,  2.00,  1.00],
    "WFG3": [6.00,  4.00,  1.00,  5.00,  3.00,  2.00],
    "WFG4": [2.00,  4.00,  1.00,  5.00,  3.00,  6.00],
    "WFG5": [3.00,  5.00,  2.00,  6.00,  4.00,  1.00],
    "WFG6": [6.00,  5.00,  1.00,  4.00,  3.00,  2.00],
    "WFG7": [5.00,  4.00,  2.00,  6.00,  3.00,  1.00],
    "WFG8": [2.00,  4.00,  1.00,  5.00,  3.00,  6.00],
    "WFG9": [5.00,  1.00,  2.00,  3.00,  4.00,  6.00],
    "ZDT1": [4.00,  5.00,  2.00,  6.00,  3.00,  1.00],
    "ZDT2": [6.00,  5.00,  3.00,  4.00,  1.00,  2.00],
    "ZDT3": [4.00,  5.00,  2.00,  6.00,  3.00,  1.00],
    "ZDT4": [1.00,  1.00,  1.00,  1.00,  1.00,  1.00],
    "ZDT6": [4.00,  5.00,  1.00,  2.00,  3.00,  6.00],
}
HV_AVG = {"MGPSO": 3.79, "SGMGPSO": 4.07, "SGMGPSO-PD-TVSR": 1.79,
          "SGMGPSO_PD": 4.50, "SGMGPSO_TVSR": 2.79, "SGPSO": 3.00}

ALGO_COLS = ["MGPSO", "SGMGPSO", "SGMGPSO-PD-TVSR", "SGMGPSO_PD", "SGMGPSO_TVSR", "SGPSO"]


def build_rank_table(raw_dict, avg_dict, functions):
    """Convert flat raw rank arrays into a structured list of dicts."""
    rows = []
    for fn in functions:
        row = {"function": fn}
        for i, algo in enumerate(ALGO_COLS):
            row[algo] = raw_dict[fn][i]
        rows.append(row)
    return {
        "per_function": rows,
        "average_rank": avg_dict,
    }


def main():
    with open(JSON_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    statistical_analysis = {
        "_description": (
            "Statistical significance testing performed over 30 independent runs "
            "on 14 benchmark functions (ZDT1-6, WFG1-9). "
            "Wilcoxon signed-rank test (pairwise) and Friedman test (global)."
        ),
        "wilcoxon_signed_rank_test": {
            "_description": (
                "Pairwise Wilcoxon signed-rank test. "
                "Null hypothesis: no significant difference between SGMGPSO-PD-TVSR "
                "and the compared algorithm. Median p-value across 14 benchmarks reported."
            ),
            "HV": WILCOXON_HV,
            "IGD": WILCOXON_IGD,
        },
        "friedman_test": {
            "_description": (
                "Global Friedman test across all 6 algorithms and 14 benchmarks. "
                "Null hypothesis: all algorithms perform equally."
            ),
            "HV":  FRIEDMAN["HV"],
            "IGD": FRIEDMAN["IGD"],
        },
        "ranking_tables": {
            "_description": (
                "Per-function algorithm ranks (1 = best) computed from mean IGD/HV "
                "over 30 runs. Lower rank is better."
            ),
            "IGD_Mean": build_rank_table(IGD_RANKS_RAW, IGD_AVG, FUNCTIONS),
            "HV_Mean":  build_rank_table(HV_RANKS_RAW,  HV_AVG,  FUNCTIONS),
        },
    }

    data["statistical_analysis"] = statistical_analysis

    with open(JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"[OK] Updated: {JSON_PATH}")
    print(f"     Added top-level key: 'statistical_analysis'")
    print(f"       - wilcoxon_signed_rank_test  (HV: {len(WILCOXON_HV)} pairs, IGD: {len(WILCOXON_IGD)} pairs)")
    print(f"       - friedman_test              (HV & IGD)")
    print(f"       - ranking_tables             (IGD_Mean & HV_Mean, {len(FUNCTIONS)} functions)")


if __name__ == "__main__":
    main()
