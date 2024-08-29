const WebSocket = require('ws');
const dotenv = require("dotenv")
dotenv.config()

const server = new WebSocket.Server({ port: process.env.PORT || 3000 });

let rooms = {};

server.on('connection', (socket) => {
    socket.on('message', (message) => {
        const data = JSON.parse(message);

        switch (data.type) {
            case 'host':
                if (!rooms[data.room]) {
                    rooms[data.room] = [];
                }
                rooms[data.room].push(socket);
                socket.send(JSON.stringify({ type: 'notification', message: `Sala ${data.room} criada.` }));
                break;
            case 'join':
                if (rooms[data.room]) {
                    rooms[data.room].push(socket);
                    rooms[data.room].forEach(client => {
                        if (client !== socket && client.readyState === WebSocket.OPEN) {
                            client.send(JSON.stringify({ type: 'notification', message: `Um novo usuário entrou na sala ${data.room}.` }));
                        }
                    });
                }
                break;
            case 'message':
                if (rooms[data.room]) {
                    rooms[data.room].forEach(client => {
                        if (client.readyState === WebSocket.OPEN) {
                            client.send(JSON.stringify({ type: 'message', message: data.message }));
                        }
                    });
                }
                break;
            case 'leave':
                if (rooms[data.room]) {
                    rooms[data.room] = rooms[data.room].filter(client => client !== socket);
                    socket.send(JSON.stringify({ type: 'notification', message: `Você saiu da sala ${data.room}.` }));
                    if (rooms[data.room].length === 0) {
                        delete rooms[data.room];
                    }
                }
                break;
        }
    });

    socket.on('close', () => {
        for (const room in rooms) {
            rooms[room] = rooms[room].filter(client => client !== socket);
            if (rooms[room].length === 0) {
                delete rooms[room];
            }
        }
    });
});

console.log('Servidor WebSocket rodando na porta 3000');