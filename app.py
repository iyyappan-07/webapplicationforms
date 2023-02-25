from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
@app.route("/homepage")
def homepage():
    return render_template("register.html")
    
    
@app.route("/suucees",methods=["POST","GET"])
def finalpage():
    if request.method=="POST":
        n= request.form.get("name")
        a= request.form.get("age")
        c= request.form.get("city")
        d= request.form.get("degree")
        return render_template("finish.html",name=n,age=a,city=c,degree=d )
    


if __name__=="__main__":
    app.run(debug=True)
