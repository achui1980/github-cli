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
@click.option('--reviewer', default='', help='Reviewer for the PR')  # 新增 reviewer 参数
def create_pr_command(source, target, body, reviewer):
    """提交PR"""
    check_git_repository(None, None, None)  # 默认检查Git仓库
    # 获取最新的commit message作为title
    title = run_command("git log -1 --pretty=%B").strip()
    result = create_pr(source, target, title, body, reviewer)  # 传递 reviewer 参数
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