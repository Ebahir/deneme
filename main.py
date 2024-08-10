from flask import Flask
import random

app = Flask(__name__)

liste = [
    "Teknolojik bağımlılıktan mustarip olan çoğu kişi, kendilerini şebeke kapsama alanı dışında bulduklarında veya cihazlarını kullanamadıkları zaman yoğun stres yaşarlar.",
    "2018 yılında yapılan bir araştırmaya göre 18-34 yaş arası kişilerin %50'den fazlası kendilerini akıllı telefonlarına bağımlı olarak görüyor.",
    "Elon Musk, sosyal ağların içeriği görüntülemek için mümkün olduğunca fazla zaman harcamamız için bizi platformun içinde tutmak üzere tasarlandığını iddia ediyor.",
    "Sosyal ağların olumlu ve olumsuz yanları vardır ve bu platformları kullanırken her ikisinin de farkında olmalıyız."
]

@app.route("/")
def hello_world():
    return '<p>Cristiano Ronaldo dos Santos Aveiro</p><a href="/ikinci">Rastgele bir gerçeği görüntüle!</a>   <a href="/yazitura">yazı/tura</a>'

@app.route("/ikinci")
def ikinci():
    return f'<p>{random.choice(liste)}</p><a href="/">Anasayfa</a>'

@app.route("/yazitura")
def yazitura():
    result = random.choice(["Yazı", "Tura"])
    return f'<p>{result}</p><a href="/yazitura">Tekrar Dene</a> <a href="/">Anasayfa</a>'

app.run(debug=True)
