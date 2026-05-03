import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rc('font', family='AppleGothic') # Mac用の日本語フォントを指定
# 1. Excelの読み込み
df = pd.read_excel(r'/Users/wadamoto/Documents/家計簿.xlsx', usecols='B:F', header=9)
# 2. 追加：日付列が「日付ではない」行（Totalなど）を削除する
# pd.to_datetimeを使って、日付に変換できない文字を「空（NaN）」にする
df['日付'] = pd.to_datetime(df['日付'], errors='coerce')

# 「空」になった行（合計行など）を丸ごと削除する
df = df.dropna(subset=['日付'])

# 確認用：これで合計行が消えて、綺麗なデータだけが残ります
print(df.tail()) 
# 2. データのクリーニング（前回学んだ、エラー回避の魔法）
df['支出'] = pd.to_numeric(df['支出'], errors='coerce')
df = df.dropna(subset=['支出', '費目'])

# 3. カテゴリごとに金額を合計する
category_totals = df.groupby('費目')['支出'].sum()

# 4. 円グラフを描画する
plt.figure(figsize=(8, 8))
category_totals.plot.pie(autopct='%1.1f%%', startangle=90)
plt.title("Spending by Category")
plt.ylabel("") # 横のラベルを消して見やすくする
plt.show()
