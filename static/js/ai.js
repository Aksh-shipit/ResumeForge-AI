const generateBtn = document.getElementById("generateSummary");

generateBtn.addEventListener("click", async () => {

    const role = document.getElementById("targetRole").value;

    const skills = document.getElementById("skillsInput").value;

    const experience = document.getElementById("experienceInput").value;

    if (!role || !skills || !experience) {
        alert("Please fill all the fields.");
        return;
    }

    generateBtn.innerText = "Generating...";
    generateBtn.disabled = true;

    try {

        const response = await fetch("/generate-summary", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                role,
                skills,
                experience
            })

        });

        if (!response.ok) {
            throw new Error("Server Error");
        }

        const data = await response.json();

        document.getElementById("summaryPreview").innerText = data.summary;

    } catch (error) {

        console.error(error);

        alert("Failed to generate AI summary.");

    }

    generateBtn.innerText = "Generate AI Summary";
    generateBtn.disabled = false;

});