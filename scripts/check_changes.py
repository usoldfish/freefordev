#!/usr/bin/env python3
"""每周巡检:1) 检查全部服务链接是否存活 2) 对比上游 free-for-dev 新增了哪些服务。

输出: reports/check-YYYY-MM-DD.md,并更新 data/upstream_snapshot.txt
用法: python scripts/check_changes.py
"""
import concurrent.futures as cf
import re
import urllib.request
from datetime import date
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
UPSTREAM_README = "https://raw.githubusercontent.com/ripienaar/free-for-dev/master/README.md"
SNAPSHOT = ROOT / "data" / "upstream_snapshot.txt"
REPORTS = ROOT / "reports"
UA = {"User-Agent": "Mozilla/5.0 (compatible; freefordev-cn-checker/1.0)"}


def load_services():
    out = []
    for f in sorted((ROOT / "data" / "services").glob("*.yaml")):
        cat = yaml.safe_load(f.read_text(encoding="utf-8"))
        for s in cat["services"]:
            out.append((cat["name"], s["name"], s["url"]))
    return out


def check_url(item):
    cat, name, url = item
    for method in ("HEAD", "GET"):
        try:
            req = urllib.request.Request(url, headers=UA, method=method)
            with urllib.request.urlopen(req, timeout=15) as r:
                return (cat, name, url, r.status, "")
        except Exception as e:  # noqa: BLE001
            err = str(e)
    # 4xx 常见于反爬(403/405),单独标注而非判死
    m = re.search(r"HTTP Error (\d+)", err)
    code = int(m.group(1)) if m else 0
    return (cat, name, url, code, err[:80])


def fetch_upstream_names():
    try:
        req = urllib.request.Request(UPSTREAM_README, headers=UA)
        with urllib.request.urlopen(req, timeout=30) as r:
            text = r.read().decode("utf-8", "ignore")
    except Exception as e:  # noqa: BLE001
        print(f"⚠️ 无法获取上游 README: {e}")
        return None
    # 上游条目格式:  * [Name](url) - description
    return sorted(set(re.findall(r"^\s*[*-] \[([^\]]+)\]\(http", text, re.M)))


def main():
    today = date.today().isoformat()
    REPORTS.mkdir(exist_ok=True)
    services = load_services()

    print(f"检查 {len(services)} 个链接…")
    with cf.ThreadPoolExecutor(max_workers=16) as ex:
        results = list(ex.map(check_url, services))

    dead = [r for r in results if r[3] == 0 or r[3] >= 500]
    suspicious = [r for r in results if 400 <= r[3] < 500 and r[3] not in (403, 405, 429)]

    upstream = fetch_upstream_names()
    new_upstream, removed_upstream = [], []
    if upstream is not None:
        old = SNAPSHOT.read_text(encoding="utf-8").splitlines() if SNAPSHOT.exists() else []
        if old:
            new_upstream = sorted(set(upstream) - set(old))
            removed_upstream = sorted(set(old) - set(upstream))
        SNAPSHOT.write_text("\n".join(upstream), encoding="utf-8")

    L = [f"# 每周巡检报告 {today}", ""]
    L.append(f"- 检查链接:{len(services)} 个;疑似失效:{len(dead)};异常状态:{len(suspicious)}")
    if upstream is not None:
        L.append(f"- 上游 free-for.dev 共 {len(upstream)} 条;新增 {len(new_upstream)},移除 {len(removed_upstream)}")
    L.append("")
    if dead:
        L += ["## ❌ 疑似失效链接(请人工确认)", ""]
        L += [f"- [{n}]({u})({c})— 状态 {s} {e}" for c, n, u, s, e in dead]
        L.append("")
    if suspicious:
        L += ["## ⚠️ 异常状态码", ""]
        L += [f"- [{n}]({u})({c})— 状态 {s}" for c, n, u, s, _ in suspicious]
        L.append("")
    if new_upstream:
        L += ["## 🆕 上游新增服务(评估是否收录)", ""]
        L += [f"- {n}" for n in new_upstream[:50]]
        L.append("")
    if removed_upstream:
        L += ["## 🗑️ 上游移除服务(评估是否下架)", ""]
        L += [f"- {n}" for n in removed_upstream[:50]]
        L.append("")
    if not (dead or suspicious or new_upstream or removed_upstream):
        L.append("✅ 本周一切正常,无需处理。")

    out = REPORTS / f"check-{today}.md"
    out.write_text("\n".join(L), encoding="utf-8")
    print(f"✅ 报告已生成: {out}")
    # 给 GitHub Actions 用的信号:有事要处理则退出码 78 之外的方案——用输出文件即可
    (REPORTS / "latest.md").write_text("\n".join(L), encoding="utf-8")


if __name__ == "__main__":
    main()
