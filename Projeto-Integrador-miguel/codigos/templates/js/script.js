//const socket = new WebSocket('wss://testeweb-sooty.vercel.app');
const socket = new WebSocket('wss://testeweb-y7ke.onrender.com');
let currentRoom = null;

socket.onopen = () => {
    console.log('Conectado ao servidor WebSocket');
};

socket.onmessage = (event) => {
    const data = JSON.parse(event.data);

    if (data.type === 'message') {
        displayMessage(data.message);
    } else if (data.type === 'notification') {
        displayMessage(`Sistema: ${data.message}`);
    }
};

document.getElementById('host-room').onclick = () => {
    const roomName = document.getElementById('room-name').value;
    if (roomName) {
        socket.send(JSON.stringify({ type: 'host', room: roomName }));
        enterRoom(roomName);
    }
};

document.getElementById('join-room').onclick = () => {
    const roomName = document.getElementById('room-name').value;
    if (roomName) {
        socket.send(JSON.stringify({ type: 'join', room: roomName }));
        enterRoom(roomName);
    }
};

document.getElementById('send-message').onclick = () => {
    const message = document.getElementById('message-input').value;
    if (message && currentRoom) {
        socket.send(JSON.stringify({ type: 'message', room: currentRoom, message: message }));
        displayMessage(`Você: ${message}`);
        document.getElementById('message-input').value = '';
    }
};

document.getElementById('leave-room').onclick = () => {
    if (currentRoom) {
        socket.send(JSON.stringify({ type: 'leave', room: currentRoom }));
        exitRoom();
    }
};

function enterRoom(room) {
    currentRoom = room;
    document.getElementById('room-selection').classList.add('hidden');
    document.getElementById('chat-container').classList.remove('hidden');
    displayMessage(`Você entrou na sala: ${room}`);
}

function exitRoom() {
    currentRoom = null;
    document.getElementById('room-selection').classList.remove('hidden');
    document.getElementById('chat-container').classList.add('hidden');
    document.getElementById('messages').innerHTML = '';
}

function displayMessage(message) {
    const messageContainer = document.getElementById('messages');
    const messageElement = document.createElement('div');
    messageElement.textContent = message;
    messageContainer.appendChild(messageElement);
    messageContainer.scrollTop = messageContainer.scrollHeight;
}