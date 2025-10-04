document.querySelectorAll('.nav-link').forEach(link => {
    link.addEventListener('click', e => {
        e.preventDefault();
        const sectionId = e.target.getAttribute('data-section');
        document.getElementById(sectionId)?.scrollIntoView({behavior: 'smooth'});
    });
});