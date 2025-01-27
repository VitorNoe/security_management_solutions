// Simulating API call for security check
document.getElementById("security-form").addEventListener("submit", function (event) {
  event.preventDefault();
  const email = document.getElementById("account-email").value;
  const resultsDiv = document.getElementById("results");

  // Reset results area
  resultsDiv.innerHTML = "Checking security...";

  // Simulate a delay for API processing
  setTimeout(() => {
    if (email.includes("test")) {
      resultsDiv.innerHTML = `<span style="color: red;">⚠️ Warning: Your account may be vulnerable!</span>`;
    } else {
      resultsDiv.innerHTML = `<span style="color: lightgreen;">✅ Great! Your account appears secure.</span>`;
    }
  }, 1500);
});
