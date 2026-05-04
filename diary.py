import flet as ft
import datetime
import os
import random

def main(page: ft.Page):
    page.title = "AI日記アドバイザー（お試し版）"
    page.window_width = 450
    page.window_height = 600
    page.theme_mode = ft.ThemeMode.LIGHT

    # AIのフリをして返信する関数（ここを改造しました！）
    def get_ai_advice(diary_text):
        # AIが考えそうな返信パターンをいくつか用意
        responses = [
            "今日もお疲れ様！素晴らしい一日でしたね。明日も応援しています！",
            "そんなことがあったんですね。たまにはゆっくり休むのも大切ですよ。",
            "一歩ずつ進んでいる感じが素敵です。明日はもっと良い日になりますよ！",
            "あなたの感性が光る日記ですね。明日も楽しみです！"
        ]
        # ランダムに1つ選んで返す
        return random.choice(responses)

    def save_clicked(e):
        if not diary_input.value:
            diary_input.error_text = "内容を入力してください"
            page.update()
            return
        
        save_button.disabled = True
        save_button.text = "AIが考え中..."
        page.update()
        
        # 1. 疑似AIから言葉をもらう
        import time
        time.sleep(1) # AIが考えているふりをして1秒待つ
        advice = get_ai_advice(diary_input.value)
        
        # 2. 日記とAIの言葉をデスクトップに保存
        today = datetime.date.today().strftime("%Y-%m-%d")
        save_path = os.path.expanduser("~/Desktop/my_diary.txt")
        with open(save_path, "a", encoding="utf-8") as f:
            f.write(f"【{today}】\n内容: {diary_input.value}\nAI(疑似)より: {advice}\n{'-'*20}\n")
        
        # 3. 画面に表示
        ai_response_text.value = advice
        diary_input.value = ""
        save_button.disabled = False
        save_button.text = "日記を保存する"
        page.update()

    # --- 画面レイアウト ---
    title_text = ft.Text("今日のできごとは？", size=25, weight="bold")
    diary_input = ft.TextField(label="ここに日記を書いてください", multiline=True, min_lines=8)
    save_button = ft.ElevatedButton("日記を保存する", on_click=save_clicked)
    ai_response_text = ft.Text("ここにAIの言葉が表示されます", italic=True, color="blue", size=14)

    page.add(
        ft.Column([
            title_text,
            diary_input,
            save_button,
            ft.Divider(),
            ft.Text("AIからの返信:", weight="bold"),
            ai_response_text
        ], scroll=ft.ScrollMode.AUTO)
    )

ft.app(target=main)
