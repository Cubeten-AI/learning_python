const API_KEY = 'kAQjZzXL7LEFOLyKYAylc8YD2H6TRvUiUtOc4iaj'; // Get free key from api-ninjas.com

const categorySelect = document.getElementById('categorySelect');
const searchBtn = document.getElementById('searchBtn');
const loader = document.getElementById('loader');
const error = document.getElementById('error');
const result = document.getElementById('result');
const hobbyCount = document.getElementById('hobbyCount');
const hobbiesGrid = document.getElementById('hobbiesGrid');

async function findHobbies() {
    if (API_KEY === '') {
        showError("Please add your API key in script.js");
        return;
    }

    const category = categorySelect.value;
    
    loader.classList.add('active');
    error.classList.remove('active');
    result.classList.remove('active');

    try {
        let url = 'https://api.api-ninjas.com/v1/hobbies';
        if (category) {
            url += `?category=${encodeURIComponent(category)}`;
        }

        const res = await fetch(url, {
            headers: { 'X-Api-Key': API_KEY }
        });

        if (!res.ok) {
            throw new Error(`Error: ${res.status}`);
        }

        const data = await res.json();
        console.log(data)
        console.log(Array.isArray(data));

        if (!data || data.length === 0) {
            throw new Error("No hobbies found for this category");
        }
        const hobbies = Array.isArray(data) ? data : [data];
        displayHobbies(hobbies, category);

    } catch (err) {
        showError(err.message || "Failed to fetch hobbies");
    } finally {
        loader.classList.remove('active');
    }
}

function displayHobbies(hobbies, category) {
    const categoryName = category || "All Categories";

    hobbyCount.textContent = `Found ${hobbies.length} hobby in ${categoryName}`;

    hobbiesGrid.innerHTML = "";

    hobbies.forEach((item) => {
        const card = document.createElement("div");
        card.className = "hobby-card";

        card.innerHTML = `
            <h3>${item.hobby}</h3>
            <p>Category: ${item.category}</p>
            <a href="${item.link}" target="_blank">Learn More</a>
        `;

        hobbiesGrid.appendChild(card);
    });

    result.classList.add("active");
}

function showError(msg) {
    error.textContent = msg;
    error.classList.add('active');
}

// Event listeners
searchBtn.addEventListener('click', findHobbies);

// Load all hobbies on page load
window.addEventListener('load', findHobbies);
