
const projectContainer = document.getElementById("projectContainer");
const projectPreview = document.getElementById("projectPreview");
const addProject = document.getElementById("addProject");

let projects = [];

function renderProjects() {

    projectPreview.innerHTML = "";

    if (projects.length === 0) {
        projectPreview.innerHTML = "<p>No projects added.</p>";
        return;
    }

    projects.forEach((project) => {

        projectPreview.innerHTML += `
            <div class="project-preview">

                <h4>${project.title || "Project Title"}</h4>

                <p><strong>Technologies:</strong> ${project.tech || "-"}</p>

                ${
                    project.github
                        ? `<p><strong>GitHub:</strong>
                           <a href="${project.github}" target="_blank">
                           ${project.github}
                           </a></p>`
                        : ""
                }

                <p>${project.description || ""}</p>

            </div>
        `;

    });

}

function createProjectCard() {

    const index = projects.length;

    projects.push({
        title: "",
        tech: "",
        github: "",
        description: ""
    });

    const card = document.createElement("div");

    card.className = "project-card";

    card.innerHTML = `
        <input
            type="text"
            placeholder="Project Title">

        <input
            type="text"
            placeholder="Technologies Used (React, Flask, MongoDB...)">

        <input
            type="url"
            placeholder="GitHub Repository Link">

        <textarea
            placeholder="Describe your project..."></textarea>

        <button
            type="button"
            class="remove-btn">
            Remove
        </button>
    `;

    const titleInput = card.querySelectorAll("input")[0];
    const techInput = card.querySelectorAll("input")[1];
    const githubInput = card.querySelectorAll("input")[2];
    const descriptionInput = card.querySelector("textarea");

    titleInput.addEventListener("input", (e) => {
        projects[index].title = e.target.value;
        renderProjects();
    });

    techInput.addEventListener("input", (e) => {
        projects[index].tech = e.target.value;
        renderProjects();
    });

    githubInput.addEventListener("input", (e) => {
        projects[index].github = e.target.value;
        renderProjects();
    });

    descriptionInput.addEventListener("input", (e) => {
        projects[index].description = e.target.value;
        renderProjects();
    });

    card.querySelector(".remove-btn").addEventListener("click", () => {

        projectContainer.removeChild(card);

        projects.splice(index, 1);

        renderProjects();

    });

    projectContainer.appendChild(card);

}

if (addProject) {
    addProject.addEventListener("click", createProjectCard);
} else {
    console.error("Add Project button not found!");
}