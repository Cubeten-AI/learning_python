const apiKey = "1PHT6gpUiEo5zRRjDRkrsINsR20HXoN38AvVoHvA"; // Replace with your API Ninjas key

const wordInput = document.getElementById("wordInput");
const searchBtn = document.getElementById("searchBtn");
const resultDiv = document.getElementById("result");
const errorMsg = document.getElementById("error");
const loader = document.getElementById("loader");
const audioBtn = document.getElementById("audioBtn");

let currentAudio = null;

async function searchWord() {
    const word = wordInput.value.trim();
    
    if (!word) {
        showError("Please enter a word");
        return;
    }

    // Reset UI
    errorMsg.classList.add("hidden");
    resultDiv.classList.add("hidden");
    loader.classList.remove("hidden");

    const url = `https://api.api-ninjas.com/v1/dictionary?word=${word}`;

    try {
        const res = await fetch(url, {
            headers: { 'X-Api-Key': apiKey }
        });

        if (!res.ok) throw new Error("API request failed");
        
        const data = await res.json();

        if (!data.definition) {
            throw new Error("Word not found");
        }

        displayResult(word, data);
        
    } catch (err) {
        showError(err.message);
    } finally {
        loader.classList.add("hidden");
    }
}

function displayResult(word, data) {
    document.getElementById("word").innerText = word;
    document.getElementById("definition").innerText = data.definition;
    
    // API Ninjas doesn't return phonetics or examples, so we handle that
    document.getElementById("phonetic").innerText = "";
    document.getElementById("example").innerText = "Not available with this API";
    audioBtn.classList.add("hidden");

    resultDiv.classList.remove("hidden");
}

function showError(message) {
    errorMsg.innerText = message;
    errorMsg.classList.remove("hidden");
}

searchBtn.addEventListener("click", searchWord);
wordInput.addEventListener("keypress", (e) => {
    if (e.key === "Enter") searchWord();
});