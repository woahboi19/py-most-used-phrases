from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup
from collections import Counter
from string import punctuation

app = Flask(__name__)


@app.route('/')
def index():
  return render_template("index.html")


@app.route('/soru1')
def soru1html():
    return render_template("soru1.html")


@app.route('/soru2')
def soru2html():
    return render_template("soru2.html")


@app.route('/soru3')
def soru3html():
    return render_template("soru3.html")


@app.route('/soru4')
def soru4html():
    return render_template("soru4.html")


@app.route('/soru5')
def soru5html():
    return render_template("soru5.html")


@app.route('/soru1cevap/', methods=["GET", "POST"])
def soru1cevap():
    deneme=request.form.get('text')
    print(deneme)
    r = requests.get(deneme)

    soup = BeautifulSoup(r.content, "html.parser")

    text = (''.join(s.findAll(text=True)) for s in soup.findAll('p'))

    c = Counter((x.rstrip(punctuation).lower() for y in text for x in y.split()))
    print(c.most_common())  # prints most common words staring at most common.
    return 'You entered: {}'.format(request.form['text']), 204



@app.route('/soru2cevap/', methods=["GET", "POST"])
def soru2cevap():

        deneme=request.form.get('text')
        deneme2=request.form.get('text2')
        
        r1 = requests.get(deneme)
        r2 = requests.get(deneme2)

        soup = BeautifulSoup(r1.content, "html.parser")
        text1 = (''.join(s.findAll(text=True)) for s in soup.findAll('p'))

        soup = BeautifulSoup(r2.content, "html.parser")
        text2 = (''.join(s.findAll(text=True)) for s in soup.findAll('p'))

        s1 = (x.rstrip(punctuation).lower() for y in text1 for x in y.split())
        s2 = (x.rstrip(punctuation).lower() for y in text2 for x in y.split())
        f1 = Counter(filter(lambda a: len(a) >= 4, s1))
        f2 = Counter(filter(lambda a: len(a) >= 4, s2))
        print(f1.most_common(5))
        print(f2.most_common(5))

        return 'Click.', 204
@app.route('/soru3cevap/', methods=["GET", "POST"])
def soru3cevap():
    deneme=request.form.get('text')
    deneme2=request.form.get('text2')
    r1 = requests.get(deneme)
    r2 = requests.get(deneme2)

    soup = BeautifulSoup(r1.content, "html.parser")
    text1 = (''.join(s.findAll(text=True)) for s in soup.findAll('p'))

    soup = BeautifulSoup(r2.content, "html.parser")
    text2 = (''.join(s.findAll(text=True)) for s in soup.findAll('p'))
    textc = (''.join(s.findAll(text=True)) for s in soup.findAll('p'))


    s1 = (x.rstrip(punctuation).lower() for y in text1 for x in y.split())
    s2 = (x.rstrip(punctuation).lower() for y in text2 for x in y.split())
    f1 = Counter(filter(lambda a: len(a) >= 4, s1))
    f2 = Counter(filter(lambda a: len(a) >= 4, s2))

    k1 = f1.most_common(5)
    k2 = f2.most_common(5)
    l1 = [item for t in k1 for item in t]
    l2 = [item for t in k2 for item in t]

    print(l1)
    print(l2)
    freq = 1
    for i in range(0,5):
      for j in range(0,5):
        if l1[i*2] == l2[j*2]:
          freq = freq*l2[j*2+1]
    
    a = Counter((x.rstrip(punctuation).lower() for y in textc for x in y.split()))
    kl = a.most_common()
    kel = [item for t in kl for item in t]
    tpl = 0

    for i in range(0,int(len(kel)/2)):
        tpl += kel[2*i+1]

    freq = freq/tpl
    print(freq)
    return 'Click.', 204

if __name__ == '__main__':
    app.run(debug=True)
