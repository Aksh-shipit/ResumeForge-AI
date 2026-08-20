const analyzeBtn = document.getElementById("analyzeResume");

analyzeBtn.addEventListener("click", async () => {

    analyzeBtn.innerText = "Analyzing...";

    const education = [];
    document.querySelectorAll("#educationPreview .education-preview")
        .forEach(item => education.push(item.innerText));

    const skills = [];
    document.querySelectorAll("#skillsPreview span")
        .forEach(item => skills.push(item.innerText));

    const experience = [];
    document.querySelectorAll("#experiencePreview .experience-preview")
        .forEach(item => experience.push(item.innerText));

    const projects = [];
    document.querySelectorAll("#projectPreview .project-preview")
        .forEach(item => projects.push(item.innerText));

    const resumeData = {

        name: document.getElementById("fullName").value,

        role: document.getElementById("targetRole").value,

        summary: document.getElementById("summaryPreview").innerText,

        education,

        skills,

        experience,

        projects

    };

    try {

        const response = await fetch("/analyze-resume", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify(resumeData)

        });

        const data = await response.json();

        const list = document.getElementById("suggestionsPreview");

        list.innerHTML = "";

        data.suggestions.forEach(item => {

            const li = document.createElement("li");

            li.innerText = item;

            list.appendChild(li);

        });

    } catch (err) {

        console.error(err);

        alert("Unable to analyze resume.");

    }

    analyzeBtn.innerText = "Analyze Resume";

});