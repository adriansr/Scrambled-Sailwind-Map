#!/usr/bin/env python3
import sys
import json
from pathlib import Path

def update(data: dict, lat: float, lon: float) -> dict:
    d = [0, 0]
    c = data['coordinates']
    num_bodies = len(c)
    c0 = c[0]
    for coord in c0:
        d[0] += coord[0]
        d[1] += coord[1]
    d[0] /= len(c0)
    d[1] /= len(c0)
    d[0] = lon - d[0]
    d[1] = lat - d[1]
    for i in range(num_bodies):
        for j in range(len(c[i])):
            c[i][j][0] += d[0]
            c[i][j][1] += d[1]
    data['coordinates'] = c
    return data

def main(filepath: str, lat: float, lon: float):
    path = Path(filepath)
    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    updated = update(data, lat, lon)

    with path.open("w", encoding="utf-8") as f:
        json.dump(updated, f, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(f"Usage: {sys.argv[0]} <file.json> <LAT> <LON>")
        sys.exit(1)
    main(sys.argv[1], float(sys.argv[2]), float(sys.argv[3]))

