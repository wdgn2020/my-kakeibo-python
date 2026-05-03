import flet as ft
import datetime

def main(page: ft.Page):
    page.title = "マイ日記アプリ"
    page.window_width = 400
    page.window_height = 500
    page.theme_mode = ft.ThemeMode.LIGHT

    # 保存ボタンが押された時の処理
    def save_clicked(e):
        if not diary_input.value:
            diary_input.error_text = "内容を入力してください"
            page.update()
        else:
            today = datetime.date.today().strftime("%Y-%m-%d")
            with open("my_diary.txt", "a", encoding="utf-8") as f:
                f.write(f"【{today}】\n{diary_input.value}\n{'-'*20}\n")
            
            diary_input.value = ""
            diary_input.error_text = None
            # 完了メッセージを表示
            page.snack_bar = ft.SnackBar(ft.Text("日記を保存しました！"))
            page.snack_bar.open = True
            page.update()

    # 画面の部品（アイコンを使わない設定に変更）
    title_text = ft.Text("今日のできごとは？", size=25, weight="bold")
    diary_input = ft.TextField(
        label="ここに日記を書いてください",
        multiline=True,
        min_lines=10,
        autofocus=True
    )
    save_button = ft.ElevatedButton("日記を保存する", on_click=save_clicked)

    # 画面に並べる
    page.add(
        ft.Column([
            title_text,
            diary_input,
            save_button
        ], horizontal_alignment="center")
    )

# 確実に文字入力ができるように「ブラウザ」で開く設定
ft.app(target=main, view=ft.AppView.WEB_BROWSER)
