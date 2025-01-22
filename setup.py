from setuptools import setup, find_packages

setup(
    name='github-cli',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'click',
    ],
    python_requires='>=3.8',  # 添加最低Python版本要求
    entry_points={
        'console_scripts': [
            'qgh=cli:github_cli',
        ],
    },
)
# 添加 following to show how to upload to pip repo
# Upload to pip repo command:
# python setup.py sdist bdist_wheel
# twine upload dist/*
