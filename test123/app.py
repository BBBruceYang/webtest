import os
# We'll render HTML templates and access data sent by POST
# using the request object from flask. Redirect and url_for
# will be used to redirect the user once the upload is done
# and send_from_directory will help us to send/show on the
# browser the file that the user just uploaded
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from werkzeug import secure_filename
from flask_bootstrap import Bootstrap
# Initialize the Flask application
app = Flask(__name__)
#存放上傳資料的資料夾
UPLOAD_FOLDER = 'D:\\flask\\test123'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# 設定允許被上傳的檔案格式
app.config['ALLOWED_EXTENSIONS'] = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
# For a given file, return whether it's an allowed type or not
def allowed_file(filename):
  return '.' in filename and \
      filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']
# This route will show a form to perform an AJAX request
# jQuery is loaded to execute the request and update the
# value of the operation
@app.route('/')
def index():
  return render_template('index.html')

# Route that will process the file upload
@app.route('/upload', methods=['POST'])
def upload():
  # 取得上傳資料的名稱
  uploaded_files = request.files.getlist("file[]")
  filenames = []
  for file in uploaded_files:
    # 檢查上傳的資料格是是否符合
    if file and allowed_file(file.filename):
      # "SECURE_FILENAME"Make the filename safe, remove unsupported chars
      filename = secure_filename(file.filename)
      # 將上傳的檔案從"暫存資料夾"移到我們設定的資料夾
      #Move the file form the temporal folder to the upload folder we setup
      file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
      # 將這次上傳的資料放進料表中，方便等下查看Save the filename into a list, we'll use it later
      filenames.append(filename)
      print ("讀文件之前")
      #測試開啟
      #with open(os.path.join(app.config['UPLOAD_FOLDER'],filename),'r',  encoding = 'utf-8') as f: file_content  = f.read()
      print ("讀文件之後")
      #將頁面導向"uploaded_file"頁面
      # Redirect the user to the uploaded_file route, whichwill basicaly show on the browser the uploaded file
  # Load an html page with a link to each uploaded file
  return render_template('upload.html', filenames=filenames)
# This route is expecting a parameter containing the name
# of a file. Then it will locate that file on the upload
# directory and show it on the browser, so if the user uploads
# an image, that image is going to be show after the upload
@app.route('/uploads/<filename>')
def uploaded_file(filename):
  print (filename)
  #return send_from_directory(app.config['UPLOAD_FOLDER'],
  #              filename)
  with  open(os.path.join(app.config['UPLOAD_FOLDER'],filename)) as f:
      file_content = f.read()
  return render_template('result.html', file_content = file_content)

@app.route('/getuser')
def  getuser():
        for file in uploaded_files:

            # You should use os.path.join here too.
            with  open(os.path.join(app.config['UPLOAD_FOLDER'],filename)) as f:
                  file_content = f.read()
        return file_content

if __name__ == '__main__':
  app.run(
    host="127.0.0.1",
    port=int("5000"),
    debug=True
  )