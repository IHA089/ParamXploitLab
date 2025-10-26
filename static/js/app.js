document.addEventListener("DOMContentLoaded", function() {

    console.log("Futuristic JS Loaded.");

    const elementsToReveal = document.querySelectorAll('.car-card');

    const observer = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('is-visible');
                observer.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.1 
    });

    elementsToReveal.forEach(element => {
        observer.observe(element);
    });

});
