#!/usr/bin/env python3
"""生成每周简报草稿:X(Twitter)帖子 + Newsletter Markdown。

内容 = 本周数据变更(git diff)+ 按周轮换的 3 个精选服务(indie>=4)。
输出: digests/YYYY-Wxx-x.md 与 digests/YYYY-Wxx-newsletter.md
用法: python scripts/gen_digest.py
"""
import subprocess
from datetime import date
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
DIGESTS = ROOT / "digests"
CN = {"ok": "国内可直连", "partial": "国内部分可用", "blocked": "国内需科学上网"}
CC = {"no": "无需信用卡", "yes": "需信用卡", "partial": "部分功能需信用卡"}


def load_all():
    cats = []
    for f in sorted((ROOT / "data" / "services").glob("*.yaml")):
        cats.append(yaml.safe_load(f.read_text(encoding="utf-8")))
    cats.sort(key=lambda c: c["order"])
    return cats


def week_changes():
    """过去 7 天 data/ 目录的提交摘要。"""
    try:
        log = subprocess.run(
            ["git", "log", "--since=7 days ago", "--pretty=- %s", "--", "data/"],
            cwd=ROOT, capture_output=True, text=True, check=True,
        ).stdout.strip()
        return [l for l in log.splitlines() if l.strip()]
    except Exception:  # noqa: BLE001
        return []


def picks(cats, week_no):
    """按周数轮换精选 3 个 indie>=4 的服务,保证每周不重样。"""
    pool = [(c, s) for c in cats for s in c["services"] if s["indie"] >= 4]
    if not pool:
        return []
    start = (week_no * 3) % len(pool)
    return [pool[(start + i) % len(pool)] for i in range(3)]


def main():
    today = date.today()
    year, week_no, _ = today.isocalendar()
    tag = f"{year}-W{week_no:02d}"
    DIGESTS.mkdir(exist_ok=True)

    meta = yaml.safe_load((ROOT / "data" / "meta.yaml").read_text(encoding="utf-8"))
    cats = load_all()
    total = sum(len(c["services"]) for c in cats)
    changes = week_changes()
    sel = picks(cats, week_no)

    # ---- X 帖子草稿(短,可直接复制发) ----
    x = [f"# X 帖子草稿 · {tag}", "", "> 复制下方内容直接发推,或拆成 Thread。", "", "---", ""]
    x.append(f"🧰 本周免费开发服务精选(第 {week_no} 期)\n")
    for c, s in sel:
        x.append(f"▸ {s['name']} · {c['icon']} {c['name']}")
        x.append(f"  {s['free_quota']} · {CC[str(s['credit_card'])]}\n")
    x.append(f"共收录 {total} 个免费服务,全部标注中国可用性 👇")
    x.append(meta["site_url"])
    x.append("\n#buildinpublic #indiehacker #免费资源 #独立开发")
    (DIGESTS / f"{tag}-x.md").write_text("\n".join(x), encoding="utf-8")

    # ---- Newsletter 草稿 ----
    n = [f"# FreeDev 中文周报 · {tag}", ""]
    n.append(f"你好,这里是 FreeDev 中文版周报——每周精选值得白嫖的开发者服务,当前共收录 {total} 个。")
    n.append("")
    n.append("## 🌟 本周精选")
    n.append("")
    for c, s in sel:
        n.append(f"### {s['name']}({c['icon']} {c['name']})")
        n.append("")
        n.append(s["desc"])
        n.append("")
        n.append(f"- **免费额度**:{s['free_quota']}")
        n.append(f"- **信用卡**:{CC[str(s['credit_card'])]}")
        n.append(f"- **中国可用性**:{CN[s['china']]}" + (f"({s['china_note']})" if s.get("china_note") else ""))
        n.append(f"- **Indie 适配度**:{'⭐' * s['indie']}")
        n.append(f"- 官网:{s['url']}")
        n.append("")
    n.append("## 🔄 本周数据变更")
    n.append("")
    if changes:
        n += changes
    else:
        n.append("- 本周无数据变更(巡检正常)。")
    n.append("")
    n.append(f"完整清单与筛选:{meta['site_url']}")
    n.append("")
    n.append("*本简报由脚本自动生成,发布前请人工过一遍。*")
    (DIGESTS / f"{tag}-newsletter.md").write_text("\n".join(n), encoding="utf-8")

    print(f"✅ 简报草稿已生成: digests/{tag}-x.md, digests/{tag}-newsletter.md")


if __name__ == "__main__":
    main()
