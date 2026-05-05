import flet as ft
import datetime
import os
import random
import time

def main(page: ft.Page):
    page.title = "自分専用・日記アプリ"
    page.window_width = 450
    page.window_height = 600
    page.theme_mode = ft.ThemeMode.LIGHT

    # 疑似AIから返信をもらう関数（API不要！）
    def get_ai_advice(diary_text):
        responses = [
            "今日もお疲れ様！素晴らしい一日でしたね。明日も応援しています！",
            "そんなことがあったんですね。たまにはゆっくり休むのも大切ですよ。",
            "一歩ずつ進んでいる感じが素敵です。明日はもっと良い日になりますよ！",
            "あなたの感性が光る日記ですね。明日も楽しみです！",
            "今日という日を大切にしたあなたに、明日はきっといいことがありますよ。",
            "日記に書くことで、気持ちがスッキリしますよね。ナイスです！"
        ]
        # AIが考えているふりをして、少しだけ待つ演出
        time.sleep(1.5)
        return random.choice(responses)

    def save_clicked(e):
        if not diary_input.value:
            diary_input.error_text = "内容を入力してください"
            page.update()
            return
        
        # 処理中の表示
        save_button.disabled = True
        save_button.text = "AI（疑似）が考え中..."
        page.update()
        
        # 1. 疑似AIから言葉をもらう
        advice = get_ai_advice(diary_input.value)
        
        # 2. 日記と返信をデスクトップに保存
        today = datetime.date.today().strftime("%Y-%m-%d")
        save_path = os.path.expanduser("~/Desktop/my_diary.txt")
        with open(save_path, "a", encoding="utf-8") as f:
            f.write(f"【{today}】\n内容: {diary_input.value}\n返信: {advice}\n{'-'*20}\n")
        
        # 3. 画面に表示
        ai_response_text.value = advice
        diary_input.value = "" 
        save_button.disabled = False
        save_button.text = "日記を保存する"
        page.update()

    # --- 画面のレイアウト ---
    title_text = ft.Text("今日のできごとは？", size=25, weight="bold")
    diary_input = ft.TextField(
        label="ここに日記を書いてください",
        multiline=True,
        min_lines=8,
        autofocus=True
    )
    save_button = ft.ElevatedButton("日記を保存する", on_click=save_clicked)
    
    ai_label = ft.Text("AI（疑似）からの返信:", weight="bold", size=16)
    ai_response_text = ft.Text("ここに言葉が表示されます", italic=True, color="blue", size=14)

    page.add(
        ft.Column([
            title_text,
            diary_input,
            save_button,
            ft.Divider(),
            ai_label,
            ai_response_text
        ], scroll=ft.ScrollMode.AUTO)
    )

ft.app(target=main)
