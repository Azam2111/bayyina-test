# -*- coding: utf-8 -*-
"""A2 yakuniy imtihon (klassik guruh uchun) — mustaqil HTML qurish."""
import json, random, re, unicodedata, sys, os
from content_qiroat_kitoba import QIROAT, KITOBA

# Manba papkalar: skript joylashgan papkadan bir pogona yuqorida
# ("placement testla" ildizi). Boshqa joyda bolsa: BAYYINA_SRC muhit ozgaruvchisi.
BASE = os.environ.get("BAYYINA_SRC") or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if not os.path.isdir(os.path.join(BASE, "A2_QOVAID_TESTLAR_JSON")) and os.path.isdir("/mnt/user-data/uploads"):
    BASE = "/mnt/user-data/uploads"
SRC_Q = os.path.join(BASE, "A2_QOVAID_TESTLAR_JSON", "a2_{n}_qovaid.json")
SRC_M = os.path.join(BASE, "A2_MUFRADOT_TESTLAR_JSON", "a2_{n}_mufradot.json")
SRC_I = os.path.join(BASE, "A2_ISTIMA_TESTLAR_JSON", "a2_{n}_istima.json")
ISTIMA_LESSONS = [3, 4, 11]
SEED = 20260915

# Savol manbasi:
#   "tanvir" — Tanvirdagi mavjud A2 yakuniy imtihonning AYNAN OZI (testlar/a2_yakuniy.json,
#              200 savol) mufradot/qovaid boyicha ajratiladi. Azamning 2026-09-16 qarori.
#   "sample" — bazadan yangi tasodifiy tanlov (har darsdan 8 tadan, SEED boyicha).
SOURCE = "tanvir"
HERE = os.path.dirname(os.path.abspath(__file__))
YAKUNIY = os.path.join(HERE, "testlar", "a2_yakuniy.json")
if not os.path.exists(YAKUNIY):
    YAKUNIY = "/mnt/user-data/uploads/bayyina-test/testlar/a2_yakuniy.json"

HARAKAT = re.compile(r"[ً-ْٰـ]")

def nrm(t):
    t = HARAKAT.sub("", str(t or ""))
    t = re.sub(r"\s+", " ", t).strip().lower()
    return t

def load(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)

def pick(kind, src, per_lesson, target, rng):
    """Har darsdan teng olib, yetmagani kop savolli darslardan toldiriladi."""
    pools, chosen, seen = {}, [], set()
    for n in range(1, 13):
        d = load(src.format(n=n))
        qs = [q for q in d["questions"] if q.get("opts") and len(set(q["opts"])) == len(q["opts"]) >= 2]
        rng.shuffle(qs)
        pools[n] = qs
    for n in range(1, 13):
        took = 0
        for q in pools[n]:
            if took >= per_lesson:
                break
            k = nrm(q["q"])
            if k in seen:
                continue
            seen.add(k)
            q = dict(q); q["dars"] = n
            chosen.append(q); took += 1
        pools[n] = [q for q in pools[n] if nrm(q["q"]) not in seen]
    # qolgan joyni toldirish (eng kop qolgan darsdan navbatma-navbat)
    while len(chosen) < target:
        n = max(pools, key=lambda k: len(pools[k]))
        if not pools[n]:
            break
        q = pools[n].pop(0)
        k = nrm(q["q"])
        if k in seen:
            continue
        seen.add(k)
        q = dict(q); q["dars"] = n
        chosen.append(q)
    rng.shuffle(chosen)
    return chosen[:target]

def clean(q):
    return {"q": q["q"], "opts": q["opts"], "correct": q["correct"],
            "izoh": q.get("izoh", ""), "dars": q.get("dars")}

def is_mufradot(q):
    """Tanvir yakuniy imtihonida mufradot savollari ikki shablonda:
    «X» - to'g'ri tarjimasi?  /  «X» so'zining ma'nosi?"""
    t = q["q"].strip()
    return ("tarjima" in t) or (t.startswith("«") and
                                re.search(r"ma[''']nosi\?$", t) is not None)

