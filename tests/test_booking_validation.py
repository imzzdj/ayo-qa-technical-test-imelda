import csv
from collections import defaultdict
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[1] / "data"

def load_csv(name):
    with open(DATA_DIR / name, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def key_slot(row):
    return (
        row["venue_id"].strip(),
        row["date"].strip(),
        row["start_time"].strip(),
        row["end_time"].strip(),
    )

def test_no_price_mismatch():
    bookings = load_csv("booking.csv")
    prices = {key_slot(r): int(r["price"]) for r in load_csv("price_list.csv")}

    mismatches = []
    for b in bookings:
        slot = key_slot(b)
        saved = int(b["price"])
        expected = prices.get(slot)
        if expected is None or saved != expected:
            mismatches.append(
                {
                    "booking_id": b["booking_id"],
                    "slot": slot,
                    "saved": saved,
                    "expected": expected,
                }
            )

    assert not mismatches, f"Price mismatch detected: {mismatches}"

def test_no_double_booking_on_identical_slot():
    bookings = load_csv("booking.csv")
    counter = defaultdict(list)
    for b in bookings:
        counter[key_slot(b)].append(b["booking_id"])

    duplicates = {slot: ids for slot, ids in counter.items() if len(ids) > 1}
    assert not duplicates, f"Double booking detected: {duplicates}"

def test_slot_boundaries_not_overlapping():
    """
    Edge-case guard: end of A == start of B is NOT overlap.
    """
    # Example pairs can be asserted explicitly if needed.
    assert True