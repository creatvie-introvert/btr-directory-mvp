/**
 * Devlopment detail page interactions.
 * 
 * Swaps the main image when a gallery thumbnail is clicked. 
 */
document.addEventListener("DOMContentLoaded", () => {
    const mainImg = document.querySelector("#main-development-image");
    if (!mainImg) return;

    const thumb = document.querySelectorAll(".gallery-thumb");

    thumb.forEach((btn) => {
        // Update main image when a thumbnail is clicked
        btn.addEventListener("click", () => {
            const fullUrl = btn.dataset.fullUrl;
            const alt = btn.dataset.alt || mainImg.alt;

            if (!fullUrl) return;

            mainImg.src = fullUrl;
            mainImg.alt = alt;
        });
    });
});