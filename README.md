# Idea Forge Skill v1.1

这是一个面向科研 idea 挖掘、查新、评审与 proposal 设计的可安装 skill 包。

v1.1 是修补版，重点解决：流程命名歧义、工具能力幻觉、查新过载、AC 结论过绝对、外部内容 prompt injection、伦理合规缺口、归档持久化不清等问题。

## 目录结构

```text
idea-forge-skill-v1.1/
├── SKILL.md
├── README.md
├── CHANGELOG.md
├── SOURCE_NOTE.md
├── PATCH_NOTES.md
├── references/
│   ├── mining-strategies.md
│   ├── review-rubric.md
│   ├── domain-ai-mm-sp.md
│   └── proposal-template.md
├── assets/
│   └── tools_config.yaml
└── archive/
    └── rejected-ideas.md
```

## 使用方式

将本目录作为一个 skill 安装或挂载到智能体环境中。启动时优先读取 `SKILL.md`，并在需要时引用 `references/` 中的评审标准、挖掘策略、领域知识与 proposal 模板。

推荐触发语：

- “帮我验证这个科研 idea 是否值得做”
- “从 AVSE / 多模态 / 信号处理方向帮我挖掘研究 idea”
- “用 Idea Forge 对这个方案做顶刊级评审”
- “把通过评审的 idea 设计成完整 proposal”

## 默认运行设定

```text
入口：自动推断，默认种子入口
严格度：顶刊评审模式
检查点：完整模式；L1/L2 可按用户要求合并；L3 默认硬停
工具：配置文件仅表示期望能力，必须以实际运行环境为准
查新：L1 轻量扫描，L3 深度查新
结论：使用研究决策式 AC 结论，不默认使用绝对 Accept / Reject
```

## v1.1 推荐使用姿势

对于一个已有 idea：

```text
用 Idea Forge v1.1 顶刊评审模式快速验证这个 idea。先做 L1 轻量查新和 L3 深审，不要直接写 proposal。
```

对于从零找方向：

```text
用 Idea Forge v1.1 从 AVSE / 多模态语音方向做探索入口。L1 和 L2 合并输出，先给 8-15 个候选 idea 卡片，然后我选 3 个进入 L3。
```

对于需要完整方案：

```text
用 Idea Forge v1.1 对这个 idea 做 L3 审核；如果结论是 Strong Proceed 或 Proceed with Risks，再生成 L4 proposal。
```
