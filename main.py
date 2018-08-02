from flask import Flask
from flask import request
from flask import render_template
from flask import redirect

app =Flask(__name__)

from wtforms import Form,TextField,PasswordField,validators

    
class LoginForm(Form): #python form
    username = TextField("username",[validators.Required()])
    password = PasswordField("passwowd",[validators.Required()])
@app.route("/user",methods=['GET','POST'])
def login():
    myForm = LoginForm(request.form) #python form
    if request.method=='POST':        
        # username=request.form['username']
        # password=request.form['password']
        # if username=="YAHOO" and password=="123456":
        if myForm.username.data=="YAHOO" and myForm.password.data=="123456" and myForm.validate():#python form
            return redirect("http://tw.yahoo.com")
        else:
            message="Login Failed"
            return render_template('index.html',message=message,form=myForm)
            # return render_template('index.html',message=message)
    return render_template('index.html',form=myForm) #python form
    # return render_template('index.html')
if __name__=="__main__":
    app.run('0.0.0.0',port=80)
