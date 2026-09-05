#!/usr/bin/env python3
"""BubR1 AlphaFold (AF-O60566-F1 v6) geometry around N1002 and MVA reference residues.
Public protein-level data only. No patient data touched."""
import sys, json, math
cif = sys.argv[1] if len(sys.argv) > 1 else "work/track2/AF-O60566-F1-model_v6.cif"
atoms = []
for line in open(cif):
    if not line.startswith("ATOM"):
        continue
    f = line.split()
    # _atom_site fields: group id type_symbol label_atom_id . label_comp_id label_asym_id ...
    name, res, resi = f[3], f[5], int(f[8])
    x, y, z, plddt = float(f[10]), float(f[11]), float(f[12]), float(f[14])
    atoms.append((resi, res, name, x, y, z, plddt))
byres = {}
for a in atoms:
    byres.setdefault(a[0], []).append(a)
seq = {r: v[0][1] for r, v in byres.items()}
def plddt(r):
    return sum(a[6] for a in byres[r]) / len(byres[r])
def sidechain(r):
    sc = [a for a in byres[r] if a[2] not in ("N", "CA", "C", "O")]
    return sc or byres[r]
def mindist(r1, r2):
    return min(math.dist(a[3:6], b[3:6]) for a in byres[r1] for b in byres[r2])
def cb(r):
    for a in byres[r]:
        if a[2] == "CB":
            return a[3:6]
    for a in byres[r]:
        if a[2] == "CA":
            return a[3:6]
def neighbours(r, cut=8.0):
    c = cb(r)
    return sorted(q for q in byres if q != r and math.dist(cb(q), c) <= cut)
def burial(r, cut=10.0):
    """count of CB atoms within cut A: crude burial proxy"""
    c = cb(r)
    return sum(1 for q in byres if q != r and math.dist(cb(q), c) <= cut)
targets = [1002, 1008, 1012, 921, 909, 844, 814, 795, 882, 911, 737, 792, 1042, 1043]
out = {"model": cif, "residues": {}}
for r in targets:
    if r not in byres:
        continue
    out["residues"][r] = {
        "aa": seq[r], "plddt": round(plddt(r), 1),
        "cb_neighbours_10A": burial(r),
        "neighbours_8A": neighbours(r),
    }
pairs = [(1002, 1008), (1002, 1012), (1002, 882), (1002, 795), (1002, 911), (1002, 909), (1002, 921), (1002, 844), (1002, 814)]
out["min_heavy_atom_distance_A"] = {f"{a}-{b}": round(mindist(a, b), 2) for a, b in pairs if a in byres and b in byres}
dom = [r for r in byres if 766 <= r <= 1050]
out["kinase_domain_mean_plddt"] = round(sum(plddt(r) for r in dom) / len(dom), 1)
bur = sorted((burial(r), r) for r in dom)
out["burial_rank_of_1002_in_domain"] = {
    "value": burial(1002),
    "percentile": round(100 * sum(1 for b, _ in bur if b < burial(1002)) / len(bur), 1),
    "domain_median": bur[len(bur) // 2][0],
}
print(json.dumps(out, indent=1))
