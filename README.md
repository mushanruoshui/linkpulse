# LinkPulse

短链接服务与访问分析平台 —— 一个以工程化实践为目标的后端项目。

## 项目状态

🚧 开发中 · 当前进度：**W1 项目骨架**

## 技术栈

| 层 | 选型 |
|---|---|
| 语言 | Python 3.10+ |
| Web 框架 | FastAPI |
| ORM / 迁移 | SQLAlchemy 2.0 + Alembic |
| 数据库 | MySQL 8 |
| 缓存 | Redis 7 |
| 异步任务 | Celery |
| 容器 / 部署 | Docker · docker compose · Nginx |
| CI/CD | GitHub Actions |
| 可观测性 | 结构化日志(JSON) · Prometheus · Grafana |
| 测试 | pytest · httpx |

## 里程碑

- [ ] **M1 项目骨架** —— 短链创建 + 302 跳转 + 数据库迁移 + 10 个测试
- [ ] **M2 数据优化** —— 100 万行造数 + 索引优化 + 游标分页
- [ ] **M3 缓存** —— Redis Cache Aside + 穿透/击穿/雪崩防护 + 限流
- [ ] **M4 异步** —— Redis 计数 + Celery 批量落库
- [ ] **M5 可观测性** —— JSON 日志 + request_id + Prometheus + Grafana
- [ ] **M6 部署** —— Docker 多阶段构建 + compose + Nginx/HTTPS + CI/CD

## 环境要求

- Ubuntu 22.04+
- Python 3.10+
- Git

## 本地启动

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## 项目结构

```text
app/          # 应用代码（分层：api / schemas / services / repositories / core / middleware）
tests/        # pytest 测试
deploy/       # 部署配置（systemd / compose / nginx）
docs/         # 设计与复盘文档
ops/          # 运维脚本（provision.sh 等）
```

> M1 完成后补充各层职责说明。

## 开发约定

- 分支：`main` 保持可用，功能开发走 `feat/xxx`，通过 PR 合并
- 提交信息前缀：`feat:` `fix:` `docs:` `test:` `chore:` `refactor:`
- 配置：`.env` 不入库，参照 `.env.example`
- 测试：新增功能须带测试，`pytest` 全绿方可合并

## License
