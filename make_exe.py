import PyInstaller.__main__

PyInstaller.__main__.run([
    '--name=github-cli',
    '--onefile',
    '--windowed',  # 如果不需要控制台窗口，可以使用这个选项
    'cli.py'
])