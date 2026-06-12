# PerfectWorld Codex Plugin

PerfectWorld 是一套 Codex-native 专家角色插件，面向从 0 立项到发布后的完整开发流程。

它会在每一轮任务开始时重新判断当前最合适的角色，并用中文说明：

```text
我是完美世界 XXX，我擅长 XXX，本轮我负责 XXX 问题。
```

## 包含内容

- `.agents/plugins/marketplace.json`：Codex marketplace 定义。
- `plugins/perfectworld/`：PerfectWorld 插件本体。
- `plugins/perfectworld/skills/`：完美世界专家角色技能。
- `plugins/perfectworld/assets/`：插件图标和展示资源。


## 安装

仓库是公开仓库，使用者可以在 Codex CLI 中添加 marketplace：

```powershell
codex plugin marketplace add Liutianyuan/perfectworld
```

然后安装插件：

```powershell
codex plugin add perfectworld@perfectworld
```

安装后，建议开启一个新的 Codex 线程，让 Codex 重新加载插件技能。

## 本地测试

从这个目录本地测试 marketplace：

```powershell
codex plugin marketplace add .
codex plugin add perfectworld@perfectworld
```


