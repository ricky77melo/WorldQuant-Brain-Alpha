import zipapp
import os
import shutil
import subprocess
import sys


def create_zipapp():
    # 创建临时目录
    build_dir = "build"
    if os.path.exists(build_dir):
        shutil.rmtree(build_dir)
    os.makedirs(build_dir)

    # 复制源文件
    source_files = [
        "main.py",
        "brain_batch_alpha.py",
        "alpha_strategy.py",
        "dataset_config.py",
    ]

    for file in source_files:
        shutil.copy2(file, build_dir)

    # 复制配置文件
    config_files = [
        "brain_credentials.txt",
        "alpha_ids.txt",
    ]

    for file in config_files:
        if os.path.exists(file):
            shutil.copy2(file, build_dir)
        else:
            print(f"Warning: {file} not found, will be created on first run")

    # 创建 requirements.txt
    with open(os.path.join(build_dir, "requirements.txt"), "w") as f:
        f.write("requests>=2.31.0\npandas>=2.0.0\n")

    # 创建 __main__.py
    with open(os.path.join(build_dir, "__main__.py"), "w") as f:
        f.write("""
import sys
import os


def install_deps():
    import subprocess
    import pkg_resources

    required = {'requests>=2.31.0', 'pandas>=2.0.0'}
    installed = {f"{pkg.key}=={pkg.version}" for pkg in pkg_resources.working_set}
    missing = required - installed

    if missing:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', *missing])


if __name__ == '__main__':
    # 安装依赖
    install_deps()

    # 导入主程序
    from main import main
    main()
""")

    # 创建可执行文件
    output = "Alpha_Tool.pyz"
    if os.path.exists(output):
        os.remove(output)

    zipapp.create_archive(
        build_dir,
        output,
        main="__main__:main",
        compressed=True
    )

    print(f"\n✅ 成功创建 {output}")
    print("使用方法：")
    print(f"python {output}")


if __name__ == "__main__":
    create_zipapp()
