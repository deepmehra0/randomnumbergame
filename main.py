import flask
import random
app =flask.Flask(__name__)

@app.route('/')
def guess_number():
    return('<h1 align="center"> Guess a number between 0 to 9  </h1> \
           <Body bgcolor="#9C9EFE"><img src ="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" width =650px ></body>\
           ')
rand = random.randint(0,9)
@app.route('/<int:value>')
def answer(value):
    if value < rand:
        return ('<h1 align="center"> Opps Number Is Too Low  </h1> \
                <Body bgcolor="#B1E1FF">   <img src ="https://media1.giphy.com/media/3oEdv88Zd7WWhqZhDO/giphy.gif?cid=790b761125aec7b08289867456cd71d275de2be2ce457fa3&rid=giphy.gif&ct=g" width =650px> </Body> ')
    if value > rand:
        return ('<h1 align="center"> Opps Number Is Too High  </h1> \
                    <Body bgcolor="#8FE3CF">     <img src ="https://media4.giphy.com/media/2xPJCQNmugCWvpYiia/200w.webp?cid=ecf05e47lbfsgaxlw1wd5anemtzei6egcavdr2t0qjr11m7x&rid=200w.webp&ct=g" width =650px></body>\
                       ')
    if value ==rand:
        return ('<h1 align="center"> Well done You Win   </h1> \
                           <Body bgcolor="#E8F9FD">      <img  src ="https://media3.giphy.com/media/2RGhmKXcl0ViM/200w.webp?cid=ecf05e477tl7yaduz87v43wswfq5kvspj0kj19f8zkdrla0j&rid=200w.webp&ct=g"  width =650px></body>')
if __name__ == '__main__' :
    app.run(debug='on')
