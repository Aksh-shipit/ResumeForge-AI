const downloadBtn =
document.getElementById("downloadResume");

downloadBtn.addEventListener("click", async () => {

    const education = [];

    document.querySelectorAll("#educationPreview .education-preview")
        .forEach(item => {
            education.push(item.innerText);
        });

    const skills = [];

    document.querySelectorAll("#skillsPreview span")
        .forEach(item => {
            skills.push(item.innerText);
        });

    const experience = [];

    document.querySelectorAll("#experiencePreview .experience-preview")
        .forEach(item => {
            experience.push(item.innerText);
        });

    const projects = [];

    document.querySelectorAll("#projectPreview .project-preview")
        .forEach(item => {
            projects.push(item.innerText);
        });

    const resumeData = {
    name: document.getElementById("fullName").value,
    email: document.getElementById("email").value,
    phone: document.getElementById("phone").value,
    address: document.getElementById("address").value,
    linkedin: document.getElementById("linkedin").value,
    github: document.getElementById("github").value,

    summary: document.getElementById("summaryPreview").innerText,

    education,
    skills,
    experience,
    projects,

    template: document.getElementById("templateSelect").value
};
    const response =
    await fetch("/download-resume", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify(resumeData)

    });

    const blob =
    await response.blob();

    const url =
    window.URL.createObjectURL(blob);

    const a =
    document.createElement("a");

    a.href = url;

    a.download = "Resume.pdf";

    document.body.appendChild(a);

    a.click();

    a.remove();

});