import os

from PIL import Image


def create_icns():
    """创建 .icns 文件"""
    try:
        # 检查源图片
        png_path = os.path.join(os.path.dirname(__file__), 'icon.png')
        if not os.path.exists(png_path):
            print("⚠️ 未找到 icon.png，将创建默认图标")
            # 创建一个简单的默认图标
            img = Image.new('RGB', (512, 512), color='white')
            img.save(png_path)

        # 创建临时 iconset 目录
        iconset_name = "icon.iconset"
        if not os.path.exists(iconset_name):
            os.makedirs(iconset_name)

        # 需要的图标尺寸
        icon_sizes = [16, 32, 64, 128, 256, 512]

        # 打开原始图片
        img = Image.open(png_path)

        # 生成不同尺寸的图标
        for size in icon_sizes:
            img_copy = img.copy()
            img_copy.thumbnail((size, size), Image.Resampling.LANCZOS)
            img_copy.save(f"{iconset_name}/icon_{size}x{size}.png")

        # 使用 iconutil 创建 .icns 文件（仅在 Mac 上可用）
        if os.system('which iconutil') == 0:
            os.system(f'iconutil -c icns {iconset_name}')
        else:
            print("⚠️ iconutil 不可用，跳过 .icns 创建")

        print("✅ 图标处理完成")

    except Exception as e:
        print(f"❌ 创建图标时出错: {str(e)}")
        # 不抛出异常，让构建继续进行


if __name__ == "__main__":
    create_icns()
