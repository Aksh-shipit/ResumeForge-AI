const templateSelect = document.getElementById("templateSelect");
const resume = document.querySelector(".resume");

if (templateSelect && resume) {

    templateSelect.addEventListener("change", () => {

        resume.classList.remove(
            "classic-template",
            "modern-template",
            "dark-template"
        );

        if (templateSelect.value === "classic") {
            resume.classList.add("classic-template");
        }

        if (templateSelect.value === "modern") {
            resume.classList.add("modern-template");
        }

        if (templateSelect.value === "dark") {
            resume.classList.add("dark-template");
        }

    });

    resume.classList.add("classic-template");

}