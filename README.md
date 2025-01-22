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
```bash 
qgh branch main feature-branch
```
### 提交 PR
#### 参数说明：
- <source>：源分支名称。
- <target>：目标分支名称。
- --body：PR 的描述内容（可选）。

#### 示例：
假设你有一个名为 feature-branch 的分支，你需要提交一个 PR 到 main 分支，并且添加一些描述信息，你可以执行以下命令：
```bash 
qgh pr feature-branch main --body "This PR adds a new feature."
```

### 删除本地分支
#### 参数说明：
- <branch>：要删除的本地分支名称。
#### 示例：
如果你有一个名为 feature-branch 的分支，你可以执行以下命令将其从本地删除：
```bash 
qgh delete feature-branch
```

## 贡献指南