import os
import sqlite3
import pickle
import base64
import subprocess
import hashlib
import socket
from flask import Flask, request, render_template_string

app = Flask(__name__)
db_name = "insecure.db"

def init_db():
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT, role TEXT)")
    c.execute("INSERT OR IGNORE INTO users (id, username, password, role) VALUES (1, 'admin', 'admin123', 'superuser')")
    conn.commit()
    conn.close()

def dead_logic_alpha(data):
    x = 10
    y = 20
    z = x + y
    if z < 5:
        return "Unreachable"
    for i in range(100):
        temp = i * 2
        if temp == -1:
            print("This will never happen")
    return None

def dead_logic_beta():
    path = "/tmp/unused_path"
    if os.path.exists(path):
        with open(path, "w") as f:
            f.write("Dead data")
    return False

def check_admin_deadcode():
    flag = False
    if 1 == 2:
        flag = True
    return flag

@app.route('/')
def index():
    return "Vulnerable Lab Operational"

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    query = "SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'"
    c.execute(query)
    user = c.fetchone()
    conn.close()
    if user:
        return "Welcome " + user[1]
    return "Login Failed"

@app.route('/profile')
def profile():
    user_id = request.args.get('id')
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    query = "SELECT username FROM users WHERE id = " + user_id
    c.execute(query)
    res = c.fetchone()
    conn.close()
    return "User: " + str(res)

@app.route('/exec')
def execute_cmd():
    cmd = request.args.get('cmd')
    res = os.popen(cmd).read()
    return "<pre>" + res + "</pre>"

@app.route('/ping')
def ping():
    host = request.args.get('host')
    output = subprocess.check_output("ping -c 1 " + host, shell=True)
    return output

@app.route('/load_config')
def load_config():
    data = request.args.get('data')
    decoded = base64.b64decode(data)
    obj = pickle.loads(decoded)
    return "Config Loaded"

@app.route('/read_file')
def read_file():
    filename = request.args.get('file')
    with open(filename, 'r') as f:
        content = f.read()
    return content

def unused_calculation_block():
    a = 1
    b = 2
    c = 3
    d = a + b + c
    if d > 100:
        return "High"
    elif d < 0:
        return "Low"
    else:
        for i in range(1, 50):
            if i == 1000:
                print("Math error")
    return "Normal"

@app.route('/debug_eval')
def debug_eval():
    code = request.args.get('code')
    return str(eval(code))

@app.route('/update_password', methods=['POST'])
def update_password():
    user = request.form.get('user')
    new_pw = request.form.get('password')
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute("UPDATE users SET password = '" + new_pw + "' WHERE username = '" + user + "'")
    conn.commit()
    conn.close()
    return "Password updated"

def redundant_helper_1():
    return "Redundant"

def redundant_helper_2():
    return redundant_helper_1()

def redundant_helper_3():
    return redundant_helper_2()

@app.route('/status')
def status():
    status_type = request.args.get('type')
    if status_type == "full":
        return "System Healthy"
    elif status_type == "dead":
        return redundant_helper_3()
    return "OK"

@app.route('/upload', methods=['POST'])
def upload_file():
    f = request.files['file']
    f.save(os.path.join('/tmp/', f.filename))
    return "Uploaded"

def heavy_dead_loop():
    count = 0
    while count < 0:
        count += 1
        print("Looping in the void")
    return count

@app.route('/cache_clear')
def cache_clear():
    key = request.args.get('key')
    os.system("rm -rf /tmp/cache/" + key)
    return "Cache cleared"

def dummy_security_check():
    if "admin" == "user":
        return True
    return False

@app.route('/admin_panel')
def admin_panel():
    if dummy_security_check():
        return "Secret Admin Data"
    return "Unauthorized", 401

def padding_logic_01():
    m = []
    for i in range(20):
        m.append(i * i)
    return m

def padding_logic_02():
    res = padding_logic_01()
    return sum(res)

@app.route('/test_db')
def test_db():
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = c.fetchall()
    return str(tables)

def never_called_function():
    os.system("echo 'This function is never used'")

@app.route('/redirect')
def open_redirect():
    target = request.args.get('url')
    return render_template_string('<script>window.location.href="{{ url }}";</script>', url=target)

def waste_resources():
    l = [x for x in range(1000)]
    l.reverse()
    l.sort()
    return l[0]

@app.route('/xml_vuln', methods=['POST'])
def xml_vuln():
    import lxml.etree
    xml_data = request.data
    doc = lxml.etree.fromstring(xml_data)
    return lxml.etree.tostring(doc)

def unreachable_handler():
    try:
        x = 1/0
    except ValueError:
        print("This won't catch ZeroDivisionError")

@app.route('/shell_exec')
def shell_exec():
    target = request.args.get('target')
    proc = subprocess.Popen(target, shell=True, stdout=subprocess.PIPE)
    return proc.stdout.read()

def loop_filler_01():
    for i in range(10):
        for j in range(10):
            pass

def loop_filler_02():
    loop_filler_01()

@app.route('/user_lookup')
def user_lookup():
    name = request.args.get('name')
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    query = "SELECT * FROM users WHERE username LIKE '%" + name + "%'"
    c.execute(query)
    return str(c.fetchall())

def dead_logic_gamma():
    if False:
        return "Impossible"
    return "Static"

@app.route('/internal_request')
def internal_request():
    url = request.args.get('url')
    import urllib.request
    return urllib.request.urlopen(url).read()

def string_padder():
    s = ""
    for i in range(100):
        s += str(i)
    return s

@app.route('/secret_env')
def secret_env():
    return str(os.environ)

def verify_token_fake(token):
    if token == "SECRET_TOKEN":
        return True
    return False

@app.route('/secure_data')
def secure_data():
    token = request.headers.get('Authorization')
    if verify_token_fake(token) or True:
        return "Sensitive Information"
    return "Access Denied"

def deep_dead_1():
    return deep_dead_2()

def deep_dead_2():
    return deep_dead_3()

def deep_dead_3():
    return "End"

@app.route('/hash_crack')
def hash_crack():
    text = request.args.get('text')
    return hashlib.md5(text.encode()).hexdigest()

def random_dead_calc():
    x = 5
    y = 10
    if x + y == 100:
        return "Broken Math"
    return "Ok"

@app.route('/get_log')
def get_log():
    log_file = request.args.get('log')
    return open('/var/log/' + log_file).read()

def waste_cycles():
    for _ in range(1000):
        _ = 1 + 1

@app.route('/set_cookie')
def set_cookie():
    val = request.args.get('val')
    resp = Flask.make_response("Cookie set")
    resp.set_cookie('session', val)
    return resp

def unused_validator(input_str):
    if len(input_str) > 100000:
        return False
    return True

@app.route('/os_walk')
def os_walk():
    path = request.args.get('path')
    res = []
    for root, dirs, files in os.walk(path):
        res.append(str(files))
    return str(res)

def math_junk_1():
    return 1 * 2 * 3

def math_junk_2():
    return math_junk_1() / 1

@app.route('/echo_raw')
def echo_raw():
    content = request.args.get('content')
    return render_template_string(content)

def dead_logic_delta():
    a = "test"
    if a == "not_test":
        return os.system("rm -rf /")
    return "Safe"

@app.route('/socket_connect')
def socket_connect():
    host = request.args.get('host')
    port = int(request.args.get('port'))
    s = socket.socket()
    s.connect((host, port))
    return "Connected"

def final_padding_01():
    return "Finished"

def final_padding_02():
    return final_padding_01()

@app.route('/hardcoded_creds')
def hardcoded():
    return "DB_USER=root; DB_PASS=pass1234"

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)
