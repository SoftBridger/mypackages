"""
用于将Dataframe转换为dict组成的list
"""

import pandas as pd
from gradio import Dataframe


def to_dictlist(df: Dataframe):
    dictlist = []
    for index, row in df.iterrows():
        a_dictlist = row.to_dict()
        dictlist.append(a_dictlist)
    print(dictlist)
    return dictlist


if __name__ == '__main__':
    df_new = pd.DataFrame({"li_no": [1, 2],
                           "li_text": ["保障结构完好、外观整洁和附属设施齐全完好。", "配备必要的检测和养护设备、设施。"]})
    to_dictlist(df_new)

