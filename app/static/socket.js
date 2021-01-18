let socket = io();
let serverStatus = closed;


socket.on("sv_status", ({ status }) => {
    let open = document.querySelector("#open-server");
    let closed = document.querySelector("#closed-server");

    console.log(status);

    if(status) {
        open.style.display = "flex";
        closed.style.display = "none";
    } else {
        open.style.display = "none";
        closed.style.display = "flex";
    }
})

/*

    Closed server config

*/

const activateServer = () => {
    socket.emit("open_request");
}
document.querySelector("button#open-button").addEventListener("click", activateServer);

/*

    Open server config

*/

let msg_dialog = document.querySelector("#msg-dialog");
let send_dialog = document.querySelector("#send-dialog");
let cmd = document.querySelector("#command");

socket.on("connect", () => {
    console.log("Connected")
});

socket.on("mc_console_msg", ({ msg }) => {
    msg_dialog.innerHTML += `<p>${ msg }</p>`;
})

send_dialog.addEventListener("submit", (e) => {
    e.preventDefault();
    let parsed_cmd = cmd.value + "\n";
    cmd.value = "";
    socket.emit("client_send_command", parsed_cmd);
})