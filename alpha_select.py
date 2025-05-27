import pandas as pd




if __name__=='__main__':
    pd.set_option('display.max_colwidth', None)
    alpha_df=pd.read_csv('alpha_list.csv')
    alpha_df['abs_sharpe']=alpha_df['sharpe'].abs()
    alpha_df['abs_fitness']=alpha_df['fitness'].abs()
    alpha_df=alpha_df.sort_values('abs_fitness', ascending=False)
    print(alpha_df.head(20))