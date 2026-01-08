document.addEventListener("DOMContentLoaded", () => {
    const mainImg = document.querySelector("#main-development-image");
    if (!mainImg) return;

    const thumbs = document.querySelectorAll(".gallery-thumb");

    thumbs.forEach((btn) => {
        btn.addEventListener("click", () => {
            const fullUrl = btn.dataset.fullUrl;
            const alt = btn.dataset.alt || mainImg.alt;

            if (!fullUrl) return;

            mainImg.src = fullUrl;
            mainImg.alt = alt;
        });
    });
});