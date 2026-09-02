from job_agent.evaluate import evaluate, load_labels


def test_evaluation_metrics_and_costs():
    predictions = [
        {"case_id": "C1", "action": "apply"},
        {"case_id": "C2", "action": "skip"},
        {"case_id": "C3", "action": "research"},
    ]
    result = evaluate(predictions, {"C1": "apply", "C2": "apply", "C3": "research"})
    assert result["correct"] == 2
    assert result["total_hypothetical_cost"] == 103
    assert result["confusion_matrix"]["apply"]["skip"] == 1


def test_loads_markdown_table_labels(tmp_path):
    labels = tmp_path / "labels.md"
    labels.write_text(
        "| Case | Mandatory | Evidence | Posting | Expected action |\n"
        "|---|---|---|---|---|\n"
        "| C17 | Pass | Pass | Pass | Apply |\n",
        encoding="utf-8",
    )
    assert load_labels(labels) == {"C17": "apply"}
