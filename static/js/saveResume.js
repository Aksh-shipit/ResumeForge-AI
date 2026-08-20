const saveBtn = document.getElementById("saveResume");

if (saveBtn) {

    saveBtn.addEventListener("click", async () => {

        
        const education = [];
        document.querySelectorAll("#educationPreview .education-preview")
            .forEach(item => {
                education.push(item.innerText);
            });

        const skills = []
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

            title: document.getElementById("fullName").value + " Resume",

            name: document.getElementById("fullName").value,

            email: document.getElementById("email").value,

            phone: document.getElementById("phone").value,

            address: document.getElementById("address").value,

            linkedin: document.getElementById("linkedin").value,

            github: document.getElementById("github").value,

            summary: document.getElementById("summaryPreview").innerText,

            education: education,

            skills: skills,

            experience: experience,

            projects: projects,

            template: document.getElementById("templateSelect").value

        };

        // resumeId comes from script.js
        const url = resumeId
            ? `/update-resume/${resumeId}`
            : "/save-resume";

        try {
             saveBtn.disabled = true;
saveBtn.textContent = "Saving...";

await new Promise(resolve => setTimeout(resolve, 800));
            const response = await fetch(url, {

                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify(resumeData)

            });

            const result = await response.json();

console.log(result);

showToast(result.message);

// Change button to success
saveBtn.textContent = "✔ Resume Saved";
saveBtn.style.background = "#16a34a";

// Wait 2 seconds before redirecting
setTimeout(() => {
    saveBtn.disabled = false;
    saveBtn.textContent = "Save Resume";
    saveBtn.style.background = "";

    window.location.href = "/my-resumes";
}, 2000);
        } catch (error) {

            console.error(error);

            showToast("Failed to save resume.");

            saveBtn.disabled = false;
saveBtn.textContent = "Save Resume";

        }

    });

}