// You may use JavaScript to handle form submission and display results
document.getElementById("choice").addEventListener("change", function () {
  const choice = this.value;
  const additionalFields = document.getElementById("additional-fields");

  // Show additional fields based on user's choice
  if (choice === "2" || choice === "3") {
    additionalFields.style.display = "block";
  } else {
    additionalFields.style.display = "none";
  }
});
