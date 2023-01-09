from flask import Flask,render_template,request,jsonify,url_for,redirect,session


from chat import get_response
app = Flask(__name__)
app.secret_key="somesecretkeyyhatonlyishouldsee"


class User:
    def __init__(self,id,username,password):
        self.id = id
        self.username = username
        self.password = password
    def __repr__(self):
        return f'<User: {self.username}>'
   
   
users = []
users.append(User(id=1, username='josue', password='bluesgospel2@'))
users.append(User(id=2, username='william', password='secret'))
users.append(User(id=3, username='carlos', password='carlos'))     
    
print(users)
    








@app.get('/base')
def index_get():
    return render_template('base.html')



@app.route('/', methods=['GET', 'POST'])
def login_get():
    if request.method=='POST':
        session.pop('user_id', None)
        username = request.form['username']
        password = request.form['password']
        user = [x for x in users if x.username == username][0]
        if user and user.password == password:
            session['user_id'] = user.id
            return redirect(url_for('index_get'))
        
        return redirect(url_for('login'))
            
        
    
    return render_template('login.html')


@app.post('/predict')
def predict():
    text = request.get_json().get("message")
    response = get_response(text)
    message = {'answer': response}
    return jsonify(message) 
 

 
if __name__ == '__main__':
    app.run(debug = True)
    
