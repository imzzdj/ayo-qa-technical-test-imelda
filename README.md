# AYO QA Technical Test — Imelda Rudyanto

## Studi Kasus 1
- Skrip: `tests/test_booking_validation.py`
- Data: `data/booking.csv`, `data/price_list.csv`
- Menangkap mismatch harga & double-book pada slot identik.
- Jalankan:
  ```bash
  python -m venv .venv && source .venv/bin/activate
  pip install -r requirements.txt
  pytest -q
  ```

## Studi Kasus 2 (Ringkasan)
- Website & App: area prioritas pengujian + mekanisme (E2E, API, Perf, Security, A11y).
- Rujukan publik: situs & store listing AYO.
