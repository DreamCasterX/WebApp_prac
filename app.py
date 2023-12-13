from flask import Flask, render_template
app = Flask(__name__)   # __name__ = 當前模組 (主程式是__main__)


@app.route("/")  # 網頁資料夾的根目錄
def hello():    # 這裡會把hello()函式當成參數丟到 app.route()的函式去執行, 會先執行完app.route後才跑hello()自己  
               # 也就是說app.route()提供給hello()附加/裝飾的功能
    return """
<h1>歡迎來到Mike的測試網頁</h1></br>
<a href="https://google.com/" target="_blank">點我打開Google</a></br>
"""
            
            
@app.route("/home")  # 網頁資料夾的/home目錄
def home():   
    return render_template("home.html")
            
            
if __name__ == "__main__":  # 如果以主程式執行
    app.run()  # 立刻啟動伺服器
    


