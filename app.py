from email import message
from flask import Flask, render_template, request, url_for
from flask_mail import Mail, Message
from dotenv import load_dotenv
import os
import smtplib
# import socket
# socket.gethostbyname("")

from email.utils import formataddr
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

@app.route("/")
def index() :
    return render_template("index.html")
# @app.route("/", methods=['POST', 'GET'])
# def color(num=None):
#     if request.method == 'POST':
#         temp = request.form['num']
#         temp = int(temp)

#         temp1 = request.form['char1']
#         print(temp)
#         print(temp1)
        
#     elif request.method == 'GET':

#         pass

#     return render_template("./screens/color.html", num=temp, char1=temp1)

@app.route("/", methods=['POST', 'GET'])
def send_email(name=None, mobile=None, email=None, bac=None, desc=None):
    name = request.form["name"]
    mobile = request.form["mobile"]
    email = request.form["email"]
    bac = request.form["bac"]
    desc = request.form["desc"]
    # msg = Message('Hello', sender=os.environ.get("MAIL_USERNAME"), recipients=[email])
    
    # msg.html = f"<h1>{name}님</h1>  <h2>전화번호: {mobile}<h2> <h2>소요예산: {bac}</h2> <br /> <br /> <br /> {desc}"
    # with smtplib.SMTP(host="smtp.gamil.com", port=587) as app:
    #     app.starttls()
    #     app.login(os.environ.get("MAIL_USERNAME"),  os.environ.get("MAIL_PASSWORD"))
    #     app.sendmail(email, os.environ.get("MAIL_USERNAME"), msg)
    # mail.send(msg)

        
    # if request.method == 'POST':
    print(name)
    print(mobile)
    print(email)
    print(bac)
    print(desc)

    # msg = Message("Hello", sender=os.environ.get("MAIL_USERNAME"), recipients=[email])
    # msg.html = f"<h1>{name}님</h1>  <h2>전화번호: {mobile}<h2> <h2>소요예산: {bac}</h2> <br /> <br /> <br /> {desc}"
    # with smtplib.SMTP(host="smtp.gamil.com", port=587) as app:
    #     app.starttls()
    #     app.login(os.environ.get("MAIL_USERNAME"),  os.environ.get("MAIL_PASSWORD"))
    #     app.sendmail(email, os.environ.get("MAIL_USERNAME"), msg)
    # mail.send(msg)
    # return True

    mail_username = os.environ.get('MAIL_USERNAME')
    mail_password = os.environ.get('MAIL_PASSWORD')
    mail_port = int(os.environ.get('MAIL_PORT'))
    mail_server = os.environ.get('MAIL_SERVER')

    from_addr = formataddr(('counselor', email))
    to_addr = formataddr(('me', mail_username))
    session = None

    print("username : ", mail_username)
    print("password : ", mail_password)
    print("username : ",  mail_port)
    print("password : ", mail_server)

    try:
        # SMTP 세션 생성
        session = smtplib.SMTP(mail_server, mail_port)
        session.set_debuglevel(False)
        # SMTP 계정 인증 설정
        session.ehlo()
        session.starttls()
        session.login(mail_username, mail_password)
        # 메일 콘텐츠 설정

        # 메일 송/수신 옵션 설정
        message = MIMEMultipart("alternative")

        message.set_charset('utf8')
        message['From'] = from_addr
        message['To'] = to_addr
        message['Subject'] = 'mustang 상담'
        # 메일 콘텐츠 - 내용
        body = f'''
        <p> 이름: {name} </p>
        <p> 전화번호: {mobile} </p>
        <p> 이메일: {email} </p>
        <p> 소요예산: {bac} </p>
        <br />
        <hr />
        <br />
        내용: {desc}
        '''
        bodyPart = MIMEText(body, 'html', 'utf8')

        message.attach( bodyPart )
        # 메일 발송
        session.sendmail(from_addr, to_addr, message.as_string())
        print('성공했다!!!!!!!!!!')
    except Exception as e:
        print(e)
    finally:
        name=None
        mobile=None
        email=None
        bac=None
        desc=None
                
        if session is not None:
            session.quit()

    # elif request.method == 'GET':
    #     pass

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)


#     <!-- <div>
#      <label for="num">몇 번</label>
#      <input class="color_tap color_tap_2" type="text" name="num" />
#  </div>
# <button class="color_tap color_tap_3" type="submit" >제출</button> -->
# <!-- <p>
#   {% if num == None %}
#       <h5>아직 아무 값도 입력이 안되었습니다.</h5>
#   {% else %}
#        <h5>{{num}}을 입력받았습니다.</h5>
   
#        {% for i in range(1, num+1)  %}
       
   
#        <p>
#            {% for j in range(0, i) %} 
#                {{char1}}
#            {% endfor %} 
#        </p>
#        {% endfor %}
#    {% endif %}
# </p> -->

# <!-- {% if color_data == 1 %} -->

# <!-- {% elif color_data == 2 %}
#   <div>a</div>
#   {% endif %} -->

# <!-- <ul class="color_tap_wrapper">
#   <li class="nav-item">
#    <a class="color_tap color_tap_1 nav-link" href="#"></a>
#   </li>
#   <li class="color_tap color_tap_2"></li>
#   <li class="color_tap color_tap_3"></li>
#   <li class="color_tap color_tap_4"></li>
#   <li class="color_tap color_tap_5"></li>
#   <li class="color_tap color_tap_6"></li>
#   <li class="color_tap color_tap_7"></li>
#   <li class="color_tap color_tap_8"></li>
#   <li class="color_tap color_tap_9"></li>
#   <li class="color_tap color_tap_0"></li>
#  </ul> -->
