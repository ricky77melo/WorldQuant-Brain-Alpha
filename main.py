"""WorldQuant Brain 批量 Alpha 生成系统"""

import os

from brain_batch_alpha import BrainBatchAlpha
from dataset_config import get_dataset_by_index, get_dataset_list

STORAGE_ALPHA_ID_PATH = "alpha_ids.txt"


def submit_alpha_ids(brain, num_to_submit=2):
    """提交保存的 Alpha ID"""
    try:
        if not os.path.exists(STORAGE_ALPHA_ID_PATH):
            print("❌ 没有找到保存的Alpha ID文件")
            return

        with open(STORAGE_ALPHA_ID_PATH, 'r') as f:
            alpha_ids = [line.strip() for line in f.readlines() if line.strip()]

        if not alpha_ids:
            print("❌ 没有可提交的Alpha ID")
            return

        print("\n📝 已保存的Alpha ID列表:")
        for i, alpha_id in enumerate(alpha_ids, 1):
            print(f"{i}. {alpha_id}")

        if num_to_submit > len(alpha_ids):
            num_to_submit = len(alpha_ids)

        selected_ids = alpha_ids[:num_to_submit]
        successful, failed = brain.submit_multiple_alphas(selected_ids)

        # 更新 alpha_ids.txt
        remaining_ids = [id for id in alpha_ids if id not in successful]
        with open(STORAGE_ALPHA_ID_PATH, 'w') as f:
            f.writelines([f"{id}\n" for id in remaining_ids])

    except Exception as e:
        print(f"❌ 提交 Alpha 时出错: {str(e)}")


def main():
    """主程序入口"""
    try:
        print("🚀 启动 WorldQuant Brain 批量 Alpha 生成系统")

        print("\n📋 请选择运行模式:")
        print("1: 自动模式 (测试并自动提交 2 个合格 Alpha)")
        print("2: 仅测试模式 (测试并保存合格 Alpha ID)")
        print("3: 仅提交模式 (提交已保存的合格 Alpha ID)")

        mode = int(input("\n请选择模式 (1-3): "))
        if mode not in [1, 2, 3]:
            print("❌ 无效的模式选择")
            return

        brain = BrainBatchAlpha()

        if mode in [1, 2]:
            print("\n📊 可用数据集列表:")
            for dataset in get_dataset_list():
                print(dataset)

            dataset_index = input("\n请选择数据集编号: ")
            dataset_name = get_dataset_by_index(dataset_index)
            if not dataset_name:
                print("❌ 无效的数据集编号")
                return

            print("\n📈 可用策略模式:")
            print("1: 基础策略模式")
            print("2: 多因子组合模式")

            strategy_mode = int(input("\n请选择策略模式 (1-2): "))
            if strategy_mode not in [1, 2]:
                print("❌ 无效的策略模式")
                return

            results = brain.simulate_alphas(None, strategy_mode, dataset_name)

            if mode == 1:
                submit_alpha_ids(brain, 2)

        elif mode == 3:
            num_to_submit = int(input("\n请输入要提交的 Alpha 数量: "))
            if num_to_submit <= 0:
                print("❌ 无效的提交数量")
                return
            submit_alpha_ids(brain, num_to_submit)

    except Exception as e:
        print(f"❌ 程序运行出错: {str(e)}")


if __name__ == "__main__":
    main()
