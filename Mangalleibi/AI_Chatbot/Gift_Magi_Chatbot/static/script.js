function askQuestion() {

    let input = document.getElementById("question");
    let question = input.value.trim();

    if (question === "") {
        return;
    }

    let chatBox = document.getElementById("chat-box");

    // Show user message
    chatBox.innerHTML += `
        <div class="message user">
            <div class="bubble">
                ${question}
            </div>

            <div class="avatar">
                👤
            </div>
        </div>
    `;

    input.value = "";

    // Show Thinking
    chatBox.innerHTML += `
        <div class="message assistant" id="thinking">
            <div class="avatar">
                🤖
            </div>

            <div class="bubble">
                Thinking... 🤔
            </div>
        </div>
    `;

    chatBox.scrollTop = chatBox.scrollHeight;

    // Send to Flask
    fetch("/ask", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            question: question
        })

    })

    .then(response => {

        if (!response.ok) {
            throw new Error("Server error: " + response.status);
        }

        return response.json();

    })

    .then(data => {

        // Remove Thinking
        let thinking = document.getElementById("thinking");

        if (thinking) {
            thinking.remove();
        }

        // Create AI message
        chatBox.innerHTML += `
            <div class="message assistant">

                <div class="avatar">
                    🤖
                </div>

                <div class="bubble">
                    ${data.answer.replace(/\n/g, "<br>")}
                </div>

            </div>
        `;

        chatBox.scrollTop = chatBox.scrollHeight;

    })

    .catch(error => {

        console.log(error);

        let thinking = document.getElementById("thinking");

        if (thinking) {
            thinking.remove();
        }

        chatBox.innerHTML += `
            <div class="message assistant">

                <div class="avatar">
                    🤖
                </div>

                <div class="bubble">
                    Sorry, something went wrong. 😔
                </div>

            </div>
        `;

    });
}


// Press Enter to send

document.getElementById("question").addEventListener("keydown", function(event) {

    if (event.key === "Enter") {

        event.preventDefault();

        askQuestion();

    }

});


// Clear Chat

function clearChat() {

    document.getElementById("chat-box").innerHTML = `

        <div class="message assistant">

            <div class="avatar">
                🤖
            </div>

            <div class="bubble">

                Hello! 👋 I'm your Gift of the Magi
                AI storyteller.

                <br><br>

                Ask me anything about the story!

            </div>

        </div>

    `;

}