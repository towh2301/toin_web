document.querySelectorAll(".lang-switch .btn").forEach(btn => {
    btn.addEventListener("click", async function (e) {
        document.querySelectorAll(".lang-switch .btn").forEach(b => b.classList.remove("active"));
        this.classList.add("active");

        // Get selected language
        let lang = this.dataset.lang;
        console.log("Selected language:", lang);

        // TODO: trigger Django i18n or custom logic to switch content
        const langCode = e.target.getAttribute('data-lang'); // 1️⃣ get the language code

        // Set langcode
        const response = await fetch('/i18n/setlang/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-CSRFToken': csrf_token, // Django needs this for POST
            },
            body: new URLSearchParams({
                language: langCode, // required field name
                next: window.location.pathname // optional redirect after switch
            })
        })

        // Reload the page to apply new language
        if (!response.ok) {
            console.error('Language switch failed', response.status, await response.text());
            return;
        }

        // Get current path
        let path = window.location.pathname;

        // Replace prefix (/vi/, /jp/, /en/) with the new one
        path = path.replace(/^\/(vi|jp|en)\//, '/' + langCode + '/');

        // If no prefix exists, prepend it
        if (!path.startsWith('/' + langCode + '/')) {
            path = '/' + langCode + path;
        }

        window.location.href = path;
    });
})
;