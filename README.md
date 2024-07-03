# Flask Mail Sender

This is a simple Flask web application that allows users to send emails through a web form. 

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/sadikulislam/Flask-Mail.git
    cd flask_mail_project
    ```

2. **Create a virtual environment and activate it:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**

    ```bash
    pip install -r requirement.txt
    ```

4. **Create a `.env` file in the project root directory and add your email configuration:**

    ```env
    MAIL_SERVER=smtp.gmail.com
    MAIL_PORT=587
    MAIL_USE_TLS=True
    MAIL_USE_SSL=False
    MAIL_USERNAME=your-email@gmail.com
    MAIL_PASSWORD=your-email-password
    MAIL_DEFAULT_SENDER=your-email@gmail.com
    ```

    **Note:** If you have 2-Step Verification enabled on your Google account, you need to create an App Password and use it as `MAIL_PASSWORD`.


## Usage

1. **Run the Flask application:**

    ```bash
    python3 app.py
    ```

2. **Open your browser and go to `http://127.0.0.1:5000/` to access the email sending form.**

## Project Structure

```plaintext
flask_mail_project/
├── venv/
├── .env
├── app.py
├── config.py
├── README.md
└── requirement.txt


## Troubleshooting

SMTP Authentication Error
If you encounter an SMTPAuthenticationError, ensure:

Your email and password in .env are correct.
You have allowed less secure apps in your Google account settings.
If you have 2-Step Verification enabled, you are using an App Password.

