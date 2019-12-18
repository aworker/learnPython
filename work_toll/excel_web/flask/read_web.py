from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import xlrd
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def root():
    if request.method == 'POST':
        #将网络传输的文件存储起来
        f = request.files['file']
        basepath = os.path.dirname(__file__)  # 当前文件所在路径
        file_name = f.filename
        # file_name = secure_filename(f.filename)
        upload_path = os.path.join(basepath, 'static/upload', file_name)
        save = f.save(upload_path)

        #将存储的文件打开
        data = xlrd.open_workbook('./西部大区核销房源明细表.xlsx')

        return redirect(url_for('upload'))

    return render_template('upload.html')


if __name__ == '__main__':
    app.run(debug=True, port=6699)

