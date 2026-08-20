console.log("ATS JS Loaded");

const atsBtn = document.getElementById("checkATS");
const resultBox = document.getElementById("atsResult");

if (atsBtn) {

    atsBtn.addEventListener("click", async () => {

        console.log("ATS Button Clicked");

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

        const data = {

            name: document.getElementById("fullName").value,

            email: document.getElementById("email").value,

            phone: document.getElementById("phone").value,

            summary: document.getElementById("summaryPreview").innerText,

            education: education,

            skills: skills,

            experience: experience,

            projects: projects

        };

        try {

            const response = await fetch("/ats-score", {

                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify(data)

            });

            const result = await response.json();

            resultBox.style.display = "block";

            resultBox.innerHTML = `
                <h3>📊 ATS Score: ${result.score}/100</h3>

                <p><strong>${
                    result.score >= 80
                        ? "✅ Excellent Resume"
                        : result.score >= 60
                        ? "🟡 Good Resume"
                        : "🔴 Needs Improvement"
                }</strong></p>

                <ul>
                    ${result.feedback.map(item => `<li>${item}</li>`).join("")}
                </ul>
            `;

        } catch (error) {

            console.error(error);

            resultBox.style.display = "block";

            resultBox.innerHTML = `
                <h3>❌ Failed to calculate ATS Score</h3>
            `;
        }

    });

}