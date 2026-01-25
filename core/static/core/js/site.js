document.addEventListener("DOMContentLoaded", () => {
    function submitSearchOnClear(formSelector, inputSelector) {
        const form = document.querySelector(formSelector);
        const input = document.querySelector(inputSelector);

        if (!form || !input) return;

        input.addEventListener("search", () => {
            // submit form when the user clicks enter or x button
            if (input.value.trim() === "") {
                form.submit();
            }
        });
    }
    submitSearchOnClear(".search-form", "#city-q")
})