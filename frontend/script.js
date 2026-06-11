function sendMessage() {
  let userInput = document.getElementById("msg").value;

  if (!userInput) return;

  const chatBox = document.getElementById("chat");

  // show user message
  chatBox.innerHTML += `<p class="user"><b>You:</b> ${userInput}</p>`;

  fetch("http://127.0.0.1:5000/chat", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ message: userInput })
  })
  .then(res => res.json())
  .then(data => {
    chatBox.innerHTML += `<p class="bot"><b>Bot:</b> ${data.reply}</p>`;
  })
  .catch(err => {
    chatBox.innerHTML += `<p class="bot">Error connecting to backend</p>`;
    console.log(err);
  });

  document.getElementById("msg").value = "";
}