import os.path
import tensorflow as tf
from keras import preprocessing
import numpy as np
# import PIL
from flask import Flask, render_template, request
from keras.models import load_model

from keras.preprocessing import image

app = Flask(__name__)

dic = { 0 : 'Baterai Hp', 1 : 'Baterai Laptop', 2 : 'Botol Kaca',
        3 : 'Botol Plastik', 4 : 'Kaleng', 5 : 'Kardus', 6 : 'Kertas'}

model = load_model('model/model.h5')

model.make_predict_function()

# def predict_label(img_path):
# 	i = image.load_img(img_path, target_size=(200,200))
# 	i = image.img_to_array(i)/255.0
# 	i = i.reshape(1, 100,100,3)
# 	p = model.predict_classes(i)
# 	return dic[p[0]]

def predict_label(img_path):
    img = tf.keras.utils.load_img(img_path, target_size=(200, 200))
    x = tf.keras.utils.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    images = np.vstack([x])
    predict = model.predict(images)
    classes = np.argmax(predict)
    if classes == 0:
        kalimat = """Gambar diatas ini merupakan jenis sampah B3(Bahan Berbahaya & Beracun) yaitu baterai HP
        Sampah ini tidak boleh dibuang ke tempat sampah karena mengandung berbagai logam berat, seperti merkuri, mangan, timbal, kadmium, nikel dan lithium, yang berbahaya bagi lingkungan dan kesehatan kita. Baterai bekas sebaiknya tidak dibuang ke sembarang, sebaiknya dikumpulkan dan dibuang melalui bank sampah 
        Bahkan limbah baterai hp ini dapat dimanfaatkan menjadi produk lain seperti powerbank, untuk yang kreatif simak video berikut :
        """
        link = "https://www.youtube.com/watch?v=puaJscR-quU"
        kaca = ""
        kaleng = ""
        return kalimat, link, kaca, kaleng, classes

    elif classes == 1:
        kalimat = """Gambar diatas ini merupakan jenis sampah B3(Bahan Berbahaya & Beracun) yaitu baterai laptop
        Sampah ini tidak boleh dibuang ke tempat sampah karena mengandung berbagai logam berat, seperti merkuri, mangan, timbal, kadmium, nikel dan lithium, yang berbahaya bagi lingkungan dan kesehatan kita. Baterai bekas sebaiknya tidak dibuang ke sembarang, sebaiknya dikumpulkan dan dibuang melalui bank sampah
        Bahkan limbah baterai laptop ini dapat dimanfaatkan menjadi produk lain seperti powerbank, untuk yang kreatif simak video berikut : 
        """
        link = "https://www.youtube.com/watch?v=U4FByVjomUE"
        kaca = ""
        kaleng = ""
        return kalimat, link, kaca, kaleng, classes

    elif classes == 2:
        # kalimat = """Gambar diatas ini merupakan jenis sampah anorganik yaitu kemasan minuman yang tidak dapat diuraikan
        # Sampah ini berbahan plastik atau kaca atau kaleng. Saran daur ulang untuk sampah tersebut dapat dimanfaatkan menjadi berbagai kerajinan tangan.
        # Berikut link saran daur ulang untuk sampah berbahan kaca :
        # """

        kalimat = """Berikut link saran daur ulang untuk sampah kemasan minuman berbahan Plastik : Berikut link saran daur ulang untuk sampah kemasan minuman berbahan Kaca : Berikut link saran daur ulang untuk sampah kemasan minuman berbahan Kaleng : 
        """

        plastik = "https://www.99.co/blog/indonesia/daur-ulang-plastik/"
        kaca = "https://www.fimela.com/lifestyle/read/3767947"
        kaleng = "https://www.hipwee.com/tips/11-daur-ulang-kaleng-bekas"
        return kalimat, plastik, kaca, kaleng, classes

    elif classes == 3:
        # kalimat = """Gambar diatas ini merupakan jenis sampah anorganik yaitu kemasan minuman yang tidak dapat diuraikan
        # Sampah ini berbahan plastik atau kaca atau kaleng. Berikut link saran daur ulang untuk sampah kemasan minuman berbahan plastik :
        # """
        kalimat = """Berikut link saran daur ulang untuk sampah kemasan minuman berbahan Plastik : Berikut link saran daur ulang untuk sampah kemasan minuman berbahan Kaca : Berikut link saran daur ulang untuk sampah kemasan minuman berbahan Kaleng : 
        """
        plastik = "https://www.99.co/blog/indonesia/daur-ulang-plastik/"
        kaca = "https://www.fimela.com/lifestyle/read/3767947"
        kaleng = "https://www.hipwee.com/tips/11-daur-ulang-kaleng-bekas"
        return kalimat, plastik, kaca, kaleng, classes

    elif classes == 4:
        kalimat = """Gambar diatas ini merupakan jenis sampah anorganik yaitu kemasan minuman yang tidak dapat diuraikan
        Sampah ini berbahan plastik atau kaca atau kaleng. Saran daur ulang untuk sampah tersebut dapat dimanfaatkan menjadi berbagai kerajinan tangan. Berikut link saran daur ulang untuk sampah kemasan minuman berbahan kaleng :
        """
        plastik = "https://www.99.co/blog/indonesia/daur-ulang-plastik/"
        kaca = "https://www.fimela.com/lifestyle/read/3767947"
        kaleng = "https://www.hipwee.com/tips/11-daur-ulang-kaleng-bekas"
        return kalimat, plastik, kaca, kaleng, classes
        
    elif classes == 5:
        kalimat = """Gambar diatas ini merupakan jenis sampah Anorganik yaitu Kardus
        Sampah kardus merupakan sampah yang tidak dapat diurai secara alami, namun sampah ini dapat diolah menjadi kerajinan atau barang yang memiliki manfaat dan nilai ekonomis seperti tempat tisu, kotak pensil, bingkai foto, celengan, hiasan meja dan masih banyak lagi yang dapat dibuat dari kardus bekas.
        Berikut link saran daur ulang untuk sampah kardus : 
        """
        link = "https://www.ruparupa.com/blog/kerajinan-tangan-dari-kardus/"
        kaca = ""
        kaleng = ""
        return kalimat, link, kaca, kaleng, classes

    elif classes == 6:
        kalimat = """Gambar diatas ini merupakan jenis sampah Anorganik yaitu Kertas
        Sampah koran dan majalah merupakan sampah yang tidak dapat diurai secara alami, namun sampah ini dapat diolah menjadi kerajinan atau barang yang memiliki manfaat dan nilai ekonomis seperti vas bunga, bunga hias, hiasan dinding, taplak dan masih banyak lagi hiasan yang dapat dihasikan dari kertas bekas. Bahkan kertas bekas juga dapat didaur ulang sehingga menghasilkan kertas baru kembali.
        Berikut link saran daur ulang untuk sampah kertas :
        """
        link = "https://www.gadis.co.id/Lifestyle/105425/diy-kertas-daur-ulang-hasilnya-aesthetic-dan-ramah-lingkungan"
        kaca = ""
        kaleng = ""
        return kalimat, link, kaca, kaleng, classes

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/services")
def services():
    return render_template("upload.html")

@app.route("/submit", methods = ['GET', 'POST'])
def get_output():
    
    if request.method == 'POST':
        img = request.files['gambar']
        img_path = "static/images" + img.filename	
        img.save(img_path)
        p, l, kaleng, plastik, classes = predict_label(img_path)
    
    if classes == 2:
        return render_template("kemasan.html", prediction = p, link = l, kaleng = kaleng, plastik = plastik, img_path = img_path)
    elif classes == 3:
        return render_template("kemasan.html", prediction = p, link = l, kaleng = kaleng, plastik = plastik, img_path = img_path)
    elif classes == 4:
        return render_template("kemasan.html", prediction = p, link = l, kaleng = kaleng, plastik = plastik, img_path = img_path)

    
    return render_template("upload.html", prediction = p, link = l, img_path = img_path)

if __name__ =='__main__':
	app.debug = True
	app.run(debug = True)