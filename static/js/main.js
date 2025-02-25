document.addEventListener("DOMContentLoaded", () => {
    const statusMessage = document.getElementById("status-message");

    if (statusMessage) {
        setTimeout(() => {
            statusMessage.innerHTML = ""; // Clears messages after 5 seconds
        }, 5000);
    }
});