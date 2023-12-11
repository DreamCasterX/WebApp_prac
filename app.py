from flask import Flask
app = Flask(__name__)   # __name__ = 當前模組 (主程式是__main__)


@app.route("/")  # 網頁資料夾的根目錄
def home():    # 這裡會把home()函式當成參數丟到 app.route()的函式去執行, 會先執行完app.route後才跑home()自己  
               # 也就是說app.route()提供給home()附加/裝飾的功能
    return "Helo<br/>Mike"


@app.route("/test")  # 網頁資料夾的/test目錄
def test():
    return " THIS IS TEST PAGE"
    
            
if __name__ == "__main__":  # 如果以主程式執行
    app.run()  # 立刻啟動伺服器
    


