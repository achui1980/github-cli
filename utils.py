import subprocess
import os

def run_command(command):
    """运行shell命令并返回输出"""
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        raise Exception(f"Command failed: {result.stderr}")
    return result.stdout

def create_branch(source_branch, new_branch):
    """从指定分支创建远端分支"""
    # 先从源分支拉取最新的代码
    pull_command = f"git pull origin {source_branch}"
    print(f"Executing: {pull_command}")  # 添加打印语句
    run_command(pull_command)
    command = f"git checkout -b {new_branch} {source_branch}"
    print(f"Executing: {command}")  # 添加打印语句
    run_command(command)
    command = f"git push origin {new_branch}"
    print(f"Executing: {command}")  # 添加打印语句
    return run_command(command)

def delete_local_branch(branch):
    """删除本地分支"""
    command = f"git branch -d {branch}"
    print(f"Executing: {command}")  # 添加打印语句
    return run_command(command)

def create_pr(head, base, title, body=''):
    """提交PR"""
    # 检查 head 和 base 分支的 SHA 值
    head_sha = run_command(f"git rev-parse {head}").strip()
    base_sha = run_command(f"git rev-parse {base}").strip()
    if not head_sha or not base_sha:
        raise Exception("Head or base SHA is blank.")
    command = f"gh pr create --head {head} --base {base} --title '{title}' --body '{body}'"
    return run_command(command)

def is_git_repository():
    """检查当前目录是否为Git仓库"""
    try:
        subprocess.run(['git', 'rev-parse', '--is-inside-work-tree'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except subprocess.CalledProcessError:
        return False