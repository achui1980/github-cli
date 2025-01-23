from setuptools import setup, find_packages

setup(
    name='github-cli',
    version='0.1.0',
    # packages=find_packages(),
    py_modules=['cli', 'utils'],
    install_requires=[
        'click',
        # 'PyInstaller',  # 确保 PyInstaller 在依赖项中
    ],
    python_requires='>=3.8',  # 添加最低Python版本要求
    entry_points={
        'console_scripts': [
            'qgh=cli:github_cli',
        ],
    },
)