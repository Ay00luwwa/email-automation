import yagmail

yag = yagmail.SMTP('ijidakinroayooluwa@gmail.com')

html_content = """
<html>
    <body>
        <h1 style="color: blue;">Hello there!</h1>
        <p style="font-size: 20px;">This is an email sent with <strong>yagmail</strong>.</p>
        <button>auto mail</button>
    </body>
</html>
"""

yag.send(
    to='havamon154@vikinoko.com',
    subject='automated mail',
    contents=html_content
)

#you can also send mails without using html






