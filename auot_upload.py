#-*- coding:utf-8 -*-
from flask import Flask
from flask import url_for 
from flask import request
from flask import make_response
from flask import render_template
from flask_json import FlaskJSON, JsonError, json_response, as_json, jsonify
import time
import json
import httplib2

import sys
reload(sys)
sys.setdefaultencoding('utf8')

app = Flask(__name__)

config_file = "./config"

modules = [
            {"id":1, "name":"爱奇艺应用商店", "icon":"/static/img/aiqiyi.png"},
            {"id":2, "name":"安贝市场", "icon":"/static/img/anbei.png"},
            {"id":3, "name":"安卓园", "icon":"/static/img/anzhuo.png"},
            {"id":4, "name":"安粉网", "icon":"/static/img/anfen.png"},
            {"id":5, "name":"锤子应用商城", "icon":"/static/img/chuizi.png"},
            {"id":6, "name":"华为开发者联盟", "icon":"/static/img/huawei.png"},
            {"id":7, "name":"联通沃商店", "icon":"/static/img/liantong.png"},
            {"id":8, "name":"木蚂蚁", "icon":"/static/img/mumayi.png"},
            {"id":9, "name":"移动应用商场", "icon":"/static/img/yidong.png"},
            {"id":10, "name":"应用贝", "icon":"/static/img/yingyongbei.png"},
            {"id":11, "name":"oppo", "icon":"/static/img/oppo.png", "url":"http://open.oppomobile.com/newuser/authdev", "method":"GET", "func":"upload_oppo"}
        ]



def upload_aiyiqi(account, password, appId):
    print "aiyiqi"
    pass

def upload_anbei(account, password, appId):
    pass

def upload_anzhuoyuan(account, password, appId):
    pass

def upload_anfenwang(account, password, appId):
    pass

def upload_chuizi(account, password, appId):
    pass

def upload_huawei(account, password, appId):
    pass

def upload_liantong(account, password, appId):
    pass

def upload_mumayi(account, password, appId):
    pass

def upload_yidong(account, password, appId):
    pass

def upload_yingyongbei(account, password, appId):
    pass

def upload_oppo(account, password, appId):
    print "oppo"
    pass

funcMap = {
            "id_1":  upload_aiyiqi,
            "id_2":  upload_anbei,
            "id_3":  upload_anzhuoyuan,
            "id_4":  upload_anfenwang,
            "id_5":  upload_chuizi,
            "id_6":  upload_huawei,
            "id_7":  upload_liantong,
            "id_8":  upload_mumayi,
            "id_9":  upload_yidong,
            "id_10":  upload_yingyongbei,
            "id_11": upload_oppo,
          }

def func_dispatch(account, password, appId):
    funcMap_key = "id_" + str(appId)
    funcMap[funcMap_key](account, password, appId)

@app.route('/auto_upload', methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        return render_template('login.html',  serverIp=serverIp, serverPort=serverPort)
    
    if request.method == "POST":
        time.sleep(1)
        json_data = request.get_json()
        print json_data

        if (json_data['method'] == 'login'):
            if account == json_data['account'] and password == json_data['password']:
                return jsonify(status=1, html=render_template('auto_upload.html', modules=modules))
            else:
                return jsonify(status=-1)
        elif (json_data['method'] == 'upload'):
            func_dispatch(json_data['account'], json_data['password'], json_data['appId']);
            return jsonify(status=-1)
        else:
            return jsonify(status=-1, html=render_template('auto_upload.html', modules=modules))


if __name__ == "__main__":
    app.debug = True

    f = file(config_file);
    config_json = json.load(f)
    f.close();
    account  = config_json["account"]
    password = config_json["password"]
    serverIp = config_json["host"]
    serverPort = config_json["port"]

    app.run(host=serverIp)
