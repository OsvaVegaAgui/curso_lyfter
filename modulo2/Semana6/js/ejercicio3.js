const empYes = document.getElementById("employee-yes");
const empNo = document.getElementById("employee-no");

const jobInput = document.getElementById("job-input");

const showJob = () => {
    if (empYes.checked) {
        jobInput.style.display = "inline-block";
    } else {
        jobInput.style.display = "none";
    }
};

empYes.addEventListener("change", showJob);
empNo.addEventListener("change", showJob);

