document.addEventListener("DOMContentLoaded", function () {

    const container = document.getElementById('formset-container');
    const addButton = document.getElementById('add-form');

    // =========================
    // STATUS SYSTEM (PRO CMS)
    // =========================
    function initStatusSystem() {
    const buttons = document.querySelectorAll('.status-btn');

    buttons.forEach(btn => {
        const input = btn.querySelector('.status-input');

        // Initial state (for edit page)
        if (input.checked) {
            btn.classList.add('active');
        }

        btn.addEventListener('click', function () {

            // 🔥 Clear all
            buttons.forEach(b => {
                b.classList.remove('active');
                b.querySelector('.status-input').checked = false;
            });

            // 🔥 Set current
            this.classList.add('active');
            input.checked = true;
        });
    });
}

    initStatusSystem();


    // =========================
    // CATEGORY SYSTEM
    // =========================
    document.querySelectorAll('.category-pill').forEach(pill => {
        pill.addEventListener('click', function (e) {
            e.preventDefault();

            document.querySelectorAll('.category-pill').forEach(p => p.classList.remove('active'));
            this.classList.add('active');

            const newCatInput = document.querySelector('[name="new_category"]');
            if (newCatInput) newCatInput.value = '';
        });
    });


    const newCatInput = document.querySelector('[name="new_category"]');
    if (newCatInput) {
        newCatInput.addEventListener('input', function () {
            if (this.value.trim()) {
                document.querySelectorAll('.category-pill').forEach(p => p.classList.remove('active'));
            }
        });
    }


    // =========================
    // ADD FORMSET (SAFE CLONE)
    // =========================
    if (addButton && container) {
        addButton.addEventListener('click', function () {

            const totalForms = document.getElementById('id_post_media-TOTAL_FORMS');
            let formCount = parseInt(totalForms.value, 10);

            let newForm = container.children[0].cloneNode(true);

            newForm.innerHTML = newForm.innerHTML.replace(/-\d+-/g, `-${formCount}-`);

            // reset inputs
            newForm.querySelectorAll('input, textarea, select').forEach(el => {

                if (el.type === "checkbox") {
                    el.checked = false;
                } else if (el.name && el.name.endsWith('-DELETE')) {
                    el.checked = false;
                } else {
                    el.value = "";
                }

            });

            // clear preview images
            newForm.querySelectorAll('img.preview-img').forEach(img => img.remove());

            // reset order
            const orderInput = newForm.querySelector('[name$="-order"]');
            if (orderInput) orderInput.value = formCount;

            // reset media
            const mediaInput = newForm.querySelector('[name$="-media"]');
            if (mediaInput) mediaInput.value = '';

            container.appendChild(newForm);
            totalForms.value = formCount + 1;

        });
    }


    // =========================
    // SORTABLE (ORDER SYSTEM)
    // =========================
    if (window.Sortable && container) {
        new Sortable(container, {
            animation: 150,
            onEnd: function () {

                document.querySelectorAll('.formset-item').forEach((item, index) => {
                    const orderInput = item.querySelector('[name$="-order"]');
                    if (orderInput) orderInput.value = index;
                });

            }
        });
    }

});