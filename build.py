import PyInstaller.__main__
import os
import sys
import shutil

# 确保目录存在
if not os.path.exists('dist'):
    os.makedirs('dist')

# 设置命令行参数
args = [
    'main.py',  # 主程序入口
    '--name=Alpha_工具',  # 可执行文件名
    '--onefile',  # 打包成单个文件
    '--console',  # 使用控制台窗口（改为控制台模式）
    '--add-data=dataset_config.py{0}.'.format(os.pathsep),  # 添加配置文件
    '--add-data=alpha_strategy.py{0}.'.format(os.pathsep),  # 添加策略文件
    '--add-data=brain_batch_alpha.py{0}.'.format(os.pathsep),  # 添加核心处理文件
    '--clean',  # 清理临时文件
    '--noconfirm',  # 不确认覆盖
]

# 如果有图标文件，添加图标
if os.path.exists('icon.ico'):
    args.append('--icon=icon.ico')

# 运行打包命令
PyInstaller.__main__.run(args)

# 打包完成后，复制或创建配置文件到dist目录
print("\n正在处理配置文件...")
try:
    # 处理认证文件
    if os.path.exists('brain_credentials.txt'):
        shutil.copy2('brain_credentials.txt', 'dist/')
        print("✅ brain_credentials.txt 复制成功")
    else:
        # 创建示例认证文件
        with open('dist/brain_credentials.txt', 'w') as f:
            f.write('["your_email@example.com","your_password"]')
        print("✅ 创建了示例 brain_credentials.txt")

    # 处理Alpha ID文件
    if os.path.exists('alpha_ids.txt'):
        shutil.copy2('alpha_ids.txt', 'dist/')
        print("✅ alpha_ids.txt 复制成功")
    else:
        # 创建空的alpha_ids.txt
        with open('dist/alpha_ids.txt', 'w') as f:
            ...
        print("✅ 创建了空的 alpha_ids.txt")

except Exception as e:
    print(f"❌ 处理配置文件时出错: {str(e)}")
