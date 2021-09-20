from flask import Flask, render_template, request, redirect, session


app = Flask(__name__)  
app.secret_key = 'secret'


@app.route('/')         
def survey():
    
    if 'visits' in session:
        session['visits'] = session['visits'] + 1  # reading and updating session data
    else:
        session['visits'] = 1

    if 'counter' not in session:
        session['counter'] =0
    
    return render_template("index.html")

@app.route('/process', methods=['POST'])  
def process_form():
    print(request.form)
    session['data'] = request.form
    return redirect ("/result")
 
@app.route('/result')  
def showResult():
    return render_template("result.html")

if __name__=="__main__":   
    app.run(debug=True)    