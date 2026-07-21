// Delete confirmation
function confirmDelete(id) {
    if (confirm("Are you sure you want to delete this todo?")) {
        window.location.href = "/delete/" + id;
    }
}

// Validate Add Form
function validateAddForm() {
    const name = document.getElementById("name");
    const work = document.getElementById("work");

    if (name.value.trim() === "" || work.value.trim() === "") {
        alert("Please fill in all fields.");
        return false;
    }

    return true;
}

// Validate Edit Form
function validateEditForm() {
    const name = document.getElementById("edit_name");
    const work = document.getElementById("edit_work");

    if (name.value.trim() === "" || work.value.trim() === "") {
        alert("Please fill in all fields.");
        return false;
    }

    return true;
}

// Highlight the search box when page loads
window.onload = function () {
    const search = document.querySelector("input[name='id']");
    if (search) {
        search.focus();
    }
};
