"""Step 0: cut Kazakhstan's bounding box out of the global Ookla files -> data_raw.csv.

Sources (downloaded 2026-11-25, see data_note.pdf):
  https://ookla-open-data.s3.amazonaws.com/parquet/performance/type=fixed/year=2025/quarter=3/2025-07-01_performance_fixed_tiles.parquet
  https://ookla-open-data.s3.amazonaws.com/parquet/performance/type=fixed/year=2026/quarter=3/2026-07-01_performance_fixed_tiles.parquet
  https://ookla-open-data.s3.amazonaws.com/parquet/performance/type=mobile/year=2026/quarter=3/2026-07-01_performance_mobile_tiles.parquet
The global files (~370 MB each) are not in the repo; this script rebuilds data_raw.csv from them.
No cleaning here: the box also holds tiles from Russia, China, Uzbekistan, Kyrgyzstan and
Turkmenistan. analysis.ipynb removes them.
"""
from pathlib import Path

import pandas as pd
import pyarrow.dataset as ds

HERE = Path(__file__).parent
BBOX = dict(lon_min=46.4, lon_max=87.4, lat_min=40.5, lat_max=55.5)  # Kazakhstan's extreme points
FILES = {("2025Q3", "fixed"): "data/raw/ookla_fixed_2025Q3.parquet",
         ("2026Q3", "fixed"): "data/raw/ookla_fixed_2026Q3.parquet",
         ("2026Q3", "mobile"): "data/raw/ookla_mobile_2026Q3.parquet"}

parts = []
for (quarter, network), path in FILES.items():
    d = ds.dataset(HERE / path)
    f = ((ds.field("tile_x") >= BBOX["lon_min"]) & (ds.field("tile_x") <= BBOX["lon_max"]) &
         (ds.field("tile_y") >= BBOX["lat_min"]) & (ds.field("tile_y") <= BBOX["lat_max"]))
    t = d.to_table(filter=f, columns=["quadkey", "tile_x", "tile_y", "avg_d_kbps", "avg_u_kbps",
                                      "avg_lat_ms", "tests", "devices"]).to_pandas()
    t.insert(0, "network", network)
    t.insert(0, "quarter", quarter)
    parts.append(t)
    print(quarter, network, len(t), "tiles in the box")
raw = pd.concat(parts, ignore_index=True)
raw.to_csv(HERE / "data_raw.csv", index=False)
print("data_raw.csv", raw.shape)
