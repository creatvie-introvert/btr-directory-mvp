document.addEventListener("DOMContentLoaded", () => {
    submitSearchOnClear(".search-form", "#city-q");
    autoSubmitOnSelectChange();

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

    function autoSubmitOnSelectChange(selector = ".filter-select") {
        const filterSelect = document.querySelectorAll(selector);

        filterSelect.forEach((select) => {
            select.addEventListener("change", () => {
                const form = select.closest("form");
                if (form) {
                    form.submit();
                }
            });
        });
    }
});