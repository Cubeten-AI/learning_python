// Confirm before deleting a blog
function confirmDelete() {
    return confirm("Are you sure you want to delete this blog?");
}

// Auto-hide alerts after 5 seconds
setTimeout(() => {
    const alerts = document.querySelectorAll(".alert");

    alerts.forEach(alert => {
        alert.style.transition = "0.5s";
        alert.style.opacity = "0";

        setTimeout(() => {
            alert.remove();
        }, 500);

    });

}, 5000);

// Focus search box
const searchBox = document.querySelector("input[name='q']");

if(searchBox){
    searchBox.focus();
}
