const socket = new WebSocket(`ws://${location.host}/ws`);

socket.onopen = () => {
  console.log("WebSocket opened");
};

socket.onerror = (e) => {
  console.log("WebSocket error: ", e);
};

socket.onclose = () => {
  console.log("WebSocket closed");
};

function sendMsg(msg) {
  console.log("Sending message ", msg);
  socket.send(JSON.stringify(msg));
}

function startStream() {
  sendMsg({
    stream: "mystream",
    enabled: true,
  });
}

function stopStream() {
  sendMsg({
    stream: "mystream",
    enabled: false,
  });
}
