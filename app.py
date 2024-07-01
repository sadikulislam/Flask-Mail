from config import app, mail
from flask_mail import Message


@app.route('/send')
def send_mail():
    msg = Message("Hello from Flask!!", recipients=["mrneo.mx@gmail.com"])
    msg.body = "This is a test email."
    mail.send(msg)
    return "Mail sent succesfully!"

if __name__ == '__main__':
    app.run(debug=True)