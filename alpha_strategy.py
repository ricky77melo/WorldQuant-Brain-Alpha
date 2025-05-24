"""Alpha 策略生成模块"""
import pandas as pd

class AlphaStrategy:
    def get_simulation_data(self, datafields, mode=1):
        """根据模式生成策略列表"""

        if mode == 1:
            return self.generate_basic_strategy(datafields)
        elif mode == 2:
            return self.generate_multi_factor_strategy(datafields)
        else:
            print("❌ 无效的策略模式")
            return []

    def generate_basic_strategy(self, datafields):
        """生成基础策略"""

        strategies = pd.read_parquet('expr_list.parquet', engine='pyarrow')['expr'].tolist()
        for strategy in strategies:
            print(strategy)
        

        #     # 1. 日内策略
        #     strategies.extend([
        #         # 日内收益率
        #         "group_rank((close - open)/open, subindustry)",

        #         # 隔夜收益率
        #         "group_rank((open - delay(close, 1))/delay(close, 1), subindustry)",

        #         # 高低价差异
        #         "group_rank((high - low)/open, subindustry)"
        #     ])

        #     # 2. 波动率策略
        #     strategies.extend([
        #         # 波动率偏度
        #         f"power(ts_std_dev(abs({field}), 30), 2) - power(ts_std_dev({field}, 30), 2)",

        #         # 波动率动态调整
        #         f"group_rank(std({field}, 20)/mean({field}, 20) * (1/cap), subindustry)"
        #     ])

        #     # 3. 成交量策略
        #     if field in ['volume', 'turnover']:
        #         strategies.extend([
        #             # 成交量异常
        #             "group_rank((volume/sharesout - mean(volume/sharesout, 20))/std(volume/sharesout, 20), subindustry)",

        #             # 成交量趋势
        #             "ts_corr(volume/sharesout, abs(returns), 10)"
        #         ])

        #     # 4. 市场微观结构
        #     strategies.extend([
        #         # 小单买卖压力
        #         f"group_neutralize(power(rank({field} - group_mean({field}, 1, subindustry)), 3), bucket(rank(cap), range='0,1,0.1'))",

        #         # 流动性压力
        #         f"group_rank(correlation({field}, volume/sharesout, 20), subindustry)"
        #     ])

        #     # 5. 条件触发策略
        #     strategies.extend([
        #         # 条件触发
        #         f"trade_when(ts_rank(ts_std_dev(returns, 10), 252) < 0.9, {field}, -1)",

        #         # 市场状态过滤
        #         f"trade_when(volume > mean(volume, 20), {field}, -1)"
        #     ])

        return strategies

    def generate_multi_factor_strategy(self, datafields):
        """生成多因子组合策略"""

        strategies = []
        n = len(datafields)

        for i in range(0, n-1, 2):
            field1 = datafields[i]
            field2 = datafields[i+1]

            # 1. 回归中性化
            strategies.extend([
                f"regression_neut(vector_neut({field1}, {field2}), abs(ts_mean(returns, 252)/ts_std_dev(returns, 252)))",

                # 多重回归
                f"regression_neut(regression_neut({field1}, {field2}), ts_std_dev(returns, 30))"
            ])

            # 2. 条件组合
            strategies.extend([
                # 条件选择
                f"if_else(rank({field1}) > 0.5, {field2}, -1 * {field2})",

                # 分组组合
                f"group_neutralize({field1} * {field2}, bucket(rank(cap), range='0.1,1,0.1'))"
            ])

            # 3. 复杂信号
            strategies.extend([
                # 信号强度
                f"power(rank(group_neutralize(-ts_decay_exp_window(ts_sum(if_else({field1}-group_mean({field1},1,industry)-0.02>0,1,0)*ts_corr({field2},cap,5),3),50),industry)),2)",

                # 市场状态
                f"trade_when(ts_rank(ts_std_dev(returns,10),252)<0.9, {field1} * {field2}, -1)"
            ])

        return strategies
