const educationContainer =
document.getElementById("educationContainer");

const educationPreview =
document.getElementById("educationPreview");

const addEducation =
document.getElementById("addEducation");

let educationList = [];

function renderEducation() {

    educationPreview.innerHTML = "";

    if (educationList.length === 0) {

        educationPreview.innerHTML =
        "<p>No education added.</p>";

        return;

    }

    educationList.forEach((edu) => {

        educationPreview.innerHTML += `
            <div style="margin-bottom:20px;">
                <strong>${edu.college}</strong><br>
                ${edu.degree}<br>
                ${edu.year}<br>
                CGPA : ${edu.cgpa}
            </div>
        `;

    });

}

function createEducationCard() {

    const index = educationList.length;

    educationList.push({

        college: "",

        degree: "",

        year: "",

        cgpa: ""

    });

    const card =
    document.createElement("div");

    card.className = "education-card";

    card.innerHTML = `

        <input
            type="text"
            placeholder="College Name">

        <input
            type="text"
            placeholder="Degree">

        <input
            type="text"
            placeholder="Year">

        <input
            type="text"
            placeholder="CGPA">

        <button class="remove-btn">

            Remove

        </button>

    `;

    const inputs =
    card.querySelectorAll("input");

    inputs[0].addEventListener("input",(e)=>{

        educationList[index].college =
        e.target.value;

        renderEducation();

    });

    inputs[1].addEventListener("input",(e)=>{

        educationList[index].degree =
        e.target.value;

        renderEducation();

    });

    inputs[2].addEventListener("input",(e)=>{

        educationList[index].year =
        e.target.value;

        renderEducation();

    });

    inputs[3].addEventListener("input",(e)=>{

        educationList[index].cgpa =
        e.target.value;

        renderEducation();

    });

    card.querySelector(".remove-btn")
    .addEventListener("click",()=>{

        educationContainer.removeChild(card);

        educationList.splice(index,1);

        renderEducation();

    });

    educationContainer.appendChild(card);

}

addEducation.addEventListener(
"click",
createEducationCard
);