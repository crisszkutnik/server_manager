let socket = io();
socket.on("connect", () => {
    console.log("Connected")
});

socket.on("message", (message) => {
    alert(message);
})