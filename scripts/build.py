#!/usr/bin/env python3
"""构建脚本:校验 data/services/*.yaml → 生成 dist/(网站)+ README.md(中文清单)。

用法: python scripts/build.py
依赖: pip install pyyaml
"""
import json
import sys
from datetime import date
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data" / "services"
DIST = ROOT / "dist"

CC_VALUES = {"no", "yes", "partial"}
CN_VALUES = {"ok", "partial", "blocked"}
CC_MD = {"no": "✅ 无需", "yes": "⚠️ 需要", "partial": "🔶 部分"}
CN_MD = {"ok": "✅ 可直连", "partial": "🔶 部分可用", "blocked": "❌ 需科学上网"}
REQUIRED = ["name", "url", "desc", "free_quota", "credit_card", "china", "indie"]


def load_meta():
    return yaml.safe_load((ROOT / "data" / "meta.yaml").read_text(encoding="utf-8"))


def load_categories():
    cats, errors = [], []
    for f in sorted(DATA_DIR.glob("*.yaml")):
        cat = yaml.safe_load(f.read_text(encoding="utf-8"))
        for field in ("key", "name", "icon", "order", "services"):
            if field not in cat:
                errors.append(f"{f.name}: 缺少分类字段 {field}")
        for s in cat.get("services", []):
            sid = f"{f.name}/{s.get('name', '?')}"
            for field in REQUIRED:
                if field not in s or s[field] in (None, ""):
                    errors.append(f"{sid}: 缺少字段 {field}")
            if str(s.get("credit_card")) not in CC_VALUES:
                errors.append(f"{sid}: credit_card 必须是 {CC_VALUES}")
            if str(s.get("china")) not in CN_VALUES:
                errors.append(f"{sid}: china 必须是 {CN_VALUES}")
            if not isinstance(s.get("indie"), int) or not 1 <= s["indie"] <= 5:
                errors.append(f"{sid}: indie 必须是 1-5 的整数")
        cats.append(cat)
    if errors:
        print("❌ 数据校验失败:")
        for e in errors:
            print("  -", e)
        sys.exit(1)
    cats.sort(key=lambda c: c["order"])
    return cats


def build_json(cats, meta):
    total = sum(len(c["services"]) for c in cats)
    data = {
        "updated": date.today().isoformat(),
        "total": total,
        "repo": meta.get("repo", ""),
        "categories": cats,
    }
    DIST.mkdir(exist_ok=True)
    (DIST / "data.json").write_text(
        json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8"
    )
    # 把数据内嵌进 HTML,双击 file:// 打开也能用(无需本地服务器)
    html = (ROOT / "site" / "index.html").read_text(encoding="utf-8")
    payload = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    marker = '<script id="inline-data" type="application/json">'
    if marker not in html:
        raise SystemExit("❌ site/index.html 缺少 inline-data 标记")
    html = html.replace(marker, marker + payload, 1)
    (DIST / "index.html").write_text(html, encoding="utf-8")
    return total


def build_readme(cats, meta, total):
    L = []
    L.append(f"# 🧰 {meta['site_name']}")
    L.append("")
    L.append(f"> {meta['tagline']}")
    L.append("")
    L.append(
        f"精选 **{total} 个**对独立开发者最有价值的免费服务,每条均标注:"
        "**免费额度 · 是否需要信用卡 · 中国大陆可用性 · Indie Hacker 适配度(⭐1-5)**。"
    )
    L.append("")
    L.append(f"🌐 **在线浏览(可筛选/搜索):{meta['site_url']}**")
    L.append("")
    L.append(
        f"灵感来自 [free-for.dev]({meta['upstream']}),在其基础上做了中文化、"
        "结构化数据(YAML)、中国可用性标注与每周自动巡检。"
        "数据每周由 GitHub Actions 自动检查,仍可能过时,请以官网为准。"
    )
    L.append("")
    L.append("**图例**:💳 信用卡要求 · 🇨🇳 中国大陆直连情况 · ⭐ Indie 适配度")
    L.append("")
    L.append("## 目录")
    L.append("")
    for c in cats:
        L.append(f"- [{c['icon']} {c['name']}](#{c['key']}) ({len(c['services'])})")
    L.append("")
    for c in cats:
        L.append(f'<a id="{c["key"]}"></a>')
        L.append("")
        L.append(f"## {c['icon']} {c['name']}")
        L.append("")
        if c.get("desc"):
            L.append(f"> {c['desc']}")
            L.append("")
        L.append("| 服务 | 简介 | 免费额度 | 💳 信用卡 | 🇨🇳 中国 | ⭐ |")
        L.append("| --- | --- | --- | --- | --- | --- |")
        for s in c["services"]:
            note = f"<br>🌏 {s['china_note']}" if s.get("china_note") else ""
            L.append(
                f"| [{s['name']}]({s['url']}) | {s['desc']} | {s['free_quota']} "
                f"| {CC_MD[str(s['credit_card'])]} | {CN_MD[s['china']]}{note} "
                f"| {'⭐' * s['indie']} |"
            )
        L.append("")
    L.append("---")
    L.append("")
    L.append("## 参与共建")
    L.append("")
    L.append(
        "所有数据在 [`data/services/`](data/services/) 的 YAML 文件中,"
        "改一个字段、提一个 PR 即可。新增服务请填全部字段(见现有条目格式)。"
    )
    L.append("")
    L.append(f"*本 README 由 `scripts/build.py` 自动生成于 {date.today().isoformat()},请勿手改。*")
    (ROOT / "README.md").write_text("\n".join(L), encoding="utf-8")


def main():
    meta = load_meta()
    cats = load_categories()
    total = build_json(cats, meta)
    build_readme(cats, meta, total)
    print(f"✅ 构建完成:{len(cats)} 个分类 / {total} 个服务")
    print(f"   - dist/index.html + dist/data.json(网站)")
    print(f"   - README.md(中文清单)")


if __name__ == "__main__":
    main()
