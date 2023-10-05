from flask import Flask, render_template, request, redirect, url_for, flash
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def main():
    return render_template('website.html')

@app.route('/Who-we-are')
def Who_we_are():
    return render_template('Who we are.html')

@app.route('/Case-study')
def Case_study():
    return render_template('Case study.html')


@app.route('/Contact-us', methods=['GET', 'POST'])
def Contact_us():
    if request.method == 'POST':
        recipient_email = 'kangyecn@gmail.com'  # Replace with your recipient email
        sender_email = 'kangyecncn@gmail.com'  # Replace with your Gmail email
        sender_password = 'xqudhrnvtfnrrbmp'  # Replace with your Gmail password

        subject = request.form['subject']
        sender_name = request.form['name']
        cc_email = request.form['cc_email']
        company_name = request.form['company_name']
        message = request.form['message']

        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Cc'] = cc_email
        msg['Subject'] = subject

        body = f"Name: {sender_name}\nEmail: {cc_email}\nCompany: {company_name}\n\n{message}"
        msg.attach(MIMEText(body, 'plain'))

        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, [recipient_email, cc_email], msg.as_string())
            server.quit()
            flash('Message sent successfully!', 'success')
        except Exception as e:
            flash(f'Error: {e}', 'error')

        return redirect(url_for('Contact_us'))

    return render_template('Contact Us.html')

if __name__ == '__main__':
    app.run(debug=True)
