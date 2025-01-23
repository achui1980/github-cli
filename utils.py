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

def read_reviewers_from_file(file_path):
    """从文件中读取 reviewer"""
    if not file_path:
        return ''
    try:
        with open(file_path, 'r') as file:
            reviewers = file.readline().strip()
        return reviewers
    except FileNotFoundError:
        raise Exception(f"Reviewer file not found: {file_path}")
    except Exception as e:
        raise Exception(f"Error reading reviewer file: {e}")

def create_pr(head, base, title, body='', reviewer=''):
    """提交PR"""
    head_sha = run_command(f"git rev-parse {head}").strip()
    base_sha = run_command(f"git rev-parse {base}").strip()
    if not head_sha or not base_sha:
        raise Exception("Head or base SHA is blank.")
    
    # 使用引号包裹参数，避免空格问题
    command = ['gh', 'pr', 'create',
              '--head', head,
              '--base', base,
              '--title', title]
    
    if body:
        command.extend(['--body', body])
    
    if reviewer:
        command.extend(['--reviewer', reviewer])
    
    # 使用 subprocess.run 执行命令列表
    return run_command(command)

def is_git_repository():
    """检查当前目录是否为Git仓库"""
    try:
        subprocess.run(['git', 'rev-parse', '--is-inside-work-tree'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except subprocess.CalledProcessError:
        return False

def add_reviewers_to_pr(pr_number, reviewers):
    """添加reviewers到已存在的PR"""
    if not reviewers:
        return "No reviewers specified"
    
    command = [
        'gh', 'pr', 'edit',
        str(pr_number),
        '--add-reviewer', reviewers
    ]
    return run_command(command)