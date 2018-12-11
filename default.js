const {browserWindow,electron} = require('electron');
const url = require('url');
const path = require('path');
const app = require('electron');
const cp= require('child_process');

let def_win

def_win = new browserWindow({height:900,width:1440});
function createWindow(){
win.loadURL({
	path:path.join(__dirname,'main.html');
	protocol:'files',
	slashes:true
})
};

app.on('ready',createWindow);

cp.exec("python index.py",(stdout,stderr)==>{
	if(stdout:'Houseparty'){
		cp.exec("electron main.js");
	}
} 