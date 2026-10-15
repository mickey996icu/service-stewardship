# service-stewardship

一个轻量、平台无关的 Agent skill：理解意图，问清关键未知，带功课建议，主动推进并持续跟进，如实反馈结果，从纠正积累有适用边界的判例。可用于个人助手、项目助理、研究助理等持续协作。

中文指令；不绑定模型或工具。skill 本身不提供记忆、调度或执行能力，不新增统一审批流程。

## 安装

```sh
git clone https://github.com/mickey996icu/service-stewardship.git
cd service-stewardship
```

从本仓库根目录，将 `skills/service-stewardship` 整个目录复制到宿主支持的 skills 目录。保留 `references/`。例如 Codex 的用户目录：

```sh
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
# 若已有同名目录，先查看差异；不要覆盖现有安装。
cp -R -n skills/service-stewardship "${CODEX_HOME:-$HOME/.codex}/skills/"
```

确认宿主发现后，可用 `$service-stewardship` 调用；其他 Agent 使用其对应 skill 加载方式。未提供跨平台自动安装器。此示例不安装运行依赖，也不会迁移旧 skill 或用户记忆。

示例请求（虚构）：“使用 $service-stewardship，整理项目发布事项；沿用已有授权，查明缺口后直接问我，继续完成不依赖答复的部分。”

## 内容

- [可安装 skill](skills/service-stewardship/SKILL.md)：直接影响行动的指导。
- [来源与适配](skills/service-stewardship/references/sources-and-adaptation.md)：具体章节、核读范围和历史语境取舍。
- [LLM 适配](skills/service-stewardship/references/llm-adaptation.md)：原始论文、机制区分与假设。
- [验证记录](validation/REPORT.md)：格式检查、独立定性演练及仍需实测的限制。

本项目重新审阅并重写了既有服务经验草稿，未将旧审核结论当作新验证。书籍主题释义与现代规范分列；技术方案不归因于原书。无原书全文、大段摘录、真实用户案例、凭据或生产配置。

## 许可证与贡献

本仓库可授权的原创指令、说明和虚构检查材料采用 [MIT](LICENSE)。引用的书籍、论文及外部网页不在该授权范围；见 [NOTICE](NOTICE.md)。无作者、出版社或论文作者背书。

改进建议请附脱敏的最小情境、当前指示、相关授权、可观察结果和适用边界。不要提交用户隐私、私有轨迹或把单次例外升级成全局规则。
