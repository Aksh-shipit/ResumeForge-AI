
const page = document.querySelector(".page");

const resumeData = JSON.parse(
    page.dataset.resume || "{}"
);

const resumeId =
    page.dataset.resumeId || null;

const fields = [
    {
        input: "fullName",
        preview: "previewName",
        defaultText: "Your Name"
    },
    {
        input: "email",
        preview: "previewEmail",
        defaultText: "email@example.com"
    },
    {
        input: "phone",
        preview: "previewPhone",
        defaultText: "Phone Number"
    },
    {
        input: "address",
        preview: "previewAddress",
        defaultText: "Address"
    },
    {
        input: "linkedin",
        preview: "previewLinkedIn",
        defaultText: "LinkedIn"
    },
    {
        input: "github",
        preview: "previewGithub",
        defaultText: "GitHub"
    }
];

fields.forEach(field => {
    const input = document.getElementById(field.input);
    const preview = document.getElementById(field.preview);

    if (!input || !preview) {
        console.log("Missing:", field.input, field.preview);
        return;
    }

    input.addEventListener("input", () => {
        preview.textContent = input.value || field.defaultText;
    });
});

function showToast(message){

    const toast=document.getElementById("toast");

    toast.innerText=message;

    toast.classList.add("show");

    setTimeout(()=>{

        toast.classList.remove("show");

    },2500);

}