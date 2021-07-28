from flask import Flask, render_template, request, url_for


app = Flask(__name__, static_url_path='/static')


@app.route("/")
def index(tab=None):
    return render_template("index.html", tab=tab)


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
def color(tab=None):
    if request.method == 'POST':
        temp = int(request.form['tab'])

        print(temp)
        
    elif request.method == 'GET':
        pass

    return render_template("index.html", tabValue=temp)


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
