document.addEventListener("DOMContentLoaded", () => {
    submitSearchOnClear(".search-form", "#city-q");
    autoSubmitOnSelectChange();

    function submitSearchOnClear(formSelector) {
        const forms = document.querySelectorAll(formSelector);

        forms.forEach((form) => {
            const input = form.querySelector("input[type='search']");
            if (!input) return;

            input.addEventListener("search", () => {
                if (input.value.trim() === "") {
                    form.submit();
                }
            });
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