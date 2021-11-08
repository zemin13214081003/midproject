from flask import Flask, request,render_template
import re
app = Flask(__name__) 
def func_1():
    newfuncction1="new gift is teddy"
    print("new gift is teddy")
    return newfunction1

def fun_2():
    newfunction2="new girt is car"
    print("new girt is car")
    return newfunction2

def fun_3():
    newfunction3="new girt is phone"
    print("new girt is phone")
    return newfunction3

def count_w_numb():
    str = request.form["request"]
    pattern = r',|\.|/|;|\'|`|\[|\]|<|>|\?|:|"|\{|\}|\~|!|@|#|\$|%|\^|&|\(|\)|-|=|\_|\+|，|。|、|；|‘|’|【|】|·|！| |…|（|）'
    com = re.split(pattern, str)
    lenth = len(com)
    strr = ["how many word ",lenth]
    return(strr)

def count_a_numb():
	com1 = request.form["request"]
	lenth = len(com1)
	strr = ["the length of words ", lenth]
	return(strr)
    
def home():
	return render_template("request.html")

@app.route("/grp8", methods=["GET","POST"])
def my_form_post():
	request = request.form["request"]
	if request == "new gift is teddy":
		newfunction = func_1()
		result = {"output": newfunction,
				  "Total words": count_w_numb(),
				  "Length": count_a_numb()
				  }
		result = {str(key): value for key, value in result.items()}
		return jsonify(result=result)

if __name__ == "__main__":
	app.run(debug=True)