def from_tanvir():
    qs = load(YAKUNIY)["questions"]
    muf = [clean(q) for q in qs if is_mufradot(q)]
    qov = [clean(q) for q in qs if not is_mufradot(q)]
    return qov, muf

def main():
    rng = random.Random(SEED)
    if SOURCE == "tanvir":
        qovaid, mufradot = from_tanvir()
    else:
        qovaid = [clean(q) for q in pick("qovaid", SRC_Q, 8, 100, rng)]
        mufradot = [clean(q) for q in pick("mufradot", SRC_M, 8, 100, rng)]

    istima_groups = []
    for n in ISTIMA_LESSONS:
        d = load(SRC_I.format(n=n))
        istima_groups.append({
            "title": d["title"],
            "audio": "audio/" + d["audio"],
            "tinglash": d.get("tinglash", 2),
            "questions": [{"q": q["q"], "opts": q["opts"], "correct": q["correct"],
                           "izoh": q.get("izoh", "")} for q in d["questions"]],
        })

    qiroat_groups = [{"title": g["title"], "matn": g["matn"], "questions": g["questions"]} for g in QIROAT]

    exam = {
        "meta": {
            "title": "A2 — Yakuniy imtihon (klassik guruh)",
            "subtitle": "Bayyina Akademiya · grammatika, lug'at, tinglash, o'qish va yozish bo'limlari",
            "pass": 80,
            "write_pass": 0.85,
            "write_half": 0.70,
            "write_cov": 0.90,
            "write_cov_half": 0.65,
            "version": "v2 · manba: " + SOURCE,
        },
        "sections": [
            {"id": "qovaid", "name": "1. Qovaid (grammatika)", "type": "mcq", "minutes": 55, "weight": 30,
             "desc": str(len(qovaid)) + " ta test. Har savolda bitta to'g'ri javob.", "questions": qovaid},
            {"id": "mufradot", "name": "2. Mufradot (lug'at)", "type": "mcq", "minutes": 40, "weight": 30,
             "desc": str(len(mufradot)) + " ta test. So'zning to'g'ri tarjimasini tanlang.", "questions": mufradot},
            {"id": "istima", "name": "3. Istima (tinglab tushunish)", "type": "group", "minutes": 25, "weight": 15,
             "desc": "3 ta audio. Har audioni eng ko'pi 2 marta tinglash mumkin.", "groups": istima_groups},
            {"id": "qiroat", "name": "4. Qiroat (o'qib tushunish)", "type": "group", "minutes": 20, "weight": 15,
             "desc": "2 ta matn. Matnni o'qib, savollarga javob bering.", "groups": qiroat_groups},
            {"id": "kitoba", "name": "5. Kitoba (yozish)", "type": "write", "minutes": 25, "weight": 10,
             "desc": "10 ta gapni arabchaga tarjima qiling.", "items": KITOBA},
        ],
    }

    data = json.dumps(exam, ensure_ascii=False, separators=(",", ":"))
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"_a2_klassik_template.html"), encoding="utf-8") as f:
        tpl = f.read()
    start = tpl.index("/*__DATA__*/")
    end = tpl.index("/*__ENDDATA__*/") + len("/*__ENDDATA__*/")
    out = tpl[:start] + data + tpl[end:]
    with open("a2_yakuniy_klassik.html", "w", encoding="utf-8") as f:
        f.write(out)
    with open("exam_data.json", "w", encoding="utf-8") as f:
        json.dump(exam, f, ensure_ascii=False, indent=1)

    tot = sum(len(s.get("questions") or s.get("items") or []) if s["type"] != "group"
              else sum(len(g["questions"]) for g in s["groups"]) for s in exam["sections"])
    print("qovaid:", len(qovaid), "mufradot:", len(mufradot),
          "istima:", sum(len(g["questions"]) for g in istima_groups),
          "qiroat:", sum(len(g["questions"]) for g in qiroat_groups),
          "kitoba:", len(KITOBA), "JAMI:", tot)
    print("HTML hajmi:", round(os.path.getsize("a2_yakuniy_klassik.html") / 1024), "KB")

if __name__ == "__main__":
    main()
