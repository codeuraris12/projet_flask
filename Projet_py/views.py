from flask import render_template, request, redirect, url_for
from models import User,db,app


@app.route("/login",methods=["GET","POST"])
def login_page():
    if request.method== "GET":
        return render_template("login.html")
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        user = User.query.filter_by(email=email,password=password).first()
        
        if user:
            return render_template("home.html",validation=1,user=user,lien_conn=1)
        else:
            return render_template("login.html",error="Username ou Mot de passe incorrect")


@app.route("/sign-up", methods=["GET", "POST"])
def sign_up_page():
    if request.method == "POST":
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        email = request.form["email"]
        password = request.form["password1"]
        password_confirm = request.form["password2"]
        
        if password == password_confirm:
            # Enregistrer les données de l'utilisateur dans la base de données
            user = User(first_name=first_name, last_name=last_name, email=email, password=password)
            #recherche 
            user_recherche = User.query.filter_by(email=email).first()
            if user_recherche:
                 return render_template("sign-up.html", error="L'email est déja enregistrer!")
            else:
                db.session.add(user)
                db.session.commit()
                return redirect(url_for("login_page"))
        else:
            return render_template("sign-up.html", error="Les mots de passe ne correspondent pas.")
    if request.method== "GET":
        return render_template("sign-up.html")



@app.route("/logout",methods=["GET","POST"])
def logout_page():
    if request.method == "GET":
        return render_template("login.html")

@app.route("/",methods=["GET"])
def home_page():
    return render_template("home.html",lien_conn=0)
