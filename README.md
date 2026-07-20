# 🧰 FreeDev 中文版

> 开发者免费服务情报库 · 为 Indie Hacker 而生

精选 **130 个**对独立开发者最有价值的免费服务,每条均标注:**免费额度 · 是否需要信用卡 · 中国大陆可用性 · Indie Hacker 适配度(⭐1-5)**。

🌐 **在线浏览(可筛选/搜索):https://usoldfish.github.io/freefordev/**

灵感来自 [free-for.dev](https://github.com/ripienaar/free-for-dev),在其基础上做了中文化、结构化数据(YAML)、中国可用性标注与每周自动巡检。数据每周由 GitHub Actions 自动检查,仍可能过时,请以官网为准。

**图例**:💳 信用卡要求 · 🇨🇳 中国大陆直连情况 · ⭐ Indie 适配度

## 目录

- [🌐 静态网站托管](#static-hosting) (8)
- [🚀 应用托管 / PaaS](#paas) (8)
- [⚡ Serverless / 边缘函数](#serverless) (6)
- [🗄️ 数据库](#database) (9)
- [🔐 后端即服务 / 用户认证](#baas-auth) (7)
- [💰 支付 / 变现](#payments) (6)
- [📧 邮件发送 / Newsletter](#email) (8)
- [📊 数据分析 / 统计](#analytics) (7)
- [🩺 监控 / 日志 / 报错](#monitoring) (7)
- [🔧 代码托管 / CI-CD](#devops) (6)
- [📦 CDN / DNS / 域名 / 存储](#cdn-dns-storage) (9)
- [🤖 AI / LLM API](#ai) (10)
- [🖼️ 图片 / 媒体 / 内容管理](#media-content) (9)
- [📝 表单 / 搜索](#forms-search) (6)
- [🔔 自动化 / 消息通知](#automation-notify) (9)
- [🛠️ 内网穿透 / 开发工具 / API 数据](#network-devtools) (9)
- [🎨 设计 / 素材工具](#design) (6)

<a id="static-hosting"></a>

## 🌐 静态网站托管

> 托管落地页、文档站、纯前端应用的免费方案,Indie 出海第一站。

| 服务 | 简介 | 免费额度 | 💳 信用卡 | 🇨🇳 中国 | ⭐ |
| --- | --- | --- | --- | --- | --- |
| [Cloudflare Pages](https://pages.cloudflare.com) | Cloudflare 的静态站/全栈托管,配合 Workers 可跑动态逻辑,免费层几乎无限量。 | 无限站点、无限带宽、每月 500 次构建,支持自定义域名与免费 SSL | ✅ 无需 | 🔶 部分可用<br>🌏 pages.dev 默认域名在国内不稳,绑自定义域名后基本可用但速度一般 | ⭐⭐⭐⭐⭐ |
| [Vercel](https://vercel.com) | Next.js 官方平台,前端部署体验天花板,Hobby 免费计划对个人项目足够。 | Hobby 计划:100GB 带宽/月、Serverless 函数、预览部署、自定义域名 | ✅ 无需 | 🔶 部分可用<br>🌏 vercel.app 域名被墙,必须绑自定义域名;商业项目禁用 Hobby 计划 | ⭐⭐⭐⭐⭐ |
| [Netlify](https://www.netlify.com) | 老牌 Jamstack 托管,表单、身份验证、边缘函数一应俱全。 | 100GB 带宽/月、300 分钟构建/月、边缘函数 100 万次调用 | ✅ 无需 | 🔶 部分可用<br>🌏 国内访问慢,建议套 CDN 或换 Cloudflare Pages | ⭐⭐⭐⭐ |
| [GitHub Pages](https://pages.github.com) | 白嫖界元老,仓库即网站,配合 Actions 可自动构建任何静态框架。 | 免费托管公开仓库网站,1GB 空间、100GB 带宽/月(软限制) | ✅ 无需 | 🔶 部分可用<br>🌏 国内时通时断,严肃项目建议加自定义域名 + Cloudflare | ⭐⭐⭐⭐⭐ |
| [Render(静态站)](https://render.com) | Render 的静态站点托管永久免费,全球 CDN 分发,自动从 Git 部署。 | 静态站点免费不限数量,100GB 出站带宽/月 | ✅ 无需 | 🔶 部分可用<br>🌏 onrender.com 可访问但速度一般 | ⭐⭐⭐⭐ |
| [Zeabur](https://zeabur.com) | 华人团队做的部署平台,中文界面、支持支付宝/微信付款,对国内开发者极友好。 | 免费计划可部署静态站点与体验级服务(Serverless 计划按量,静态免费) | ✅ 无需 | ✅ 可直连<br>🌏 中文文档齐全,可用支付宝付费升级,亚太节点速度好 | ⭐⭐⭐⭐⭐ |
| [Surge.sh](https://surge.sh) | 命令行一条 `surge` 即发布,做 demo 和临时页面最快。 | 无限项目、自定义域名、免费 SSL(*.surge.sh) | ✅ 无需 | 🔶 部分可用 | ⭐⭐⭐ |
| [Firebase Hosting](https://firebase.google.com/products/hosting) | Google 系静态托管,和 Firestore/Auth 全家桶联动方便。 | 10GB 存储、360MB/天 流量、自定义域名与 SSL | ✅ 无需 | ❌ 需科学上网<br>🌏 Google 系服务国内无法直连,面向海外用户可放心用 | ⭐⭐⭐ |

<a id="paas"></a>

## 🚀 应用托管 / PaaS

> 跑后端、API、容器的托管平台。注意:近年免费层普遍缩水,标注以 2026-07 核实为准。

| 服务 | 简介 | 免费额度 | 💳 信用卡 | 🇨🇳 中国 | ⭐ |
| --- | --- | --- | --- | --- | --- |
| [Render](https://render.com) | Heroku 精神继承者,三大 PaaS 中唯一保留永久免费 Web 服务的平台。 | 免费 Web 服务(512MB 内存,15 分钟无流量后休眠,冷启动 30-60 秒)+ 免费 PostgreSQL(30 天) | ✅ 无需 | 🔶 部分可用 | ⭐⭐⭐⭐⭐ |
| [Koyeb](https://www.koyeb.com) | 欧洲 Serverless 容器平台,免费层可跑一个常驻小服务。 | 1 个免费 Web 服务(512MB)+ 1 个免费 PostgreSQL(50 小时/月) | ✅ 无需 | 🔶 部分可用 | ⭐⭐⭐⭐ |
| [Railway](https://railway.com) | 体验极佳的部署平台,但已无免费层——只有一次性 $5 试用金,用完需绑卡。 | 仅一次性 $5 试用额度;Hobby $5/月(含 $5 用量) | ⚠️ 需要 | 🔶 部分可用<br>🌏 2026 年起取消预付费,必须绑后付费银行卡 | ⭐⭐⭐ |
| [Fly.io](https://fly.io) | 全球边缘部署容器,技术优秀,但 2024 年起新用户已无免费额度。 | 无免费层;新用户仅 7 天/2 VM 小时试用,之后按量付费 | ⚠️ 需要 | 🔶 部分可用 | ⭐⭐ |
| [Google Cloud Run](https://cloud.google.com/run) | 按请求计费的容器平台,免费额度对低流量 API 几乎等于白嫖。 | 每月 200 万次请求、36 万 GB-秒内存、18 万 vCPU-秒 | ⚠️ 需要 | ❌ 需科学上网<br>🌏 注册 GCP 需绑外币卡;服务本身国内无法直连 | ⭐⭐⭐ |
| [Oracle Cloud Free Tier](https://www.oracle.com/cloud/free/) | 业界最慷慨的永久免费 VPS:4 核 ARM + 24GB 内存,白嫖神话(但注册风控严)。 | 永久免费:4 OCPU ARM + 24GB 内存、2 台 AMD 小实例、200GB 存储、10TB 流量/月 | ⚠️ 需要 | ✅ 可直连<br>🌏 可选东京/首尔/新加坡区域,国内直连速度可接受;注册风控严格,可能需多次尝试 | ⭐⭐⭐⭐ |
| [Deno Deploy](https://deno.com/deploy) | Deno 官方边缘运行时,TypeScript 原生,部署 API/机器人很顺手。 | 免费计划:100 万次请求/月、100GB 流量/月 | ✅ 无需 | 🔶 部分可用 | ⭐⭐⭐⭐ |
| [Hugging Face Spaces](https://huggingface.co/spaces) | 免费托管 AI demo(Gradio/Streamlit/Docker),发 AI 小工具引流利器。 | 免费 CPU 实例(2 核 16GB)不限数量,闲置休眠 | ✅ 无需 | ❌ 需科学上网<br>🌏 国内无法直连 huggingface.co,可用镜像 hf-mirror.com 下载模型 | ⭐⭐⭐⭐ |

<a id="serverless"></a>

## ⚡ Serverless / 边缘函数

> 无服务器函数,跑 API、定时任务、Webhook 的最低成本方式。

| 服务 | 简介 | 免费额度 | 💳 信用卡 | 🇨🇳 中国 | ⭐ |
| --- | --- | --- | --- | --- | --- |
| [Cloudflare Workers](https://workers.cloudflare.com) | 边缘函数事实标准,免费层量大管饱,搭配 KV/R2/D1 可组免费全栈。 | 10 万次请求/天、KV 读 10 万次/天、D1 数据库 5GB、Cron 触发器 | ✅ 无需 | 🔶 部分可用<br>🌏 workers.dev 域名国内不稳,绑自定义域名改善 | ⭐⭐⭐⭐⭐ |
| [AWS Lambda](https://aws.amazon.com/lambda/) | Serverless 鼻祖,永久免费额度充足,但 AWS 全家桶学习成本高。 | 永久免费:100 万次请求/月 + 40 万 GB-秒计算 | ⚠️ 需要 | ✅ 可直连<br>🌏 全球区可访问;注册需外币卡,小心其他服务隐性扣费 | ⭐⭐⭐ |
| [Vercel Functions](https://vercel.com/docs/functions) | 和 Vercel 前端一体的函数,写 API 路由零配置。 | Hobby:100GB-小时/月 函数执行、1 万分钟边缘函数 | ✅ 无需 | 🔶 部分可用 | ⭐⭐⭐⭐ |
| [Netlify Functions](https://www.netlify.com/platform/core/functions/) | Netlify 内置函数,静态站加一点动态逻辑够用。 | 12.5 万次调用/月、100 小时运行时间 | ✅ 无需 | 🔶 部分可用 | ⭐⭐⭐ |
| [Val Town](https://www.val.town) | 在线写 TS 小函数即发布,自带 Cron 和 HTTP 端点,做小自动化极快。 | 免费计划:公开 Val 不限量、10 万次运行/天、Cron 定时 | ✅ 无需 | ✅ 可直连 | ⭐⭐⭐⭐ |
| [Supabase Edge Functions](https://supabase.com/edge-functions) | Supabase 自带的 Deno 边缘函数,配合其数据库/认证一站式后端。 | 免费项目含 50 万次函数调用/月 | ✅ 无需 | ✅ 可直连 | ⭐⭐⭐⭐ |

<a id="database"></a>

## 🗄️ 数据库

> 托管数据库免费层,MVP 阶段完全够用。留意“闲置暂停”策略。

| 服务 | 简介 | 免费额度 | 💳 信用卡 | 🇨🇳 中国 | ⭐ |
| --- | --- | --- | --- | --- | --- |
| [Supabase](https://supabase.com) | 开源 Firebase 替代品,Postgres + 认证 + 存储 + 实时订阅,Indie 后端首选。 | 2 个项目:500MB 数据库、1GB 存储、5 万月活认证用户;7 天不活跃会暂停项目 | ✅ 无需 | ✅ 可直连 | ⭐⭐⭐⭐⭐ |
| [Neon](https://neon.tech) | Serverless Postgres,分支功能像 Git 一样管理数据库,免费层可开 100 个项目。 | 100 个项目、每项目 0.5GB 存储 + 100 CU-小时/月、自动缩容到零 | ✅ 无需 | ✅ 可直连 | ⭐⭐⭐⭐⭐ |
| [Turso](https://turso.tech) | 边缘 SQLite(libSQL),读多写少的应用便宜到离谱,免费层超大方。 | 5GB 存储、5 亿行读/月、多数据库 | ✅ 无需 | ✅ 可直连 | ⭐⭐⭐⭐ |
| [MongoDB Atlas](https://www.mongodb.com/atlas) | 官方托管 MongoDB,免费 M0 集群稳定运行多年,文档型数据首选。 | M0 免费集群:512MB 存储,共享 CPU,不过期 | ✅ 无需 | ✅ 可直连 | ⭐⭐⭐⭐ |
| [Upstash](https://upstash.com) | Serverless Redis / Kafka / 向量库,按请求计费,做缓存、队列、限流必备。 | Redis 免费:256MB、50 万条命令/月;另有向量库与 QStash 免费层 | ✅ 无需 | ✅ 可直连 | ⭐⭐⭐⭐⭐ |
| [TiDB Cloud Serverless](https://www.pingcap.com/tidb-cloud-serverless/) | PingCAP(中国团队)的分布式 MySQL 兼容数据库,免费额度大,中文支持好。 | 每组织 5 个集群:各 5GB 行存 + 每月 5000 万 RU 请求单元 | ✅ 无需 | ✅ 可直连<br>🌏 中国团队出品,文档与社区中文友好 | ⭐⭐⭐⭐ |
| [Firebase Firestore](https://firebase.google.com/products/firestore) | Google 的文档数据库,实时同步好用,海外移动应用常客。 | 1GB 存储、5 万次读/2 万次写/天 | ✅ 无需 | ❌ 需科学上网 | ⭐⭐⭐ |
| [Convex](https://www.convex.dev) | 新一代全栈响应式数据库,TypeScript 端到端类型安全,做实时应用体验极好。 | 免费计划:100 万次函数调用/月、0.5GB 存储 | ✅ 无需 | ✅ 可直连 | ⭐⭐⭐⭐ |
| [Aiven](https://aiven.io) | 多云托管开源数据库(PG/MySQL/Redis/Kafka),有免费小实例。 | 免费计划:PostgreSQL / MySQL / Redis 各 1 个小实例(1 CPU 1GB) | ✅ 无需 | 🔶 部分可用 | ⭐⭐⭐ |

<a id="baas-auth"></a>

## 🔐 后端即服务 / 用户认证

> 登录注册、用户管理这种“每个产品都要但没人想写”的部分,直接白嫖。

| 服务 | 简介 | 免费额度 | 💳 信用卡 | 🇨🇳 中国 | ⭐ |
| --- | --- | --- | --- | --- | --- |
| [Firebase](https://firebase.google.com) | Google 全家桶 BaaS:认证、数据库、托管、推送一条龙,海外移动端标配。 | Spark 计划免费:认证 5 万月活、Firestore、Hosting、Cloud Messaging | ✅ 无需 | ❌ 需科学上网 | ⭐⭐⭐ |
| [Appwrite Cloud](https://appwrite.io) | 开源 BaaS,认证/数据库/存储/函数齐全,也可自托管零成本。 | 免费计划:7.5 万月活用户、2GB 存储、75 万次函数执行 | ✅ 无需 | ✅ 可直连 | ⭐⭐⭐⭐ |
| [PocketBase](https://pocketbase.io) | 单文件开源后端(Go + SQLite),一个二进制搞定认证+数据库+文件,自托管神器。 | 完全开源免费,自托管无任何限制,一台便宜 VPS 即可跑 | ✅ 无需 | ✅ 可直连<br>🌏 自托管方案,部署在国内服务器则完全可控 | ⭐⭐⭐⭐⭐ |
| [Clerk](https://clerk.com) | 体验最好的认证服务,预制 React 组件半小时接完登录,Indie 圈大热。 | 1 万月活用户免费,含社交登录、多因素认证 | ✅ 无需 | ✅ 可直连 | ⭐⭐⭐⭐⭐ |
| [Auth0](https://auth0.com) | 老牌企业级认证,协议支持最全,免费层 2024 年扩容到 2.5 万月活。 | 2.5 万月活用户、社交登录、Passkey | ✅ 无需 | 🔶 部分可用 | ⭐⭐⭐ |
| [Logto](https://logto.io) | 华人团队的开源认证方案,中文文档完善,Cloud 版有免费层,也可自托管。 | Cloud 免费:5 万月活用户;开源版自托管无限制 | ✅ 无需 | ✅ 可直连<br>🌏 华人团队,中文文档与微信生态支持好 | ⭐⭐⭐⭐ |
| [Kinde](https://kinde.com) | 认证 + 功能开关 + 计费权限一体的新秀,给 SaaS 起步省不少胶水代码。 | 10500 月活用户免费 | ✅ 无需 | ✅ 可直连 | ⭐⭐⭐⭐ |

<a id="payments"></a>

## 💰 支付 / 变现

> 按交易抽成、无月费的收款方案。重点标注对中国大陆主体的支持——这是国内 Indie 出海最大的坎。

| 服务 | 简介 | 免费额度 | 💳 信用卡 | 🇨🇳 中国 | ⭐ |
| --- | --- | --- | --- | --- | --- |
| [Creem](https://www.creem.io) | 专为独立开发者设计的 MoR(记录商户),明确支持中国开发者收款,Indie 圈口碑好。 | 无月费,按交易抽成;MoR 模式代缴全球销售税 | ✅ 无需 | ✅ 可直连<br>🌏 明确接受中国大陆开发者,支持提现到国内,出海收款首选之一 | ⭐⭐⭐⭐⭐ |
| [Paddle](https://www.paddle.com) | 老牌 MoR,代处理全球税务和合规,SaaS 订阅收款主流选择,接受中国主体申请。 | 无月费,按交易约 5% + $0.50 抽成 | ✅ 无需 | ✅ 可直连<br>🌏 接受中国个人/公司申请(需英文材料,审核较严) | ⭐⭐⭐⭐⭐ |
| [Lemon Squeezy](https://www.lemonsqueezy.com) | 被 Stripe 收购的 MoR,卖数字产品和 License 很顺手,对新手友好。 | 无月费,按交易 5% + $0.50 抽成 | ✅ 无需 | 🔶 部分可用<br>🌏 接受中国开发者但审核收紧,建议备好完整英文资料 | ⭐⭐⭐⭐ |
| [Stripe](https://stripe.com) | 全球支付基础设施之王,API 体验最佳;但不支持中国大陆主体直接开户。 | 无月费,按交易 2.9% + $0.30 | ✅ 无需 | 🔶 部分可用<br>🌏 需海外公司主体(常见做法:美国 LLC / 香港公司),大陆个人无法直接开户 | ⭐⭐⭐⭐ |
| [Gumroad](https://gumroad.com) | 最简单的数字产品售卖平台,挂链接就能卖,适合课程/模板/电子书试水。 | 无月费,按交易 10% 抽成(费率高但零门槛) | ✅ 无需 | 🔶 部分可用<br>🌏 收款需 PayPal/Payoneer 等渠道中转 | ⭐⭐⭐⭐ |
| [PayPal](https://www.paypal.com) | 全球通用的收款兑底方案,中国大陆可注册商家账户提现到国内银行。 | 无月费,跨境交易约 4.4% + 固定费 | ✅ 无需 | ✅ 可直连<br>🌏 大陆可注册,提现需结汇,费率偏高 | ⭐⭐⭐ |

<a id="email"></a>

## 📧 邮件发送 / Newsletter

> 事务邮件(验证码/通知)和 Newsletter(内容营销)两条线的免费方案。

| 服务 | 简介 | 免费额度 | 💳 信用卡 | 🇨🇳 中国 | ⭐ |
| --- | --- | --- | --- | --- | --- |
| [Resend](https://resend.com) | 开发者体验最好的邮件 API,React Email 写模板,Indie 圈事实标准。 | 3000 封/月(100 封/天)、1 个自定义域名 | ✅ 无需 | ✅ 可直连 | ⭐⭐⭐⭐⭐ |
| [Brevo](https://www.brevo.com) | 原 Sendinblue,事务邮件 + 营销邮件 + 短信一体,免费层按天计量。 | 300 封/天,含营销自动化基础功能 | ✅ 无需 | ✅ 可直连 | ⭐⭐⭐⭐ |
| [Amazon SES](https://aws.amazon.com/ses/) | 大规模发信最便宜的选择,$0.10/千封,量大后从免费层平滑过渡。 | 每月 3000 条消息免费(12 个月),之后 $0.10/千封 | ⚠️ 需要 | ✅ 可直连 | ⭐⭐⭐⭐ |
| [EmailJS](https://www.emailjs.com) | 纯前端直接发邮件,不用写后端,静态站联系表单神器。 | 200 封/月 | ✅ 无需 | ✅ 可直连 | ⭐⭐⭐ |
| [Buttondown](https://buttondown.com) | 极简 Newsletter 工具,Markdown 写作,API 完善,独立写作者最爱。 | 100 订阅者以内免费 | ✅ 无需 | ✅ 可直连 | ⭐⭐⭐⭐ |
| [beehiiv](https://www.beehiiv.com) | 增长功能最强的 Newsletter 平台,自带推荐网络和变现工具。 | 2500 订阅者以内免费,无限发送 | ✅ 无需 | ✅ 可直连 | ⭐⭐⭐⭐ |
| [MailerLite](https://www.mailerlite.com) | 性价比营销邮件平台,自动化流程免费层就能用。 | 1000 订阅者、1.2 万封/月 | ✅ 无需 | ✅ 可直连 | ⭐⭐⭐ |
| [Substack](https://substack.com) | 内容创作者平台,免费用全套,靠付费订阅抽成 10% 盈利。 | 完全免费使用,付费订阅收入抽成 10% | ✅ 无需 | ❌ 需科学上网<br>🌏 国内无法直接访问,面向海外读者则无影响 | ⭐⭐⭐⭐ |

<a id="analytics"></a>

## 📊 数据分析 / 统计

> 网站流量、用户行为分析。Google 系国内被墙,注意给国内站选替代品。

| 服务 | 简介 | 免费额度 | 💳 信用卡 | 🇨🇳 中国 | ⭐ |
| --- | --- | --- | --- | --- | --- |
| [Microsoft Clarity](https://clarity.microsoft.com) | 微软出品,完全免费的热图 + 会话录屏,看用户真实操作路径,无量级限制。 | 完全免费、无流量上限,含热图、录屏、AI 洞察 | ✅ 无需 | ✅ 可直连<br>🌏 国内可正常加载,微软系少数不受影响的服务 | ⭐⭐⭐⭐⭐ |
| [Umami Cloud](https://umami.is) | 开源隐私友好的 GA 替代品,界面清爽无 Cookie,云版有免费层,也可自托管。 | Cloud 免费:10 万事件/月、最多 3 个网站;自托管无限制 | ✅ 无需 | ✅ 可直连 | ⭐⭐⭐⭐⭐ |
| [PostHog](https://posthog.com) | 产品分析全家桶:事件分析、录屏、A/B 测试、功能开关,免费层大得离谱。 | 100 万事件/月、5000 条录屏/月,超出按量计费 | ✅ 无需 | ✅ 可直连 | ⭐⭐⭐⭐⭐ |
| [Google Analytics 4](https://analytics.google.com) | 行业标准,免费但学习曲线陡;国内网页加载 GA 脚本会失败。 | 标准版免费,事件近乎无限 | ✅ 无需 | ❌ 需科学上网<br>🌏 国内用户的访问不会被统计到,纯海外站可用 | ⭐⭐⭐ |
| [Cloudflare Web Analytics](https://www.cloudflare.com/web-analytics/) | 无 Cookie 的轻量统计,套了 Cloudflare 的站点零配置开启。 | 完全免费 | ✅ 无需 | 🔶 部分可用 | ⭐⭐⭐⭐ |
| [GoatCounter](https://www.goatcounter.com) | 一人开发的极简开源统计,非商业免费,几 KB 脚本不拖慢页面。 | 非商业用途免费(10 万浏览/月),开源可自托管 | ✅ 无需 | ✅ 可直连 | ⭐⭐⭐ |
| [百度统计](https://tongji.baidu.com) | 面向国内用户的站点统计标配,国内加载快、数据全。 | 基础版免费 | ✅ 无需 | ✅ 可直连<br>🌏 做中文站/国内流量必备,海外站不适用 | ⭐⭐⭐ |

<a id="monitoring"></a>

## 🩺 监控 / 日志 / 报错

> 网站宕机、程序报错第一时间知道,免费层对个人项目绰绰有余。

| 服务 | 简介 | 免费额度 | 💳 信用卡 | 🇨🇳 中国 | ⭐ |
| --- | --- | --- | --- | --- | --- |
| [UptimeRobot](https://uptimerobot.com) | 最流行的免费拨测,5 分钟间隔盯 50 个站点,配好通知就能睡安稳觉。 | 50 个监控、5 分钟间隔、邮件通知 | ✅ 无需 | ✅ 可直连 | ⭐⭐⭐⭐⭐ |
| [Sentry](https://sentry.io) | 报错追踪事实标准,前后端全覆盖,免费层个人项目够用。 | 5000 个错误/月、1 个用户、性能监控试用 | ✅ 无需 | ✅ 可直连 | ⭐⭐⭐⭐⭐ |
| [Better Stack](https://betterstack.com) | 拨测 + 状态页 + 日志一体,界面颜值高,免费层含 10 个监控。 | 10 个监控(3 分钟间隔)、状态页、1GB 日志/月 | ✅ 无需 | ✅ 可直连 | ⭐⭐⭐⭐ |
| [Healthchecks.io](https://healthchecks.io) | 反向监控 Cron 任务:定时任务没按时“打卡”就告警,开源可自托管。 | 20 个检查、邮件/Webhook 通知 | ✅ 无需 | ✅ 可直连 | ⭐⭐⭐⭐ |
| [Grafana Cloud](https://grafana.com/products/cloud/) | 指标 + 日志 + 链路追踪全套观测栈,免费层量给得很足。 | 1 万指标序列、50GB 日志、50GB 链路/月 | ✅ 无需 | ✅ 可直连 | ⭐⭐⭐ |
| [Axiom](https://axiom.co) | 新一代日志平台,免费层 0.5TB/月 摄入,查询快,API 友好。 | 0.5TB 日志摄入/月、30 天保留 | ✅ 无需 | ✅ 可直连 | ⭐⭐⭐⭐ |
| [Uptime Kuma](https://github.com/louislam/uptime-kuma) | 开源自托管拨测面板,界面精美,一个 Docker 容器搞定,国内外通吃。 | 完全开源免费,自托管无限制 | ✅ 无需 | ✅ 可直连<br>🌏 自托管,部署在国内 VPS 可监控国内外站点 | ⭐⭐⭐⭐ |

<a id="devops"></a>

## 🔧 代码托管 / CI-CD

> 代码仓库和自动化流水线,免费层已能覆盖独立开发全流程。

| 服务 | 简介 | 免费额度 | 💳 信用卡 | 🇨🇳 中国 | ⭐ |
| --- | --- | --- | --- | --- | --- |
| [GitHub](https://github.com) | 全球开发者主场,免费私有仓库 + Actions + Pages + Copilot 免费层,Indie 基本盘。 | 无限公私仓库、Actions 2000 分钟/月、Packages 500MB、Copilot 免费层 | ✅ 无需 | 🔶 部分可用<br>🌏 国内可访问但时快时慢,克隆大仓库建议用镜像或代理 | ⭐⭐⭐⭐⭐ |
| [GitHub Actions](https://github.com/features/actions) | CI/CD 首选,公开仓库完全免费不限时长,本项目的每周自动巡检就靠它。 | 公开仓库免费无限分钟;私有仓库 2000 分钟/月 | ✅ 无需 | 🔶 部分可用 | ⭐⭐⭐⭐⭐ |
| [GitLab](https://gitlab.com) | DevOps 一体化平台,自带 CI、Issue 看板、容器镜像库。 | 5 用户/组、400 计算分钟 CI/月、10GB 仓库 | ✅ 无需 | 🔶 部分可用 | ⭐⭐⭐ |
| [Gitee(码云)](https://gitee.com) | 国内最大代码托管平台,访问快,适合做 GitHub 仓库的国内镜像。 | 免费公私仓库(单仓 500MB)、Gitee Pages 需实名 | ✅ 无需 | ✅ 可直连<br>🌏 国内访问极快;公开仓库有内容审核 | ⭐⭐⭐ |
| [Codeberg](https://codeberg.org) | 非营利组织运营的 Gitea 托管,无广告无追踪,开源项目的清流备份地。 | 免费公私仓库、Codeberg Pages | ✅ 无需 | ✅ 可直连 | ⭐⭐⭐ |
| [Docker Hub](https://hub.docker.com) | 容器镜像中心,个人免费层够发布开源镜像。 | 1 个私有仓库、无限公开仓库(有拉取限速) | ✅ 无需 | ❌ 需科学上网<br>🌏 2024 年起国内直连基本不可用,需配置镜像加速器 | ⭐⭐⭐ |

<a id="cdn-dns-storage"></a>

## 📦 CDN / DNS / 域名 / 存储

> 域名解析、静态资源分发、对象存储,一个项目的“地基”部分。

| 服务 | 简介 | 免费额度 | 💳 信用卡 | 🇨🇳 中国 | ⭐ |
| --- | --- | --- | --- | --- | --- |
| [Cloudflare](https://www.cloudflare.com) | 免费 CDN + DNS + DDoS 防护 + SSL,互联网基建白嫖之王,域名注册还是成本价。 | 免费计划:CDN 无限流量、DNS、SSL、防护、R2/Workers/Pages 免费层 | ✅ 无需 | 🔶 部分可用<br>🌏 免费版无国内节点,国内访问绕行海外偏慢,但稳定可用 | ⭐⭐⭐⭐⭐ |
| [Cloudflare R2](https://www.cloudflare.com/developer-platform/r2/) | S3 兼容对象存储,杀手锏是出站流量完全免费,存图片/文件成本趋近于零。 | 10GB 存储/月、100 万次写 + 1000 万次读/月、出站流量 $0 | ✅ 无需 | 🔶 部分可用 | ⭐⭐⭐⭐⭐ |
| [Backblaze B2](https://www.backblaze.com/cloud-storage) | 最便宜的对象存储之一,配合 Cloudflare 出站免费,备份首选。 | 10GB 免费存储,每天 1GB 免费下载 | ✅ 无需 | 🔶 部分可用 | ⭐⭐⭐ |
| [七牛云](https://www.qiniu.com) | 国内老牌对象存储 + CDN,实名后有免费额度,做国内图床/静态资源方便。 | 10GB 标准存储、每月 10GB HTTP CDN 流量(需实名) | ✅ 无需 | ✅ 可直连<br>🌏 国内节点速度快;绑定自定义域名需已备案 | ⭐⭐⭐ |
| [DNSPod](https://www.dnspod.cn) | 腾讯旗下 DNS 解析,国内解析速度与稳定性好,免费套餐够个人用。 | 免费套餐:域名解析、10 条负载均衡 | ✅ 无需 | ✅ 可直连 | ⭐⭐⭐ |
| [jsDelivr](https://www.jsdelivr.com) | 免费开源 CDN,直接引用 npm/GitHub 资源,国内有备案节点速度好。 | 完全免费、无限流量 | ✅ 无需 | ✅ 可直连<br>🌏 少数在国内有合规节点的免费 CDN,偶有波动 | ⭐⭐⭐⭐ |
| [is-a.dev](https://www.is-a.dev) | 免费领 xxx.is-a.dev 子域名,提 PR 即可,开发者个人主页利器。 | 免费子域名,PR 审核制 | ✅ 无需 | ✅ 可直连 | ⭐⭐⭐ |
| [js.org](https://js.org) | 为 JS 开源项目提供免费 xxx.js.org 子域名,指向 GitHub Pages。 | 免费子域名(需为 JS 相关项目) | ✅ 无需 | ✅ 可直连 | ⭐⭐⭐ |
| [EU.org](https://nic.eu.org) | 运营 30 年的免费域名,可托管到任意 DNS,审核慢但真免费永久。 | 免费 xxx.eu.org 域名,永久免费 | ✅ 无需 | ✅ 可直连 | ⭐⭐⭐ |

<a id="ai"></a>

## 🤖 AI / LLM API

> 大模型 API 的免费额度与免费模型,做 AI 工具产品的核心原料。变动极快,以官网为准。

| 服务 | 简介 | 免费额度 | 💳 信用卡 | 🇨🇳 中国 | ⭐ |
| --- | --- | --- | --- | --- | --- |
| [Google AI Studio(Gemini API)](https://aistudio.google.com) | Gemini 免费 API 额度业界最大方,快速验证 AI 产品想法首选。 | 免费层:Gemini Flash 系列每天上千次请求(按模型不同),含多模态 | ✅ 无需 | ❌ 需科学上网<br>🌏 国内无法直连,需海外服务器中转 | ⭐⭐⭐⭐⭐ |
| [Groq](https://groq.com) | LPU 推理快到飞起,开源模型(Llama 等)免费额度可观,做实时应用体验好。 | 免费层:按模型每天数千至数万 token 请求限额 | ✅ 无需 | 🔶 部分可用 | ⭐⭐⭐⭐ |
| [OpenRouter](https://openrouter.ai) | 一个 API 聚合所有主流模型,常年有多个免费模型可白嫖,切换零成本。 | 多个 :free 后缀模型免费(每天限次),统一 API | ✅ 无需 | 🔶 部分可用 | ⭐⭐⭐⭐⭐ |
| [硅基流动 SiliconFlow](https://siliconflow.cn) | 国内模型聚合平台,多个小模型长期免费,注册送额度,国内直连低延迟。 | Qwen 等多个 9B 以下模型免费调用,注册送 14 元额度 | ✅ 无需 | ✅ 可直连<br>🌏 国内直连,支持支付宝,做面向国内的 AI 产品首选 | ⭐⭐⭐⭐⭐ |
| [智谱 AI(GLM)](https://open.bigmodel.cn) | 清华系大模型,GLM-Flash 系列免费调用,中文能力强。 | GLM-4-Flash / GLM-4V-Flash 等 Flash 系列模型免费 | ✅ 无需 | ✅ 可直连<br>🌏 国内直连,实名后即用 | ⭐⭐⭐⭐ |
| [DeepSeek](https://platform.deepseek.com) | 性价比之王,非免费但价格低到近似免费,推理能力强,出海国内两相宜。 | 无免费层,但价格极低(输入约 ¥1-4/百万 token),注册即用 | ✅ 无需 | ✅ 可直连 | ⭐⭐⭐⭐⭐ |
| [Cloudflare Workers AI](https://developers.cloudflare.com/workers-ai/) | 在 Cloudflare 边缘跑开源模型,与 Workers 无缝集成,免费额度每天刷新。 | 每天 1 万 Neuron 免费额度(可跑 Llama、Whisper、SD 等) | ✅ 无需 | 🔶 部分可用 | ⭐⭐⭐⭐ |
| [Mistral La Plateforme](https://mistral.ai) | 欧洲开源模型厂,API 有免费实验层,小模型质量能打。 | 免费层:1 请求/秒、10 亿 token/月(实验用途) | ✅ 无需 | 🔶 部分可用 | ⭐⭐⭐ |
| [Hugging Face](https://huggingface.co) | AI 界 GitHub,模型/数据集托管免费,Inference API 有免费额度。 | 模型与数据集托管免费、Inference API 少量免费额度、Spaces 免费 CPU | ✅ 无需 | ❌ 需科学上网<br>🌏 国内需镜像站 hf-mirror.com | ⭐⭐⭐⭐ |
| [Ollama](https://ollama.com) | 本地跑开源大模型的标准工具,自己电脑就是免费额度,隐私零风险。 | 完全免费开源,本地运行无任何限制 | ✅ 无需 | ✅ 可直连 | ⭐⭐⭐⭐ |

<a id="media-content"></a>

## 🖼️ 图片 / 媒体 / 内容管理

> 图片处理、免费素材、无头 CMS,做内容型产品和媒体号的弹药库。

| 服务 | 简介 | 免费额度 | 💳 信用卡 | 🇨🇳 中国 | ⭐ |
| --- | --- | --- | --- | --- | --- |
| [Cloudinary](https://cloudinary.com) | 图片/视频云处理老大哥,URL 参数即改尺寸格式,免费层够个人项目。 | 25 Credits/月(约 25GB 存储或流量、2 万次转换) | ✅ 无需 | ✅ 可直连 | ⭐⭐⭐⭐ |
| [ImageKit](https://imagekit.io) | 实时图片优化 + CDN,可挂在已有存储(如 R2)前面,接入轻。 | 20GB 流量/月、20GB 存储 | ✅ 无需 | ✅ 可直连 | ⭐⭐⭐⭐ |
| [TinyPNG](https://tinypng.com) | 最顺手的图片压缩工具,网页拖拽即压,API 每月有免费额度。 | 网页版免费(单张 ≤5MB);API 500 次压缩/月 | ✅ 无需 | ✅ 可直连 | ⭐⭐⭐ |
| [Unsplash](https://unsplash.com) | 最大的免费商用图库,API 可直接集成到产品里。 | 图片免费商用;API 演示模式 50 次/小时 | ✅ 无需 | 🔶 部分可用<br>🌏 网站可访问,图片 CDN 国内偏慢 | ⭐⭐⭐⭐ |
| [Pexels](https://www.pexels.com) | 免费商用图片 + 视频素材,做短视频内容的免费素材库。 | 图片视频免费商用;API 200 次/小时 | ✅ 无需 | 🔶 部分可用 | ⭐⭐⭐⭐ |
| [remove.bg](https://www.remove.bg) | 一键 AI 抠图,做封面图、商品图快速出活。 | 网页版免费(预览分辨率);API 有少量免费额度 | ✅ 无需 | ✅ 可直连 | ⭐⭐⭐ |
| [Notion](https://www.notion.com) | 个人版免费的全能笔记/数据库,配 API 可直接当轻量 CMS 用。 | 个人使用免费(块数量不限)、API 免费 | ✅ 无需 | ✅ 可直连<br>🌏 国内可直连,偶尔波动 | ⭐⭐⭐⭐⭐ |
| [Sanity](https://www.sanity.io) | 开发者友好的无头 CMS,结构化内容 + 实时协作,免费层量足。 | 免费计划:20 用户、2 个数据集、10GB 流量/月 | ✅ 无需 | ✅ 可直连 | ⭐⭐⭐⭐ |
| [Contentful](https://www.contentful.com) | 老牌无头 CMS,企业感强,免费层做个人博客/官网够用。 | 免费计划:1 万条内容、5 用户、2 个 Locale | ✅ 无需 | ✅ 可直连 | ⭐⭐⭐ |

<a id="forms-search"></a>

## 📝 表单 / 搜索

> 收集用户输入和站内搜索,两件小事但自建很烦,白嫖最划算。

| 服务 | 简介 | 免费额度 | 💳 信用卡 | 🇨🇳 中国 | ⭐ |
| --- | --- | --- | --- | --- | --- |
| [Tally](https://tally.so) | 免费额度最大方的表单工具,Notion 风格编辑,免费版几乎无限制。 | 无限表单、无限提交(免费版含品牌标) | ✅ 无需 | ✅ 可直连 | ⭐⭐⭐⭐⭐ |
| [Formspree](https://formspree.io) | 静态网站表单后端,HTML form 指向它即可收提交,零后端。 | 50 次提交/月、1 个项目 | ✅ 无需 | ✅ 可直连 | ⭐⭐⭐ |
| [金数据](https://jinshuju.net) | 国内老牌表单工具,微信生态集成好,面向国内用户收集信息首选。 | 免费版:无限表单、每表单每月 100 条提交 | ✅ 无需 | ✅ 可直连<br>🌏 国内访问快,支持微信通知 | ⭐⭐⭐ |
| [Algolia](https://www.algolia.com) | 搜索即服务标杆,毫秒级搜索体验,免费层够文档站和小产品。 | 1 万条记录、1 万次搜索/月 | ✅ 无需 | ✅ 可直连 | ⭐⭐⭐⭐ |
| [Meilisearch](https://www.meilisearch.com) | 开源搜索引擎,中文分词支持好,自托管免费,云版有试用。 | 开源自托管完全免费;Cloud 14 天试用 | ✅ 无需 | ✅ 可直连 | ⭐⭐⭐⭐ |
| [Pagefind](https://pagefind.app) | 纯静态站内搜索库,构建时生成索引,零服务器零费用。 | 完全开源免费 | ✅ 无需 | ✅ 可直连 | ⭐⭐⭐⭐ |

<a id="automation-notify"></a>

## 🔔 自动化 / 消息通知

> 工作流自动化和“服务器有事叫我”的推送方案,运营效率倍增器。

| 服务 | 简介 | 免费额度 | 💳 信用卡 | 🇨🇳 中国 | ⭐ |
| --- | --- | --- | --- | --- | --- |
| [n8n](https://n8n.io) | 开源工作流自动化,节点生态强,自托管免费无限跑,AI 工作流也能编排。 | 自托管开源免费无限制;Cloud 版付费 | ✅ 无需 | ✅ 可直连<br>🌏 自托管部署在国内外均可,社区中文教程多 | ⭐⭐⭐⭐⭐ |
| [Zapier](https://zapier.com) | 自动化连接器鼻祖,应用集成最多,免费层够轻量使用。 | 100 任务/月、单步 Zap | ✅ 无需 | ✅ 可直连 | ⭐⭐⭐ |
| [Make](https://www.make.com) | 可视化自动化,比 Zapier 便宜、逻辑能力强,免费层 1000 次操作。 | 1000 次操作/月、2 个活跃场景 | ✅ 无需 | ✅ 可直连 | ⭐⭐⭐⭐ |
| [Pipedream](https://pipedream.com) | 面向开发者的自动化,节点里直接写代码,免费层对开发者相当够用。 | 免费计划:每天约 100 次工作流执行 | ✅ 无需 | ✅ 可直连 | ⭐⭐⭐⭐ |
| [ntfy.sh](https://ntfy.sh) | 极简开源推送:curl 一下手机就响,服务器告警零成本方案。 | 公共服务器免费使用,开源可自托管 | ✅ 无需 | ✅ 可直连 | ⭐⭐⭐⭐ |
| [Bark](https://github.com/Finb/Bark) | 国人开发的 iOS 推送工具,一条 URL 推到 iPhone,国内直连秒达。 | 完全免费开源,可自托管推送服务端 | ✅ 无需 | ✅ 可直连<br>🌏 国人作品,国内网络环境下最可靠的 iOS 推送 | ⭐⭐⭐⭐ |
| [Server酱](https://sct.ftqq.com) | 老牌“服务器→微信”推送,脚本跑完微信收通知,国内开发者的老朋友。 | 免费版每天 5 条推送 | ✅ 无需 | ✅ 可直连<br>🌏 推送到微信服务号,国内场景无出其右 | ⭐⭐⭐ |
| [OneSignal](https://onesignal.com) | 主流 Web/App 推送服务,免费层对起步产品足够。 | Web 推送不限订阅者、移动推送 1 万订阅者 | ✅ 无需 | 🔶 部分可用<br>🌏 依赖 FCM 的安卓推送在国内不可达,Web/iOS 可用 | ⭐⭐⭐ |
| [Telegram Bot API](https://core.telegram.org/bots) | 完全免费的 Bot 平台,做通知、社群工具、小产品分发都好用。 | 完全免费、无限消息 | ✅ 无需 | ❌ 需科学上网<br>🌏 国内无法直连,面向海外用户/科学上网人群 | ⭐⭐⭐⭐ |

<a id="network-devtools"></a>

## 🛠️ 内网穿透 / 开发工具 / API 数据

> 本地调试、抓数据、测 API 的趁手兵器。

| 服务 | 简介 | 免费额度 | 💳 信用卡 | 🇨🇳 中国 | ⭐ |
| --- | --- | --- | --- | --- | --- |
| [Cloudflare Tunnel](https://www.cloudflare.com/products/tunnel/) | 免费内网穿透,本地服务安全暴露到公网,不限流量,demo 演示利器。 | 免费、不限隧道数与流量(需 Cloudflare 托管域名) | ✅ 无需 | 🔶 部分可用 | ⭐⭐⭐⭐⭐ |
| [ngrok](https://ngrok.com) | 内网穿透代名词,一条命令开隧道,免费层带固定域名 1 个。 | 1 个静态域名、1GB 流量/月、20 万次请求 | ✅ 无需 | 🔶 部分可用<br>🌏 国内可用但延迟高,国内场景可换 frp/花生壳 | ⭐⭐⭐⭐ |
| [Tailscale](https://tailscale.com) | 零配置组网(WireGuard),自己设备连成私有网络,远程开发神器。 | 个人免费:3 用户、100 台设备 | ✅ 无需 | 🔶 部分可用<br>🌏 国内可用,中继节点在海外时延迟偏高,可自建 DERP | ⭐⭐⭐⭐⭐ |
| [frp](https://github.com/fatedier/frp) | 国人开发的开源内网穿透,自备 VPS 即全免费,国内使用最广。 | 完全开源免费(需自备有公网 IP 的服务器) | ✅ 无需 | ✅ 可直连<br>🌏 国人作品,搭配国内轻量云主机延迟最低 | ⭐⭐⭐⭐ |
| [Postman](https://www.postman.com) | API 调试标准工具,免费层个人使用足够。 | 免费:基础协作、每月 1000 次 Mock/监控调用 | ✅ 无需 | ✅ 可直连 | ⭐⭐⭐ |
| [Hoppscotch](https://hoppscotch.io) | 开源版 Postman,网页即开即用,轻快无广告,可自托管。 | 核心功能完全免费,开源可自托管 | ✅ 无需 | ✅ 可直连 | ⭐⭐⭐⭐ |
| [Firecrawl](https://www.firecrawl.dev) | 把网页抓成干净 Markdown 的 API,做 AI 应用数据源的热门选择。 | 免费 500 Credits(一次性) | ✅ 无需 | ✅ 可直连 | ⭐⭐⭐⭐ |
| [Jina Reader](https://jina.ai/reader/) | URL 前加 r.jina.ai/ 即返回页面 Markdown,免费额度大,华人团队出品。 | 免费(无 Key 限速);注册送 1000 万 token | ✅ 无需 | ✅ 可直连<br>🌏 Jina AI 为华人创办团队 | ⭐⭐⭐⭐ |
| [RSSHub](https://docs.rsshub.app) | 万物皆可 RSS 的开源项目,给没有 RSS 的网站生成订阅源,信息监控基建。 | 开源免费,自托管无限制;公共实例免费但不稳 | ✅ 无需 | 🔶 部分可用<br>🌏 公共实例国内被墙,自托管即可;国人主导的开源项目 | ⭐⭐⭐⭐ |

<a id="design"></a>

## 🎨 设计 / 素材工具

> 不会设计也能出活的免费工具,做产品界面和内容封面都靠它们。

| 服务 | 简介 | 免费额度 | 💳 信用卡 | 🇨🇳 中国 | ⭐ |
| --- | --- | --- | --- | --- | --- |
| [Figma](https://www.figma.com) | UI 设计协作标准,免费层个人做产品原型完全够。 | 免费:3 个协作设计文件、个人草稿不限、无限查看者 | ✅ 无需 | ✅ 可直连<br>🌏 国内可直连,加载偶慢 | ⭐⭐⭐⭐⭐ |
| [Canva](https://www.canva.com) | 模板化设计,社媒封面、海报、Logo 快速出图,内容创作者标配。 | 免费版:海量模板、5GB 存储 | ✅ 无需 | ✅ 可直连<br>🌏 有本地化版本可画(canva.cn) | ⭐⭐⭐⭐ |
| [Excalidraw](https://excalidraw.com) | 手绘风白板,画架构图、示意图颜值高,开源免费无需登录。 | 完全免费开源 | ✅ 无需 | ✅ 可直连 | ⭐⭐⭐⭐ |
| [Photopea](https://www.photopea.com) | 浏览器里的 Photoshop,打开 PSD 改图不装软件,免费带广告。 | 全功能免费(带侧边广告) | ✅ 无需 | ✅ 可直连 | ⭐⭐⭐ |
| [Iconify](https://iconify.design) | 20 万+ 开源图标一站集齐,一行代码按需加载,前端图标终极方案。 | 完全免费开源 | ✅ 无需 | ✅ 可直连 | ⭐⭐⭐⭐ |
| [shots.so](https://shots.so) | 把截图套上精美 mockup,做产品宣传图、App Store 素材效率极高。 | 核心功能免费 | ✅ 无需 | ✅ 可直连 | ⭐⭐⭐ |

---

## 参与共建

所有数据在 [`data/services/`](data/services/) 的 YAML 文件中,改一个字段、提一个 PR 即可。新增服务请填全部字段(见现有条目格式)。

*本 README 由 `scripts/build.py` 自动生成于 2026-07-20,请勿手改。*