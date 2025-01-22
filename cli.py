import click
from utils import create_branch, create_pr, is_git_repository, delete_local_branch, run_command
@click.group()
def github_cli():
    """GitHub CLI工具"""
    pass

def check_git_repository(ctx, param, value):
    if not is_git_repository():
        click.echo("Error: This command must be run in a Git repository.")
        ctx.exit(1)
    return value

@github_cli.command(name='branch')
@click.argument('source_branch')
@click.argument('new_branch')
def create_branch_command(source_branch, new_branch):
    """从指定分支创建远端分支"""
    check_git_repository(None, None, None)  # 默认检查Git仓库
    result = create_branch(source_branch, new_branch)
    click.echo(result)

@github_cli.command(name='pr')
@click.argument('source')  # 修改: head -> source
@click.argument('target')  # 修改: base -> target
@click.option('--body', default='', help='PR body content')
def create_pr_command(source, target, body):
    """提交PR"""
    check_git_repository(None, None, None)  # 默认检查Git仓库
    # 获取最新的commit message作为title
    title = run_command("git log -1 --pretty=%B").strip()
    # 检查 source 分支是否存在并且有新的提交
    run_command(f"git fetch origin {source}")
    run_command(f"git fetch origin {target}")
    # 确保 source 分支有新的提交
    run_command(f"git checkout {source}")
    run_command(f"git pull origin {source}")
    # 检查是否有新的提交
    diff_command = f"git diff --name-only {target} {source}"
    diff_output = run_command(diff_command).strip()
    if not diff_output:
        click.echo(f"Error: No commits between {target} and {source}.")
        click.exit(1)
    result = create_pr(source, target, title, body)
    click.echo(result)

@github_cli.command(name='del-branch')
@click.argument('branch')
def delete_branch_command(branch):
    """删除本地分支"""
    check_git_repository(None, None, None)  # 默认检查Git仓库
    result = delete_local_branch(branch)
    click.echo(result)

if __name__ == '__main__':
    github_cli()