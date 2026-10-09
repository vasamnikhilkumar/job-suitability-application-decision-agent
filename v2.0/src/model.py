from __future__ import annotations

STATES = ("H1", "H2", "H3", "H4", "H5", "H6")
ACTIONS = ("apply", "research", "request human help", "skip")

PRIORS = {"H1": 0.25, "H2": 0.25, "H3": 0.15, "H4": 0.20, "H5": 0.10, "H6": 0.05}
TRUE_ACTION = {
    "H1": "apply", "H2": "research", "H3": "request human help",
    "H4": "skip", "H5": "skip", "H6": "request human help",
}

LIKELIHOODS = {
    "E1_fit": {
        "H1": {"strong": .80, "ambiguous": .15, "contradictory": .05},
        "H2": {"strong": .25, "ambiguous": .65, "contradictory": .10},
        "H3": {"strong": .35, "ambiguous": .55, "contradictory": .10},
        "H4": {"strong": .05, "ambiguous": .15, "contradictory": .80},
        "H5": {"strong": .45, "ambiguous": .35, "contradictory": .20},
        "H6": {"strong": .25, "ambiguous": .50, "contradictory": .25},
    },
    "E2_status": {
        "H1": {"active": .85, "unclear": .12, "inactive": .03},
        "H2": {"active": .65, "unclear": .30, "inactive": .05},
        "H3": {"active": .70, "unclear": .25, "inactive": .05},
        "H4": {"active": .65, "unclear": .25, "inactive": .10},
        "H5": {"active": .05, "unclear": .20, "inactive": .75},
        "H6": {"active": .30, "unclear": .45, "inactive": .25},
    },
    "E3_clarify": {
        "H1": {"confirms": .75, "judgment": .10, "refutes": .05, "unavailable": .10},
        "H2": {"confirms": .30, "judgment": .15, "refutes": .35, "unavailable": .20},
        "H3": {"confirms": .10, "judgment": .65, "refutes": .10, "unavailable": .15},
        "H4": {"confirms": .05, "judgment": .05, "refutes": .80, "unavailable": .10},
        "H5": {"confirms": .05, "judgment": .05, "refutes": .65, "unavailable": .25},
        "H6": {"confirms": .15, "judgment": .30, "refutes": .20, "unavailable": .35},
    },
}

# money units, minutes, and attention points (0 low, 1 medium, 2 high)
CHECK_COSTS = {
    "E1_fit": {"money": .20, "minutes": 4, "attention": .25, "failure": "resume evidence can be incomplete"},
    "E2_status": {"money": .10, "minutes": 2, "attention": .10, "failure": "platform signals can be stale"},
    "E3_clarify": {"money": .50, "minutes": 20, "attention": 1.00, "failure": "employer may not reply"},
}
TIME_COST_PER_MINUTE = .03
ATTENTION_COST_PER_POINT = .50

# Rows are true actions; columns are selected actions.
LOSS = {
    "apply": {"apply": 0, "research": 5, "request human help": 6, "skip": 100},
    "research": {"apply": 5, "research": 3, "request human help": 6, "skip": 100},
    "request human help": {"apply": 5, "research": 5, "request human help": 2, "skip": 100},
    "skip": {"apply": 5, "research": 5, "request human help": 6, "skip": 0},
}

# Original Week 1 costs used by frozen P0/P2/P3. Their flat low human-help cost
# produces the documented deferral trap; P3b uses the redesigned LOSS above.
LOSS_V1 = {
    "apply": {"apply": 0, "research": 3, "request human help": 2, "skip": 100},
    "research": {"apply": 5, "research": 0, "request human help": 2, "skip": 100},
    "request human help": {"apply": 5, "research": 3, "request human help": 0, "skip": 100},
    "skip": {"apply": 5, "research": 3, "request human help": 2, "skip": 0},
}

SEED = 20260910
N_CASES = 500
