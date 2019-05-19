from flask import Flask, render_template, request, send_file, redirect
from werkzeug.utils import secure_filename
from temp.errCheck import correctName
from temp.transformer import mover, baseDel
from temp.main import preMain
from temp.processWeb import hasher
import os
import asyncio
loop = asyncio.get_event_loop()

tempPath = str(os.getcwd())
tempPath += "\\..\\child"
app = Flask(__name__, static_folder=tempPath)


from pyppeteer import launch


async def main1_():

    import os
    myStr = str(os.getcwd())
    urlPath = 'file:///' + myStr + '\\..\\resultHTML\\result.html'

    browser = await launch(
        handleSIGINT=False,
        handleSIGTERM=False,
        handleSIGHUP=False
    )
    page = await browser.newPage()
    await page.goto(urlPath)
    await page.screenshot({'path': '..\\child\\resultPNG.png'})
    await page.setCacheEnabled(enabled=False)
    await browser.close()


async def main2_():
    import os
    myStr = str(os.getcwd())
    urlPath = 'file:///' + myStr + '\\..\\resultHTML\\result.html'

    browser = await launch(
        handleSIGINT=False,
        handleSIGTERM=False,
        handleSIGHUP=False
    )
    page = await browser.newPage()
    await page.goto(urlPath)
    await page.pdf({'path': '..\\child\\resultPDF.pdf'})
    await page.setCacheEnabled(enabled=False)
    await browser.close()


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route("/submit_form", methods=["POST"])
def submit():
    baseDel("..\\child\\resultPNG.png")
    baseDel("..\\child\\resultPDF.pdf")
    baseDel("..\\resultHTML\\result.html")
    if 'file' not in request.files:
        return render_template("err.html")
    file = request.files['file']
    if file.filename == '':
        return render_template("err.html")
    if file and correctName(file.filename):
        # if everything is good
        file = request.files["file"]
        filename = secure_filename(file.filename)
        file.save(os.path.join("download", filename))
        form = request.form.to_dict()
        mover("download\\" + file.filename, "..\\csv\\normal.csv")
        preMain(hasher(form))

        loop.run_until_complete(main1_())
        return render_template("picture.html")
    return render_template("err.html")


@app.route("/hello")
def hello():
    return redirect("/download/resultPDF.pdf")


@app.route("/download/<filename>")
def download(filename):
    loop.run_until_complete(main2_())
    return send_file("../child/" + filename, as_attachment=True)


@app.after_request
def set_response_headers(response):
    response.headers['Cache-Control'] = 'no-store'
    return response


app.run(port=5000, debug=True)
