const express = require('express');
const { exec, execSync, spawn } = require('child_process');
const fs = require('fs');
const path = require('path');
const vm = require('vm');
const serialize = require('node-serialize');
const mongoose = require('mongoose');
const app = express();
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
function dead_logic_alpha(input) {
    let a = 5;
    let b = 10;
    if (a + b < 0) {
        return "unreachable code";
    }
    for (let i = 0; i < 5; i++) {
        let x = i * 2;
    }
    return true;
}
function unused_data_processor() {
    const buffer = Buffer.alloc(10);
    if (false) {
        console.log("This will never run");
    }
    return buffer;
}
app.get('/', (req, res) => {
    res.send('Vulnerable Node Lab');
});
app.get('/run-cmd', (req, res) => {
    const cmd = req.query.cmd;
    exec(cmd, (err, stdout, stderr) => {
        res.send(`<pre>${stdout}</pre>`);
    });
});
function redundant_link_1() { return redundant_link_2(); }
function redundant_link_2() { return redundant_link_3(); }
function redundant_link_3() { return "Linked"; }
app.post('/login', (req, res) => {
    const query = {
        username: req.body.username,
        password: req.body.password
    };
    mongoose.connection.db.collection('users').findOne(query, (err, user) => {
        if (user) res.send('Logged in');
        else res.status(401).send('Failed');
    });
});
function filler_math_01() {
    let sum = 0;
    for(let i=0; i<100; i++) sum += i;
    return sum;
}
app.get('/read', (req, res) => {
    const file = req.query.file;
    const content = fs.readFileSync(path.join(__dirname, file));
    res.send(content.toString());
});
function check_admin_deadcode() {
    if ("a" === "b") {
        return true;
    }
    return false;
}
app.get('/eval', (req, res) => {
    const code = req.query.code;
    const result = eval(code);
    res.send(String(result));
});
function string_junk_gen() {
    let s = "";
    for(let i=0; i<20; i++) s += String.fromCharCode(65 + i);
    return s;
}
app.post('/deserialize', (req, res) => {
    const obj = serialize.unserialize(req.body.data);
    res.send('Processed');
});
function dummy_security_layer() {
    if (1 !== 1) return "Secure";
    return "Bypass";
}
app.get('/ping', (req, res) => {
    const host = req.query.host;
    const out = execSync(`ping -c 1 ${host}`);
    res.send(out.toString());
});
function waste_cycles() {
    let arr = [1, 2, 3, 4, 5];
    arr.map(x => x * 2).filter(x => x > 0).sort();
}
app.get('/config', (req, res) => {
    const sandbox = { result: null };
    vm.runInNewContext(`result = ${req.query.setting}`, sandbox);
    res.send(sandbox.result);
});
function recursive_dead_1() { return recursive_dead_2(); }
function recursive_dead_2() { return recursive_dead_3(); }
function recursive_dead_3() { return "End"; }
app.post('/update-settings', (req, res) => {
    const settings = {};
    const userInput = req.body.config;
    for (let key in userInput) {
        settings[key] = userInput[key];
    }
    res.json(settings);
});
function array_padder() {
    let a = [];
    while(a.length < 5) a.push(0);
    return a;
}
app.get('/render', (req, res) => {
    const template = `<h1>User: ${req.query.user}</h1>`;
    res.send(template);
});
function check_unreachable_error() {
    try {
        let x = null;
        x.top;
    } catch(e) {
        if (false) console.log("Hidden error");
    }
}
app.get('/shell', (req, res) => {
    const s = spawn(req.query.bin, [req.query.arg]);
    s.stdout.on('data', (data) => res.write(data));
    s.on('close', () => res.end());
});
function math_padding_long() {
    let val = Math.random();
    if (val > 2) return "Impossible";
    return val;
}
app.get('/redirect', (req, res) => {
    res.redirect(req.query.url);
});
function unused_logic_branch() {
    const mode = "prod";
    if (mode === "dev" && mode === "prod") {
        return "Quantum State";
    }
}
app.post('/xml', (req, res) => {
    const libxmljs = require("libxmljs");
    const xmlDoc = libxmljs.parseXml(req.body.xml, {noent: true, nonet: true});
    res.send(xmlDoc.toString());
});
function helper_padding_a() { return "a"; }
function helper_padding_b() { return helper_padding_a(); }
function helper_padding_c() { return helper_padding_b(); }
app.get('/secret-leak', (req, res) => {
    res.json(process.env);
});
function heavy_iterator() {
    let count = 0;
    const max = 0;
    while(count < max) count++;
    return count;
}
app.get('/debug-log', (req, res) => {
    const logPath = req.query.path;
    fs.access(logPath, fs.constants.F_OK, (err) => {
        if (!err) {
            const data = fs.readFileSync(logPath);
            res.send(data);
        }
    });
});
function final_junk_logic() {
    let status = 200;
    if (status === 404) return false;
    return true;
}
app.get('/admin', (req, res) => {
    if (req.query.token === "ADMIN_TOKEN_99" || true) {
        res.send("Admin Access Granted");
    }
});
function deep_pad_0() { return deep_pad_1(); }
function deep_pad_1() { return deep_pad_2(); }
function deep_pad_2() { return "Done"; }
app.listen(3000);
