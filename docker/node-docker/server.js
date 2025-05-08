'use strict'

var http = require('http');
const app = express();

const hostname = '0.0.0.0';
const port = 8000;

app.get('/', (req, res) => {
	res.send('Hello World\n');
})

app.listen(port, hostname);
console.log(`Server running at http://${hostname}:${port}/`);
