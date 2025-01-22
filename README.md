# GitHub CLI 工具

## 简介
GitHub CLI 工具是一个用于简化 GitHub 操作的命令行工具，支持创建分支、提交 PR 和删除本地分支等功能。

## 安装

### 前提准备
1. 有git环境 [git](https://git-scm.com/downloads)
2. 需要安装github cli命令 [github cli](https://cli.github.com/manual/installation)
3. 需要安装python环境 [python](https://www.python.org/downloads/)

### 源码安装
1. 克隆项目：
   ```bash
   git clone <your-git-repo-url>
   cd github-cli
   ```
2. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```
3. 安装 CLI 工具：
   ```bash
   python setup.py install
   ```
4. 使用开发模式安装（可选）：
   ```bash
   pip install -e .
   ```

## 使用方法
### 创建分支
#### 参数说明：
- <source_branch>：源分支名称，新分支将基于此分支创建。
- <new_branch>：新分支的名称。
#### 示例：
假设你当前在 main 分支，并且想要创建一个名为 feature-branch 的新分支，可以执行以下命令：