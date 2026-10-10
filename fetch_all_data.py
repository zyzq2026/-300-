import akshare as ak
import pandas as pd
import os
import sys
import traceback
import time

print("========== 数据抓取工具启动 ==========")

# ========== 获取程序当前所在目录 ==========
if getattr(sys, 'frozen', False):
    # 打包后的 exe / 可执行文件运行
    app_dir = os.path.dirname(sys.executable)
else:
    # 普通 Python 脚本运行
    app_dir = os.path.dirname(os.path.abspath(__file__))

print(f"数据将保存在: {app_dir}")

try:
    # ---------------- 抓取沪深300（腾讯接口） ----------------
    print("\n[1/2] 正在抓取沪深300指数...")
    time.sleep(1)
    hs300 = ak.stock_zh_index_daily_tx(symbol="sh000300")
    
    # 统一日期格式
    hs300["date"] = hs300["date"].astype(str)
    hs300_2025 = hs300[hs300["date"] >= "2025-01-01"].reset_index(drop=True)
    
    # 保存为 Excel
    hs300_file = os.path.join(app_dir, "hs300_2025_now.xlsx")
    hs300_2025.to_excel(hs300_file, index=False)
    print(f"  ✅ 沪深300抓取成功！共 {len(hs300_2025)} 条，已保存: hs300_2025_now.xlsx")

    # ---------------- 抓取中债新综合财富(总值)指数 ----------------
    print("\n[2/2] 正在抓取中债-新综合财富(总值)指数...")
    time.sleep(1)
    cbond = ak.bond_new_composite_index_cbond(indicator="财富", period="总值")
    
    # 统一日期格式
    cbond["date"] = cbond["date"].astype(str)
    cbond_2025 = cbond[cbond["date"] >= "2025-01-01"].reset_index(drop=True)
    
    # 保存为 Excel
    cbond_file = os.path.join(app_dir, "chinabond_index_2025_now.xlsx")
    cbond_2025.to_excel(cbond_file, index=False)
    print(f"  ✅ 中债指数抓取成功！共 {len(cbond_2025)} 条，已保存: chinabond_index_2025_now.xlsx")

except Exception as e:
    print("\n❌ 抓取过程中发生错误：")
    traceback.print_exc()
