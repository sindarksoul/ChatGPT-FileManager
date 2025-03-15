const { app, BrowserWindow, session } = require('electron');

function createWindow() {
    const win = new BrowserWindow({
        width: 1000,
        height: 700,
        webPreferences: {
            nodeIntegration: true,
            webSecurity: false,  // 👈 Allow local API requests
            allowRunningInsecureContent: true  // 👈 Allow HTTP
        }
    });

    win.loadFile('index.html');

    // Fix CORS issue
    session.defaultSession.webRequest.onHeadersReceived((details, callback) => {
        callback({
            responseHeaders: {
                ...details.responseHeaders,
                "Access-Control-Allow-Origin": ["*"]
            }
        });
    });
}

app.whenReady().then(createWindow);

app.on('window-all-closed', () => {
    if (process.platform !== 'darwin') {
        app.quit();
    }
});
