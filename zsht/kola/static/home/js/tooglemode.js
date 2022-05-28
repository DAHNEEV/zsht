const toggleBtn = document.getElementById("toggle-btn");
const theme = document.body;
let darkMode = localStorage.getItem("dark-mode");

const enableDarkMode = () => {
    theme.classList.add("bg-light", "text-dark");
    theme.classList.remove("bg-dark", "text-white");
    toggleBtn.innerText = "☀️";
    localStorage.setItem("dark-mode", "enabled");
};

const disableDarkMode = () => {
    theme.classList.add("bg-dark", "text-white");
    theme.classList.remove("bg-light", "text-dark");
    toggleBtn.innerText = "🌙";
    localStorage.setItem("dark-mode", "disabled");
};

if (darkMode === "enabled") {
    enableDarkMode();
}
else {
    disableDarkMode();
}

toggleBtn.addEventListener("click", (e) => {
    darkMode = localStorage.getItem("dark-mode");
    if (darkMode === "disabled") {
        enableDarkMode();
    } else {
        disableDarkMode();
    }
});