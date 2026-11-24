# Kazakhtelecom: home internet breaks 50–150 km outside cities, not "in villages"

DA Project 2, Task 2 · Bekzat Kozy-Korpesh · group 05-P

**Problem:** home internet in Kazakhstan is slow (median 88 Mbps vs a world median of 119 Mbps), and users filed 67,544 complaints in 2025. Kazakhtelecom (~66% of fixed broadband) is wiring 3,000+ villages by 2027. The question is *which* villages and *which* fix.

**Bottleneck:** the edge of the city fibre ring.
- Villages within 50 km of a 100k+ city get a median of **94 Mbps**.
- Just past 50 km the median drops to **23 Mbps**, half of the tiles fall below 25 Mbps, and latency doubles (15 → 35 ms).
- Remote villages (250+ km) are better (41 Mbps). The trunk line stops at the suburban ring.

**Main results** (real data: 88,242 tiles, 855,745 fixed and mobile speed tests):
- **H0-4 rejected:** village speed near a city vs far from it is 94 vs 35 Mbps (p < 0.001). The same pattern holds in 2025 and with 3+ tests per tile.
- **H0-5 rejected, but the effect is tiny:** mobile beats home internet in 45.6% of village places vs 42.9% in cities. In villages fixed still wins (median 46 vs 36 Mbps), so **4G is not a substitute for fibre**. My own hypothesis was not supported, and the memo reports this openly.
- **Pairs 1–3 confirm the problem:** city 157 vs village 43 Mbps; 8.5% vs 41.9% of tiles below 25 Mbps; village median 15 → 43 Mbps in a year.

**Advice:**
- Extend trunk fibre outward through the 50–150 km belt (4,840 tiles, 51% below 25 Mbps), starting with North Kazakhstan, Akmola and Aktobe, before wiring isolated remote villages.
- Use 4G fixed-wireless only as a stopgap.

Start with **[memo.pdf](memo.pdf)** (1 page), then **[data_note.pdf](data_note.pdf)** (sources, columns, bias).

## Files

| file | what |
|---|---|
| `memo.pdf` | 1-page memo: problem → bottleneck → H1 → H0 → result → advice |
| `data_note.pdf` | sources with URLs and download date, data dictionary, bias check, what not to use it for |
| `hypotheses.md` | evidence, H0/H1 pairs and the city/village rule, written **before** the data was opened; pairs 4–5 added (dated) before mobile data was downloaded |
| `data_raw.csv` | Ookla fixed and mobile tiles in Kazakhstan's bounding box, as downloaded (194,851 rows) |
| `data_clean.csv` | clean data: Kazakhstan only, Mbps, region, settlement class (88,242 rows × 17 columns) |
| `analysis.ipynb` | raw → clean (every step logged), data dictionary, 5 hypothesis tests, robustness, charts |
| `cleaning_log.csv`, `data_dictionary.csv`, `results.csv`, `charts.png`, `charts_main.png` | outputs of the notebook |
| `extract_raw.py` | rebuilds `data_raw.csv` from the global Ookla files |
| `data/reference/` | Kazakhstan regions (geoBoundaries) and settlements (GeoNames) |

## Sources
- Ookla Speedtest Open Data, fixed tiles Q3 2025 and Q3 2026, mobile tiles Q3 2026, CC BY-NC-SA 4.0: https://github.com/teamookla/ookla-open-data
- geoBoundaries KAZ ADM1, CC BY 4.0: https://www.geoboundaries.org
- GeoNames KZ, CC BY 4.0: https://download.geonames.org/export/dump/
- Problem evidence: ranking.kz, zakon.kz, inform.kz, digitalbusiness.kz, Azattyq Ruhy (links in `hypotheses.md`)

## Reproduce

```bash
pip install -r requirements.txt
# download the three global files (190–370 MB each) into data/raw/ (URLs in extract_raw.py), then:
python extract_raw.py        # -> data_raw.csv
python build_notebook.py     # -> runs analysis.ipynb -> data_clean.csv, results.csv, charts.png
```

## Limits
- Ookla does not name the provider; the link to Kazakhtelecom rests on its ~66% fixed share.
- Speedtest users choose to test.
- Villages with no fixed line leave no data, so the real gap is probably larger.

Full bias check is in `data_note.pdf`.
