from django.shortcuts import render

ANALYSIS_METHODS = [
    {
        "name": "Disparity Baseline Audit",
        "category": "Business statistics",
        "question": "How unequal are outcomes across racial groups before controls?",
        "approach": "Group-level rates, lift metrics, confidence intervals, and visualization of variance.",
        "inputs": "Aggregated counts by group, decision outcomes, date range.",
    },
    {
        "name": "Two-Proportion / Rate Tests",
        "category": "Inference",
        "question": "Is a racial disparity statistically distinguishable from parity?",
        "approach": "Two-proportion z / chi-square tests with Holm-Bonferroni correction for multiple groups.",
        "inputs": "Binary outcomes per person, protected class indicator, sample size guidance.",
    },
    {
        "name": "Effect Size & Margin Bands",
        "category": "Inference",
        "question": "What is the magnitude and uncertainty around disparity?",
        "approach": "Risk difference and risk ratio with 95% CI; minimum detectable effect calculator.",
        "inputs": "Outcome rate, baseline rate, power/alpha preferences.",
    },
    {
        "name": "Propensity Score Weighting",
        "category": "Causal",
        "question": "Do disparities persist after balancing on covariates?",
        "approach": "Logistic PS model, IPTW, balance checks (SMD), stabilized weights.",
        "inputs": "Protected class, covariates (need, eligibility, location), outcome.",
    },
    {
        "name": "Difference-in-Differences",
        "category": "Causal",
        "question": "Did a policy change narrow or widen disparities?",
        "approach": "Pre/post trend checks, DID with group and time fixed effects, placebo periods.",
        "inputs": "Pre/post timestamps, treated vs. comparison groups, policy flag.",
    },
    {
        "name": "Hierarchical Bayes Rates",
        "category": "Advanced statistics",
        "question": "How do smaller geographies or agencies perform with partial pooling?",
        "approach": "Multilevel binomial models that borrow strength, posterior intervals for each unit.",
        "inputs": "Unit ids (office/precinct), group indicators, outcomes.",
    },
    {
        "name": "Logistic Regression Fairness Lens",
        "category": "Predictive + inference",
        "question": "What is the adjusted odds of a favorable outcome by race?",
        "approach": "Regularized logistic model with interpretable coefficients and marginal effects.",
        "inputs": "Row-level features (need, severity, income), protected class, outcome.",
    },
    {
        "name": "Random Forest Equity Audit",
        "category": "ML",
        "question": "Are complex nonlinear signals driving disparate outcomes?",
        "approach": "Sklearn RF with permutation importance, partial dependence, and counterfactual flips.",
        "inputs": "Cleaned feature matrix, group labels, outcome; fairness metrics per subgroup.",
    },
    {
        "name": "Uplift Modeling for Outreach",
        "category": "ML + causal inference",
        "question": "Which communities benefit most from outreach without widening gaps?",
        "approach": "Treatment/control uplift models, Qini curves, subgroup uplift fairness checks.",
        "inputs": "Intervention flag, engagement outcomes, subgroup indicators.",
    },
    {
        "name": "Survival / Hazard Models",
        "category": "Advanced statistics",
        "question": "Do time-to-service or exit rates differ by race?",
        "approach": "Cox PH / Aalen models, proportionality diagnostics, stratified baselines.",
        "inputs": "Event times, censoring flag, group indicator, confounders.",
    },
    {
        "name": "Outlier & Drift Guardrails",
        "category": "Monitoring",
        "question": "Are new decisions drifting toward bias or instability?",
        "approach": "Isolation Forest / KS drift tests on scores with subgroup slices and alerts.",
        "inputs": "Model scores over time, subgroup identifiers, monitoring cadence.",
    },
]

WORKFLOW_STEPS = [
    "Frame a single, testable hypothesis tied to a policy lever and protected class.",
    "Define units (person, application, precinct) and decision points where bias can enter.",
    "Map confounders and fairness-relevant covariates; declare inclusion/exclusion logic.",
    "Select the primary estimand (risk difference, risk ratio, uplift) and stopping rules.",
    "Pre-register data transformations and missingness handling to avoid p-hacking.",
    "Pick one analysis path, then precompute power/MDE to ensure sample adequacy.",
    "Run primary model; hold sensitivity checks (alternative specs, placebo tests) aside.",
    "Document governance: who approved, what data used, and accountability notes.",
    "Publish plain-language findings with uncertainty and recommended actions.",
    "Set monitoring thresholds and owners for drift, harm signals, and retraining.",
]

ACTIVE_HYPOTHESIS = {
    "title": "Equitable service approvals across racial groups after controlling for need and eligibility.",
    "why": "To ensure residents receive fair access to benefits and city contracts, and to detect structural disadvantages early.",
    "estimand": "Risk difference between protected and comparison groups for approval decisions.",
    "unit": "Individual application with decision outcome and timestamp.",
    "guardrails": [
        "No unreviewed PII; only hashed ids.",
        "Document covariates before modeling to avoid backfilling confounders.",
        "Use parity + benefit-harm framing (who is underserved, who is overburdened).",
    ],
}


def home(request):
    context = {
        "analysis_methods": ANALYSIS_METHODS,
        "workflow_steps": WORKFLOW_STEPS,
        "active_hypothesis": ACTIVE_HYPOTHESIS,
        "pillars": [
            "Transparency first: publish assumptions, confidence intervals, and caveats.",
            "Accountability: roles for analysts, data owners, and decision-makers.",
            "Kind culture: focus on structural fixes, not blame; include community review.",
            "Safety: minimize data collection, encrypt secrets, and track data lineage.",
        ],
    }
    return render(request, "core/home.html", context)
