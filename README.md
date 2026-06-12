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

## 发布到 GitHub

1. 新建一个 GitHub 仓库，例如 `Liutianyuan/perfectworld`.
2. 把本目录里的所有内容推到仓库根目录。
3. 确认 GitHub 仓库根目录包含：

```text
.agents/plugins/marketplace.json
plugins/perfectworld/.codex-plugin/plugin.json
plugins/perfectworld/skills/
plugins/perfectworld/assets/
```

如果当前机器没有安装 `git`，也可以用内置脚本通过 GitHub API 发布：

```powershell
$env:GITHUB_TOKEN = "你的 GitHub token"
.\scripts\publish-github.ps1 -Owner Liutianyuan -Repo perfectworld
```

这个 token 需要有目标仓库的 Contents 读写权限；如果要自动创建仓库，还需要创建仓库权限。

## 其他人安装

如果仓库是公开仓库，使用者可以在 Codex CLI 中添加 marketplace：

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

## 推荐测试提示词

```text
用 PerfectWorld 帮我从 0 规划一个项目
用 PerfectWorld 帮我 QA localhost:3000
用 PerfectWorld 查这个 bug 的根因
用 PerfectWorld review 当前改动
这个 UI 看起来怪怪的，用 PerfectWorld 帮我看
```
