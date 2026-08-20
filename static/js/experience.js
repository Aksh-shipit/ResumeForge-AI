const experienceContainer =
document.getElementById("experienceContainer");

const experiencePreview =
document.getElementById("experiencePreview");

const addExperience =
document.getElementById("addExperience");

let experiences = [];

function renderExperience(){

    experiencePreview.innerHTML = "";

    if(experiences.length===0){

        experiencePreview.innerHTML="<p>No experience added.</p>";

        return;

    }

    experiences.forEach((exp)=>{

        experiencePreview.innerHTML+=`

        <div class="experience-preview">

            <h4>${exp.position}</h4>

            <strong>${exp.company}</strong>

            <p>${exp.duration}</p>

            <p>${exp.description}</p>

        </div>

        `;

    });

}

function createExperienceCard(){

    const index=experiences.length;

    experiences.push({

        company:"",

        position:"",

        duration:"",

        description:""

    });

    const card=document.createElement("div");

    card.className="experience-card";

    card.innerHTML=`

        <input
        type="text"
        placeholder="Company">

        <input
        type="text"
        placeholder="Job Title">

        <input
        type="text"
        placeholder="Duration (e.g. Jan 2025 - Jul 2025)">

        <textarea
        placeholder="Describe your work..."></textarea>

        <button class="remove-btn">

        Remove

        </button>

    `;

    const inputs=card.querySelectorAll("input");

    const textarea=card.querySelector("textarea");

    inputs[0].addEventListener("input",(e)=>{

        experiences[index].company=e.target.value;

        renderExperience();

    });

    inputs[1].addEventListener("input",(e)=>{

        experiences[index].position=e.target.value;

        renderExperience();

    });

    inputs[2].addEventListener("input",(e)=>{

        experiences[index].duration=e.target.value;

        renderExperience();

    });

    textarea.addEventListener("input",(e)=>{

        experiences[index].description=e.target.value;

        renderExperience();

    });

    card.querySelector(".remove-btn")
    .addEventListener("click",()=>{

        experienceContainer.removeChild(card);

        experiences.splice(index,1);

        renderExperience();

    });

    experienceContainer.appendChild(card);

}

addExperience.addEventListener(
"click",
createExperienceCard
);