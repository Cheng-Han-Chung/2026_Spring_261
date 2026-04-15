import google.generativeai as genai

# 貼上你的真實 API Key
genai.configure(api_key="AIzaSyCSUJ1C_hjIrSKEWwKrMynQvyF7tOy_lNA")

print("🔍 正在尋找你的帳號可以使用的模型...")
for m in genai.list_models():
    # 篩選出可以支援文字生成 (generateContent) 的模型
    if 'generateContent' in m.supported_generation_methods:
        print(f"👉 找到可用模型：{m.name}")