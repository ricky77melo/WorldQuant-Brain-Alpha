from setuptools import setup, find_packages


setup(
    name="Alpha_Tool",
    version="1.0.0",
    author="YourName",
    description="WorldQuant Brain Alpha Generator",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[
        "requests>=2.31.0",
        "pandas>=2.0.0",
    ],
    entry_points={
        'console_scripts': [
            'alpha_tool=main:main',
        ],
    },
    # 包含非Python文件
    package_data={
        '': ['*.txt', '*.json', '*.ico', '*.png'],
    },
    # 额外信息
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
