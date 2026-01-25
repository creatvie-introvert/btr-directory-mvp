document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector(".search-form");
    const input = document.querySelector("#city-q");

    if (!form || !input) return;

    input.addEventListener("search", function () {
        // submit form when the user clicks enter or x button
        if (input.value.trim() === "") {
            form.submit();
        }
    });
})