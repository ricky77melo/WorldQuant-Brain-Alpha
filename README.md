# 🚀 WorldQuant Brain Alpha Generator

<div align="center">

![GitHub stars](https://img.shields.io/github/stars/YHYYDS666/WorldQuant-Brain-Alpha?style=social)
![GitHub forks](https://img.shields.io/github/forks/YHYYDS666/WorldQuant-Brain-Alpha?style=social)
![GitHub watchers](https://img.shields.io/github/watchers/YHYYDS666/WorldQuant-Brain-Alpha?style=social)

```txt
  ____    _____   _____    ____   _   _   _____ 
 |  _ \  |_   _| |  ___|  / ___| | | | | |_   _|
 | |_) |   | |   | |_    | |  _  | |_| |   | |  
 |  _ <    | |   |  _|   | |_| | |  _  |   | |  
 |_| \_\   |_|   |_|      \____| |_| |_|   |_|  
```

</div>

## 📖 项目介绍

这是一个用于自动生成和提交 WorldQuant Brain Alpha 表达式的工具。它可以帮助用户自动化测试和提交 Alpha 策略。

## 🗂️ 目录结构

```txt
WorldQuant-Brain-Alpha/
├── 📜 main.py                # 主程序入口
├── 🧠 brain_batch_alpha.py   # 核心处理模块
├── 📊 alpha_strategy.py      # 策略生成模块
├── ⚙️ dataset_config.py      # 数据集配置
├── 📋 requirements.txt       # 依赖列表
├── 🔨 build.py              # 通用构建脚本
├── 🪟 build_windows.py      # Windows构建脚本
├── 📦 setup.py              # 打包配置
├── 🗜️ create_zipapp.py      # ZIP打包脚本
└── 🍎 mac/                  # Mac相关文件
    ├── build_mac.py         # Mac构建脚本
    ├── create_icns.py       # 图标生成
    └── icon.png             # 图标源文件
```

## ✨ 功能特点

- 🤖 自动生成 Alpha 策略
- 📈 自动测试性能指标
- 🚀 自动提交合格策略
- 💾 保存策略 ID
- 🔄 支持多种运行模式

## 🛠️ 安装方法

上传文件出问题了，所有就分开放了两个版本。之后会合并成一个版本。

### Windows 用户

```bash
# 下载发布版本
✨ 从 Releases选择Alpha_Tool_v1.0版本 下载 Alpha_.zip

# 从源码构建
🔨 pip install -r requirements.txt
🚀 python build_windows.py
```

### Mac 用户

```bash
# 下载发布版本
✨ 从 Releases选择最新版 下载 Alpha_Tool_Mac.zip

  # 解压文件
  unzip Alpha_Tool_Mac.zip

  # 进入解压目录
  cd Alpha_Tool_Mac

  # 添加执行权限
  chmod +x Alpha_Tool

  # 运行程序
  ./Alpha_Tool

# 从源码构建
🔨 pip install -r requirements.txt
🚀 cd mac && python build_mac.py
```

## 📊 数据集支持

| 数据集 | 描述 | 股票范围 |
|--------|------|----------|
| 📈 fundamental6 | 基础财务数据 | TOP3000 |
| 📊 analyst4 | 分析师预测 | TOP1000 |
| 📉 pv1 | 成交量数据 | TOP1000 |

## 👍 性能要求

```txt
     ___________
    |  METRICS  |
    |-----------|
    | ✓ Sharpe  | > 1.5
    | ✓ Fitness | > 1.0
    | ✓ Turnover| 0.1-0.9
    | ✓ IC Mean | > 0.02
    |___________|
```

## 🎯 使用流程

1. 📝 配置账号信息
2. 🎲 选择数据集
3. 🔄 选择运行模式
4. 📊 等待结果生成
5. 🚀 自动提交策略

## 🤝 贡献指南

欢迎提交 Issue 和 Pull Request！

## 📄 许可证

MIT License

## 👨‍💻 联系方式

- 📧 Email: <666@woaiys.filegear-sg.me>
- 🌟 GitHub: [YHYYDS666](https://github.com/YHYYDS666)

---

⭐ 如果这个项目帮助到你，请给一个 star! ⭐

## Star History

<a href="https://star-history.com/#WorldQuant-Brain-AlphaP/WorldQuant-Brain-AlphaP&Date">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=WorldQuant-Brain-AlphaP/WorldQuant-Brain-AlphaP&type=Date&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=WorldQuant-Brain-AlphaP/WorldQuant-Brain-AlphaP&type=Date" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=WorldQuant-Brain-AlphaP/WorldQuant-Brain-AlphaP&type=Date" />
 </picture>
</a>
