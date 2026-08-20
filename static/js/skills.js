const skillInput = document.getElementById("skillInput");
const addSkillBtn = document.getElementById("addSkill");
const skillList = document.getElementById("skillList");
const skillsPreview = document.getElementById("skillsPreview");

let skills = [];

function renderSkills() {

    skillList.innerHTML = "";
    skillsPreview.innerHTML = "";

    if (skills.length === 0) {

        skillsPreview.innerHTML = "<p>No skills added.</p>";
        return;
    }

    skills.forEach((skill, index) => {

        // Form Tags
        const tag = document.createElement("div");
        tag.className = "skill-tag";

        tag.innerHTML = `
            ${skill}
            <button>&times;</button>
        `;

        tag.querySelector("button").addEventListener("click", () => {

            skills.splice(index, 1);

            renderSkills();

        });

        skillList.appendChild(tag);

        // Resume Preview

        const previewTag = document.createElement("span");

        previewTag.className = "preview-skill";

        previewTag.textContent = skill;

        skillsPreview.appendChild(previewTag);

    });

}

function addSkill() {

    const input = skillInput.value.trim();

    if (input === "") return;

    // Split by comma
    const newSkills = input.split(",");

    newSkills.forEach(skill => {

        skill = skill.trim();

        if (skill !== "" && !skills.includes(skill)) {

            skills.push(skill);

        }

    });

    skillInput.value = "";

    renderSkills();

}
addSkillBtn.addEventListener("click", addSkill);

skillInput.addEventListener("keydown", (e) => {

    if (e.key === "Enter") {

        e.preventDefault();

        addSkill();

    }

});