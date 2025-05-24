import argparse
import requests
import json
import os
from time import sleep
from requests.auth import HTTPBasicAuth

from typing import List, Dict
import time

import pyarrow as pa
import pyarrow.parquet as pq
import pandas as pd

"""数据集配置管理模块"""

DATASET_CONFIGS = {
    'fundamental6': {
        'id': 'fundamental6',
        'universe': 'TOP3000',
        'description': '基础财务数据',
        'api_settings': {
            'instrumentType': 'EQUITY',
            'region': 'USA',
            'delay': 1,
            'decay': 0,
            'neutralization': 'SUBINDUSTRY',
            'truncation': 0.08,
            'pasteurization': 'ON',
            'unitHandling': 'VERIFY',
            'nanHandling': 'ON',
            'language': 'FASTEXPR'
        },
        'fields': [
            'assets', 'liabilities', 'revenue', 'netincome',
            'cash', 'debt', 'equity', 'eps', 'pe_ratio',
            'pb_ratio', 'market_cap', 'dividend_yield'
        ]
    },
    'analyst4': {
        'id': 'analyst4',
        'universe': 'TOP1000',
        'description': '分析师预测数据',
        'api_settings': {
            'instrumentType': 'EQUITY',
            'region': 'USA',
            'delay': 1,
            'decay': 0,
            'neutralization': 'SUBINDUSTRY',
            'truncation': 0.08,
            'pasteurization': 'ON',
            'unitHandling': 'VERIFY',
            'nanHandling': 'ON',
            'language': 'FASTEXPR'
        },
        'fields': [
            'anl4_tbvps_low', 'anl4_tbvps_high',
            'anl4_tbvps_mean', 'anl4_tbvps_median'
        ]
    },
    'pv1': {
        'id': 'pv1',
        'universe': 'TOP1000',
        'description': '股市成交量数据',
        'api_settings': {
            'instrumentType': 'EQUITY',
            'region': 'USA',
            'delay': 1,
            'decay': 0,
            'neutralization': 'SUBINDUSTRY',
            'truncation': 0.08,
            'pasteurization': 'ON',
            'unitHandling': 'VERIFY',
            'nanHandling': 'ON',
            'language': 'FASTEXPR'
        },
        'fields': [
            'volume', 'close', 'open', 'high', 'low',
            'vwap', 'returns', 'turnover', 'volatility'
        ]
    }
}


def get_dataset_list():
    """获取所有可用数据集列表"""

    return [
        f"{idx+1}: {name} ({config['universe']}) - {config['description']}"
        for idx, (name, config) in enumerate(DATASET_CONFIGS.items())
    ]


def get_dataset_config(dataset_name):
    """获取指定数据集的配置"""

    return DATASET_CONFIGS.get(dataset_name)


def get_dataset_by_index(index):
    """通过索引获取数据集名称"""

    try:
        return list(DATASET_CONFIGS.keys())[int(index)-1]
    except (IndexError, ValueError):
        return None


def get_dataset_fields(dataset_name):
    """获取指定数据集的字段列表"""

    config = DATASET_CONFIGS.get(dataset_name)
    return config['fields'] if config else []


def get_api_settings(dataset_name):
    """获取指定数据集的API设置"""

    config = DATASET_CONFIGS.get(dataset_name)
    if config and 'api_settings' in config:
        settings = config['api_settings'].copy()
        settings['universe'] = config['universe']
        return settings
    return None

class AlphaGenerator:
    def __init__(self, credentials_path: str, moonshot_api_key: str):
        self.sess = requests.Session()
        self.setup_auth(credentials_path)
        self.moonshot_api_key = moonshot_api_key
        
    def setup_auth(self, credentials_path: str) -> None:
        """Set up authentication with WorldQuant Brain."""
        print(f"Loading credentials from {credentials_path}")
        with open(credentials_path) as f:
            credentials = json.load(f)
        
        username, password = credentials
        self.sess.auth = HTTPBasicAuth(username, password)
        
        print("Authenticating with WorldQuant Brain...")
        response = self.sess.post('https://api.worldquantbrain.com/authentication')
        print(f"Authentication response status: {response.status_code}")
        print(f"Authentication response: {response.text[:500]}...")  # Print first 500 chars
        
        if response.status_code != 201:
            raise Exception(f"Authentication failed: {response.text}")
        
    def get_data_fields(self) -> List[Dict]:
        """Fetch available data fields from WorldQuant Brain."""
        params = {
            'dataset.id': 'fundamental6',
            'delay': 1,
            'instrumentType': 'EQUITY',
            'limit': 50,
            'offset': 0,
            'region': 'USA',
            'universe': 'TOP3000'
        }
        
        print("Requesting data fields...")
        response = self.sess.get('https://api.worldquantbrain.com/data-fields', params=params)
        print(f"Data fields response status: {response.status_code}")
        print(f"Data fields response: {response.text[:500]}...")  # Print first 500 chars
        
        if response.status_code != 200:
            raise Exception(f"Failed to get data fields: {response.text}")
        
        data = response.json()
        if 'results' not in data:
            raise Exception(f"Unexpected data fields response format. Keys: {list(data.keys())}")
        
        return data['results']
'''

pv1=['adv20', 'cap', 'close', 'country', 'currency', 'dividend', 'exchange', 'high', 'industry', 'low', 'market', 'open', 'returns', 'sector', 'sedol', 'sharesout', 'split', 'subindustry', 'volume', 'vwap']

fundamental6=['assets', 'assets_curr', 'bookvalue_ps', 'capex', 'cash', 'cash_st', 'cashflow', 'cashflow_dividends', 'cashflow_fin', 
'cashflow_invst', 'cashflow_op', 'cogs', 'current_ratio', 'debt', 'debt_lt', 'debt_st', 'depre_amort', 'ebit', 'ebitda', 'employee', 
'enterprise_value', 'eps', 'equity', 'fnd6_acdo', 'fnd6_acodo', 'fnd6_acox', 'fnd6_acqgdwl', 'fnd6_acqintan', 'fnd6_adesinda_curcd', 
'fnd6_aldo', 'fnd6_am', 'fnd6_aodo', 'fnd6_aox', 'fnd6_aqc', 'fnd6_aqi', 'fnd6_aqs', 'fnd6_beta', 'fnd6_capxs', 'fnd6_capxv', 'fnd6_caxts', 
'fnd6_ceql', 'fnd6_ch', 'fnd6_ci', 'fnd6_cibegni', 'fnd6_cicurr', 'fnd6_cidergl', 'fnd6_cik', 'fnd6_cimii', 'fnd6_ciother', 'fnd6_cipen']


'''

if __name__=='__main__':
    generator = AlphaGenerator("brain_credentials.txt", None)
    results=generator.get_data_fields()
    resultsid=[result['id'] for result in results]

    expr=[ "-is_nan({})".format(id) for id in resultsid ]

    # 创建Pandas DataFrame
    df = pd.DataFrame({'expr':expr})

    # 转换为PyArrow Table
    table = pa.Table.from_pandas(df)

    # 写入Parquet文件
    pq.write_table(table, 'expr_list.parquet')


