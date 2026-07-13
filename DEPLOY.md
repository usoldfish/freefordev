# 🚀 部署指南(5 分钟上线)

## 1. 创建 GitHub 仓库并推送

在 [github.com/new](https://github.com/new) 创建仓库(如 `freefordev`,Public),然后在本文件夹执行:

```bash
rm -f .git/index.lock .git/HEAD.lock .git/objects/maintenance.lock  # 清理沙盒残留锁文件
git add -A && git commit -m "fix: 数据内嵌进 HTML,支持双击打开"      # 提交最后一次修复
git remote add origin https://github.com/你的用户名/freefordev.git
git branch -M main
git push -u origin main
```

> 本地 git 已初始化并完成首次提交,只需以上 4 条命令。

## 2. 开启 GitHub Pages

仓库页面 → **Settings → Pages → Build and deployment → Source** 选 **GitHub Actions**。

推送后 `deploy.yml` 会自动构建并发布,网址为
`https://你的用户名.github.io/freefordev/`。

## 3. 改两处配置

- `data/meta.yaml`:把 `repo` 和 `site_url` 里的 `YOUR_USERNAME` 换成你的用户名,提交推送(README 和网站链接会自动更新)。
- (可选)绑自定义域名:Settings → Pages → Custom domain。

## 4. 每周自动化(无需配置)

`weekly.yml` 每周一北京时间 09:00 自动:

1. 巡检全部 130 个链接是否存活
2. 对比上游 free-for.dev 的新增/移除服务
3. 生成 X 帖子草稿 + Newsletter 草稿(`digests/` 目录)
4. 提交结果并开一个 Issue 提醒你审核

也可以随时在 **Actions → 每周巡检 + 简报生成 → Run workflow** 手动触发。

## 日常维护

- 增删改服务:编辑 `data/services/*.yaml`(每条 7 个字段,照抄现有格式)
- 本地预览:`python scripts/build.py && cd dist && python3 -m http.server`
- README 是自动生成的,不要手改

## 常用命令

```bash
pip install pyyaml                 # 唯一依赖
python scripts/build.py            # 构建网站 + README
python scripts/check_changes.py    # 手动巡检
python scripts/gen_digest.py       # 手动生成简报
```
