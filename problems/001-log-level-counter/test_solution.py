from solution import count_log_levels


def test_basic_counts():
    lines = [
        "2026-10-06 12:00:01 INFO Server started",
        "2026-10-06 12:00:05 ERROR Database connection failed",
        "2026-10-06 12:01:00 INFO Request received",
    ]
    assert count_log_levels(lines) == {"INFO": 2, "ERROR": 1}


def test_case_insensitive_levels():
    lines = [
        "2026-10-06 12:00:01 error a",
        "2026-10-06 12:00:02 Error b",
        "2026-10-06 12:00:03 ERROR c",
    ]
    assert count_log_levels(lines) == {"ERROR": 3}


def test_empty_input():
    assert count_log_levels([]) == {}


def test_invalid_lines_ignored():
    lines = ["", "garbage", "2026-10-06 12:00:00 VERBOSE hi", "2026-10-06 12:00:00"]
    assert count_log_levels(lines) == {}


def test_message_is_optional():
    assert count_log_levels(["2026-10-06 12:00:00 WARNING"]) == {"WARNING": 1}


def test_input_not_modified():
    lines = ["2026-10-06 12:00:00 INFO hi", "bad"]
    snapshot = list(lines)
    count_log_levels(lines)
    assert lines == snapshot
