from flask import Flask, render_template, request, redirect

import speech_recognition as sr

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
# here we are applying the post request on
# our own html page i.e we are getting the data from our system and posting it on choose file
# option on our home page
def index():
    transcript = ""
    if request.method == "POST":
        print("FORM DATA RECEIVED")

        if "file" not in request.files:
            return redirect(request.url)
            # if someone put blank file in choose file button then
            # he will be redirected to home page

        file = request.files["file"]
        if file.filename == "":
            return redirect(request.url)
            # if someone choose transcribe button without choosing
            # file in choose file button then also he will be redirected to home page

        if file:
            recognizer = sr.Recognizer()
            audiophile = sr.AudioFile(file)
            with audiophile as source:
                data = recognizer.record(source)
                # In above we have done two steps
                # 1.we have taken the file user have uploaded created an audiophile object that our speech recognizer
                # module can understand
                # 2.and then we are opening up this audiophile and reading it in through the recognizer.

                # once we upload file and our speech recognition module understand it then we have to convert
                # it into text
                # for this we use google cloud to turn our audio file into text
            transcript = recognizer.recognize_google(data, key=None)

    return render_template('index.html', transcript=transcript)


if __name__ == '__main__':
    app.run(debug=True, threaded=True)
    # debug will allow us to command this file,
    # threaded is used to deal with number of files so that computer process multiple requests
    # at same time
